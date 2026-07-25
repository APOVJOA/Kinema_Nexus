Conversa amb Gemini
Hola gemini me ayudas a crear unos documentos para explicar unos codigos que he hecho??

¡Hola! Claro que sí, con mucho gusto te ayudo a documentar tus códigos para que queden superclaros y profesionales.

Para empezar, puedes compartirme el código por aquí o contarme un poco sobre lo que hace. También dime qué formato o estilo te sirve mejor:

Documento formal (Google Doc): Con resumen ejecutivo, explicación por módulos o funciones, flujo de datos y ejemplos de uso.

Archivo README.md: Un formato técnico y limpio, ideal para un repositorio de GitHub o GitLab.

Guía paso a paso / Tutorial: Orientado a explicárselo a principiantes, clientes o a tu equipo de trabajo.

¿De qué lenguaje de programación es tu código y cuál es su objetivo principal?

Pues mira, te comento. Tengo cuatro códigos ahora mismo, ¿vale? Por una parte tengo el código de Landmark, que sirve simplemente para encontrar las marcas, digamos, utilizando YOLO, porque es un sistema de visión artificial que uso. Usando YOLO, pues, digamos que me ayuda a guardarlo. Luego tengo pose, que es para saber las posiciones de cada sitio, post drawer, que es para dibujar solo las que necesito, y human pose detection, que es el código principal. Ahora te los voy pasando, ¿vale?

¡Entendido perfectamente! Es un proyecto de visión artificial muy interesante con YOLO y estimación de poses humanas. Separar la detección, la selección de puntos y el dibujado en distintos módulos es una excelente práctica de diseño de software.

Conforme me los vayas pasando, iré revisando la estructura y el funcionamiento de cada uno.

Para que vayamos organizándolo de la mejor manera, cuéntame:

¿Prefieres que creemos un único documento completo en Google Docs que explique todo el sistema (con secciones para cada módulo y cómo se integran con human pose detection), o documentos independientes / READMEs para cada archivo?

¿A quién va dirigida la explicación? (¿Tu equipo de trabajo, tus profesores/evaluadores, o para tu propio portafolio y referencia futura?)

¡Pásame el primer código cuando quieras y empezamos!

Este es el codigo landmark.py

class Landmark:



    def __init__(self, x=0, y=0, confidence=0):

        self.x = x

        self.y = y

        self.confidence = confidence



    def __repr__(self):

        return f"({self.x:.1f}, {self.y:.1f}) conf={self.confidence:.2f}"

¡Excelente! Este primer módulo landmark.py es la base o la clase de datos del proyecto.

Como ves, define un punto clave (keypoint o landmark) dentro de la imagen con tres atributos esenciales:

x: Coordenada horizontal del punto.

y: Coordenada vertical del punto.

confidence: Nivel de confianza o certeza que asigna el modelo YOLO al detectar ese punto (un valor entre 0 y 1).

__repr__: Un método especial que facilita imprimir o depurar el objeto en formato legible, mostrando las coordenadas con un decimal y la confianza con dos decimales.

¿Cómo quieres organizar la documentación final?
Google Doc único: Voy redactando una documentación completa y profesional que incluya la explicación detallada de cada módulo, diagramas de arquitectura y ejemplos de uso, y te genero el archivo directamente en Google Docs al terminar.

Archivos README.md independientes: Un documento en Markdown específico para cada código.

¡Envíame el siguiente código (pose.py, post_drawer.py o human_pose_detection.py) cuando gustes para ir integrándolo!

Hasta ahora este ha sido un proyecto largo, y es un proyecto largo. Entonces, lo que yo tengo pensado es, hasta ahora he hecho, digamos, fases. He hecho un MD por fase. Ahora lo que voy a hacer es una carpeta exclusivamente para la fase 16, porque la fase 16 es esta, la de YOLO, es la más larga, la que más códigos contiene. Entonces, voy a echar una carpeta y quiero un MD por cada código, es decir, voy a poner landmark.md dentro de la carpeta fase 16.

3. Descripción de Atributos
Atributo	Tipo de Dato	Valor por Defecto	Descripción
x	float / int	0	Coordenada horizontal (píxel) del punto en el plano de la imagen.
y	float / int	0	Coordenada vertical (píxel) del punto en el plano de la imagen.
confidence	float	0	Puntuación de confianza (score) asignada por YOLO, típicamente en el rango [0.0,1.0]. Indica la certidumbre de la detección.
4. Métodos de la Clase
__init__(self, x=0, y=0, confidence=0)
Constructor de la clase. Permite instanciar un landmark asignando valores iniciales a las coordenadas x, y y al nivel de confianza (confidence). Si no se proporcionan parámetros, inicializa el punto en el origen (0,0) con una confianza de 0.

__repr__(self)
Proporciona una representación en formato de cadena de texto (string) optimizada para tareas de logging, depuración (debugging) e inspección rápida en consola.

Formato de salida: (x.x, y.y) conf=0.xx

Precisión: Aplica formato de punto flotante limitado a 1 decimal para las coordenadas de píxel y 2 decimales para el valor de confianza.

5. Integración dentro de la Fase 16
Dentro de la arquitectura modular de la Fase 16, la clase Landmark interactúa en el flujo de procesamiento de la siguiente forma:

Extracción (Inferencia YOLO): El script de detección principal (human_pose_detection.py) procesa el fotograma y obtiene la salida cruda de YOLO.

Encapsulamiento: Cada coordenada detectada se transforma en un objeto Landmark.

Agregación (pose.py): Los objetos Landmark individuales se agrupan en una estructura Pose que representa el esqueleto completo o conjunto de articulaciones de una persona.

Visualización (post_drawer.py): Los dibujadores utilizan las coordenadas x, y y filtran por confidence para renderizar únicamente los puntos clave con alta precisión sobre la imagen original.

 [ YOLO Output ] ---> (Crea instancias) ---> [ Landmark(x, y, conf) ]
                                                       |
                                                       v
 [ Renderizado / Dibujado ] <--- (Agrupa) <--- [ Pose ]
6. Ejemplo de Uso
Python
from landmark import Landmark

# Crear un landmark detectado con alta confianza
codo_derecho = Landmark(x=324.56, y=180.12, confidence=0.945)

# Imprimir representación legible (invoca __repr__)
print(codo_derecho)
# Salida: (324.6, 180.1) conf=0.95

# Acceso directo a los atributos
if codo_derecho.confidence > 0.5:
    print(f"Punto válido en X: {codo_derecho.x}, Y: {codo_derecho.y}")
