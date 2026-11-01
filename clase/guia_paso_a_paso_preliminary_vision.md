# Guía Paso a Paso: Preliminary y Architecture Vision

Esta guía complementa el `README.md` del taller. Cubre las dos primeras fases de TOGAF ADM adaptadas al curso: **Preliminary** (la Ficha de Caracterización del Cliente) y **Architecture Vision** (la visión de alto nivel de la arquitectura, sus beneficios esperados, las capacidades de negocio y un borrador de principios arquitectónicos). En TOGAF los principios nacen en la fase Preliminar y las capacidades en la Visión; por eso se piden aquí, en borrador, y no al final del curso: el Taller 7 madura las capacidades y el Taller 9 confirma los principios. Todo lo que se construya aquí es la base sobre la que se apoyan los demás talleres del semestre — si el alcance queda mal definido acá, el error se arrastra hasta el Taller 9.

El diagrama de ejemplo está escrito en [Mermaid](https://mermaid.js.org/) y se renderiza automáticamente al ver este archivo en GitHub.

---

## Parte A — Preliminary: Ficha de Caracterización del Cliente

### A.1 Metodología en 5 pasos

1. **Levantar la información general del negocio** — empresa, sector, tamaño (empleados/usuarios), ubicación, tecnologías actuales.
2. **Documentar los objetivos estratégicos** — lo que el cliente quiere lograr como negocio, no como sistema. Deben ser específicos y verificables.
3. **Registrar los problemas o necesidades identificadas** — descritos como el cliente los vive (síntomas), no como una solución técnica ya decidida.
4. **Listar los procesos clave del negocio** — esta lista es el insumo directo del Taller 1 (BPMN): de aquí sale el proceso que el equipo modelará.
5. **Capturar expectativas, restricciones y persona de contacto** — qué espera el cliente de la solución, qué no se puede tocar, y quién responde las preguntas del equipo durante el semestre.

### A.2 Ejemplo guiado: Fundación Salud Viva

> Ejemplo tomado del material oficial del curso — disponible en este mismo repositorio como [`clase/Ejemplo_Ficha_Cliente_Arquitectura_Empresarial.pdf`](Ejemplo_Ficha_Cliente_Arquitectura_Empresarial.pdf).

**I. Información general del negocio**
- Empresa: Fundación Salud Viva — sector salud (atención domiciliaria y telemedicina)
- Tamaño: 70 empleados / 2.500 usuarios mensuales activos
- Ubicación: Bogotá (oficina principal) + plataforma digital nacional
- Tecnologías actuales: Google Workspace, app móvil propia (Flutter), ERP en la nube (Zoho One)

**II. Objetivos estratégicos**
1. Mejorar la eficiencia operativa reduciendo el tiempo de atención por paciente.
2. Ampliar cobertura nacional sin duplicar costos operativos.
3. Aumentar el cumplimiento con normativas de seguridad en el manejo de datos clínicos.

**III. Problemas identificados** (nótese que son síntomas, no soluciones)
- Falta de integración entre la app móvil, el ERP y la plataforma de telemedicina.
- Dificultad para generar reportes integrales de pacientes y procesos.
- No existe una arquitectura formal documentada para planear futuras expansiones.

**IV. Procesos clave del negocio**
- Gestión de citas y agendamiento médico.
- Atención médica domiciliaria y seguimiento remoto.
- Gestión administrativa y facturación a aseguradoras.

**V. Expectativas y restricciones**
- Expectativas: claridad sobre qué transformar primero, poder escalar sin rehacer todo, identificar y mitigar riesgos tecnológicos.
- Restricciones: no se pueden cambiar las herramientas básicas de oficina en 2026; toda solución debe operar en nube pública o híbrida.

**VI. Persona de contacto**
- Nombre, correo/teléfono y rol frente a la solución.

---

## Parte B — Architecture Vision

### B.1 Metodología en 6 pasos

1. **Traducir los objetivos estratégicos en una visión de arquitectura** — para cada objetivo de la Ficha, formule qué debería cambiar en la arquitectura para lograrlo.
2. **Bocetar un mapa conceptual de alto nivel** — 4 a 6 cajas grandes (negocio, datos, aplicaciones, tecnología), sin el nivel de detalle de un BPMN o un C4. Ese detalle es trabajo de los Talleres 1 a 4, no de este.
3. **Justificar los beneficios esperados** — cada beneficio debe apuntar a un objetivo estratégico específico de la Ficha, no ser una afirmación genérica ("mejora la eficiencia" sin más).
4. **Delimitar el alcance** — qué queda dentro del proyecto y qué queda explícitamente fuera (muchas veces las restricciones de la Ficha ya definen parte del "fuera de alcance").
5. **Listar las capacidades de negocio** — de 5 a 8, con verbo + objeto y sin nombrar tecnología, a partir de los procesos clave de la Ficha (sección IV). Una capacidad es lo que la organización necesita saber hacer y sobrevive aunque cambie la herramienta: el cliente seguirá necesitando «facturar a aseguradoras» aunque reemplace el ERP. Para cada una, valore el soporte tecnológico actual (alto / medio / bajo) con la evidencia que dio el cliente. Esta lista es la que el Taller 7 (sección 4.1) madura con los hallazgos de los talleres intermedios y convierte en paquetes de trabajo.
6. **Escribir un borrador de 3 principios arquitectónicos** — cada uno con nombre, declaración (una frase) e implicación (qué queda prohibido o más caro), y cada uno salido de un objetivo estratégico o de una restricción de la Ficha. Un principio sirve si permite decir «no» a algo concreto; si no descarta ninguna opción, es una frase bonita. Es un borrador: el Taller 9 (plan de gobernanza) confirma, reescribe o retira cada principio con la evidencia de los Talleres 1 a 8.

### B.2 Ejemplo guiado: Visión de Fundación Salud Viva

> Vea la trazabilidad objetivo → síntoma → beneficio → caja del mapa en versión interactiva: [`clase/visualizacion-vision-preliminar.html`](visualizacion-vision-preliminar.html).

**Mapa conceptual de alto nivel** (obsérvese que es deliberadamente impreciso — el detalle llega después):

```mermaid
flowchart LR
    subgraph negocio["Negocio"]
        proc["Atención al paciente\n(citas, domiciliaria, facturación)"]
    end
    subgraph datos["Datos"]
        info["Historia clínica y datos\nde pacientes unificados"]
    end
    subgraph apps["Aplicaciones"]
        plat["Plataforma integrada\n(app + ERP + telemedicina)"]
    end
    subgraph tec["Tecnología"]
        nube["Infraestructura en\nnube pública o híbrida"]
    end

    negocio --> apps
    datos --> apps
    apps --> tec
```

**Beneficios esperados**

| Objetivo estratégico (Ficha) | Beneficio esperado | Cómo se mide |
|---|---|---|
| Mejorar eficiencia operativa | Menos tiempo administrativo por paciente al integrar app, ERP y telemedicina | Minutos promedio de atención por paciente |
| Ampliar cobertura nacional | La plataforma soporta más usuarios sin duplicar infraestructura por ciudad | Costo operativo por usuario activo |
| Cumplir normativas de datos clínicos | Datos de pacientes con control de acceso y trazabilidad centralizados | Resultado del checklist normativo (Taller 6) |

**Alcance**

| En alcance | Fuera de alcance |
|---|---|
| Integración de app móvil, ERP y telemedicina | Reemplazo de Google Workspace (restricción de la Ficha) |
| Arquitectura de datos unificada de pacientes | Migración fuera de nube pública/híbrida |
| Documentación formal de la arquitectura actual y objetivo | Implementación real del sistema (el curso entrega el diseño, no lo construye) |

**Capacidades de negocio (borrador)** — salen de los 3 procesos clave de la Ficha; dos son transversales porque las necesitan todos los procesos. Obsérvese que ninguna lleva nombre de sistema. La columna de evidencia extiende la ficha oficial con lo que una conversación con el cliente habría dejado: está aquí para mostrar el nivel de detalle esperado, no como dato del PDF.

| Capacidad (verbo + objeto) | Proceso(s) de la Ficha que la realizan | Soporte tecnológico hoy | Evidencia (qué dijo o mostró el cliente) |
|---|---|---|---|
| Agendar y gestionar citas | Gestión de citas y agendamiento médico | Alto | La app móvil agenda y notifica; el cliente no reporta fallas en este flujo |
| Atender pacientes a domicilio | Atención médica domiciliaria | Medio | Las visitas se programan en la app, pero el registro clínico se hace en formularios de Google Workspace |
| Hacer seguimiento remoto al paciente | Seguimiento remoto (telemedicina) | Medio | La plataforma de telemedicina funciona, pero no comparte datos con la app ni con el ERP |
| Mantener una historia clínica unificada | Transversal: citas, domiciliaria y telemedicina | Bajo | Problema #1 de la Ficha: la información del paciente vive en tres sistemas que no se hablan |
| Facturar a aseguradoras | Gestión administrativa y facturación | Medio | El ERP factura, pero los soportes clínicos se recopilan a mano desde los otros dos sistemas |
| Reportar la operación a la dirección | Transversal | Bajo | Problema #2 de la Ficha: no se pueden generar reportes integrales de pacientes y procesos |

**Principios arquitectónicos (borrador)** — cada uno descarta algo concreto y sale de un objetivo o de una restricción de la Ficha:

| Principio (nombre) | Declaración | Implicación (qué descarta) | Sale de |
|---|---|---|---|
| Historia clínica única | Cada dato clínico del paciente se captura una sola vez y tiene un sistema dueño; los demás lo consultan, no lo copian. | Descarta que la app, el ERP o la telemedicina guarden su propia versión del paciente; cualquier componente nuevo que duplique datos clínicos necesita una excepción aprobada. | Objetivo 1 (eficiencia operativa) y problema #1 (falta de integración) |
| Integración por servicios, no por archivos | Los sistemas se conectan por interfaces documentadas y versionadas, nunca por exportaciones manuales ni archivos compartidos. | Descarta el intercambio de hojas de cálculo entre app, ERP y telemedicina; encarece cualquier integración que no exponga una interfaz. | Objetivo 2 (cobertura nacional sin duplicar costos) |
| Nube pública o híbrida por defecto | Todo componente nuevo se despliega en nube pública o híbrida; Google Workspace y Zoho One no se reemplazan en 2026. | Descarta servidores propios en cada ciudad y descarta migrar el ERP o la ofimática este año. | Restricciones de la Ficha (sección V) |

> Estos tres principios son un borrador a propósito. Cuando el Taller 5 muestre, por ejemplo, que los datos clínicos viajan sin cifrar, el equipo agregará un principio de seguridad; y si el Taller 3 muestra que el ERP ya expone una interfaz, el segundo principio se confirma con esa evidencia. Ese cierre se hace en el plan de gobernanza del Taller 9.

---

## Errores comunes a evitar

| Error frecuente | Por qué es un problema | Cómo corregirlo |
|---|---|---|
| Ficha con respuestas genéricas, sin datos reales del cliente | Compromete todo el semestre: si el alcance parte mal, el error se arrastra a todos los talleres siguientes | Base la ficha en una conversación real con el cliente, no en suposiciones |
| Confundir "problema" con "solución" en la sección de problemas | La ficha debe describir síntomas, no la respuesta técnica ya decidida | Escriba el problema como lo vive el cliente, no como una solución ("se necesita un data warehouse") |
| Visión sin conexión con los objetivos estratégicos de la Ficha | El resto del curso pierde el hilo de "para qué" se hace cada taller | Cada beneficio esperado debe apuntar a un objetivo estratégico específico |
| Mapa conceptual con el mismo nivel de detalle que un C4 o un BPMN | Adelanta trabajo de los Talleres 1-4 y sobra esfuerzo aquí | Mantenga el mapa a alto nivel: 4-6 cajas grandes, no procesos ni contenedores |
| Capacidades con nombre de sistema («el ERP», «la app de citas») | Son aplicaciones, no capacidades: cambian cuando cambia la herramienta y el negocio no se reconoce en ellas | Verbo + objeto, sin tecnología: «Facturar a aseguradoras», no «Zoho One» |
| Principio que no descarta nada («La arquitectura debe ser flexible y segura») | Si no prohíbe ni encarece ninguna opción, no gobierna ninguna decisión | Escriba la implicación: qué queda prohibido o necesita excepción, y de qué objetivo o restricción sale |

---

## Checklist de autoevaluación antes de entregar

- [ ] La ficha tiene información real del cliente, no genérica ni inventada.
- [ ] Los objetivos estratégicos son específicos y verificables.
- [ ] Cada problema identificado describe un síntoma, no ya una solución técnica.
- [ ] La visión de arquitectura conecta explícitamente con los objetivos estratégicos de la Ficha.
- [ ] El mapa conceptual se mantiene a alto nivel (no reemplaza los C4/BPMN de talleres posteriores).
- [ ] Están documentadas las restricciones y qué queda fuera de alcance.
- [ ] Hay de 5 a 8 capacidades con verbo + objeto, cada una atada a un proceso de la Ficha y con su soporte tecnológico valorado con evidencia.
- [ ] Hay 3 principios en borrador con nombre, declaración e implicación, y cada uno sale de un objetivo o de una restricción de la Ficha.
- [ ] Hay una persona de contacto registrada, con rol claro frente a la solución.

---

## Vista ArchiMate equivalente

La Ficha y la Visión se traducen a la **capa de Motivación** de ArchiMate (ver la [Guía de Notación ArchiMate](https://github.com/CesarAVegaF312/AREM-ArchiMate/blob/main/guia_notacion_archimate.md) para el detalle completo): el cliente y su equipo directivo son **Stakeholders**, cada objetivo estratégico de la Ficha es un **Goal**, cada restricción es una **Constraint** y cada principio en borrador es un **Principle**. Las capacidades del paso 5 son elementos **Capability** de la **capa de Estrategia**: cada una realiza un Goal y la realizan los Business Process del Taller 1.

```mermaid
flowchart TD
    stakeholder(["Directora de Operaciones - Fundación Salud Viva"])
    driver(["Falta de integración app/ERP/telemedicina"])
    goal1(["Mejorar eficiencia operativa"])
    goal2(["Ampliar cobertura nacional"])
    constraint(["No cambiar herramientas de oficina en 2026"])
    principle(["Principio: Historia clínica única"])
    cap(["Capability: Mantener una historia clínica unificada"])

    stakeholder -.->|"identifica"| driver
    driver -->|"motiva"| goal1
    driver -->|"motiva"| goal2
    constraint -.->|"limita"| goal2
    goal1 -->|"se realiza por"| principle
    cap -->|"realiza"| goal1

    classDef motivacion fill:#ccccff,color:#000,stroke:#6666cc;
    classDef estrategia fill:#f5deb3,color:#000,stroke:#c9a227;
    class stakeholder,driver,goal1,goal2,constraint,principle motivacion
    class cap estrategia
```

Estos elementos de Motivación son los que después reciben una **Realization** desde un Business Process (Taller 1) o una **Influence** desde un Requirement de seguridad (Taller 5) o normatividad (Taller 6) — la Ficha y la Visión son el punto de partida de esa trazabilidad, no un documento aislado. Las mismas Capability reaparecen en el Taller 7 (sección 4.1) con su madurez AS-IS y TO-BE, y los Principle en la vista de Motivación del Taller 9.

---

## Parte C — Ambiente del equipo y validación técnica de la entrega (opcional)

La checklist de autoevaluación se revisa a mano, y es fácil pasar por alto una capacidad con nombre de sistema o un beneficio que no apunta a ningún objetivo. Esta parte propone dejar listo desde el primer taller el repositorio donde el equipo trabajará todo el semestre y **verificar la entrega con un comando** antes de mostrarla. No es un ejercicio de programación: el verificador ya está escrito en [`validacion-tecnica/validar_vision.py`](validacion-tecnica/validar_vision.py) y solo se ejecuta.

### C.1 Qué se necesita

- [Git](https://git-scm.com/) y una cuenta de GitHub por integrante.
- Python 3 (viene en macOS y Linux; en Windows se instala desde [python.org](https://www.python.org/downloads/)). Si no puede instalarlo, sirve [Docker Desktop](https://www.docker.com/products/docker-desktop/) (ver C.3).

### C.2 Preparar el repositorio del equipo

1. Un integrante crea en GitHub el repositorio `AREM-EquipoX-NombreCliente`, con la estructura que explica [AREM-Proyecto-Cliente](https://github.com/CesarAVegaF312/AREM-Proyecto-Cliente), y agrega a los demás como colaboradores.
2. Cada integrante lo clona: `git clone https://github.com/<usuario>/AREM-EquipoX-NombreCliente.git`.
3. Se crea la carpeta `00-preliminary-vision/` y se copian ahí las plantillas de la Ficha y de la Visión de este taller, con los nombres `ficha-caracterizacion.md` y `vision.md`.
4. Cada avance se sube con `git add`, `git commit` y `git push`. Desde el primer día queda un historial de quién cambió qué y cuándo, que es lo mismo que el Taller 9 pide al hablar de gobierno de la arquitectura.

### C.3 Correr el verificador

Primero sobre el ejemplo de clase, que ya está diligenciado con los datos de Fundación Salud Viva de esta guía. Desde la carpeta raíz de este repositorio de taller:

```bash
python3 clase/validacion-tecnica/validar_vision.py clase/validacion-tecnica/ejemplo
```

Resultado esperado: `0 faltante(s), 0 por revisar`. Luego, sobre la entrega del equipo (la ruta es la carpeta donde están `ficha-caracterizacion.md` y `vision.md`):

```bash
python3 clase/validacion-tecnica/validar_vision.py ../AREM-EquipoX-NombreCliente/00-preliminary-vision
```

Sin Python, con Docker (desde la misma carpeta raíz):

```bash
docker run --rm -v "$PWD":/trabajo -w /trabajo python:3.12-alpine python clase/validacion-tecnica/validar_vision.py clase/validacion-tecnica/ejemplo
```

### C.4 Qué revisa y qué no

| Revisión | Ítem de la checklist que respalda | Tipo de resultado |
|---|---|---|
| No quedan campos de la plantilla sin llenar en la Ficha ni en la Visión | La ficha tiene información del cliente | FALTA |
| Las seis secciones de la Ficha tienen contenido, incluidas las restricciones | Restricciones documentadas; persona de contacto registrada | FALTA o REVISAR |
| Cada beneficio esperado apunta a un objetivo de la Ficha, y cada objetivo tiene al menos un beneficio | La visión conecta con los objetivos estratégicos | REVISAR |
| El mapa conceptual existe y tiene de 4 a 6 cajas | El mapa se mantiene a alto nivel | REVISAR |
| Hay alcance y fuera de alcance | Qué queda fuera de alcance | FALTA |
| Hay de 5 a 8 capacidades, con soporte alto, medio o bajo, evidencia, y un proceso de la Ficha detrás; ninguna nombra un sistema (sistema, plataforma, app, ERP, etc.) | Capacidades con verbo + objeto, atadas a un proceso | FALTA o REVISAR |
| Hay 3 principios con nombre, declaración, implicación y origen | 3 principios en borrador | FALTA |

`FALTA` significa que algo que la guía pide no está. `REVISAR` es una alerta para que el equipo mire: el verificador compara palabras, así que puede equivocarse con sinónimos, y el equipo decide.

Lo que el verificador **no** puede revisar es lo más importante: si los datos son reales, si un problema está escrito como síntoma o como solución, y si un principio de verdad descarta algo. Eso se valida con el cliente y con el docente.

### C.5 Aplicarlo al cliente real

1. Corra el verificador sobre `00-preliminary-vision/` antes de cada revisión con el docente.
2. En `entrega/referencias.md` o en las notas del equipo, registre qué alertas `REVISAR` decidió dejar y por qué (por ejemplo, un objetivo redactado con otras palabras en la Visión).

---

## Parte D — Análisis de caso real y panorama tecnológico (opcional)

### D.1 Caso: el lanzamiento de HealthCare.gov (Estados Unidos, 2013)

**Qué pasó.** HealthCare.gov, el portal federal para comprar seguros de salud creado por la ley de salud de 2010 (Affordable Care Act), salió al aire el 1 de octubre de 2013 y falló desde el primer día: muchos usuarios no podían crear su cuenta ni completar la inscripción. Notas internas publicadas después por el Comité de Supervisión de la Cámara de Representantes indican que solo seis personas lograron inscribirse el primer día; otros documentos dan cifras distintas, pero todas muy bajas. En enero de 2014 el gobierno reemplazó al contratista principal, CGI Federal, por Accenture.

En julio de 2014, la Oficina de Rendición de Cuentas del Gobierno de Estados Unidos (GAO) concluyó en el informe GAO-14-694 que los Centros de Servicios de Medicare y Medicaid (CMS), la entidad a cargo, emprendieron el desarrollo **sin una planeación ni una supervisión efectivas**: los requisitos no estaban definidos, faltaba la estrategia de adquisición exigida, no estaba claro quién administraba los contratos y no se usaron las herramientas de supervisión disponibles. Según la cobertura del informe, el costo del portal había llegado a unos 840 millones de dólares a comienzos de 2014.

**Qué falló, en el lenguaje de este taller.**

| Elemento | Qué falló |
|---|---|
| Alcance (Visión) | Los requisitos seguían sin definirse mientras se construía: no había un "en alcance" y "fuera de alcance" estable sobre el cual trabajar. |
| Persona de contacto y responsables (Ficha, sección VI) | No estaba claro quién decidía y quién supervisaba: la GAO encontró confusión en las responsabilidades de administración de los contratos. |
| Gobierno del proyecto | Faltaba la estrategia de adquisición exigida y no se usaron las herramientas de supervisión disponibles: no había con qué comprobar, durante el proyecto, si se iba por buen camino. |

**Preguntas para el análisis.**

1. Escriba la sección "Alcance" de la Visión que habría necesitado HealthCare.gov en 2012. ¿Qué habría puesto en "fuera de alcance" para llegar a tiempo al 1 de octubre de 2013?
2. ¿Qué habría cambiado si la Ficha hubiera tenido una persona de contacto con autoridad clara para decidir? ¿Quién es esa persona en su cliente real?
3. Escriba un principio arquitectónico (nombre, declaración, implicación) que habría descartado salir al aire sin pruebas completas del sistema.

**Fuentes.** [GAO-14-694, "Healthcare.gov: Ineffective Planning and Oversight Practices Underscore the Need for Improved Contract Management" (julio de 2014)](https://www.gao.gov/products/gao-14-694); [ABC News, sobre las notas internas del primer día](https://abcnews.com/blogs/politics/2013/10/memo-reveals-only-6-people-signed-up-for-obamacare-on-first-day); [FedWeek, resumen del informe de la GAO](https://www.fedweek.com/fedweek-information-technology/gao-faults-planning-oversight-in-healthcare-gov-assessment/). El sitio de la GAO no se pudo consultar directamente al preparar esta guía; los datos del informe se tomaron de fuentes que lo citan. Las cifras de inscripciones del primer día varían según el documento.

### D.2 Panorama tecnológico: dónde se documenta y se gobierna la arquitectura

La Ficha y la Visión de este curso viven en Markdown dentro de GitHub. En una organización, ese mismo contenido suele vivir en una herramienta de arquitectura empresarial. Conocerlas ayuda a recomendarle al cliente dónde mantener lo que el equipo entregue.

| Tipo | Ejemplos | Conviene cuando | Tenga en cuenta |
|---|---|---|---|
| Modelador ArchiMate de escritorio | Archi | Una organización pequeña o un equipo que empieza; es gratuito y de código abierto, y es la herramienta del curso | Es una herramienta de modelado, no un repositorio compartido con flujos de aprobación |
| Suite de modelado multinotación | Sparx Systems Enterprise Architect | Se necesita ArchiMate, BPMN y UML en un mismo modelo | Licencia comercial; curva de aprendizaje alta |
| Plataforma de arquitectura empresarial | BiZZdesign, MEGA HOPEX | Organizaciones grandes con un área de arquitectura y requisitos de gobierno, riesgo y cumplimiento | Costo y esfuerzo de implantación altos |
| Gestión del portafolio de aplicaciones (SaaS) | LeanIX, Ardoq | Se quiere un inventario vivo de aplicaciones y capacidades, mantenido entre varias áreas | Suscripción anual; los datos quedan en la nube del proveedor |
| Repositorio y colaboración | GitHub o GitLab (documentos versionados), Confluence o Notion (wikis), Miro o Mural (talleres con el cliente) | Documentar y discutir con historial, revisión y comentarios | No validan la notación ni la consistencia del modelo |

La recomendación de herramienta también es una decisión de arquitectura: tiene que respetar las restricciones de la Ficha. En el caso de Fundación Salud Viva, por ejemplo, una herramienta que no opere en la nube choca con la restricción de "nube pública o híbrida".

### D.3 Aplicarlo al cliente real

1. Busque un caso público y documentado de un proyecto de tecnología con alcance, objetivos o responsables mal definidos, preferiblemente del sector del cliente.
2. Analícelo con la [plantilla de análisis de caso](../plantillas/plantilla_analisis_caso.md) y guárdelo en `entrega/analisis-caso.md`.
3. En la sección 5 de la plantilla, compare dos herramientas del panorama anterior para mantener la arquitectura del cliente después del curso, teniendo en cuenta sus restricciones (sección V de la Ficha).

---

_Esta guía hace parte del Taller 0 de Preliminary y Architecture Vision — curso Arquitectura Empresarial, Universidad de La Sabana._
