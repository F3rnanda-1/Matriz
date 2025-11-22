estudiantes = int(input("¿Cuántos estudiantes hay en el grupo? "))
materias = int(input("¿Cuántas materias tiene el grupo? "))

matriz = []

print("\nCALIFICACIONES(0–100)")
for i in range(estudiantes):
    fila = []
    print(f"\nEstudiante {i+1}:")
    for j in range(materias):
        while True:
            calificacion = float(input(f"Calificación en materia {j+1}: "))
            if 0 <= calificacion <= 100:
                break
            else:
                print("La calificación debe estar entre 0 y 100.")
        fila.append(calificacion)
    matriz.append(fila)

promedio_estudiantes = [sum(fila) / materias for fila in matriz]

promedio_materias = []
for j in range(materias):
    suma = 0
    for i in range(estudiantes):
        suma += matriz[i][j]
    promedio_materias.append(suma / estudiantes)

maxima = max(max(fila) for fila in matriz)
minima = min(min(fila) for fila in matriz)

print("\nRESULTADOS\n")

print("Promedio por estudiante:")
for i, prom in enumerate(promedio_estudiantes, start=1):
    print(f"Estudiante {i}: {prom:.2f}")

print("\nPromedio por materia:")
for j, prom in enumerate(promedio_materias, start=1):
    print(f"Materia {j}: {prom:.2f}")

print(f"\nCalificación más alta: {maxima}")
print(f"Calificación más baja: {minima}")

print("\nHasta luego")