"""

with open("landmark.md", "w", encoding="utf-8") as f:
f.write(md_content)

print("Archivo landmark.md generado con éxito.")


```text?code_stdout&code_event_index=1
Archivo landmark.md generado con éxito.

Tu archivo landmark.md ya está listo para ser guardado dentro de tu carpeta fase 16.
Icona de MD
landmark
 MD 
Obert

Resumen del contenido incluido en landmark.md:
Visión General: Contexto dentro de la Fase 16 y el rol de esta clase de datos en el sistema YOLO.

Estructura y Código: Presentación limpia del código Python.

Tabla de Atributos: Explicación detallada de x, y y confidence.

Explicación de Métodos: Detalle técnico de __init__ y __repr__.

Flujo de Integración: Cómo conecta con pose.py, post_drawer.py y human_pose_detection.py.

Ejemplo Práctico de Uso: Fragmento de código funcional para pruebas e inspección.

¡Pásame el siguiente código (pose.py, post_drawer.py o human_pose_detection.py) y te genero su respectivo .md!

ahora vamos con pose.py

¡Perfecto! Pásame el código fuente de pose.py y preparo inmediatamente su archivo .md estructurado y detallado para la carpeta de la Fase 16. ¡Quedo atento!

from landmark import Landmark





class HumanPose:



    def __init__(self):



        self.nose = Landmark()



        self.left_eye = Landmark()

        self.right_eye = Landmark()



        self.left_ear = Landmark()

        self.right_ear = Landmark()



        self.left_shoulder = Landmark()

        self.right_shoulder = Landmark()



        self.left_elbow = Landmark()

        self.right_elbow = Landmark()



        self.left_wrist = Landmark()

        self.right_wrist = Landmark()



        self.left_hip = Landmark()

        self.right_hip = Landmark()



        self.left_knee = Landmark()

        self.right_knee = Landmark()



        self.left_ankle = Landmark()

        self.right_ankle = Landmark()

    def print_pose(self):



        print("LEFT SHOULDER :", self.left_shoulder)

        print("RIGHT SHOULDER:", self.right_shoulder)



        print("LEFT ELBOW :", self.left_elbow)

        print("RIGHT ELBOW:", self.right_elbow)



        print("LEFT WRIST :", self.left_wrist)

        print("RIGHT WRIST:", self.right_wrist)



    def print_all(self):



        for nombre, landmark in self.__dict__.items():

            print(f"{nombre:15} -> {landmark}")

    def get_arm_landmarks(self):

   

    #Devuelve únicamente las articulaciones de ambos brazos.

   



        return {

        "left_shoulder": self.left_shoulder,

        "right_shoulder": self.right_shoulder,

        "left_elbow": self.left_elbow,

        "right_elbow": self.right_elbow,

        "left_wrist": self.left_wrist,

        "right_wrist": self.right_wrist,

    }

3. Estructura de Atributos (Keypoints)
La clase inicializa por defecto 17 objetos Landmark neutros (coordenadas (0,0) y confianza 0.0), categorizados según la zona anatómica:

Zona Anatómica	Atributos Representados	Tipo
Cabeza / Rostro	nose, left_eye, right_eye, left_ear, right_ear	Landmark
Brazos / Torso Superior	left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist	Landmark
Cadera / Torso Inferior	left_hip, right_hip	Landmark
Piernas / Extremidades Inferiores	left_knee, right_knee, left_ankle, right_ankle	Landmark
4. Métodos de la Clase
print_pose(self)
Muestra en consola las coordenadas y niveles de confianza de las articulaciones principales de los brazos (hombros, codos y muñecas). Es útil para inspecciones rápidas en vivo de las extremidades superiores durante la ejecución.

print_all(self)
Itera de forma dinámica sobre todos los atributos del objeto (self.__dict__) e imprime cada keypoint alineado con su nombre. Excelente para la depuración (debugging) global del esqueleto completo.

get_arm_landmarks(self)
Devuelve un diccionario Python que contiene únicamente las instancias de Landmark asociadas a los brazos y hombros:

Python
{
    "left_shoulder": self.left_shoulder,
    "right_shoulder": self.right_shoulder,
    "left_elbow": self.left_elbow,
    "right_elbow": self.right_elbow,
    "left_wrist": self.left_wrist,
    "right_wrist": self.right_wrist,
}
Nota: Este método facilita la integración directa con filtradores o renderizadores específicos (como post_drawer.py) cuando solo interesa analizar o dibujar el tren superior.

5. Integración dentro de la Fase 16
Recepción de Datos: human_pose_detection.py asigna a cada atributo de HumanPose las coordenadas calculadas por la inferencia de YOLO.

Filtrado / Selección: Módulos de procesamiento o renderizado como post_drawer.py invocan métodos como get_arm_landmarks() para trabajar únicamente con los datos necesarios sin sobrecargar la visualización.

 [ YOLO Keypoints ] ---> [ Instancia HumanPose ]
                                 |
                                 +---> print_all() / print_pose()  (Depuración)
                                 |
                                 +---> get_arm_landmarks() -------> [ post_drawer.py ]
6. Ejemplo de Uso
Python
from pose import HumanPose

# Instanciar el esqueleto
pose = HumanPose()

# Asignar detecciones (por ejemplo, desde el detector YOLO)
pose.left_shoulder.x = 240.5
pose.left_shoulder.y = 150.0
pose.left_shoulder.confidence = 0.89

# Imprimir solo articulaciones clave del brazo
pose.print_pose()

# Obtener diccionario de brazos para el dibujador
arm_points = pose.get_arm_landmarks()
print(arm_points["left_shoulder"])
"""

with open("pose.md", "w", encoding="utf-8") as f:
f.write(md_pose_content)

print("Archivo pose.md generado con éxito.")


