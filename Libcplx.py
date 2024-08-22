import math

def saludo(nombre):
    print(f'Hola, {nombre}')

def sumar_complejos(complejo1, complejo2):
    real_sum = complejo1[0] + complejo2[0]
    imaginario_sum = complejo1[1] + complejo2[1]
    return (real_sum, imaginario_sum)

def multiplicar_complejos(complejo1, complejo2):
    real_mult1 = complejo1[0] * complejo2[0]
    imaginario_mult1 = complejo1[1] * complejo2[1]
    real_mult2 = complejo1[0] * complejo2[1]
    imaginario_mult2 = complejo1[1] * complejo2[0]
    parte_real = real_mult1 - imaginario_mult1
    parte_imaginaria = real_mult2 + imaginario_mult2
    return (parte_real, parte_imaginaria)

def restar_complejos(complejo1, complejo2):
    real_rest = complejo1[0] - complejo2[0]
    imaginario_rest = complejo1[1] - complejo2[1]
    return (real_rest, imaginario_rest)

def dividir_complejos(complejo1, complejo2):
    numerador_real = (complejo1[0] * complejo2[0]) + (complejo1[1] * complejo2[1])
    denominador = (complejo2[0] ** 2) + (complejo2[1] ** 2)
    numerador_imaginario = (complejo2[0] * complejo1[1]) - (complejo1[0] * complejo2[1])
    parte_real = numerador_real / denominador
    parte_imaginaria = numerador_imaginario / denominador
    return (parte_real, parte_imaginaria)

def modulo_complejo(complejo):
    real_cuadrado = complejo[0]**2
    imaginario_cuadrado = complejo[1]**2
    suma_cuadrados = real_cuadrado + imaginario_cuadrado
    modulo = suma_cuadrados**0.5
    return modulo

def conjugado_complejo(complejo):
    parte_real = complejo[0]
    parte_imaginaria = -complejo[1]
    return (parte_real, parte_imaginaria)

def polar_a_cartesiano(complejo):
    modulo = modulo_complejo(complejo)
    fase = fase_complejo(complejo)
    real = modulo * math.cos(fase)
    imaginario = modulo * math.sin(fase)
    return (real, imaginario)

def fase_complejo(complejo):
    tangente = complejo[1] / complejo[0]
    angulo = math.atan(tangente)
    return angulo


if __name__ == '__main__':
    print("Suma:", sumar_complejos((8,5), (3, 3)))
    print("Multiplicación:", multiplicar_complejos((1,7), (9, 3.9)))
    print("Resta:", restar_complejos((1,8), (3, 2.5)))
    print("División:", dividir_complejos((1,-6), (-4,1)))
    print("Módulo:", modulo_complejo((2,9)))
    print("Conjugado:", conjugado_complejo((6,9)))
    print("Fase:", fase_complejo((5,8)))
    print("Polar a cartesiano:", polar_a_cartesiano((3,3)))




