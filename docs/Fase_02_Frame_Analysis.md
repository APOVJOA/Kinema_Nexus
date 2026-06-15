# Fase 02 – Frame Analysis

## Objetivo

Comprender cómo representa OpenCV una imagen capturada por la cámara y analizar la información almacenada en un frame.

---

## Descripción

Tras verificar el correcto funcionamiento de la webcam en la Fase 01, el siguiente paso consistió en estudiar la estructura interna de una imagen digital capturada mediante OpenCV.

Para ello se capturó un único frame desde la cámara y se analizaron sus propiedades principales:

* Tipo de dato utilizado para almacenar la imagen.
* Dimensiones del frame.
* Número total de elementos almacenados.
* Valor de un píxel concreto.
* Separación de los canales de color BGR.

---

## Código utilizado

Archivo:

src/frame_analysis.py

El programa captura un frame de la webcam y muestra información relevante sobre su estructura interna.

---

## Resultados obtenidos

### Tipo de dato

```python
<class 'numpy.ndarray'>
```

El frame capturado se almacena como una matriz de NumPy.

---

### Dimensiones

```python
(480, 640, 3)
```

Interpretación:

* 480 filas (altura).
* 640 columnas (anchura).
* 3 canales de color.

---

### Número total de elementos

```python
921600
```

Cálculo:

480 × 640 × 3 = 921600

Cada píxel contiene tres valores asociados a los canales de color.

---

### Análisis del píxel [0,0]

Resultado obtenido:

```python
[106 108 112]
```

Este valor corresponde al píxel situado en la esquina superior izquierda de la imagen.

---

### Separación de canales

Canal Azul:

```python
106
```

Canal Verde:

```python
108
```

Canal Rojo:

```python
112
```

OpenCV utiliza el formato BGR (Blue, Green, Red) en lugar de RGB.

Los tres valores presentan intensidades similares, lo que indica que el píxel analizado corresponde a una zona con un color cercano al gris.

---

## Conceptos aprendidos

Durante esta fase se comprendieron varios conceptos fundamentales para el desarrollo del proyecto:

* Un frame es una matriz tridimensional.
* OpenCV almacena las imágenes como objetos NumPy.
* Cada píxel posee tres componentes de color.
* Los canales de color se almacenan en formato BGR.
* Es posible acceder individualmente a cualquier píxel y a cualquiera de sus canales.

---

## Conclusiones

La información visual capturada por una cámara no es más que una gran matriz numérica.

Cada posición de la matriz representa un píxel y cada píxel almacena información de color mediante tres canales independientes.

Comprender esta estructura es un paso fundamental para las siguientes fases del proyecto, donde se comenzará a localizar regiones específicas de la imagen, detectar colores y extraer información útil para controlar el robot industrial.