```text?code_stdout&code_event_index=1
Archivo pose.md generado con éxito.

Aquí tienes el archivo pose.md listo para guardarlo en la carpeta fase 16.
Icona de MD
pose
 MD 
Obert

Resumen del contenido en pose.md:
Visión General: Explicación del modelado completo del cuerpo humano basado en el formato estándar de YOLO Pose (17 puntos COCO).

Estructura e Inicialización: Desglose del mapa de atributos (nose, shoulders, elbows, etc.) y sus tipos.

Tabla Anatómica: Clasificación clara de los puntos según la zona del cuerpo.

Detalle de Métodos: Explicación técnica de print_pose(), print_all() y el selector de extremidades get_arm_landmarks().

Diagrama de Integración y Ejemplo: Muestra cómo se conectan los datos extraídos de landmark.py con las herramientas de dibujado (post_drawer.py).

¡Pásame post_drawer.py o human_pose_detection.py cuando quieras y le preparamos su documentación!

Cosa importante, de momento, de momento no nos ha hecho falta, pero ahora cuando te empiece a pasar post-raw y human pose detection, quiero que las cosas que sean más que simplemente crear una clase, compararla, darle nombres, ¿sabes lo que te quiero decir? Porque ahora mismo lo único que estamos haciendo, no es nada complicado, es self.nose que sea igual al landmark X, ¿sabes lo que te quiero decir? No es nada complicado. Pero ahora cuando empecemos con algunas cosas en específico, sí que me gustaría que explicaras esas funciones en un apartado aparte, ¿vale?

¡Entendido perfectamente! Me parece una excelente estrategia.

Hasta ahora landmark.py y pose.py han sido clases puramente estáticas de estructura y encapsulamiento de datos, pero a partir de post_drawer.py y human_pose_detection.py entran en juego los algoritmos reales:

Filtrado geométrico o espacial.

Umbrales de confianza (confidence thresholds).

Operaciones de transformación de coordenadas con OpenCV.

Lógica de inferencia y procesado de fotogramas en tiempo real.

A partir del siguiente código, cuando detecte una función con lógica algorítmica importante (no un simple setter/getter o asignación directa), añadiré una sección dedicada exclusivamente a desglosar esa función paso a paso: explicándole la matemática/lógica por detrás, por qué se hace de esa forma y cómo impacta en el rendimiento o la precisión.

¡Pásame post_drawer.py cuando quieras y le aplicamos este nuevo nivel de detalle!

este es pose_drawer.py

import cv2





def draw_landmark(img, landmark, color):



    if landmark.confidence > 0.3:



        cv2.circle(

            img,

            (int(landmark.x), int(landmark.y)),

            6,

            color,

            -1

        )





def draw_connection(img, p1, p2, color=(255,255,255)):



    if p1.confidence > 0.3 and p2.confidence > 0.3:



        cv2.line(

            img,

            (int(p1.x), int(p1.y)),

            (int(p2.x), int(p2.y)),

            color,

            2

        )





def draw_pose(frame, pose):



    frame_draw = frame.copy()



    # -----------------------------

    # Hombros

    # -----------------------------



    draw_landmark(frame_draw, pose.left_shoulder, (0,0,255))

    draw_landmark(frame_draw, pose.right_shoulder, (0,0,255))



    # -----------------------------

    # Codos

    # -----------------------------



    draw_landmark(frame_draw, pose.left_elbow, (0,255,0))

    draw_landmark(frame_draw, pose.right_elbow, (0,255,0))



    # -----------------------------

    # Muñecas

    # -----------------------------



    draw_landmark(frame_draw, pose.left_wrist, (255,0,0))

    draw_landmark(frame_draw, pose.right_wrist, (255,0,0))



    # -----------------------------

    # Brazo izquierdo

    # -----------------------------



    draw_connection(

        frame_draw,

        pose.left_shoulder,

        pose.left_elbow

    )



    draw_connection(

        frame_draw,

        pose.left_elbow,

        pose.left_wrist

    )



    # -----------------------------

    # Brazo derecho

    # -----------------------------



    draw_connection(

        frame_draw,

        pose.right_shoulder,

        pose.right_elbow

    )



    draw_connection(

        frame_draw,

        pose.right_elbow,

        pose.right_wrist

    )



    cv2.imshow("KINEMA NEXUS", frame_draw)

3. Desglose Detallado de Funciones y Lógica Algorítmica
En este módulo se introduce la primera capa lógica de filtrado numérico y representación espacial en OpenCV. A continuación, se analiza detalladamente el comportamiento de cada función:

A. draw_landmark(img, landmark, color)
Esta función dibuja un círculo sólido en la posición exacta del keypoint si cumple con las condiciones de calidad requeridas.

Filtrado por Umbral de Confianza (confidence > 0.3):
Evita dibujar marcas erróneas o "fantasmas". Si la confianza asignada por el detector es igual o inferior al 30%, la función ignora el punto.

Casting a Enteros (int(landmark.x), int(landmark.y)):
Las coordenadas generadas por YOLO vienen en formato de coma flotante (float). Como las funciones de dibujado de OpenCV operan sobre la matriz discreta de píxeles, es imprescindible castear estas coordenadas a enteros (int).

Parámetros de OpenCV (cv2.circle):

radio = 6: Define un tamaño visible pero no restrictivo para el punto.

thickness = -1: Indicar un grosor negativo ordena a OpenCV rellenar completamente el círculo.

B. draw_connection(img, p1, p2, color=(255, 255, 255))
Renderiza un segmento rectilíneo que conecta dos puntos anatómicos consecutivamente.

Evaluación de Confianza Doble (p1.confidence > 0.3 and p2.confidence > 0.3):
Lógica crítica: la línea que une dos articulaciones solo se dibuja si ambos extremos son fiables. Si uno de los dos puntos no supera el umbral (30%), la línea completa se omite para evitar conexiones flotantes o distorsionadas.

Trazado (cv2.line):
Une las coordenadas enteras de p1 y p2 con un color predeterminado blanco (o el configurado) y un grosor de línea de 2 píxeles.

C. draw_pose(frame, pose)
Es la función principal de orquestación visual. Procesa el objeto HumanPose completo e imparte el esquema de color y la topología de los brazos.

1. Inmutabilidad de la Imagen Original (frame.copy())
Python
frame_draw = frame.copy()
¿Por qué se hace esto? En OpenCV, pasar la imagen de entrada directamente modificaría los datos por referencia. Al realizar una copia con .copy(), preservamos el frame original intacto en memoria. Esto es crucial si más adelante en la aplicación se necesita procesar el fotograma limpio o pasarlo a otros algoritmos sin "contaminar" las matrices con trazos directos.

2. Esquema de Codificación por Color (Formato BGR de OpenCV)
OpenCV utiliza nativamente la codificación de canales BGR (Azul, Verde, Rojo) en lugar de RGB. El código asigna estratégicamente un color distinto para cada par de articulaciones:

Articulación	Tupla BGR	Color Resultante	Propósito Visual
Hombros (left_shoulder, right_shoulder)	(0, 0, 255)	Rojo	Identificar la base del torso superior.
Codos (left_elbow, right_elbow)	(0, 255, 0)	Verde	Identificar la articulación intermedia del brazo.
Muñecas (left_wrist, right_wrist)	(255, 0, 0)	Azul	Identificar los puntos extremidad / efectores finales.
Conexiones	(255, 255, 255)	Blanco	Trazado continuo del esqueleto (por defecto).
3. Topología de Conexiones Dibujadas
El algoritmo conecta explícitamente la cadena cinemática de los brazos:

Brazo Izquierdo: Hombro Izquierdo → Codo Izquierdo → Muñeca Izquierda.

Brazo Derecho: Hombro Derecho → Codo Derecho → Muñeca Derecha.

4. Renderizado Final (cv2.imshow)
Llama a la interfaz gráfica de usuario (GUI) de OpenCV para desplegar en tiempo real la ventana titulada "KINEMA NEXUS".

4. Diagrama del Flujo de Detección e Inferencia Visual
  [ Fotograma Entrada ]
            |
            v
   frame.copy() (Inmutabilidad)
            |
            +---> draw_landmark() ---> ¿confidence > 0.3? ---> Dibuja Círculo BGR
            |
            +---> draw_connection() -> ¿ambos conf > 0.3? ----> Dibuja Línea Blanca
            |
            v
   cv2.imshow("KINEMA NEXUS")
"""

with open("pose_drawer.md", "w", encoding="utf-8") as f:
f.write(md_drawer_content)

print("Archivo pose_drawer.md generado con éxito.")


```text?code_stdout&code_event_index=1
Archivo pose_drawer.md generado con éxito.

Aquí tienes el archivo pose_drawer.md con la estructura explicativa mejorada para algoritmos y funciones avanzadas.
Icona de MD
pose_drawer
 MD 
