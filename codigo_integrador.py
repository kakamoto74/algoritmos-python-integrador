# Lista de estudiantes (cada uno es un diccionario)
estudiantes = [
    {"nombre": "Ana", "dni": 43123456, "nota_final": 8.5},
    {"nombre": "Luis", "dni": 40987654, "nota_final": 7.0},
    {"nombre": "Marta", "dni": 42111222, "nota_final": 9.2},
    {"nombre": "Pedro", "dni": 40123456, "nota_final": 6.8},
]

# Búsqueda lineal por DNI
def busqueda_lineal_por_dni(lista, dni):
    for estudiante in lista:
        if estudiante["dni"] == dni:
            return estudiante
    return None

# Ordenamiento burbuja por nota_final
def ordenar_por_nota(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["nota_final"] > lista[j + 1]["nota_final"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Búsqueda binaria por DNI (requiere lista ordenada por DNI)
def busqueda_binaria_por_dni(lista, dni):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = lista[medio]["dni"]
        if actual == dni:
            return lista[medio]
        elif actual < dni:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

# Ejecución y validación del funcionamiento
print("Lista original:")
for e in estudiantes:
    print(e)

print("\nEstudiante con DNI 42111222:")
print(busqueda_lineal_por_dni(estudiantes, 42111222))

print("\nLista ordenada por nota:")
ordenar_por_nota(estudiantes)
for e in estudiantes:
    print(e)

print("\nLista ordenada por DNI para búsqueda binaria:")
estudiantes.sort(key=lambda x: x["dni"])
for e in estudiantes:
    print(e)

print("\nEstudiante con DNI 40123456 (binaria):")
print(busqueda_binaria_por_dni(estudiantes, 40123456))