# Fase 05 - Región de Interés (ROI)

## Objetivo

Aprender a seleccionar y analizar únicamente una región específica de una imagen en lugar de procesar el frame completo.

---

## Descripción

Hasta esta fase, el análisis se realizaba sobre la totalidad de la imagen capturada por la cámara. Sin embargo, en muchos sistemas de visión artificial no es necesario procesar todos los píxeles del frame.

Para optimizar el análisis, se introdujo el concepto de ROI (Region Of Interest), una técnica que permite seleccionar únicamente una zona concreta de la imagen para trabajar sobre ella.

La ROI se obtiene mediante el uso de slicing de NumPy, definiendo límites de filas y columnas que delimitan una región rectangular dentro del frame original.

---

## Conceptos Aprendidos

### ROI (Region Of Interest)

Una ROI es una subimagen extraída de una imagen principal.

Ejemplo:

```python
roi = frame[100:200, 300:400]
```

Este código selecciona todos los píxeles comprendidos entre:

* Filas 100 a 199
* Columnas 300 a 399

---

### Slicing de imágenes

Las imágenes pueden dividirse utilizando la misma sintaxis empleada para trabajar con matrices NumPy.

```python
frame[inicio_y:fin_y, inicio_x:fin_x]
```

donde:

* inicio_y y fin_y delimitan las filas.
* inicio_x y fin_x delimitan las columnas.

---

### ROI dinámica

En lugar de utilizar coordenadas fijas, se calculó una ROI centrada dinámicamente en la imagen.

```python
centro_y = alto // 2
centro_x = ancho // 2
```

Posteriormente se definieron los límites:

```python
inicio_y = centro_y - 50
fin_y = centro_y + 50

inicio_x = centro_x - 50
fin_x = centro_x + 50
```

---

### Tamaño de la ROI

El tamaño de la región depende de la distancia que se suma y resta respecto al centro.

Ejemplos:

* ±50 → ROI de 100×100
* ±100 → ROI de 200×200
* ±150 → ROI de 300×300

---

### Control de límites

Se identificó la necesidad de verificar que los límites de la ROI permanezcan dentro de las dimensiones reales de la imagen.

Condiciones generales:

```python
inicio_y >= 0
fin_y <= alto

inicio_x >= 0
fin_x <= ancho
```

Esto evita acceder a zonas inexistentes del frame.

---

## Logros Alcanzados

* Comprensión del concepto de ROI.
* Uso de slicing para extraer regiones de una imagen.
* Construcción de una ROI centrada dinámicamente.
* Modificación del tamaño de la ROI mediante parámetros.
* Comprensión de los límites físicos de una imagen.
* Introducción al concepto de Boundary Checking.

---

## Aplicación en Kinema Nexus

Las ROI serán fundamentales para optimizar futuros procesos de visión artificial.

Permitirá:

* Analizar únicamente zonas relevantes.
* Reducir la cantidad de información procesada.
* Mejorar el rendimiento de algoritmos de detección.
* Facilitar el seguimiento de objetos.
* Servir como base para el control visual del robot.

En fases posteriores, las ROI se utilizarán para localizar objetos, calcular desplazamientos respecto al centro de referencia y generar coordenadas útiles para la integración con RoboDK y sistemas robóticos reales.

---

## Conclusión

La Fase 05 introduce una de las herramientas más utilizadas en visión artificial: las Regiones de Interés (ROI).

Gracias a esta técnica es posible concentrar el análisis en áreas específicas de una imagen, reduciendo la complejidad del procesamiento y preparando el sistema para futuras tareas de detección, seguimiento y control robótico.

Esta fase representa la transición desde el análisis de píxeles individuales hacia el análisis de regiones completas de imagen.
