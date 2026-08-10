# Kinema Nexus - Mejoras Futuras y Pendientes

## Objetivo

Este documento recoge funcionalidades, mejoras y líneas de investigación que pueden resultar interesantes para Kinema Nexus, pero que **no forman parte del roadmap principal de desarrollo**.

El objetivo es evitar que estas mejoras interrumpan el desarrollo del sistema principal.

Durante el desarrollo del roadmap se priorizará exclusivamente alcanzar la versión integrada y funcional definida en las fases actuales.

Una vez completado el roadmap, estas propuestas podrán revisarse y priorizarse para futuras versiones del proyecto.

---

# Criterio de inclusión

Una propuesta debe añadirse a este documento cuando:

* Sea técnicamente interesante.
* Pueda mejorar el sistema.
* Requiera una investigación o desarrollo adicional considerable.
* No sea necesaria para completar el roadmap actual.
* Pueda provocar una desviación significativa del desarrollo previsto.

**Regla principal:**

> Si una mejora no es necesaria para alcanzar el objetivo de la fase actual, se documenta y se continúa con el roadmap.

---

# Mejoras futuras

## 01 - Entrenamiento de un modelo YOLO específico para Kinema Nexus

### Descripción

Entrenar un modelo de detección de pose específicamente adaptado a las condiciones de uso de Kinema Nexus.

El modelo actual utiliza un modelo YOLO Pose generalista. En futuras versiones podría desarrollarse un modelo especializado para las condiciones concretas del sistema.

### Posibles mejoras

* Mayor precisión en hombros, codos y muñecas.
* Mejor comportamiento con brazos extendidos.
* Reducción de detecciones incorrectas.
* Mejor funcionamiento con oclusiones.
* Adaptación a diferentes posiciones del usuario.
* Adaptación a las condiciones visuales del entorno quirúrgico.

### Motivo para posponerlo

El modelo actual es suficiente para continuar desarrollando la arquitectura principal del sistema.

El entrenamiento de un modelo propio no es necesario para completar el roadmap actual.

**Estado:** Pendiente después del roadmap.

---

# 02 - Sistema de visión 3D

### Descripción

Investigar la utilización de información de profundidad para obtener posiciones tridimensionales del brazo humano.

El sistema actual trabaja principalmente con coordenadas obtenidas a partir de una imagen 2D.

Una futura versión podría incorporar información de profundidad para obtener:

```text
X
Y
Z
```

en lugar de trabajar únicamente con:

```text
X
Y
```

### Posibles soluciones

* Cámara RGB-D.
* Sistemas de profundidad.
* Estéreo mediante dos cámaras.
* Reconstrucción 3D.
* Otros sistemas de estimación de profundidad.

### Motivo para posponerlo

El objetivo actual es desarrollar el sistema utilizando una única cámara y completar el pipeline previsto.

La incorporación de visión 3D aumentaría considerablemente la complejidad del proyecto.

**Estado:** Pendiente después del roadmap.

---

# 03 - Calibración avanzada de cámara

### Descripción

Desarrollar un sistema avanzado de calibración que permita transformar las coordenadas obtenidas por la cámara en coordenadas físicas del espacio de trabajo.

### Posibles mejoras

* Calibración intrínseca de la cámara.
* Calibración extrínseca.
* Corrección de distorsión.
* Conversión de píxeles a unidades físicas.
* Definición automática del sistema de referencia.

### Motivo para posponerlo

La primera versión del sistema puede desarrollarse utilizando el sistema de referencia y las técnicas de calibración definidas dentro del roadmap.

Las técnicas avanzadas podrán incorporarse posteriormente.

**Estado:** Pendiente después del roadmap.

---

# 04 - Filtrado y estabilización avanzada de landmarks

### Descripción

Implementar técnicas avanzadas para reducir el ruido y las oscilaciones producidas por la detección de pose.

### Posibles mejoras

* Filtros temporales.
* Media móvil.
* Filtro de Kalman.
* Interpolación de posiciones perdidas.
* Predicción de movimiento.
* Detección de movimientos físicamente imposibles.

