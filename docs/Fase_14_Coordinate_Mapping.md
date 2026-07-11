# Fase 14 - Coordinate Mapping

## Objetivo

Una vez que el sistema es capaz de detectar, localizar y seguir un objeto dentro de la imagen, el siguiente paso consiste en convertir esas coordenadas de píxel en coordenadas que puedan ser interpretadas por un robot.

En esta fase se realiza la primera transformación entre el sistema de visión y un sistema de coordenadas físico, estableciendo la base para la futura comunicación con RoboDK y, posteriormente, con el robot real.

---

# ¿Por qué es necesaria esta fase?

Hasta ahora toda la información obtenida pertenece al sistema de referencia de la cámara.

Por ejemplo:

```
Objeto detectado

X = 420 px
Y = 185 px
```

Sin embargo, un robot no trabaja en píxeles.

Un robot necesita coordenadas físicas, normalmente expresadas en milímetros.

Por tanto, es necesario realizar una conversión entre ambos sistemas.

---

# Sistema de coordenadas de la cámara

OpenCV utiliza un sistema de referencia cuyo origen se encuentra en la esquina superior izquierda de la imagen.

```
(0,0)
 +-----------------------------> X
 |
 |
 |
 |
 V
 Y
```

Características:

- El eje X aumenta hacia la derecha.
- El eje Y aumenta hacia abajo.
- Las unidades están expresadas en píxeles.

---

# Sistema de coordenadas del robot

En robótica es habitual utilizar un sistema cartesiano cuyo origen se sitúa en un punto de referencia del robot.

En este proyecto se ha tomado como referencia el centro de la imagen.

```
            +Y
             ↑
             |
-X ----------+---------- +X
             |
             |
             ↓
            -Y
```

En este sistema:

- El eje X positivo apunta hacia la derecha.
- El eje X negativo apunta hacia la izquierda.
- El eje Y positivo apunta hacia arriba.
- El eje Y negativo apunta hacia abajo.

Este comportamiento resulta mucho más intuitivo para controlar posteriormente un brazo robótico.

---

# Definición del tamaño del robot

Para poder realizar la conversión se define el tamaño físico del espacio alcanzable por el robot.

```python
ancho_robot = 300
alto_robot = 200
```

Estas variables representan las dimensiones físicas del área máxima de movimiento del robot.

Las unidades utilizadas son milímetros.

---

# Dimensiones de la imagen

También se definen las dimensiones del frame capturado.

```python
ancho_imagen = 640
alto_imagen = 480
```

Estas dimensiones permiten calcular la relación entre píxeles y milímetros.

---

# Centro de la imagen

El origen del nuevo sistema de referencia se sitúa en el centro del frame.

```python
centro_imagen_x = ancho_imagen // 2
centro_imagen_y = alto_imagen // 2
```

En una imagen de 640x480:

```
Centro

X = 320 px
Y = 240 px
```

A partir de este punto todas las coordenadas serán relativas al centro de la imagen.

---

# Escala píxel → milímetro

Una vez conocidas las dimensiones del robot y las dimensiones de la imagen puede calcularse la relación entre ambas.

```python
escala_x = ancho_robot / ancho_imagen
escala_y = alto_robot / alto_imagen
```

Por ejemplo:

```
640 px  → 300 mm

1 px ≈ 0.468 mm
```

Esta relación permite convertir cualquier posición detectada en la imagen a coordenadas físicas.

---

# Conversión de coordenadas

La conversión utilizada es:

```python
x_mm = (cx - centro_imagen_x) * escala_x
y_mm = (centro_imagen_y - cy) * escala_y
```

Observaciones:

- Se resta el centro para cambiar el origen.
- El eje Y se invierte para adaptarlo al sistema cartesiano del robot.
- Finalmente se multiplica por la escala correspondiente.

Ejemplo:

```
Imagen

X = 420 px

Centro = 320 px

ΔX = 100 px

100 px × 0.468

≈ 46.8 mm
```

