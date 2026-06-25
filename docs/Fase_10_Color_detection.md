# Fase 10 - Color Detection

## Objetivo

Detectar colores específicos dentro de una imagen utilizando el espacio de color HSV.

---

## Descripción

En la Fase 09 se introdujo el espacio de color HSV y se estudió cómo representa OpenCV los colores mediante los canales:

```text
H = Hue (tono)
S = Saturation (saturación)
V = Value (brillo)
```

En esta fase se utiliza esa información para realizar la primera detección visual real del proyecto.

El objetivo consiste en identificar todos los píxeles que pertenecen a un determinado color y diferenciarlos del resto de la imagen.

---

## Concepto de Detección por Color

Detectar un color consiste en responder a la siguiente pregunta para cada píxel de la imagen:

```text
¿Pertenece este píxel al color que estoy buscando?
```

Si la respuesta es sí:

```text
255 (blanco)
```

Si la respuesta es no:

```text
0 (negro)
```

El resultado es una imagen binaria denominada máscara.

---

## Conversión a HSV

Antes de detectar colores, la imagen debe convertirse desde BGR a HSV:

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

Esta operación:

* No modifica la imagen original.
* No calcula medias.
* No realiza análisis estadísticos.
* No altera las dimensiones de la imagen.

Simplemente convierte cada píxel desde:

```text
[B, G, R]
```

a:

```text
[H, S, V]
```

La estructura de la imagen permanece exactamente igual.

---

## Definición de Rangos

Una vez convertida la imagen a HSV, se define un rango de valores que representan el color que se desea detectar.

Ejemplo para rojo:

```python
rojo_bajo = np.array([0, 100, 100])
rojo_alto = np.array([10, 255, 255])
```

---

## Interpretación del Rango

### Límite inferior

```python
[0, 100, 100]
```

Significa:

```text
Hue        >= 0
Saturation >= 100
Value      >= 100
```

---

### Límite superior

```python
[10, 255, 255]
```

Significa:

```text
Hue        <= 10
Saturation <= 255
Value      <= 255
```

---

## ¿Por qué se utiliza el rango 0-10?

En OpenCV, el canal Hue utiliza valores comprendidos entre:

```text
0 y 179
```

Cada rango representa una familia de colores.

Ejemplos aproximados:

```text
0   → Rojo
15  → Naranja
30  → Amarillo
60  → Verde
120 → Azul
150 → Morado
```

Por este motivo:

```python
[0, 100, 100]
```

hasta

```python
[10, 255, 255]
```

representa una región cercana al rojo.

El detector busca todos los píxeles cuyo tono se encuentre dentro de ese intervalo.

---

## ¿Por qué se utilizan 100 y 255 en Saturación y Brillo?

Los canales Saturation y Value permiten eliminar ruido visual.

Si se utilizara:

```text
S = 0
```

también podrían detectarse:

* Grises.
* Blancos.
* Colores muy apagados.

Si se utilizara:

```text
V = 0
```

también podrían detectarse zonas prácticamente negras.

Al exigir:

```text
S >= 100
V >= 100
```

se obliga al píxel a poseer:

* Suficiente intensidad de color.
* Suficiente iluminación.

Esto mejora la robustez de la detección.

---

## Creación de la Máscara

Una vez definido el rango, OpenCV genera una máscara mediante:

```python
mascara = cv2.inRange(
    hsv,
    rojo_bajo,
    rojo_alto
)
```

La función analiza todos los píxeles de la imagen.

Conceptualmente realiza:

```text
¿H está dentro del rango?
¿S está dentro del rango?
¿V está dentro del rango?
```

Si todas las condiciones se cumplen:

```text
255
```

Si alguna falla:

```text
0
```

---

## Resultado de la Máscara

La máscara es una imagen binaria:

```text
Blanco → color detectado
Negro  → resto de la imagen
```

Visualmente:

```text
Objeto rojo    → blanco
Fondo          → negro
```

De esta forma se aísla únicamente la información que interesa analizar.

---

## Adaptación a Otros Colores

La detección funciona exactamente igual para cualquier otro color.

Únicamente es necesario modificar los rangos HSV.

Ejemplos aproximados:

```text
Rojo    → H ≈ 0
Amarillo→ H ≈ 30
Verde   → H ≈ 60
Azul    → H ≈ 120
Morado  → H ≈ 150
```

Por tanto, el mismo algoritmo puede utilizarse para detectar múltiples colores cambiando únicamente los límites definidos.

---

## Relación con las Fases Anteriores

La detección de color no sustituye las técnicas aprendidas anteriormente.

Una vez generada la máscara siguen siendo válidas operaciones como:

* Acceso a píxeles.
* Extracción de ROI.
* Cálculo de medias.
* Análisis de regiones.

La diferencia es que ahora se trabaja sobre una imagen que contiene únicamente la información relevante.

---

## Logros Alcanzados

* Comprensión de la detección basada en rangos HSV.
* Definición de límites inferiores y superiores.
* Uso de la función `cv2.inRange()`.
* Creación de máscaras binarias.
* Aislamiento visual de colores específicos.
* Preparación de la imagen para futuras etapas de localización y seguimiento.

---

## Aplicación en Kinema Nexus

La detección por color constituye la primera técnica de segmentación visual del proyecto.

Gracias a esta fase es posible:

* Identificar objetos por su color.
* Separar objetos del fondo.
* Reducir la cantidad de información a procesar.
* Preparar sistemas de localización automática.

Este mecanismo servirá como base para determinar posteriormente la posición exacta de objetos dentro de la imagen.

---

## Conclusión

La Fase 10 introduce la detección de colores mediante rangos HSV y máscaras binarias.

A partir de una imagen completa, el sistema es capaz de aislar únicamente los píxeles que cumplen determinadas condiciones de color.

Este proceso constituye el primer paso hacia la localización, seguimiento e interacción con objetos dentro del entorno visual.
