Fase 06 - Análisis de Regiones de Imagen
Objetivo

Aprender a obtener información global de una Región de Interés (ROI) a partir del análisis de los valores de sus píxeles.

Descripción

En la Fase 05 se introdujo el concepto de ROI (Region Of Interest), una técnica que permite seleccionar una zona concreta de la imagen para su análisis.

En esta fase se da un paso más, pasando de la simple extracción de una región al análisis de su contenido.

En lugar de trabajar con cada píxel de forma individual, se calcula un valor representativo de toda la región mediante el promedio de sus valores de color.

Este valor resume la información visual de la ROI en un único conjunto de datos.

Conceptos Aprendidos
Análisis de una ROI

Una ROI está formada por múltiples píxeles, cada uno con valores en los canales B, G y R.

Para obtener una representación global de la región, se calcula la media de todos los píxeles:

b_medio, g_medio, r_medio = roi.mean(axis=(0, 1))

Este cálculo devuelve un valor medio por canal que representa el comportamiento general de la región.

Interpretación del valor medio

El valor medio no corresponde a un píxel real, sino a una tendencia global del color en la región.

Dependiendo del contenido de la imagen, los resultados pueden interpretarse de la siguiente manera:

Valores altos en el canal rojo indican predominancia de tonos rojizos.
Valores similares en los tres canales indican regiones claras o neutras.
Valores bajos en todos los canales indican regiones oscuras.

Ejemplos:

B ≈ 25, G ≈ 30, R ≈ 210

(región con predominancia de rojo)

B ≈ 220, G ≈ 220, R ≈ 220

(región clara o blanca)

B ≈ 15, G ≈ 15, R ≈ 15

(región oscura)

Vector de información

El resultado del análisis de una ROI puede expresarse como un vector:

[B_medio, G_medio, R_medio]

Este vector representa una descripción simplificada de la región de la imagen.

De píxeles a información estructurada

En esta fase se produce una transición importante:

Antes se analizaban píxeles individuales.
Ahora se analiza la región como una unidad completa.

Esto permite transformar la imagen en información estructurada y más fácil de interpretar.

Logros Alcanzados
Comprensión del análisis estadístico aplicado a una ROI.
Cálculo del valor medio de los píxeles de una región.
Interpretación del color dominante en una zona de la imagen.
Transformación de una ROI en un vector de características.
Evolución del sistema desde píxeles individuales a análisis regional.
Consolidación del uso de ROI como unidad de análisis.
Aplicación en Kinema Nexus

El análisis de regiones permite avanzar en el desarrollo del sistema de visión artificial de Kinema Nexus.

Gracias a esta técnica es posible:

Analizar zonas específicas de la imagen sin procesar todo el frame.
Determinar si una región es clara u oscura.
Detectar predominancia de color en áreas concretas.
Comparar diferentes regiones de la imagen.
Servir como base para futuros sistemas de detección y seguimiento.

En fases posteriores, este análisis permitirá interpretar el entorno del robot de forma más eficiente y estructurada.

Conclusión

La Fase 06 introduce el análisis cuantitativo de regiones de imagen mediante el uso de valores medios.

A partir de este punto, la imagen deja de ser únicamente una matriz de píxeles y pasa a convertirse en información estructurada.

Este cambio es fundamental dentro del sistema de visión artificial, ya que permite avanzar hacia niveles más altos de interpretación visual.