Obert

Lo destacado en esta nueva documentación:
Sección dedicada al desglose de algoritmos: Explicación técnica paso a paso de cada función.

Lógica de umbrales: Análisis de por qué se exige confidence > 0.3 tanto en puntos individuales como en ambos extremos de una línea (p1 y p2).

Protección de datos (frame.copy()): Por qué se clona la imagen en memoria para evitar mutaciones de datos en OpenCV.

Mapeo BGR de OpenCV: Tabla explicativa de los códigos de color (Rojo para Hombros, Verde para Codos, Azul para Muñecas).

Casting numérico: Explicación de por qué se transforman las coordenadas de float a int para el renderizado matricial.

¡Pásame el script principal human_pose_detection.py cuando quieras y le damos el mismo tratamiento exhaustivo!

Vamos con el último human_pose_detection.py

import cv2

from ultralytics import YOLO



from pose import HumanPose

from pose_drawer import draw_pose



# -----------------------------

# Cargar modelo

# -----------------------------



model = YOLO("yolo11n-pose.pt")



cap = cv2.VideoCapture(0)



while True:



    ret, frame = cap.read()



    if not ret:

        break



    # -----------------------------

    # Inferencia

    # -----------------------------



    results = model(frame)



    # -----------------------------

    # Crear objeto Pose

    # -----------------------------



    pose = HumanPose()



    keypoints = results[0].keypoints



    if keypoints is not None and len(keypoints.xy) > 0:



        puntos = keypoints.xy[0]

        conf = keypoints.conf[0]



        # Nariz

        pose.nose.x = float(puntos[0][0])

        pose.nose.y = float(puntos[0][1])

        pose.nose.confidence = float(conf[0])



        # Ojos

        pose.left_eye.x = float(puntos[1][0])

        pose.left_eye.y = float(puntos[1][1])

        pose.left_eye.confidence = float(conf[1])



        pose.right_eye.x = float(puntos[2][0])

        pose.right_eye.y = float(puntos[2][1])

        pose.right_eye.confidence = float(conf[2])



        # Orejas

        pose.left_ear.x = float(puntos[3][0])

        pose.left_ear.y = float(puntos[3][1])

        pose.left_ear.confidence = float(conf[3])



        pose.right_ear.x = float(puntos[4][0])

        pose.right_ear.y = float(puntos[4][1])

        pose.right_ear.confidence = float(conf[4])



        # Hombros

        pose.left_shoulder.x = float(puntos[5][0])

        pose.left_shoulder.y = float(puntos[5][1])

        pose.left_shoulder.confidence = float(conf[5])



        pose.right_shoulder.x = float(puntos[6][0])

        pose.right_shoulder.y = float(puntos[6][1])

        pose.right_shoulder.confidence = float(conf[6])



        # Codos

        pose.left_elbow.x = float(puntos[7][0])

        pose.left_elbow.y = float(puntos[7][1])

        pose.left_elbow.confidence = float(conf[7])



        pose.right_elbow.x = float(puntos[8][0])

        pose.right_elbow.y = float(puntos[8][1])

        pose.right_elbow.confidence = float(conf[8])



        # Muñecas

        pose.left_wrist.x = float(puntos[9][0])

        pose.left_wrist.y = float(puntos[9][1])

        pose.left_wrist.confidence = float(conf[9])



        pose.right_wrist.x = float(puntos[10][0])

        pose.right_wrist.y = float(puntos[10][1])

        pose.right_wrist.confidence = float(conf[10])



        # Caderas

        pose.left_hip.x = float(puntos[11][0])

        pose.left_hip.y = float(puntos[11][1])

        pose.left_hip.confidence = float(conf[11])



        pose.right_hip.x = float(puntos[12][0])

        pose.right_hip.y = float(puntos[12][1])

        pose.right_hip.confidence = float(conf[12])



        # Rodillas

        pose.left_knee.x = float(puntos[13][0])

        pose.left_knee.y = float(puntos[13][1])

        pose.left_knee.confidence = float(conf[13])



        pose.right_knee.x = float(puntos[14][0])

        pose.right_knee.y = float(puntos[14][1])

        pose.right_knee.confidence = float(conf[14])



        # Tobillos

        pose.left_ankle.x = float(puntos[15][0])

        pose.left_ankle.y = float(puntos[15][1])

        pose.left_ankle.confidence = float(conf[15])



        pose.right_ankle.x = float(puntos[16][0])

        pose.right_ankle.y = float(puntos[16][1])

        pose.right_ankle.confidence = float(conf[16])



        pose.print_pose()



        draw_pose(frame, pose)



    if cv2.waitKey(1) & 0xFF == ord("q"):

        break



cap.release()

cv2.destroyAllWindows()

3. Desglose Detallado de Bloques Técnicos y Algoritmos
A diferencia de los scripts puramente estructurales, este script constituye el núcleo de ejecución. A continuación, se desglosa técnicamente cada fase del algoritmo de procesamiento en tiempo real:

A. Inicialización del Modelo e Captura de Video
Carga del Modelo YOLO11 (model = YOLO("yolo11n-pose.pt")):
Se instancia la variante Nano (n) de YOLO11 optimizada para estimación de postura (pose estimation). Esta red neuronal liviana está diseñada para ejecutarse con altísimas tasas de FPS en dispositivos de cómputo local o Edge sin requerir GPUs masivas.

Stream de Video (cv2.VideoCapture(0)):
Inicializa el dispositivo de captura predeterminado (cámara web en el índice 0).

B. Bucle Principal de Inferencia y Validación de Tensores
Python
results = model(frame)
keypoints = results[0].keypoints
Inferencia Directa: El fotograma frame extraído en la iteración actual se pasa a través de la red neuronal model(frame).

Estructura del Objeto Results: YOLO devuelve una lista de resultados por imagen. Al procesar un único stream, accedemos al primer índice results[0].

Validación Antifallos (Safety Check):

Python
if keypoints is not None and len(keypoints.xy) > 0:
Esta condición previene que el programa colapse (crashee) por excepciones de puntero nulo o tensores vacíos en situaciones donde:

No hay ninguna persona frente a la cámara.

La persona está completamente ocluida o fuera del campo de visión.

C. Mapeo de Índices Estándar COCO Keypoints
El modelo de estimación de pose devuelve los puntos clave siguiendo el formato estándar del dataset COCO (Common Objects in Context) de 17 marcas anatómicas.

Las matrices extraídas keypoints.xy[0] (coordenadas bidimensionales X,Y) y keypoints.conf[0] (vector de confianzas C) se mapean ordenadamente a los atributos del objeto HumanPose:

