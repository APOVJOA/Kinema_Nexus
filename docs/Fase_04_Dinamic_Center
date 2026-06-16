# Fase 04 - Cálculo Dinámico del Centro

## Objetivo

Aprender a calcular automáticamente el centro de una imagen utilizando sus dimensiones reales.

---

## Descripción

Hasta esta fase, el acceso a posiciones concretas de la imagen se realizaba utilizando coordenadas fijas.

Por ejemplo:

```python
frame[240,320]
```

Sin embargo, estas coordenadas solo son válidas para una resolución específica.

En esta fase se utilizaron las dimensiones obtenidas mediante `frame.shape` para calcular automáticamente el centro de cualquier imagen, independientemente de su tamaño.

---

## Conceptos Aprendidos

### Obtención de dimensiones

OpenCV permite conocer las dimensiones de una imagen mediante:

```python
frame.shape
```

El resultado sigue la estructura:

```python
(alto, ancho, canales)
```

Por ejemplo:

```python
(480, 640, 3)
```

Donde:

* Alto = 480 píxeles
* Ancho = 640 píxeles
* Canales = 3 (BGR)

---

### Cálculo del centro

Una vez obtenidas las dimensiones, el centro puede calcularse de forma automática:

```python
centro_y = alto // 2
centro_x = ancho // 2
```

De esta forma, el programa puede localizar el centro de cualquier imagen sin necesidad de conocer previamente su resolución.

---

## Logros Alcanzados

Al finalizar esta fase se consiguió:

* Obtener las dimensiones reales de una imagen.
* Calcular coordenadas dinámicamente.
* Localizar el centro de cualquier frame.
* Escribir código independiente de la resolución de la cámara.
* Comprender la diferencia entre coordenadas fijas y coordenadas calculadas.

---

## Aplicación en Kinema Nexus

En futuras fases será necesario comparar posiciones de objetos respecto al centro de la imagen.

Este cálculo permitirá:

* Saber si un objeto está a la izquierda o a la derecha.
* Medir desplazamientos respecto al centro.
* Establecer referencias geométricas para el seguimiento de objetos.
* Preparar la conversión de coordenadas de imagen a coordenadas robóticas.

---

## Conclusión

Esta fase introdujo el concepto de geometría dinámica dentro de una imagen.

En lugar de trabajar con coordenadas fijas, el sistema pasó a calcular automáticamente posiciones de referencia utilizando las dimensiones reales del frame, permitiendo que el código funcione correctamente con cualquier resolución.
