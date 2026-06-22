# Fase 07 - Visual Markers

## Objetivo

Aprender a representar información visual directamente sobre la imagen mediante el uso de marcadores gráficos.

---

## Descripción

Hasta este punto del proyecto, la información obtenida del frame se mostraba principalmente mediante texto en consola.

En esta fase se introduce el concepto de marcador visual, una herramienta que permite representar información directamente sobre la imagen capturada por la cámara.

Gracias a estos elementos es posible visualizar puntos de interés, regiones de análisis, trayectorias y datos relevantes de forma intuitiva.

Los marcadores visuales constituyen una parte fundamental de cualquier sistema de visión artificial, ya que permiten verificar visualmente el funcionamiento de los algoritmos desarrollados.

---

## Conceptos Aprendidos

### Punto de referencia

Un punto permite representar una coordenada específica dentro de la imagen.

Para ello se utiliza la función:

```python
cv2.circle()
```

Los puntos suelen emplearse para mostrar posiciones relevantes como:

* Centro de la imagen.
* Posición de un objeto.
* Coordenadas detectadas por un algoritmo.

---

### Líneas

Las líneas permiten conectar dos puntos dentro de la imagen.

Para ello se utiliza:

```python
cv2.line()
```

Su uso es habitual para:

* Representar trayectorias.
* Mostrar direcciones.
* Conectar articulaciones en sistemas de seguimiento corporal.

---

### Rectángulos

Los rectángulos permiten delimitar regiones específicas de la imagen.

Para ello se utiliza:

```python
cv2.rectangle()
```

En Kinema Nexus esta técnica resulta especialmente útil para visualizar las Regiones de Interés (ROI).

De esta forma es posible observar exactamente qué zona está siendo analizada por el sistema.

---

### Texto sobre la imagen

La información también puede mostrarse directamente sobre el frame.

Para ello se utiliza:

```python
cv2.putText()
```

Esta función permite representar:

* Coordenadas.
* Valores calculados.
* Resultados de análisis.
* Información de depuración.

---

## Visualización de Información

Durante esta fase se combinan diferentes marcadores para representar información relevante sobre la imagen:

* Punto central de referencia.
* Línea de orientación.
* Rectángulo delimitando la ROI.
* Coordenadas mostradas sobre el frame.

Estos elementos permiten comprender mejor la relación entre los datos calculados y su posición dentro de la imagen.

---

## Logros Alcanzados

* Comprensión de los marcadores visuales.
* Representación gráfica de coordenadas.
* Dibujo de puntos sobre la imagen.
* Dibujo de líneas entre posiciones.
* Delimitación visual de regiones de interés.
* Inserción de texto sobre el frame.
* Relación entre datos calculados y representación visual.

---

## Aplicación en Kinema Nexus

Los marcadores visuales serán una herramienta fundamental durante todo el desarrollo del proyecto.

Permiten:

* Verificar visualmente el funcionamiento de los algoritmos.
* Comprobar la posición de puntos detectados.
* Visualizar regiones de análisis.
* Mostrar información de depuración.
* Facilitar el desarrollo de sistemas de seguimiento.

En fases posteriores se utilizarán para representar articulaciones, trayectorias y elementos detectados por los algoritmos de visión artificial.

---

## Conclusión

La Fase 07 introduce la representación gráfica de información sobre imágenes.

Gracias al uso de puntos, líneas, rectángulos y texto, el sistema deja de depender exclusivamente de la consola y comienza a mostrar resultados directamente sobre el frame.

Este cambio supone un paso importante hacia sistemas de visión artificial más avanzados, ya que permite visualizar de forma inmediata la información generada por los algoritmos.

---

# Referencia de Funciones Utilizadas

## cv2.circle()

Permite dibujar un círculo sobre una imagen.

```python
cv2.circle(imagen, centro, radio, color, grosor)
```

Parámetros:

* imagen: imagen sobre la que se dibuja.
* centro: coordenadas (x, y).
* radio: tamaño del círculo.
* color: color en formato BGR.
* grosor:

  * valor positivo: borde.
  * -1: círculo relleno.

---

## cv2.line()

Permite dibujar una línea entre dos puntos.

```python
cv2.line(imagen, punto_inicio, punto_fin, color, grosor)
```

Parámetros:

* imagen: imagen sobre la que se dibuja.
* punto_inicio: coordenadas iniciales.
* punto_fin: coordenadas finales.
* color: color en formato BGR.
* grosor: espesor de la línea.

---

## cv2.rectangle()

Permite dibujar un rectángulo.

```python
cv2.rectangle(imagen, esquina_superior_izquierda, esquina_inferior_derecha, color, grosor)
```

Parámetros:

* imagen: imagen sobre la que se dibuja.
* esquina_superior_izquierda: coordenadas iniciales.
* esquina_inferior_derecha: coordenadas finales.
* color: color en formato BGR.
* grosor: espesor del borde.

---

## cv2.putText()

Permite escribir texto sobre una imagen.

```python
cv2.putText(imagen, texto, posicion, fuente, escala, color, grosor)
```

Parámetros:

* imagen: imagen sobre la que se escribe.
* texto: cadena de caracteres.
* posicion: coordenadas (x, y).
* fuente: tipo de letra.
* escala: tamaño del texto.
* color: color en formato BGR.
* grosor: espesor de los caracteres.