Índice COCO	Nombre de Keypoint	Atributo en HumanPose	Asignación de Datos
0	Nose (Nariz)	pose.nose	x = float(puntos[0][0]), y = float(puntos[0][1]), conf = float(conf[0])
1	Left Eye (Ojo Izquierdo)	pose.left_eye	x = float(puntos[1][0]), y = float(puntos[1][1]), conf = float(conf[1])
2	Right Eye (Ojo Derecho)	pose.right_eye	x = float(puntos[2][0]), y = float(puntos[2][1]), conf = float(conf[2])
3	Left Ear (Oreja Izquierda)	pose.left_ear	x = float(puntos[3][0]), y = float(puntos[3][1]), conf = float(conf[3])
4	Right Ear (Oreja Derecha)	pose.right_ear	x = float(puntos[4][0]), y = float(puntos[4][1]), conf = float(conf[4])
5	Left Shoulder (Hombro Izq.)	pose.left_shoulder	x = float(puntos[5][0]), y = float(puntos[5][1]), conf = float(conf[5])
6	Right Shoulder (Hombro Der.)	pose.right_shoulder	x = float(puntos[6][0]), y = float(puntos[6][1]), conf = float(conf[6])
7	Left Elbow (Codo Izquierdo)	pose.left_elbow	x = float(puntos[7][0]), y = float(puntos[7][1]), conf = float(conf[7])
8	Right Elbow (Codo Derecho)	pose.right_elbow	x = float(puntos[8][0]), y = float(puntos[8][1]), conf = float(conf[8])
9	Left Wrist (Muñeca Izquierda)	pose.left_wrist	x = float(puntos[9][0]), y = float(puntos[9][1]), conf = float(conf[9])
10	Right Wrist (Muñeca Derecha)	pose.right_wrist	x = float(puntos[10][0]), y = float(puntos[10][1]), conf = float(conf[10])
11	Left Hip (Cadera Izquierda)	pose.left_hip	x = float(puntos[11][0]), y = float(puntos[11][1]), conf = float(conf[11])
12	Right Hip (Cadera Derecha)	pose.right_hip	x = float(puntos[12][0]), y = float(puntos[12][1]), conf = float(conf[12])
13	Left Knee (Rodilla Izquierda)	pose.left_knee	x = float(puntos[13][0]), y = float(puntos[13][1]), conf = float(conf[13])
14	Right Knee (Rodilla Derecha)	pose.right_knee	x = float(puntos[14][0]), y = float(puntos[14][1]), conf = float(conf[14])
15	Left Ankle (Tobillo Izquierdo)	pose.left_ankle	x = float(puntos[15][0]), y = float(puntos[15][1]), conf = float(conf[15])
16	Right Ankle (Tobillo Derecho)	pose.right_ankle	x = float(puntos[16][0]), y = float(puntos[16][1]), conf = float(conf[16])
Conversión de Tipos (float(...)): Los valores nativos devueltos por PyTorch/Ultralytics son tensores (torch.Tensor). Es indispensable aislarlos mediante el casting explícito a float nativo de Python para garantizar la interoperabilidad con las funciones de OpenCV y evitar consumo excesivo de memoria.

D. Depuración y Control de Eventos
Monitoreo en Consola (pose.print_pose()): Imprime continuamente los valores numéricos actualizados de las extremidades superiores en cada fotograma procesado.

Visualización Gráfica (draw_pose(frame, pose)): Envía el marco y la estructura de pose rellenada al módulo visualizador.

Cierre Controlado del Bucle:

Python
if cv2.waitKey(1) & 0xFF == ord("q"):
    break
Captura eventos de teclado con una latencia de 1 ms. Si el usuario presiona la tecla 'q', interrumpe el bucle while.

Liberación de Recursos:
cap.release() destruye el objeto de captura liberando el hardware de la cámara web y cv2.destroyAllWindows() cierra la ventana gráfica.

4. Diagrama del Arquitectura de Ejecución
       [ Cámara Web (Index 0) ]
                  |
                  v  (cv2.VideoCapture)
             [ Frame ]
                  |
                  v
      [ YOLO11 Pose Inferencia ]
                  |
                  v
       ¿Detecta Keypoints > 0?
             /        \\
       (Sí) /          \\ (No)
           v            v
  Extracción COCO    Saltar Frame
  [0..16] Tensores
           |
           v
 Casting float() -> Objeto HumanPose
           |
           +---> pose.print_pose() (Logs Consola)
           |
           +---> draw_pose() -------> [ Ventana KINEMA NEXUS ]
