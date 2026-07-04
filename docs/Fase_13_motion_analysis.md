# Fase 13 - Motion Analysis

## Objetivo

Analizar el movimiento de un objeto detectado a partir de su desplazamiento entre frames consecutivos, obteniendo información sobre su dirección, velocidad relativa y trayectoria.

---

# Descripción

En la Fase 12 se consiguió realizar el seguimiento continuo de un objeto mediante el almacenamiento de su posición en cada frame.

En esta fase el sistema evoluciona desde el seguimiento hacia el análisis del movimiento (*Motion Analysis*).

Utilizando el historial de posiciones almacenado durante el seguimiento, es posible calcular cómo se desplaza el objeto, en qué dirección se mueve y con qué velocidad relativa.

Además, se obtiene información global de toda la trayectoria recorrida, permitiendo describir el movimiento del objeto de forma cuantitativa.

---

# Conceptos Aprendidos

## Desplazamiento entre frames

Cada nueva posición del objeto puede compararse con la posición anterior.

Si las posiciones son:

```
Anterior: (x₁, y₁)

Actual:   (x₂, y₂)
```

El desplazamiento viene dado por:

```python
dx = x2 - x1
dy = y2 - y1
```

Estos valores representan el cambio horizontal y vertical del objeto entre dos imágenes consecutivas.

---

## Dirección del movimiento

A partir del desplazamiento es posible determinar la dirección principal del movimiento.

Si el desplazamiento horizontal es mayor que el vertical:

```python
if abs(dx) > abs(dy):
```

el movimiento será horizontal.

Dependiendo del signo de `dx`:

- dx > 0 → Derecha
- dx < 0 → Izquierda

Si ocurre lo contrario:

- dy > 0 → Abajo
- dy < 0 → Arriba

De esta forma el sistema puede identificar automáticamente hacia dónde se está desplazando el objeto.

---

## Velocidad relativa

La distancia recorrida entre dos frames puede calcularse mediante el Teorema de Pitágoras.

```
Velocidad = √(dx² + dy²)
```

En Python:

```python
velocidad = np.sqrt(dx**2 + dy**2)
```

El resultado representa la velocidad relativa del objeto medida en píxeles por frame.

En esta fase todavía no se utilizan unidades reales, ya que aún no se ha realizado la calibración entre la cámara y el sistema robótico.

---

## Distancia recorrida

Cada desplazamiento calculado puede acumularse para conocer la distancia total recorrida por el objeto durante el seguimiento.

```python
distancia_total += velocidad
```

La distancia total representa la suma de todos los desplazamientos detectados desde el inicio del seguimiento.

---

## Velocidad media

Conociendo la distancia recorrida y el número de desplazamientos realizados, es posible calcular una velocidad media.

```python
velocidad_media = distancia_total / (len(trayectoria) - 1)
```

Este valor proporciona una estimación global del comportamiento del objeto durante todo el seguimiento.

---

## Trayectoria analizada

Gracias al historial de posiciones almacenado en la Fase 12, el sistema puede representar y analizar el recorrido completo realizado por el objeto.

Cada punto registrado forma parte de la trayectoria y permite reconstruir el movimiento seguido a lo largo del tiempo.

---

# Comandos Nuevos

## np.sqrt()

```python
np.sqrt(valor)
```

Calcula la raíz cuadrada de un número.

En esta fase se utiliza para obtener la distancia recorrida entre dos posiciones consecutivas mediante el Teorema de Pitágoras.

---

## abs()

```python
abs(valor)
```

Devuelve el valor absoluto de un número.

Permite comparar desplazamientos sin tener en cuenta si el movimiento es positivo o negativo.

---

## Operador **

```python
dx**2
```

Eleva un número a una potencia.

En esta fase se utiliza para calcular el cuadrado de los desplazamientos horizontal y vertical.

---

## Acumulación mediante +=

```python
distancia_total += velocidad
```

Añade el valor de una variable sobre sí misma.

Permite acumular progresivamente la distancia recorrida durante todo el seguimiento.

---

# Interpretación de los resultados

Durante la ejecución pueden observarse datos como:

```
Dirección: Derecha

dX: 8

dY: 2

Velocidad: 8.25 px/frame

Distancia: 452.6 px

Velocidad media: 5.41 px/frame
```

Estos valores describen el comportamiento dinámico del objeto en cada instante y durante toda la trayectoria recorrida.

---

# Logros Alcanzados

- Cálculo del desplazamiento entre frames consecutivos.
- Determinación automática de la dirección del movimiento.
- Cálculo de la velocidad relativa del objeto.
- Obtención de la distancia total recorrida.
- Cálculo de la velocidad media.
- Interpretación cuantitativa de la trayectoria.
- Evolución desde el seguimiento hacia el análisis del movimiento.

---

# Aplicación en Kinema Nexus

El análisis del movimiento representa un paso fundamental dentro del sistema de visión artificial de Kinema Nexus.

Gracias a esta fase el sistema es capaz de:

- Detectar hacia dónde se desplaza un objeto.
- Medir la rapidez con la que se mueve.
- Registrar la distancia recorrida.
- Analizar la trayectoria seguida durante el seguimiento.

Esta información será utilizada posteriormente para predecir movimientos, planificar trayectorias robóticas y adaptar el comportamiento del robot en función del desplazamiento observado.

---

# Conclusión

La Fase 13 introduce el análisis dinámico del movimiento de objetos mediante el cálculo de desplazamientos, direcciones y velocidades relativas.

El sistema deja de limitarse a localizar y seguir un objeto para comenzar a interpretar su comportamiento a lo largo del tiempo.

Con esta fase concluye el bloque dedicado al seguimiento de objetos, dejando preparado el sistema para el siguiente paso del proyecto: transformar la información obtenida por la cámara en coordenadas utilizables por un brazo robótico mediante procesos de calibración y mapeo espacial.