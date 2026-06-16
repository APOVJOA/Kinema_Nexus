# Fase 03 - Navegación de Píxeles

## Objetivo

Comprender cómo navegar dentro de una imagen utilizando coordenadas de píxeles.

---

## Descripción

En esta fase se accedió directamente a diferentes píxeles de un frame capturado por la cámara para comprender cómo OpenCV almacena y organiza la información de una imagen.

Se analizaron tres posiciones representativas:

* Esquina superior izquierda.
* Centro de la imagen.
* Esquina inferior derecha.

Esto permitió entender cómo se representan las coordenadas dentro de un frame.

---

## Conceptos Aprendidos

### Coordenadas de una imagen

OpenCV almacena las imágenes como matrices de NumPy.

El acceso a un píxel se realiza mediante:

```python
frame[fila, columna]
```

Donde:

* La fila representa la posición vertical.
* La columna representa la posición horizontal.

---

### Sistema de coordenadas

Las coordenadas comienzan en la esquina superior izquierda:

```text
(0,0) ------------------> Columnas
  |
  |
  |
  v
Filas
```

Ejemplos:

```python
frame[0,0]
```

Representa la esquina superior izquierda.

```python
frame[240,320]
```

Representa el centro de una imagen de 640x480 píxeles.

```python
frame[479,639]
```

Representa la esquina inferior derecha.

---

## Logros Alcanzados

Al finalizar esta fase se consiguió:

* Acceder a cualquier píxel de una imagen.
* Interpretar correctamente las coordenadas de un frame.
* Comprender la relación entre posiciones de la matriz y posiciones visuales.
* Identificar zonas concretas dentro de una imagen mediante coordenadas.

---

## Aplicación en Kinema Nexus

En futuras fases será necesario detectar objetos y obtener sus coordenadas dentro de la imagen.

Comprender cómo navegar entre píxeles es un paso fundamental para:

* Localizar objetos.
* Calcular posiciones.
* Seguir movimientos.
* Convertir coordenadas de imagen en coordenadas utilizables por un robot.

---

## Conclusión

Esta fase permitió comprender cómo OpenCV organiza espacialmente una imagen y cómo acceder a cualquier punto de ella mediante coordenadas.

Este conocimiento constituye la base para las futuras tareas de detección y seguimiento de objetos dentro del proyecto Kinema Nexus.