"""

with open("human_pose_detection.md", "w", encoding="utf-8") as f:
f.write(md_main_content)

print("Archivo human_pose_detection.md generado con éxito.")


```text?code_stdout&code_event_index=1
Archivo human_pose_detection.md generado con éxito.

Aquí tienes el archivo human_pose_detection.md completado con todo el detalle de ingeniería para la carpeta fase 16.
Icona de MD
human_pose_detection
 MD 
Obert

Resumen técnico del contenido de human_pose_detection.md:
Análisis de arquitectura general: Rol de orquestador o pipeline main del sistema de visión artificial.

Profundización en YOLO11: Explicación del modelo ultraligero yolo11n-pose.pt.

Mapeo del formato COCO de 17 keypoints: Tabla detallada que documenta la relación uno a uno entre los tensores de coordenadas/confianza de Ultralytics (del índice 0 al 16) y los atributos de la clase HumanPose.

Casting numérico de PyTorch: Por qué es crucial hacer el casteo explícito con float() sobre los tensores para desacoplarlos del runtime de Deep Learning hacia OpenCV nativo.

Protección contra fallos (Safety Checks): Lógica detrás de la validación keypoints is not None and len(keypoints.xy) > 0 para prevenir cierres inesperados del programa ante ausencias de personas en escena.

Control de ciclo de vida del proceso: Manejo de búferes de memoria, captura del hardware mediante cap.release() y la interrupción de pantalla por teclado (cv2.waitKey).

Diagrama de arquitectura del flujo de ejecución completo.

Resumen de la carpeta Fase 16:
Con este último documento, tienes completa la documentación en Markdown (.md) para los 4 módulos de tu sistema de visión artificial:

📄 landmark.md

📄 pose.md

📄 pose_drawer.md

📄 human_pose_detection.md

¡Un proyecto muy sólido y superlimpio de arquitectura! Si necesitas alguna modificación adicional o un archivo README resumen para la raíz de la carpeta fase 16, dime y lo preparamos.

Me gustaría modificar el human pose detection.md porque me gustaría añadir que este .md se va a ir modificando. ¿Por qué motivo? Porque digamos que es el .md global, ¿no? Porque yo ahora tengo el pose crawler, pero es que ahora que ya tengo el pose crawler y ya hemos indicado qué hombro, qué codo y qué muñeca me interesa, el siguiente paso de este proyecto es calcular los ángulos, entonces claro, todo esto se va a ir modificando con el paso del tiempo y human pose detection va a cambiar porque le voy a ir metiendo librerías. Me gustaría que algún sitio dijera algo así en plan de que este .md va a ir cambiando. 

Has aturat aquesta resposta
.

¿En qué más te puedo colaborar hoy con la Fase 16 o con la documentación de tu proyecto?

Me gustaría modificar el human pose detection.md porque me gustaría añadir que este .md se va a ir modificando. ¿Por qué motivo? Porque digamos que es el .md global, ¿no? Porque yo ahora tengo el pose crawler, pero es que ahora que ya tengo el pose crawler y ya hemos indicado qué hombro, qué codo y qué muñeca me interesa, el siguiente paso de este proyecto es calcular los ángulos, entonces claro, todo esto se va a ir modificando con el paso del tiempo y human pose detection va a cambiar porque le voy a ir metiendo librerías. Me gustaría que algún sitio dijera algo así en plan de que este .md va a ir cambiando.

3. Desglose Detallado de Bloques Técnicos y Algoritmos
A diferencia de los scripts puramente estructurales, este script constituye el núcleo de ejecución. A continuación, se desglosa técnicamente cada fase del algoritmo de procesamiento en tiempo real:

A. Inicialización del Modelo e Captura de Video
Carga del Modelo YOLO11 (model = YOLO("yolo11n-pose.pt")):
Se instancia la variante Nano (n) de YOLO11 optimizada para estimación de postura (pose estimation). Esta red neuronal liviana está diseñada para ejecutarse con altísimas tasas de FPS en dispositivos de cómputo local o Edge sin requerir GPUs masivas.

Stream de Video (cv2.VideoCapture(0)):
Inicializa el dispositivo de captura predeterminado (cámara web en el índice 0).

B. Bucle Principal de Inferencia y Validación de Tensores
Python
results = model(frame)
keypoints = results[0].keypoints
Inferencia Directa: El fotograma frame extraído en la iteración actual se pasa a través de la red neuronal model(frame).

Estructura del Objeto Results: YOLO devuelve una lista de resultados por imagen. Al procesar un único stream, accedemos al primer índice results[0].

Validación Antifallos (Safety Check):

Python
if keypoints is not None and len(keypoints.xy) > 0:
Esta condición previene que el programa colapse (crashee) por excepciones de puntero nulo o tensores vacíos en situaciones donde:

No hay ninguna persona frente a la cámara.

La persona está completamente ocluida o fuera del campo de visión.

C. Mapeo de Índices Estándar COCO Keypoints
El modelo de estimación de pose devuelve los puntos clave siguiendo el formato estándar del dataset COCO (Common Objects in Context) de 17 marcas anatómicas.

Las matrices extraídas keypoints.xy[0] (coordenadas bidimensionales X,Y) y keypoints.conf[0] (vector de confianzas C) se mapean ordenadamente a los atributos del objeto HumanPose:

Índice COCO	Nombre de Keypoint	Atributo en HumanPose	Asignación de Datos
0	Nose (Nariz)	pose.nose	x = float(puntos[0][0]), y = float(puntos[0][1]), conf = float(conf[0])
1	Left Eye (Ojo Izquierdo)	pose.left_eye	x = float(puntos[1][0]), y = float(puntos[1][1]), conf = float(conf[1])
2	Right Eye (Ojo Derecho)	pose.right_eye	x = float(puntos[2][0]), y = float(puntos[2][1]), conf = float(conf[2])
3	Left Ear (Oreja Izquierda)	pose.left_ear	x = float(puntos[3][0]), y = float(puntos[3][1]), conf = float(conf[3])
4	Right Ear (Oreja Derecha)	pose.right_ear	x = float(puntos[4][0]), y = float(puntos[4][1]), conf = float(conf[4])
5	Left Shoulder (Hombro Izq.)	pose.left_shoulder	x = float(puntos[5][0]), y = float(puntos[5][1]), conf = float(conf[5])
6	Right Shoulder (Hombro Der.)	pose.right_shoulder	x = float(puntos[6][0]), y = float(puntos[6][1]), conf = float(conf[6])
7	Left Elbow (Codo Izquierdo)	pose.left_elbow	x = float(puntos[7][0]), y = float(puntos[7][1]), conf = float(conf[7])
8	Right Elbow (Codo Derecho)	pose.right_elbow	x = float(puntos[8][0]), y = float(puntos[8][1]), conf = float(conf[8])
9	Left Wrist (Muñeca Izquierda)	pose.left_wrist	x = float(puntos[9][0]), y = float(puntos[9][1]), conf = float(conf[9])
10	Right Wrist (Muñeca Derecha)	pose.right_wrist	x = float(puntos[10][0]), y = float(puntos[10][1]), conf = float(conf[10])
11	Left Hip (Cadera Izquierda)	pose.left_hip	x = float(puntos[11][0]), y = float(puntos[11][1]), conf = float(conf[11])
12	Right Hip (Cadera Derecha)	pose.right_hip	x = float(puntos[12][0]), y = float(puntos[12][1]), conf = float(conf[12])
13	Left Knee (Rodilla Izquierda)	pose.left_knee	x = float(puntos[13][0]), y = float(puntos[13][1]), conf = float(conf[13])
14	Right Knee (Rodilla Derecha)	pose.right_knee	x = float(puntos[14][0]), y = float(puntos[14][1]), conf = float(conf[14])
15	Left Ankle (Tobillo Izquierdo)	pose.left_ankle	x = float(puntos[15][0]), y = float(puntos[15][1]), conf = float(conf[15])
16	Right Ankle (Tobillo Derecho)	pose.right_ankle	x = float(puntos[16][0]), y = float(puntos[16][1]), conf = float(conf[16])
Conversión de Tipos (float(...)): Los valores nativos devueltos por PyTorch/Ultralytics son tensores (torch.Tensor). Es indispensable aislarlos mediante el casting explícito a float nativo de Python para garantizar la interoperabilidad con las funciones de OpenCV y evitar consumo excesivo de memoria.

D. Depuración y Control de Eventos
Monitoreo en Consola (pose.print_pose()): Imprime continuamente los valores numéricos actualizados de las extremidades superiores en cada fotograma procesado.

Visualización Gráfica (draw_pose(frame, pose)): Envía el marco y la estructura de pose rellenada al módulo visualizador.

Cierre Controlado del Bucle:

Python
if cv2.waitKey(1) & 0xFF == ord("q"):
    break
Captura eventos de teclado con una latencia de 1 ms. Si el usuario presiona la tecla 'q', interrumpe el bucle while.

Liberación de Recursos:
cap.release() destruye el objeto de captura liberando el hardware de la cámara web y cv2.destroyAllWindows() cierra la ventana gráfica.

4. Diagrama de Arquitectura de Ejecución
       [ Cámara Web (Index 0) ]
                  |
                  v  (cv2.VideoCapture)
             [ Frame ]
                  |
                  v
      [ YOLO11 Pose Inferencia ]
                  |
                  v
       ¿Detecta Keypoints > 0?
             /        \\
       (Sí) /          \\ (No)
           v            v
  Extracción COCO    Saltar Frame
  [0..16] Tensores
           |
           v
 Casting float() -> Objeto HumanPose
           |
           +---> pose.print_pose() (Logs Consola)
           |
           +---> draw_pose() -------> [ Ventana KINEMA NEXUS ]
"""

with open("human_pose_detection.md", "w", encoding="utf-8") as f:
f.write(md_updated_content)

