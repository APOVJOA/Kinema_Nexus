# Kinema Nexus - Roadmap de Desarrollo

## Objetivo Final

Desarrollar un sistema de visión artificial capaz de capturar información visual mediante una cámara, procesarla con Python y OpenCV, y utilizar esa información para controlar un brazo robótico a través de RoboDK y ESP32.

---

# BLOQUE 1 - Fundamentos de Visión Artificial

Objetivo:

Comprender cómo OpenCV captura y representa una imagen digital.

---

## Fase 01 - Camera Test

Estado: Completada

Objetivo:

Verificar la conexión entre Python y la cámara.

Resultados esperados:

* Captura de vídeo en tiempo real.
* Apertura correcta de la webcam.
* Gestión básica de errores.
* Liberación correcta de recursos.

---

## Fase 02 - Frame Analysis

Estado: Completada

Objetivo:

Comprender cómo OpenCV almacena una imagen.

Resultados esperados:

* Entender qué es un frame.
* Analizar dimensiones de la imagen.
* Comprender la estructura NumPy.
* Analizar canales BGR.
* Leer información de píxeles individuales.

---

## Fase 03 - Pixel Navigation

Estado: Completada

Objetivo:

Aprender a desplazarse dentro de una imagen mediante coordenadas.

Resultados esperados:

* Comprender el sistema fila-columna.
* Localizar cualquier píxel de la imagen.
* Interpretar posiciones dentro del frame.
* Relacionar coordenadas con posiciones visuales.

---

# BLOQUE 2 - Geometría de Imagen

Objetivo:

Trabajar con posiciones y regiones dentro de la imagen.

---

## Fase 04 - Dynamic Image Center

Objetivo:

Calcular automáticamente el centro de cualquier imagen.

Resultados esperados:

* Obtener dimensiones dinámicamente.
* Calcular coordenadas centrales.
* Adaptar el código a diferentes resoluciones.

---

## Fase 05 - Regions of Interest (ROI)

Objetivo:

Trabajar únicamente sobre zonas específicas de la imagen.

Resultados esperados:

* Recortar regiones.
* Analizar áreas concretas.
* Reducir información innecesaria.

---

## Fase 06 - Pixel Area Analysis

Objetivo:

Analizar grupos de píxeles en lugar de un único píxel.

Resultados esperados:

* Comprender vecindarios.
* Preparar futuras detecciones.

---

# BLOQUE 3 - Manipulación de Imagen

Objetivo:

Modificar visualmente la imagen para depuración y validación.

---

## Fase 07 - Visual Markers

Objetivo:

Mostrar información visual sobre la imagen.

Resultados esperados:

* Dibujar puntos.
* Dibujar líneas.
* Dibujar rectángulos.
* Mostrar coordenadas.

---

## Fase 08 - Coordinate Tracking

Objetivo:

Representar posiciones detectadas visualmente.

Resultados esperados:

* Marcar centros.
* Mostrar coordenadas en pantalla.
* Validar detecciones.

---

# BLOQUE 4 - Procesamiento de Color

Objetivo:

Extraer información útil basada en colores.

---

## Fase 09 - Color Spaces

Objetivo:

Comprender RGB, BGR y HSV.

Resultados esperados:

* Diferenciar espacios de color.
* Preparar detección robusta.

---

## Fase 10 - Color Detection

Objetivo:

Detectar colores específicos.

Resultados esperados:

* Detectar objetos por color.
* Obtener coordenadas de objetos.

---

## Fase 11 - Object Localization

Objetivo:

Determinar la posición exacta de un objeto.

Resultados esperados:

* Centro del objeto.
* Coordenadas X/Y.
* Tamaño aproximado.

---

# BLOQUE 5 - Seguimiento de Objetos

Objetivo:

Detectar objetos en movimiento.

---

## Fase 12 - Object Tracking

Objetivo:

Seguir un objeto entre frames.

Resultados esperados:

* Seguimiento continuo.
* Actualización de coordenadas.

---

## Fase 13 - Motion Analysis

Objetivo:

Analizar desplazamientos.

Resultados esperados:

* Dirección.
* Velocidad relativa.
* Trayectoria.

---

# BLOQUE 6 - Integración con RoboDK

Objetivo:

Transformar visión artificial en movimiento robótico.

---

## Fase 14 - Coordinate Mapping

Objetivo:

Convertir coordenadas de imagen en coordenadas del robot.

Resultados esperados:

* Relación cámara-robot.
* Sistema de referencia.

---

## Fase 15 - RoboDK Communication

Objetivo:

Enviar posiciones a RoboDK.

Resultados esperados:

* Movimiento virtual.
* Simulación controlada.

---

## Fase 16 - Visual Servoing Basic

Objetivo:

Mover el robot utilizando información visual.

Resultados esperados:

* Seguimiento automático de objetivos.

---

# BLOQUE 7 - Hardware Real

Objetivo:

Salir de la simulación y controlar hardware.

---

## Fase 17 - ESP32 Communication

Objetivo:

Comunicar Python con ESP32.

Resultados esperados:

* Envío de coordenadas.
* Recepción de comandos.

---

## Fase 18 - Robot Control

Objetivo:

Mover el brazo físico.

Resultados esperados:

* Movimiento real.
* Respuesta a eventos visuales.

---

# BLOQUE 8 - Interacción Humana

Objetivo:

Controlar el sistema mediante gestos.

---

## Fase 19 - Hand Detection

Objetivo:

Detectar la mano del usuario.

Resultados esperados:

* Posición de la mano.
* Seguimiento básico.

---

## Fase 20 - Gesture Control

Objetivo:

Interpretar gestos.

Resultados esperados:

* Comandos mediante movimientos.
* Interacción humano-robot.

---

# Resultado Final

Sistema completo capaz de:

* Capturar vídeo.
* Analizar imágenes.
* Detectar objetos.
* Calcular posiciones.
* Controlar un brazo robótico.
* Interactuar con usuarios mediante visión artificial.
