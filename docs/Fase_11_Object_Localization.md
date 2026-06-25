# Fase 11 - Object Localization

## Objetivo

Determinar la posición exacta de un objeto detectado dentro de la imagen.

## Resultados Esperados

* Obtener el centro del objeto.
* Obtener sus coordenadas X/Y.
* Obtener un tamaño aproximado.
* Mejorar la robustez de la detección mediante limpieza de máscara.

---

# Descripción

En la fase anterior se introdujo la detección de colores mediante el espacio HSV y el uso de máscaras binarias.

En esta fase se da un paso más, transformando una región detectada por color en un objeto identificable dentro de la imagen.

Para ello se utilizan técnicas de procesamiento de imagen que permiten:

* Limpiar la máscara.
* Detectar contornos.
* Seleccionar el objeto principal.
* Calcular su posición.
* Estimar su tamaño.

Esta información constituye la base necesaria para futuras tareas de seguimiento de objetos y control robótico.

---

# Flujo General del Proceso

```text
Frame
↓
Conversión HSV
↓
Máscara de color
↓
Limpieza de máscara
↓
Detección de contornos
↓
Selección del objeto principal
↓
Centro del objeto
↓
Coordenadas X/Y
↓
Área aproximada
```

---

# Detección por Color

Se define un rango de color utilizando valores HSV.

```python
rojo_bajo = np.array([0, 100, 100])
rojo_alto = np.array([10, 255, 255])
```

Posteriormente se genera una máscara binaria:

```python
mascara = cv2.inRange(
    hsv,
    rojo_bajo,
    rojo_alto
)
```

Los píxeles que pertenecen al rango seleccionado aparecen en blanco.

Los píxeles que no pertenecen al rango aparecen en negro.

---

# Limpieza de Máscara

Las cámaras reales producen ruido visual:

* Reflejos.
* Sombras.
* Cambios de iluminación.
* Imperfecciones de color.

Para reducir estos efectos se utiliza una operación morfológica.

Primero se crea un kernel:

```python
kernel = np.ones((5,5), np.uint8)
```

Posteriormente se aplica una operación de cierre:

```python
mascara_limpia = cv2.morphologyEx(
    mascara,
    cv2.MORPH_CLOSE,
    kernel
)
```

Esta operación permite:

* Rellenar pequeños huecos.
* Unir regiones cercanas.
* Reducir fragmentaciones del objeto.

---

# Detección de Contornos

Una vez obtenida la máscara limpia, se buscan las fronteras de los objetos detectados.

```python
contornos, _ = cv2.findContours(
    mascara_limpia,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

Cada contorno representa una posible región detectada.

---

# Selección del Objeto Principal

Puede ocurrir que existan múltiples contornos.

Para seleccionar únicamente el objeto más relevante se escoge el contorno con mayor área.

```python
contorno_principal = max(
    contornos,
    key=cv2.contourArea
)
```

De esta forma se ignoran pequeños fragmentos o ruido residual.

---

# Centro del Objeto

Una vez seleccionado el contorno principal, se calculan sus momentos geométricos.

```python
M = cv2.moments(contorno_principal)
```

A partir de ellos se obtiene el centro geométrico:

```python
cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])
```

Donde:

* cx → coordenada horizontal.
* cy → coordenada vertical.

Estas coordenadas representan la posición del objeto dentro de la imagen.

---

# Visualización del Centro

El centro puede representarse mediante un marcador visual.

```python
cv2.circle(
    frame,
    (cx, cy),
    5,
    (255,0,0),
    -1
)
```

Esto facilita la validación visual de la detección.

---

# Obtención del Tamaño Aproximado

El tamaño del objeto puede estimarse mediante el área de su contorno.

```python
area = cv2.contourArea(
    contorno_principal
)
```

Este valor corresponde al número aproximado de píxeles ocupados por el objeto.

No representa una medida física real, pero permite comparar tamaños relativos dentro de la imagen.

---

# Visualización de Información

Las coordenadas y el área pueden mostrarse directamente sobre la imagen.

```python
cv2.putText(
    frame,
    texto,
    (x, y),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255,255,255),
    2
)
```

Esto permite visualizar en tiempo real la información obtenida.

---

# Conceptos Aprendidos

* Detección de objetos mediante color.
* Limpieza de máscaras binarias.
* Uso de operaciones morfológicas.
* Detección de contornos.
* Selección del objeto principal.
* Cálculo del centro geométrico.
* Obtención de coordenadas.
* Estimación de tamaño mediante área.
* Visualización de información sobre la imagen.

---

# Aplicación en Kinema Nexus

Esta fase constituye el primer sistema completo de localización de objetos dentro del proyecto.

A partir de este punto el sistema es capaz de:

* Detectar objetos por color.
* Determinar dónde se encuentran.
* Calcular su posición.
* Estimar su tamaño.
* Representar la información visualmente.

Estas capacidades serán utilizadas posteriormente para:

* Seguimiento de objetos.
* Análisis de movimiento.
* Conversión de coordenadas.
* Control de robots reales y simulados.

---

# Comandos Introducidos

## np.array()

Permite crear vectores y matrices NumPy.

```python
np.array([0,100,100])
```

Utilizado para definir rangos HSV.

---

## cv2.inRange()

Genera una máscara binaria.

```python
cv2.inRange(
    imagen,
    limite_inferior,
    limite_superior
)
```

Devuelve blanco para los píxeles dentro del rango.

Devuelve negro para los píxeles fuera del rango.

---

## np.ones()

Crea una matriz rellena de unos.

```python
np.ones((5,5), np.uint8)
```

Utilizada para construir kernels morfológicos.

---

## cv2.morphologyEx()

Aplica operaciones morfológicas.

```python
cv2.morphologyEx(
    imagen,
    operacion,
    kernel
)
```

Permite limpiar máscaras binarias.

---

## cv2.MORPH_CLOSE

Operación de cierre morfológico.

Permite:

* Rellenar huecos.
* Unir regiones próximas.

---

## cv2.findContours()

Detecta contornos dentro de una imagen binaria.

```python
cv2.findContours()
```

Devuelve una lista de contornos encontrados.

---

## cv2.drawContours()

Dibuja contornos sobre una imagen.

```python
cv2.drawContours()
```

Permite visualizar regiones detectadas.

---

## cv2.contourArea()

Calcula el área de un contorno.

```python
cv2.contourArea(contorno)
```

Utilizado para estimar el tamaño de un objeto.

---

## max()

Permite obtener el elemento con mayor valor.

```python
max(
    contornos,
    key=cv2.contourArea
)
```

Utilizado para seleccionar el contorno principal.

---

## cv2.moments()

Calcula momentos geométricos.

```python
cv2.moments(contorno)
```

Permite obtener el centro geométrico de una región.

---

## cv2.circle()

Dibuja círculos.

```python
cv2.circle()
```

Utilizado para marcar el centro del objeto.

---

## cv2.putText()

Escribe texto sobre una imagen.

```python
cv2.putText()
```

Utilizado para mostrar coordenadas e información adicional.

---

# Conclusión

La Fase 11 transforma una detección basada únicamente en color en un sistema capaz de localizar objetos dentro de una imagen.

A partir de una máscara binaria se obtiene una representación estructurada del objeto mediante:

* Posición.
* Centro.
* Coordenadas.
* Tamaño.

Este paso marca la transición entre la simple detección visual y la obtención de información útil para el seguimiento y control robótico.

