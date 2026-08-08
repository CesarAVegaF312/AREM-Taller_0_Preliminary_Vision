# 🛠️ Taller 0: Preliminary y Architecture Vision

## 🎯 Objetivo

Establecer el alcance, el contexto estratégico y la visión de alto nivel de la arquitectura del cliente real — fases **Preliminary** y **Architecture Vision** de TOGAF ADM — como base para todo el trabajo del semestre. Lo que se defina aquí es lo que heredan todos los talleres siguientes: si el alcance queda mal definido, el error se arrastra hasta la presentación final.

⏰ **Este taller corresponde al cierre del Corte 1 (14 de agosto), junto con el Taller 1 (Business Architecture) y el Taller 2 (Datos AS-IS).**

---

## 📘 Guía paso a paso

Antes de reunirse con el cliente, revise la [**Guía Paso a Paso: Preliminary y Architecture Vision**](clase/guia_paso_a_paso_preliminary_vision.md). Incluye la metodología para construir la Ficha de Caracterización y el Documento de Visión, un ejemplo completo tomado del material oficial del curso (Fundación Salud Viva), y una tabla de errores comunes.

## 🏥 Caso base de referencia: Fundación Salud Viva

Este es el ejemplo oficial de ficha de caracterización distribuido en `Material/Proyecto` del curso. Úselo como referencia de formato y de profundidad — no lo copie para su cliente real.

**Contexto:** Fundación Salud Viva es una entidad de salud (atención domiciliaria y telemedicina) que quiere integrar su app móvil, su ERP y su plataforma de telemedicina, ampliar cobertura nacional y mejorar su cumplimiento normativo en el manejo de datos clínicos.

---

## 🧪 Parte 1: Trabajo en Clase

Durante la clase se espera que el equipo:

Siga la [guía paso a paso](clase/guia_paso_a_paso_preliminary_vision.md) para entender la estructura de ambos entregables sobre el caso de Fundación Salud Viva:

1. Identifique cómo se traduce cada objetivo estratégico de la Ficha en un elemento de la Visión.
2. Distinga un problema (síntoma) de una solución ya decidida en la sección de necesidades.
3. Revise por qué el mapa conceptual de la Visión se mantiene deliberadamente a alto nivel.
4. Valide el ejemplo contra la [checklist de autoevaluación](clase/guia_paso_a_paso_preliminary_vision.md#checklist-de-autoevaluación-antes-de-entregar).

- Reciba retroalimentación del docente y registre avances en `clase/notas.md` (use la [plantilla de notas](plantillas/plantilla_notas.md)).

---

## 🧠 Parte 2: Aplicación al Cliente Real

Antes del cierre del Corte 1, el equipo debe:

- Reunirse con el cliente real y diligenciar la Ficha de Caracterización en `entrega/ficha-caracterizacion.md` (use la [plantilla de ficha](plantillas/plantilla_ficha_caracterizacion.md), con la misma estructura del formato oficial en Word).
- Redactar el Documento de Visión en `entrega/vision.md` (use la [plantilla de visión](plantillas/plantilla_vision.md)): mapa conceptual de alto nivel, beneficios esperados trazados a los objetivos estratégicos, y alcance del proyecto.
- Registrar cualquier fuente consultada en `entrega/referencias.md` con la [plantilla de referencias](plantillas/plantilla_referencias.md).

---

## 📁 Estructura esperada del repositorio

```text
taller-00-preliminary-vision/
├── README.md
├── clase/
│   ├── guia_paso_a_paso_preliminary_vision.md   # Metodología y ejemplo guiado (Ficha + Visión)
│   └── notas.md                                 # Ver plantillas/plantilla_notas.md
├── entrega/
│   ├── ficha-caracterizacion.md                 # Ver plantillas/plantilla_ficha_caracterizacion.md
│   ├── vision.md                                # Ver plantillas/plantilla_vision.md
│   └── referencias.md                           # Ver plantillas/plantilla_referencias.md
└── plantillas/
    ├── plantilla_ficha_caracterizacion.md
    ├── plantilla_vision.md
    ├── plantilla_notas.md
    └── plantilla_referencias.md
```

---

## ⚠️ Errores comunes

Antes de entregar, compare su ficha y su visión contra los errores más frecuentes (respuestas genéricas, problemas redactados como soluciones, visión sin conexión con los objetivos estratégicos, mapa conceptual demasiado detallado) documentados en la [sección de errores comunes de la guía paso a paso](clase/guia_paso_a_paso_preliminary_vision.md#errores-comunes-a-evitar).

## 📤 Entregables

- Ficha de Caracterización del Cliente
- Documento de Visión de Arquitectura (con mapa conceptual de alto nivel)
- Referencias, si aplica investigación de sector

---

## 📊 Rúbrica de Evaluación

| Criterio                              | Excelente (5)                                                              | Aceptable (3) / Insuficiente (1–2)                         |
|----------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------|
| Ficha de caracterización                | Información completa, específica y verificada con el cliente real            | Genérica, incompleta o sin contacto real con el cliente         |
| Objetivos estratégicos y problemas      | Objetivos verificables; problemas descritos como síntomas, no soluciones      | Objetivos vagos o problemas presentados ya como solución técnica |
| Visión de arquitectura                  | Conecta claramente los beneficios esperados con los objetivos estratégicos    | Visión desconectada de la ficha o genérica                      |
| Alcance y restricciones                 | Alcance y restricciones explícitos y realistas                                | Alcance ambiguo o no declarado                                  |

---

## ✅ Licencia

Este taller hace parte del curso de Arquitectura Empresarial - Universidad de La Sabana. Uso académico bajo licencia MIT.