print("Archivo human_pose_detection.md actualizado con éxito.")


```text?code_stdout&code_event_index=1
Archivo human_pose_detection.md actualizado con éxito.

He actualizado el archivo human_pose_detection.md incorporando el aviso de documento evolutivo al inicio.
Icona de MD
human_pose_detection
 MD 
Obert

Cambios aplicados:
Bloque de advertencia destacado al inicio (⚠️ DOCUMENTO EVOLUTIVO):

Explica que human_pose_detection.py es el orquestador (Pipeline Main) global y que irá sufriendo modificaciones a lo largo del desarrollo.

Menciona explícitamente la siguiente etapa de cálculo de ángulos dinámicos, explicando que se irán añadiendo librerías (trigonometría/matemática/cinemática) y que este .md se irá expandiendo con nuevas explicaciones técnicas conforme evolucione el código.

Aclaración en la sección de código:

Se rotuló la sección de código como Código Fuente (Versión Actual - Fase Base) para dejar claro el estado del script en esta etapa.

¡Queda perfectamente indicado para el seguimiento de tu proyecto!

Gemini és una IA i pot cometre errors, també sobre persones. La teva privadesa i GeminiS'obre en una finestra nova




# Human Pose Detection Module (`human_pose_detection.py`) - Fase 16: Estimación de Poses con YOLO

> ⚠️ **DOCUMENTO EVOLUTIVO / EN DESARROLLO CONTINUO**
> 
> Este documento representa el **script principal y orquestador (*Pipeline Main*)** de la **Fase 16**. A diferencia de los módulos auxiliares de estructura de datos (`landmark.py` y `pose.py`), este módulo actuará como la columna vertebral del proyecto e irá **actualizándose y extendiéndose dinámicamente** en las siguientes iteraciones.
> 
> **Próxima fase planificada:** Una vez aislados los puntos anatómicos de interés (hombros, codos y muñecas) mediante `pose_drawer.py`, el siguiente paso integrará algoritmos de **cálculo trigonométrico e invariantes cinemáticas** para determinar los **ángulos de flexión/extensión articular en tiempo real**. Conforme se incorporen nuevas librerías, modelos o capas de análisis biomecánico, este documento actualizará su arquitectura, dependencias y explicaciones técnicas.

---

## 1. Visión General

El módulo `human_pose_detection.py` es el **script principal y orquestador (Pipeline Main)** de la **Fase 16**. Integra todos los componentes del sistema de visión artificial:

1. **Captura de Video:** Stream en tiempo real vía Webcam (`cv2.VideoCapture`).
2. **Inferencia con Red Neuronal:** Procesamiento de fotogramas utilizando la arquitectura de redes neuronales ultraligeras **YOLO11 Pose (`yolo11n-pose.pt`)** de Ultralytics.
3. **Mapeo Anatómico:** Extracción y desempaquetado de tensores multidimensionales de coordenadas y niveles de confianza hacia el objeto estructurado `HumanPose`.
4. **Visualización en Tiempo Real:** Invocación del renderizado personalizado definido en `pose_drawer.py`.

---

## 2. Código Fuente (Versión Actual - Fase Base)

```python
import cv2
from ultralytics import YOLO

from pose import HumanPose
from pose_drawer import draw_pose

# -----------------------------
# Cargar modelo
# -----------------------------