### Motivo para posponerlo

Durante el desarrollo inicial se utilizarán las coordenadas proporcionadas directamente por YOLO y las validaciones geométricas desarrolladas dentro del roadmap.

Los sistemas de filtrado avanzado se estudiarán posteriormente.

**Estado:** Pendiente después del roadmap.

---

# 05 - Sistema avanzado de validación de pose

### Descripción

Desarrollar un sistema capaz de determinar si una pose detectada es físicamente coherente antes de utilizarla para controlar el robot.

### Posibles comprobaciones

* Longitud relativa de los segmentos del brazo.
* Límites articulares.
* Velocidad máxima de movimiento.
* Continuidad temporal.
* Coherencia entre landmarks.
* Detecciones duplicadas o incorrectas.

### Motivo para posponerlo

El roadmap actual ya contempla el análisis geométrico necesario para desarrollar una primera versión funcional.

Las técnicas avanzadas podrán añadirse posteriormente.

**Estado:** Pendiente después del roadmap.

---

# 06 - Sistema de detección de herramienta quirúrgica

### Descripción

Desarrollar un sistema específico para detectar y seguir la herramienta utilizada por el usuario.

La herramienta podría convertirse posteriormente en el principal elemento de referencia para el movimiento del robot.

### Posibles mejoras

* Detección mediante visión artificial.
* Seguimiento de la herramienta.
* Estimación de orientación.
* Detección de pérdida de herramienta.
* Cambio automático entre herramienta y mano como referencia.

### Motivo para posponerlo

La primera versión del sistema se centrará en la detección y análisis del brazo humano.

La integración completa de la herramienta se realizará posteriormente si se determina necesaria.

**Estado:** Pendiente después del roadmap.

---

# 07 - Optimización de rendimiento

### Descripción

Optimizar el sistema para conseguir una mayor frecuencia de procesamiento y una menor latencia.

### Posibles mejoras

* Optimización de inferencia YOLO.
* Uso de GPU.
* Reducción de resolución cuando sea posible.
* Procesamiento paralelo.
* Optimización de comunicación.
* Reducción de latencia entre visión y robot.

**Estado:** Pendiente después del roadmap.

---

# 08 - Sistema de seguridad avanzado

### Descripción

Desarrollar mecanismos adicionales para garantizar que una detección incorrecta nunca provoque un movimiento peligroso del robot.

### Posibles mejoras

* Límites de movimiento.
* Zonas prohibidas.
* Parada automática.
* Watchdog.
* Validación de comandos.
* Supervisión de comunicación.
* Estado seguro ante pérdida de detección.

**Estado:** Pendiente después del roadmap.

---

# 09 - Mejoras futuras no clasificadas

Este apartado se utilizará para registrar nuevas ideas que aparezcan durante el desarrollo pero que no sean necesarias para completar el roadmap.

Cada propuesta deberá incluir:

* Descripción.
* Beneficio esperado.
* Complejidad aproximada.
* Motivo para posponerla.
* Estado.

---

# Regla de desarrollo

Kinema Nexus seguirá el roadmap principal hasta completar el sistema integrado.

Las mejoras incluidas en este documento **no deben incorporarse al desarrollo principal salvo que se determine que son imprescindibles para completar una fase del roadmap**.

Si durante el desarrollo aparece una nueva idea:

```text
¿Es necesaria para completar el roadmap?
        │
       NO
        ↓
Registrar en este documento
        ↓
Continuar con el roadmap
```

De esta forma, el proyecto mantiene un alcance controlado y, una vez completada la versión principal, se dispone de una lista organizada de posibles mejoras para futuras versiones.

---

# Objetivo posterior al roadmap

Una vez completada la última fase del roadmap:

1. Revisar todas las mejoras pendientes.
2. Evaluar su dificultad y beneficio.
3. Priorizar las más importantes.
4. Crear un nuevo roadmap de evolución.
5. Implementar las mejoras de forma progresiva.

**Kinema Nexus v1 → Roadmap principal**

**Kinema Nexus v2 → Mejoras y evolución futura**