Resultado:

```
Robot

X = 46.8 mm
```

---

# Visualización de las coordenadas

Las coordenadas convertidas se muestran sobre la imagen.

```python
cv2.putText(
    frame,
    f"Robot X:{x_mm:.1f} mm",
    (10,210),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0,255,255),
    2
)

cv2.putText(
    frame,
    f"Robot Y:{y_mm:.1f} mm",
    (10,240),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0,255,255),
    2
)
```

De esta forma es posible comprobar visualmente que la conversión se está realizando correctamente.

---

# Zona de trabajo

Aunque el robot pueda alcanzar un determinado espacio físico, no siempre interesa utilizar toda esa superficie.

Por ello se define una zona de trabajo independiente.

Ejemplo:

```python
zona_x_min = -150
zona_x_max = 150

zona_y_min = -100
zona_y_max = 100
```

Estas variables representan el área donde el robot tiene permitido trabajar.

Esta separación permite reutilizar el mismo robot para diferentes aplicaciones simplemente modificando los límites de la zona de trabajo.

---

# Validación de la zona de trabajo

La posición calculada se comprueba respecto a la zona definida.

```python
if (zona_x_min <= x_mm <= zona_x_max) and (zona_y_min <= y_mm <= zona_y_max):
    estado = "Dentro de la zona"
else:
    estado = "Fuera de la zona"
```

Posteriormente el estado se muestra sobre la imagen.

```python
cv2.putText(
    frame,
    estado,
    (10,270),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0,255,0) if estado == "Dentro de la zona" else (0,0,255),
    2
)
```

De esta forma el operador puede verificar inmediatamente si el objeto detectado pertenece al área de trabajo permitida.

---

# Resultado obtenido

Al finalizar esta fase el sistema es capaz de:

- Detectar un objeto mediante visión artificial.
- Obtener su posición en píxeles.
- Convertir dicha posición a milímetros.
- Cambiar el origen de coordenadas al centro de la imagen.
- Adaptar el sistema de referencia al utilizado por el robot.
- Definir una zona de trabajo independiente del alcance físico del robot.
- Validar si el objeto pertenece o no a dicha zona.

---

# Importancia de esta fase

Esta fase constituye el primer puente entre la visión artificial y la robótica.

Hasta ahora todas las operaciones se realizaban sobre imágenes.

A partir de este momento la información generada puede ser utilizada directamente para controlar un robot, ya sea en un entorno de simulación como RoboDK o en un brazo robótico físico.

La separación entre el alcance físico del robot y la zona de trabajo proporciona además una arquitectura flexible que permitirá adaptar el mismo sistema a diferentes aplicaciones sin modificar el proceso de conversión de coordenadas.

---

# Nuevos comandos utilizados

## División entera

```python
//
```

Permite obtener el centro de la imagen utilizando únicamente valores enteros.

Ejemplo:

```python
centro_x = ancho // 2
```

---

## Conversión de coordenadas

```python
x_mm = (cx - centro_imagen_x) * escala_x
```

Transforma una coordenada en píxeles a una coordenada física.

---

## Escalado

```python
escala_x = ancho_robot / ancho_imagen
```

Calcula la equivalencia entre píxeles y milímetros.

---

## Operadores de comparación encadenados

```python
-150 <= x_mm <= 150
```

Permiten comprobar si un valor pertenece a un intervalo.

---

## Operador lógico

```python
and
```

Permite comprobar varias condiciones simultáneamente.

---

## Operador condicional (ternario)

```python
(0,255,0) if estado == "Dentro de la zona" else (0,0,255)
```

Selecciona automáticamente un color dependiendo del estado del sistema.

---

# Resultado final de la fase

El sistema ya no trabaja únicamente con imágenes.

Ahora es capaz de transformar la información visual obtenida por la cámara en coordenadas físicas interpretables por un robot, estableciendo la base necesaria para la comunicación con RoboDK y el posterior control de un brazo robótico.