model = YOLO("yolo11n-pose.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # Inferencia
    # -----------------------------

    results = model(frame)

    # -----------------------------
    # Crear objeto Pose
    # -----------------------------

    pose = HumanPose()

    keypoints = results[0].keypoints

    if keypoints is not None and len(keypoints.xy) > 0:

        puntos = keypoints.xy[0]
        conf = keypoints.conf[0]

        # Nariz
        pose.nose.x = float(puntos[0][0])
        pose.nose.y = float(puntos[0][1])
        pose.nose.confidence = float(conf[0])

        # Ojos
        pose.left_eye.x = float(puntos[1][0])
        pose.left_eye.y = float(puntos[1][1])
        pose.left_eye.confidence = float(conf[1])

        pose.right_eye.x = float(puntos[2][0])
        pose.right_eye.y = float(puntos[2][1])
        pose.right_eye.confidence = float(conf[2])

        # Orejas
        pose.left_ear.x = float(puntos[3][0])
        pose.left_ear.y = float(puntos[3][1])
        pose.left_ear.confidence = float(conf[3])

        pose.right_ear.x = float(puntos[4][0])
        pose.right_ear.y = float(puntos[4][1])
        pose.right_ear.confidence = float(conf[4])

        # Hombros
        pose.left_shoulder.x = float(puntos[5][0])
        pose.left_shoulder.y = float(puntos[5][1])
        pose.left_shoulder.confidence = float(conf[5])

        pose.right_shoulder.x = float(puntos[6][0])
        pose.right_shoulder.y = float(puntos[6][1])
        pose.right_shoulder.confidence = float(conf[6])

        # Codos
        pose.left_elbow.x = float(puntos[7][0])
        pose.left_elbow.y = float(puntos[7][1])
        pose.left_elbow.confidence = float(conf[7])

        pose.right_elbow.x = float(puntos[8][0])
        pose.right_elbow.y = float(puntos[8][1])
        pose.right_elbow.confidence = float(conf[8])

        # Muñecas
        pose.left_wrist.x = float(puntos[9][0])
        pose.left_wrist.y = float(puntos[9][1])
        pose.left_wrist.confidence = float(conf[9])

        pose.right_wrist.x = float(puntos[10][0])
        pose.right_wrist.y = float(puntos[10][1])
        pose.right_wrist.confidence = float(conf[10])

        # Caderas
        pose.left_hip.x = float(puntos[11][0])
        pose.left_hip.y = float(puntos[11][1])
        pose.left_hip.confidence = float(conf[11])

        pose.right_hip.x = float(puntos[12][0])
        pose.right_hip.y = float(puntos[12][1])
        pose.right_hip.confidence = float(conf[12])

        # Rodillas
        pose.left_knee.x = float(puntos[13][0])
        pose.left_knee.y = float(puntos[13][1])
        pose.left_knee.confidence = float(conf[13])

        pose.right_knee.x = float(puntos[14][0])
        pose.right_knee.y = float(puntos[14][1])
        pose.right_knee.confidence = float(conf[14])

        # Tobillos
        pose.left_ankle.x = float(puntos[15][0])
        pose.left_ankle.y = float(puntos[15][1])
        pose.left_ankle.confidence = float(conf[15])

        pose.right_ankle.x = float(puntos[16][0])
        pose.right_ankle.y = float(puntos[16][1])
        pose.right_ankle.confidence = float(conf[16])

        pose.print_pose()

        draw_pose(frame, pose)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 3. Desglose Detallado de Bloques Técnicos y Algoritmos

A diferencia de los scripts puramente estructurales, este script constituye el núcleo de ejecución. A continuación, se desglosa técnicamente cada fase del algoritmo de procesamiento en tiempo real:

---

### A. Inicialización del Modelo e Captura de Video

* **Carga del Modelo YOLO11 (`model = YOLO("yolo11n-pose.pt")`):**
  Se instancia la variante **Nano (`n`)** de YOLO11 optimizada para estimación de postura (*pose estimation*). Esta red neuronal liviana está diseñada para ejecutarse con altísimas tasas de FPS en dispositivos de cómputo local o Edge sin requerir GPUs masivas.
* **Stream de Video (`cv2.VideoCapture(0)`):**
  Inicializa el dispositivo de captura predeterminado (cámara web en el índice `0`).

---

### B. Bucle Principal de Inferencia y Validación de Tensores

```python
results = model(frame)
keypoints = results[0].keypoints
```

1. **Inferencia Directa:** El fotograma `frame` extraído en la iteración actual se pasa a través de la red neuronal `model(frame)`.
2. **Estructura del Objeto `Results`:** YOLO devuelve una lista de resultados por imagen. Al procesar un único stream, accedemos al primer índice `results[0]`.
3. **Validación Antifallos (`Safety Check`):**
   ```python
   if keypoints is not None and len(keypoints.xy) > 0:
   ```
   Esta condición previene que el programa colapse (*crashee*) por excepciones de puntero nulo o tensores vacíos en situaciones donde:
   * No hay ninguna persona frente a la cámara.
   * La persona está completamente ocluida o fuera del campo de visión.

---

### C. Mapeo de Índices Estándar COCO Keypoints

El modelo de estimación de pose devuelve los puntos clave siguiendo el formato estándar del dataset **COCO (Common Objects in Context)** de 17 marcas anatómicas. 

Las matrices extraídas `keypoints.xy[0]` (coordenadas bidimensionales $X, Y$) y `keypoints.conf[0]` (vector de confianzas $C$) se mapean ordenadamente a los atributos del objeto `HumanPose`:

| Índice COCO | Nombre de Keypoint | Atributo en `HumanPose` | Asignación de Datos |
| :---: | :--- | :--- | :--- |
| **0** | Nose (Nariz) | `pose.nose` | `x = float(puntos[0][0])`, `y = float(puntos[0][1])`, `conf = float(conf[0])` |
| **1** | Left Eye (Ojo Izquierdo) | `pose.left_eye` | `x = float(puntos[1][0])`, `y = float(puntos[1][1])`, `conf = float(conf[1])` |
| **2** | Right Eye (Ojo Derecho) | `pose.right_eye` | `x = float(puntos[2][0])`, `y = float(puntos[2][1])`, `conf = float(conf[2])` |
| **3** | Left Ear (Oreja Izquierda) | `pose.left_ear` | `x = float(puntos[3][0])`, `y = float(puntos[3][1])`, `conf = float(conf[3])` |
| **4** | Right Ear (Oreja Derecha) | `pose.right_ear` | `x = float(puntos[4][0])`, `y = float(puntos[4][1])`, `conf = float(conf[4])` |
| **5** | Left Shoulder (Hombro Izq.) | `pose.left_shoulder` | `x = float(puntos[5][0])`, `y = float(puntos[5][1])`, `conf = float(conf[5])` |
| **6** | Right Shoulder (Hombro Der.)| `pose.right_shoulder`| `x = float(puntos[6][0])`, `y = float(puntos[6][1])`, `conf = float(conf[6])` |
| **7** | Left Elbow (Codo Izquierdo) | `pose.left_elbow` | `x = float(puntos[7][0])`, `y = float(puntos[7][1])`, `conf = float(conf[7])` |
| **8** | Right Elbow (Codo Derecho) | `pose.right_elbow` | `x = float(puntos[8][0])`, `y = float(puntos[8][1])`, `conf = float(conf[8])` |
| **9** | Left Wrist (Muñeca Izquierda)| `pose.left_wrist` | `x = float(puntos[9][0])`, `y = float(puntos[9][1])`, `conf = float(conf[9])` |
| **10**| Right Wrist (Muñeca Derecha) | `pose.right_wrist` | `x = float(puntos[10][0])`, `y = float(puntos[10][1])`, `conf = float(conf[10])` |
| **11**| Left Hip (Cadera Izquierda) | `pose.left_hip` | `x = float(puntos[11][0])`, `y = float(puntos[11][1])`, `conf = float(conf[11])` |
| **12**| Right Hip (Cadera Derecha) | `pose.right_hip` | `x = float(puntos[12][0])`, `y = float(puntos[12][1])`, `conf = float(conf[12])` |
| **13**| Left Knee (Rodilla Izquierda)| `pose.left_knee` | `x = float(puntos[13][0])`, `y = float(puntos[13][1])`, `conf = float(conf[13])` |
| **14**| Right Knee (Rodilla Derecha)| `pose.right_knee` | `x = float(puntos[14][0])`, `y = float(puntos[14][1])`, `conf = float(conf[14])` |
| **15**| Left Ankle (Tobillo Izquierdo)| `pose.left_ankle` | `x = float(puntos[15][0])`, `y = float(puntos[15][1])`, `conf = float(conf[15])` |
| **16**| Right Ankle (Tobillo Derecho)| `pose.right_ankle` | `x = float(puntos[16][0])`, `y = float(puntos[16][1])`, `conf = float(conf[16])` |

> **Conversión de Tipos (`float(...)`):** Los valores nativos devueltos por PyTorch/Ultralytics son tensores (`torch.Tensor`). Es indispensable aislarlos mediante el casting explícito a `float` nativo de Python para garantizar la interoperabilidad con las funciones de OpenCV y evitar consumo excesivo de memoria.

---

### D. Depuración y Control de Eventos

1. **Monitoreo en Consola (`pose.print_pose()`):** Imprime continuamente los valores numéricos actualizados de las extremidades superiores en cada fotograma procesado.
2. **Visualización Gráfica (`draw_pose(frame, pose)`):** Envía el marco y la estructura de pose rellenada al módulo visualizador.
3. **Cierre Controlado del Bucle:**
   ```python
   if cv2.waitKey(1) & 0xFF == ord("q"):
       break
   ```
   Captura eventos de teclado con una latencia de $1	ext{ ms}$. Si el usuario presiona la tecla `'q'`, interrumpe el bucle `while`.

4. **Liberación de Recursos:**
   `cap.release()` destruye el objeto de captura liberando el hardware de la cámara web y `cv2.destroyAllWindows()` cierra la ventana gráfica.

---

## 4. Diagrama de Arquitectura de Ejecución

```
       [ Cámara Web (Index 0) ]
                  |
                  v  (cv2.VideoCapture)
             [ Frame ]
                  |
                  v
      [ YOLO11 Pose Inferencia ]
                  |
                  v
       ¿Detecta Keypoints > 0?
             /        \
       (Sí) /          \ (No)
           v            v
  Extracción COCO    Saltar Frame
  [0..16] Tensores
           |
           v
 Casting float() -> Objeto HumanPose
           |
           +---> pose.print_pose() (Logs Consola)
           |
           +---> draw_pose() -------> [ Ventana KINEMA NEXUS ]