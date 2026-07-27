import math


# ==========================================
# VECTORES
# ==========================================

def calculate_vector(origin, destination):

    dx = destination.x - origin.x
    dy = destination.y - origin.y

    return dx, dy


def normalize_vector(vector):

    modulo = math.sqrt(
        vector[0]**2 +
        vector[1]**2
    )

    if modulo == 0:
        return (0, 0)

    vector_normalizado = (
        vector[0] / modulo,
        vector[1] / modulo
    )

    return vector_normalizado

# ==========================================
# ÁNGULOS
# ==========================================

def calculate_angle(vector_A, vector_B):

    # Producto escalar
    producto_escalar = (
        vector_A[0] * vector_B[0] +
        vector_A[1] * vector_B[1]
    )

    # Módulos
    modulo_vector_A = math.sqrt(
        vector_A[0]**2 +
        vector_A[1]**2
    )

    modulo_vector_B = math.sqrt(
        vector_B[0]**2 +
        vector_B[1]**2
    )

    if modulo_vector_A == 0 or modulo_vector_B == 0:
        return 0

    # Coseno del ángulo
    coseno_angulo = (
        producto_escalar /
        (modulo_vector_A * modulo_vector_B)
    )

    # Evita errores numéricos
    coseno_angulo = max(-1.0, min(1.0, coseno_angulo))

    # Ángulo en grados
    angulo = math.degrees(math.acos(coseno_angulo))

    return angulo

# ==========================================
# DISTANCIAS
# ==========================================

def calculate_distance(origin, destination):

    dx = destination.x - origin.x
    dy = destination.y - origin.y

    distancia = math.sqrt(
        dx**2 +
        dy**2
    )

    return distancia