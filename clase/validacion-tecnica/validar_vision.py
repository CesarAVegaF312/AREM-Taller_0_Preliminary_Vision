"""Verificador de la entrega del Taller 0 (Ficha de Caracterización y Documento de Visión).

Revisa la forma y la trazabilidad de los dos documentos contra la checklist de la guía:
que no queden campos de la plantilla sin llenar, que cada beneficio apunte a un objetivo
de la Ficha, que haya de 5 a 8 capacidades sin nombre de sistema y 3 principios completos.
No juzga si el contenido es cierto o bueno: eso lo decide el equipo con el cliente.

Uso:  python3 validar_vision.py [carpeta]
      (por defecto revisa la carpeta "entrega")
"""

import re
import sys
import unicodedata
from pathlib import Path

PALABRAS_DE_SISTEMA = [
    "sistema", "plataforma", "app", "aplicacion", "software", "erp", "crm",
    "portal", "modulo", "base de datos", "herramienta", "zoho", "sap", "excel",
]
PALABRAS_VACIAS = {
    "de", "del", "la", "las", "el", "los", "en", "y", "o", "a", "con", "por",
    "para", "un", "una", "al", "que", "se", "su", "sus", "sin",
}

resultados = []


def registrar(estado, mensaje):
    resultados.append((estado, mensaje))


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def raices(texto):
    """Primeras 5 letras de cada palabra significativa, para comparar sin importar la conjugación."""
    palabras = re.findall(r"[a-z0-9]+", normalizar(texto))
    return {p[:5] for p in palabras if p not in PALABRAS_VACIAS and len(p) > 2}


def coincide(frase, candidatas, umbral=0.5):
    """Indica si la frase comparte al menos la mitad de sus palabras con alguna candidata."""
    propias = raices(frase)
    if not propias:
        return False
    return any(len(propias & raices(c)) / len(propias) >= umbral for c in candidatas)


def secciones(texto):
    """Divide un documento Markdown en {encabezado de nivel 2: contenido}."""
    partes, actual = {}, None
    for linea in texto.splitlines():
        if linea.startswith("## "):
            actual = linea[3:].strip()
            partes[actual] = []
        elif actual is not None:
            partes[actual].append(linea)
    return {k: "\n".join(v) for k, v in partes.items()}


def buscar_seccion(partes, inicio):
    for nombre, contenido in partes.items():
        if normalizar(nombre).startswith(normalizar(inicio)):
            return contenido
    return None


def filas_tabla(contenido):
    """Devuelve las filas de la primera tabla de la sección, sin encabezado ni separador."""
    filas = []
    for linea in contenido.splitlines():
        linea = linea.strip()
        if not linea.startswith("|"):
            if filas:
                break
            continue
        celdas = [c.strip() for c in linea.strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in celdas if c):
            continue
        filas.append(celdas)
    return filas[1:]


def filas_llenas(filas):
    return [f for f in filas if any(f)]


def items_lista(contenido):
    """Devuelve el texto de cada viñeta o ítem numerado (vacío si no se llenó)."""
    items = []
    lineas = contenido.splitlines()
    for n, linea in enumerate(lineas):
        m = re.match(r"(\s*)(?:[-*]|\d+\.)\s*(.*)$", linea)
        if not m or linea.strip().startswith(">"):
            continue
        texto = m.group(2).strip()
        # Un ítem "Etiqueta:" con sub-viñetas llenas debajo no está vacío.
        if texto.endswith(":"):
            hijos = []
            for siguiente in lineas[n + 1:]:
                h = re.match(r"(\s+)(?:[-*]|\d+\.)\s*(.*)$", siguiente)
                if not h or len(h.group(1)) <= len(m.group(1)):
                    break
                hijos.append(h.group(2).strip())
            if hijos and all(hijos):
                texto = texto + " " + "; ".join(hijos)
        items.append(texto)
    return items


