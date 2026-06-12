# Fase 01 - Camera Test

## Objetivo

El objetivo de esta primera prueba es verificar que el entorno de desarrollo es capaz de acceder a la cámara del ordenador y mostrar el flujo de vídeo en tiempo real mediante OpenCV.

Esta prueba constituye el primer paso del proyecto Kinema Nexus, ya que toda la información visual utilizada posteriormente para detectar movimientos humanos procederá de la cámara.

---

## Herramientas utilizadas

* Python
* OpenCV
* Visual Studio Code
* Webcam integrada del ordenador

---

## Código utilizado

```python
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error al capturar imagen")
        break

    cv2.imshow("Kinema Nexus - Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## Explicación del funcionamiento

### Apertura de la cámara

```python
cap = cv2.VideoCapture(0)
```

Se crea un objeto que establece la conexión con la cámara principal del sistema.

El parámetro `0` indica que se utilizará la primera cámara disponible.

---

### Comprobación de acceso

```python
if not cap.isOpened():
```

Se verifica que OpenCV ha conseguido acceder correctamente al dispositivo de captura.

---

### Captura de imágenes

```python
ret, frame = cap.read()
```

La función captura un frame del flujo de vídeo.

* `ret`: indica si la captura se realizó correctamente.
* `frame`: contiene la imagen capturada.

---

### Visualización

```python
cv2.imshow(...)
```

Muestra el frame capturado en una ventana gráfica.

Al ejecutarse continuamente dentro del bucle, se genera la sensación de vídeo en tiempo real.

---

### Finalización

```python
cap.release()
cv2.destroyAllWindows()
```

Se libera la cámara y se cierran todas las ventanas abiertas por OpenCV.

---

## Resultado obtenido

La aplicación consiguió acceder correctamente a la webcam y mostrar el vídeo en tiempo real.

La prueba confirma que:

* OpenCV está correctamente instalado.
* Python puede acceder a dispositivos de captura.
* El sistema es capaz de procesar frames en tiempo real.
* La base para futuros algoritmos de visión artificial está operativa.

---

## Relación con Kinema Nexus

En fases posteriores cada frame será analizado para:

1. Detectar articulaciones humanas.
2. Obtener coordenadas espaciales.
3. Calcular ángulos de movimiento.
4. Enviar información a un sistema robótico.

Por tanto, esta prueba representa el punto de partida de toda la cadena de percepción visual del proyecto.
