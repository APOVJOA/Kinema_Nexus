# Fase 09 - Color Spaces

## Objetivo

Comprender los diferentes espacios de color utilizados en visión artificial, especialmente BGR y HSV, y preparar la base necesaria para la detección robusta de colores.

---

## Descripción

Hasta este punto del proyecto, todas las imágenes capturadas por OpenCV se han procesado utilizando el espacio de color BGR.

Cada píxel de la imagen está compuesto por tres canales:

```text
[B, G, R]
```

donde:

* B = Blue (Azul)
* G = Green (Verde)
* R = Red (Rojo)

Aunque este formato es adecuado para representar imágenes, no resulta el más práctico para detectar colores específicos.

Por este motivo, OpenCV permite convertir una imagen a otros espacios de color más adecuados para tareas de visión artificial.

En esta fase se introduce el espacio HSV.

---

## Conversión de BGR a HSV

La conversión se realiza mediante:

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

### ¿Qué hace esta función?

La función no modifica la imagen original.

Tampoco calcula medias, promedios o análisis estadísticos.

Simplemente transforma cada píxel de la imagen desde el espacio BGR al espacio HSV.

Conceptualmente:

```text
Frame original (BGR)
        ↓
cv2.cvtColor(...)
        ↓
Frame convertido (HSV)
```

La estructura de la imagen permanece intacta:

```text
Alto × Ancho × 3 canales
```

Únicamente cambia el significado de los tres canales.

---

## Comparación entre BGR y HSV

Un mismo píxel puede representarse de dos formas distintas:

```text
BGR:
[144, 156, 180]
```

```text
HSV:
[10, 51, 180]
```

Ambos conjuntos de datos describen exactamente el mismo píxel.

La diferencia está en la forma de representar el color.

---

## El espacio de color HSV

HSV significa:

```text
H = Hue
S = Saturation
V = Value
```

---

### Hue (H)

Representa el tono o tipo de color.

Permite distinguir entre:

* Rojo
* Amarillo
* Verde
* Azul
* Morado

En OpenCV el canal H utiliza valores entre:

```text
0 → 179
```

Ejemplos aproximados:

```text
0   → Rojo
15  → Naranja
30  → Amarillo
60  → Verde
120 → Azul
150 → Morado
```

El canal Hue es el más importante para la detección de colores.

---

### Saturation (S)

Representa la intensidad del color.

Valores típicos:

```text
0   → Gris
255 → Color totalmente saturado
```

Cuanto mayor sea la saturación, más intenso será el color.

Valores bajos indican colores apagados o cercanos al gris.

---

### Value (V)

Representa el brillo.

Valores típicos:

```text
0   → Negro
255 → Máximo brillo
```

Este canal permite diferenciar zonas oscuras y zonas iluminadas.

---

## Interpretación de un píxel HSV

Ejemplo:

```text
[10, 51, 180]
```

Interpretación:

```text
H = 10
→ Tono rojizo-anaranjado

S = 51
→ Color poco saturado

V = 180
→ Región relativamente brillante
```

De esta forma resulta más sencillo comprender el color real del píxel.

---

## Conservación de la estructura de la imagen

Una de las características más importantes de la conversión es que la imagen mantiene exactamente la misma estructura.

Por tanto, todas las técnicas aprendidas en fases anteriores siguen siendo válidas.

Por ejemplo:

### Acceso a un píxel

```python
frame[y, x]
```

puede convertirse en:

```python
hsv[y, x]
```

---

### Extracción de una ROI

```python
roi = frame[y1:y2, x1:x2]
```

puede convertirse en:

```python
roi_hsv = hsv[y1:y2, x1:x2]
```

---

### Cálculo de medias

En BGR:

```python
b_medio, g_medio, r_medio = roi.mean(axis=(0,1))
```

En HSV:

```python
h_medio, s_medio, v_medio = roi_hsv.mean(axis=(0,1))
```

La operación es exactamente la misma.

Lo único que cambia es el significado de los canales.

---

## ¿Por qué HSV es útil para detectar colores?

En BGR, un mismo objeto puede presentar valores muy diferentes dependiendo de la iluminación.

Por ejemplo, un objeto rojo puede producir valores distintos si:

* Está iluminado por una lámpara.
* Se encuentra en sombra.
* Recibe luz solar directa.

Sin embargo, en HSV el tono (Hue) permanece mucho más estable.

Por este motivo la mayoría de sistemas de detección de color utilizan HSV en lugar de BGR.

---

## Logros Alcanzados

* Comprensión del espacio de color BGR.
* Introducción al espacio de color HSV.
* Conversión entre espacios de color mediante OpenCV.
* Comprensión de los canales H, S y V.
* Interpretación de valores HSV.
* Comprensión de que la estructura de la imagen permanece inalterada tras la conversión.
* Reutilización de técnicas de ROI y análisis sobre imágenes HSV.

---

## Aplicación en Kinema Nexus

La detección de colores será una capacidad fundamental en las siguientes fases del proyecto.

Gracias al espacio HSV será posible:

* Detectar objetos por color.
* Aislar regiones específicas de la imagen.
* Obtener coordenadas de objetos.
* Realizar seguimiento visual más robusto frente a cambios de iluminación.

La comprensión de HSV constituye la base necesaria para los futuros sistemas de detección y seguimiento visual de Kinema Nexus.

---

## Conclusión

La Fase 09 introduce los espacios de color como herramienta fundamental de la visión artificial.

Mediante la conversión de BGR a HSV se obtiene una representación más adecuada para trabajar con colores.

Aunque la información visual sigue siendo la misma, la interpretación de los datos cambia significativamente, permitiendo desarrollar sistemas de detección mucho más robustos y eficientes.
