# Modelo de Dominio

## Objetivo

Este documento describe las entidades principales del negocio del Sistema LPA y la forma en que se relacionan entre sí.

No representa el diseño de la base de datos.

---

# Área

## Descripción

Representa un área de producción donde el Departamento de Calidad realiza auditorías.

## Ejemplos

- Ensamble Final
- Pulido

## Responsabilidades

- Identificar dónde se realiza una auditoría.
- Agrupar las auditorías correspondientes a esa área.

## Relaciones

- Puede tener cero o varias células.
- Puede tener una o varias auditorías.

---

# Célula

## Descripción

Representa una línea o célula de producción dentro de un área.

No todas las áreas utilizan células.

## Ejemplos

Ensamble Final

- Célula 1
- Célula 2
- ...
- Célula 7

Pulido

- Célula A
- Célula B

## Responsabilidades

- Identificar el lugar específico donde se ejecuta una auditoría.

## Relaciones

- Pertenece a un Área.
- Puede estar asociada a múltiples ejecuciones de auditoría.

---

# Capa

## Descripción

Representa el nivel jerárquico dentro del proceso LPA.

## Capas

- Auditor
- Supervisor
- Gerente

## Responsabilidades

Determinar el tipo de auditoría que debe realizarse.

## Relaciones

- Una capa puede tener una o varias auditorías.

---

# Auditoría

## Descripción

Define una auditoría disponible dentro del sistema.

Una auditoría contiene los criterios que deben verificarse.

Cada auditoría pertenece a una capa y, cuando aplica, a un área específica.

## Ejemplos

- Auditoría Ensamble Final
- Auditoría Pulido
- Auditoría Supervisor
- Auditoría Gerente

## Responsabilidades

- Definir los criterios de evaluación.
- Definir la frecuencia de ejecución.
- Determinar la capa responsable.

## Relaciones

- Pertenece a una Capa.
- Puede pertenecer a un Área.
- Contiene múltiples criterios.
- Puede ejecutarse múltiples veces.

---

# Criterio

## Descripción

Representa un punto de inspección dentro de una auditoría.

Cada criterio corresponde a un aspecto que debe verificarse durante la ejecución.

## Ejemplos

- Se realiza la inspección Check Do Check.
- La estación de trabajo se mantiene limpia.
- Se realiza la prueba de sonido.

## Responsabilidades

Definir qué debe inspeccionarse durante una auditoría.

## Relaciones

- Pertenece a una Auditoría.
- Puede tener múltiples respuestas a lo largo del tiempo.

---

# Ejecución de Auditoría

## Descripción

Representa una auditoría realizada por un usuario en una fecha determinada.

Cada ejecución conserva su propio historial de respuestas.

## Responsabilidades

- Registrar quién realizó la auditoría.
- Registrar la fecha.
- Registrar observaciones generales.
- Conservar el historial.

## Relaciones

- Pertenece a una Auditoría.
- Es realizada por un Usuario.
- Contiene múltiples respuestas.
- Puede generar hallazgos.

---

# Respuesta

## Descripción

Representa el resultado obtenido para un criterio durante una ejecución de auditoría.

## Valores posibles

- Verde
- Amarillo
- Rojo
- No aplica

## Responsabilidades

Registrar el resultado observado para cada criterio.

## Relaciones

- Pertenece a una Ejecución de Auditoría.
- Pertenece a un Criterio.
- Puede generar un Hallazgo.

---

# Hallazgo

## Descripción

Representa una desviación detectada durante una auditoría.

Su registro depende del criterio del auditor.

No toda respuesta en rojo genera obligatoriamente un hallazgo.

## Responsabilidades

- Registrar la desviación.
- Asociar evidencia.
- Registrar responsables.

## Relaciones

- Pertenece a una Respuesta.
- Puede tener múltiples evidencias.
- Puede tener múltiples responsables.

---

# Evidencia

## Descripción

Representa archivos asociados a un hallazgo.

Inicialmente el sistema solo manejará fotografías.

## Responsabilidades

Documentar visualmente un hallazgo.

## Relaciones

- Pertenece a un Hallazgo.

---

# Usuario

## Descripción

Representa una persona que utiliza el sistema.

## Roles

- Administrador
- Auditor
- Supervisor
- Gerente

## Responsabilidades

- Iniciar sesión.
- Ejecutar auditorías.
- Consultar información.

## Relaciones

- Puede estar asignado a múltiples áreas.
- Puede realizar múltiples ejecuciones de auditoría.

---

# Relaciones del dominio

Usuario
│
├── realiza
▼
Ejecución de Auditoría
│
├── pertenece a
▼
Auditoría
│
├── pertenece a una Capa
├── puede pertenecer a un Área
└── contiene Criterios
│
▼
Respuesta
│
▼
Hallazgo
│
▼
Evidencia

Área
│
└── puede contener
│
▼
Célula