def revisar_ficha(texto):
    if "_[" in texto:
        registrar("FALTA", "Ficha: quedan campos de la plantilla sin llenar (texto entre _[ ]_ en el encabezado).")
    partes = secciones(texto)
    requeridas = [
        ("I.", "I. Información general del negocio"),
        ("II.", "II. Objetivos estratégicos"),
        ("III.", "III. Problemas o necesidades"),
        ("IV.", "IV. Procesos clave"),
        ("V.", "V. Expectativas"),
        ("VI.", "VI. Persona de contacto"),
    ]
    for prefijo, nombre in requeridas:
        contenido = buscar_seccion(partes, prefijo)
        if contenido is None:
            registrar("FALTA", f"Ficha: no se encontró la sección «{nombre}».")
            continue
        items = items_lista(contenido)
        vacios = [i for i in items if i == "" or re.fullmatch(r".*:\s*", i)]
        llenos = [i for i in items if i not in vacios]
        if not llenos:
            registrar("FALTA", f"Ficha: la sección «{nombre}» está vacía.")
        elif vacios:
            registrar("REVISAR", f"Ficha: la sección «{nombre}» tiene {len(vacios)} ítem(s) sin llenar.")
        else:
            registrar("OK", f"Ficha: sección «{nombre}» diligenciada.")

    expectativas = buscar_seccion(partes, "V.") or ""
    m = re.search(r"\*\*Restricciones:\*\*(.*)", expectativas, re.S)
    if m is None or not m.group(1).strip():
        registrar("FALTA", "Ficha: no hay restricciones declaradas (sección V). Si el cliente no tiene, escríbalo.")

    objetivos = [i for i in items_lista(buscar_seccion(partes, "II.") or "") if i]
    procesos = [i for i in items_lista(buscar_seccion(partes, "IV.") or "") if i]
    return objetivos, procesos


