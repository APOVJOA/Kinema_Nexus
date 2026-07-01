# Fase 12 - Object Tracking

## Objetivo

Aprender a realizar el seguimiento continuo de un objeto entre frames consecutivos, manteniendo actualizada su posición en tiempo real.

---

# Descripción

En la Fase 11 se consiguió detectar un objeto mediante segmentación por color y localizar su posición dentro de la imagen utilizando contornos y momentos geométricos.

En esta fase el sistema evoluciona desde la detección puntual hacia el seguimiento continuo (*Object Tracking*).

En lugar de tratar cada frame como una imagen independiente, el programa conserva la posición del objeto a lo largo del tiempo, permitiendo reconstruir su movimiento.

Cada nueva posición detectada se almacena y se utiliza para representar gráficamente la trayectoria seguida por el objeto.

---

# Conceptos Aprendidos

## Seguimiento entre frames

El vídeo está formado por una sucesión de imágenes denominadas *frames*.

En cada uno de ellos el sistema realiza el mismo proceso:

- Detecta el objeto.
- Calcula su centro.
- Guarda su posición.

Al repetir este procedimiento continuamente es posible seguir el movimiento del objeto a lo largo del tiempo.

---

## Historial de posiciones

Para conservar la trayectoria se utiliza una lista donde se almacenan las coordenadas del centro del objeto.

```python
trayectoria = []
```

Cada vez que se detecta una nueva posición:

```python
trayectoria.append((cx, cy))
```

La lista contiene todas las posiciones detectadas durante el seguimiento.

Ejemplo:

```
[(210,150),
 (215,152),
 (220,156),
 (225,160)]
```

Cada elemento representa el centro del objeto en un instante determinado.

---

## Reconstrucción de la trayectoria

Una vez almacenadas las posiciones, la trayectoria puede dibujarse uniendo cada punto con el siguiente.

```python
for i in range(1, len(trayectoria)):
    cv2.line(
        frame,
        trayectoria[i-1],
        trayectoria[i],
        (255,255,0),
        2
    )
```

Aunque cada frame es una imagen nueva, el programa vuelve a dibujar todas las líneas utilizando la información almacenada en la lista.

De esta forma la trayectoria permanece visible durante todo el seguimiento.

---

## Limitación del historial

Si la trayectoria creciera indefinidamente, el número de segmentos aumentaría continuamente reduciendo el rendimiento del programa.

Para evitarlo se limita el número máximo de posiciones almacenadas.

```python
if len(trayectoria) > 100:
    trayectoria.pop(0)
```

Con ello siempre se conservan únicamente los últimos cien puntos detectados.

---

## De la detección al seguimiento

Hasta la fase anterior el sistema únicamente respondía a la pregunta:

> ¿Dónde está el objeto?

A partir de esta fase también puede responder:

> ¿Por dónde se ha movido?

Este cambio supone la transición desde la localización estática hacia el seguimiento temporal de objetos.

---

# Comandos Nuevos

## Lista de Python

```python
trayectoria = []
```

Crea una lista vacía donde almacenar información.

En esta fase se utiliza para guardar todas las posiciones detectadas del objeto.

---

## append()

```python
trayectoria.append((cx, cy))
```

Añade un nuevo elemento al final de una lista.

En este caso se almacena una tupla con las coordenadas del centro del objeto.

---

## pop()

```python
trayectoria.pop(0)
```

Elimina un elemento de la lista.

Al utilizar el índice `0` se elimina el elemento más antiguo, manteniendo un tamaño constante de la trayectoria.

---

## len()

```python
len(trayectoria)
```

Devuelve el número de elementos almacenados en la lista.

Se utiliza para limitar el tamaño máximo del historial.

---

## range()

```python
range(1, len(trayectoria))
```

Genera una secuencia de índices que permite recorrer la lista y unir cada punto con el siguiente.

---

## cv2.line()

```python
cv2.line(frame, punto1, punto2, color, grosor)
```

Dibuja una línea entre dos puntos.

Parámetros:

- **frame** → Imagen sobre la que se dibuja.
- **punto1** → Coordenadas del punto inicial `(x, y)`.
- **punto2** → Coordenadas del punto final `(x, y)`.
- **color** → Color en formato BGR.
- **grosor** → Espesor de la línea en píxeles.

En esta fase se utiliza para representar la trayectoria seguida por el objeto.

---

# Logros Alcanzados

- Comprensión del seguimiento continuo entre frames.
- Almacenamiento del historial de posiciones.
- Representación gráfica de la trayectoria recorrida.
- Actualización dinámica del seguimiento.
- Introducción del concepto de memoria temporal en visión artificial.
- Preparación para el análisis del movimiento.

---

# Aplicación en Kinema Nexus

El seguimiento continuo constituye una de las bases del sistema de visión artificial de Kinema Nexus.

Gracias a esta técnica es posible:

- Mantener localizado un objeto mientras se desplaza.
- Registrar su recorrido.
- Visualizar la trayectoria seguida.
- Disponer de un historial de posiciones para futuros cálculos de movimiento.

Esta información será utilizada en las siguientes fases para calcular velocidades, desplazamientos y direcciones, permitiendo posteriormente controlar un brazo robótico mediante información visual.

---

# Conclusión

La Fase 12 introduce el concepto de **Object Tracking**, permitiendo realizar el seguimiento continuo de un objeto entre frames consecutivos.

El sistema deja de analizar imágenes de forma independiente y comienza a incorporar memoria temporal mediante el almacenamiento del historial de posiciones.

La representación de la trayectoria constituye el primer paso hacia el análisis del movimiento, que será desarrollado en la siguiente fase mediante el cálculo de desplazamientos, direcciones y velocidades.