def revisar_vision(texto, objetivos, procesos):
    marcadores = ["_Nombre del cliente real._", "- Nombre 1", '["..."]']
    if any(m in texto for m in marcadores):
        registrar("FALTA", "Visión: quedan textos de ejemplo de la plantilla (cliente, integrantes o cajas \"...\" del mapa).")
    partes = secciones(texto)

    mapa = buscar_seccion(partes, "Mapa conceptual") or ""
    cajas = len(re.findall(r"^\s*subgraph\b", mapa, re.M))
    if "```mermaid" not in mapa and "![" not in mapa:
        registrar("FALTA", "Visión: no hay mapa conceptual (ni diagrama Mermaid ni imagen).")
    elif '["..."]' in mapa:
        registrar("FALTA", "Visión: el mapa conceptual todavía tiene las cajas \"...\" de la plantilla.")
    elif "```mermaid" in mapa and not 4 <= cajas <= 6:
        registrar("REVISAR", f"Visión: el mapa conceptual tiene {cajas} cajas; la guía pide de 4 a 6, a alto nivel.")
    else:
        registrar("OK", "Visión: mapa conceptual presente.")

    beneficios = filas_llenas(filas_tabla(buscar_seccion(partes, "Beneficios") or ""))
    if not beneficios:
        registrar("FALTA", "Visión: la tabla de beneficios esperados está vacía.")
    for fila in beneficios:
        objetivo = fila[0]
        if len(fila) < 3 or not all(fila[:3]):
            registrar("FALTA", f"Visión: el beneficio de «{objetivo or '(sin objetivo)'}» tiene columnas vacías (beneficio o cómo se mide).")
        elif objetivos and not coincide(objetivo, objetivos):
            registrar("REVISAR", f"Visión: el objetivo «{objetivo}» no se parece a ningún objetivo de la Ficha (sección II). Cada beneficio debe apuntar a uno de ellos.")
    if beneficios and objetivos:
        sin_beneficio = [o for o in objetivos if not any(coincide(f[0], [o]) for f in beneficios)]
        for o in sin_beneficio:
            registrar("REVISAR", f"Visión: el objetivo de la Ficha «{o}» no tiene ningún beneficio esperado asociado.")
        if not sin_beneficio:
            registrar("OK", "Visión: cada objetivo de la Ficha tiene al menos un beneficio esperado.")

    alcance = filas_tabla(buscar_seccion(partes, "Alcance") or "")
    dentro = [f[0] for f in alcance if f and f[0]]
    fuera = [f[1] for f in alcance if len(f) > 1 and f[1]]
    if not dentro or not fuera:
        registrar("FALTA", "Visión: el alcance debe tener al menos un elemento en alcance y uno fuera de alcance.")
    else:
        registrar("OK", f"Visión: alcance definido ({len(dentro)} en alcance, {len(fuera)} fuera de alcance).")

    capacidades = filas_llenas(filas_tabla(buscar_seccion(partes, "Capacidades") or ""))
    if not 5 <= len(capacidades) <= 8:
        registrar("FALTA", f"Visión: hay {len(capacidades)} capacidades; la guía pide de 5 a 8.")
    else:
        registrar("OK", f"Visión: {len(capacidades)} capacidades de negocio.")
    for fila in capacidades:
        fila = fila + [""] * (4 - len(fila))
        nombre, proceso, soporte, evidencia = fila[:4]
        if not all([nombre, proceso, soporte, evidencia]):
            registrar("FALTA", f"Visión: la capacidad «{nombre or '(sin nombre)'}» tiene columnas vacías.")
            continue
        palabras = [p for p in PALABRAS_DE_SISTEMA if re.search(rf"\b{p}\b", normalizar(nombre))]
        if palabras:
            registrar("REVISAR", f"Visión: la capacidad «{nombre}» parece nombrar un sistema ({', '.join(palabras)}). Debe ser verbo + objeto, sin tecnología.")
        if normalizar(soporte).strip("* ") not in ("alto", "medio", "bajo"):
            registrar("FALTA", f"Visión: el soporte tecnológico de «{nombre}» debe ser alto, medio o bajo (dice «{soporte}»).")
        if procesos and not normalizar(proceso).startswith("transversal") and not coincide(proceso, procesos):
            registrar("REVISAR", f"Visión: el proceso «{proceso}» de la capacidad «{nombre}» no se parece a ningún proceso clave de la Ficha (sección IV).")

    principios = filas_llenas(filas_tabla(buscar_seccion(partes, "Principios") or ""))
    completos = [f for f in principios if len(f) >= 4 and all(f[:4])]
    if len(principios) != 3:
        registrar("FALTA", f"Visión: hay {len(principios)} principios; la guía pide 3 en borrador.")
    if len(completos) < len(principios):
        registrar("FALTA", "Visión: hay principios sin nombre, declaración, implicación o de dónde salen.")
    elif len(principios) == 3:
        registrar("OK", "Visión: 3 principios con nombre, declaración, implicación y origen.")

    justificacion = (buscar_seccion(partes, "Justificación") or "").strip()
    plantilla = "Explique en 2-3 párrafos"
    if not justificacion.replace("---", "").strip() or justificacion.startswith(plantilla):
        registrar("FALTA", "Visión: falta la justificación (o quedó el texto de la plantilla).")
    else:
        registrar("OK", "Visión: justificación escrita.")


def main():
    carpeta = Path(sys.argv[1] if len(sys.argv) > 1 else "entrega")
    ficha = carpeta / "ficha-caracterizacion.md"
    vision = carpeta / "vision.md"
    for archivo in (ficha, vision):
        if not archivo.exists():
            print(f"FALTA    No existe {archivo}")
            sys.exit(1)

    objetivos, procesos = revisar_ficha(ficha.read_text(encoding="utf-8"))
    revisar_vision(vision.read_text(encoding="utf-8"), objetivos, procesos)

    for estado, mensaje in resultados:
        print(f"{estado:<8} {mensaje}")
    faltas = sum(1 for e, _ in resultados if e == "FALTA")
    revisar = sum(1 for e, _ in resultados if e == "REVISAR")
    print()
    print(f"Resultado: {faltas} faltante(s), {revisar} por revisar.")
    print("El verificador revisa forma y trazabilidad, no si el contenido es cierto: eso se valida con el cliente.")
    sys.exit(1 if faltas else 0)


if __name__ == "__main__":
    main()
