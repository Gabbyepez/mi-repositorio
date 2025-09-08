# -*- coding: utf-8 -*-
# Registro de Temperaturas Diarias (matriz 3D + promedios + CSV + gráfica)

import random
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 3  # cantidad de semanas

# 2️⃣ Crear matriz 3D vacía
temperaturas = []
for ciudad in ciudades:
    semanas = []
    for s in range(num_semanas):
        dias_temperatura = [0 for _ in dias]
        semanas.append(dias_temperatura)
    temperaturas.append(semanas)

# 3️⃣ Llenar la matriz con temperaturas aleatorias
rangos_por_ciudad = {
    "Quito": (9, 23),
    "Guayaquil": (22, 33),
    "Cuenca": (10, 22),
}

for i, ciudad in enumerate(ciudades):
    min_temp, max_temp = rangos_por_ciudad[ciudad]
    for s in range(num_semanas):
        for d in range(len(dias)):
            temperaturas[i][s][d] = random.randint(min_temp, max_temp)

# 4️⃣ Mostrar la matriz completa
print("Matriz 3D con temperaturas por ciudad, semana y día:")
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for s in range(num_semanas):
        print(f"  Semana {s+1}: {temperaturas[i][s]}")

# 5️⃣ Calcular promedios semanales
promedios = [[0 for _ in range(num_semanas)] for _ in ciudades]
for i in range(len(ciudades)):
    for s in range(num_semanas):
        suma = sum(temperaturas[i][s])
        promedio = suma / len(dias)
        promedios[i][s] = promedio

# 6️⃣ Mostrar promedios
print("\nPROMEDIOS SEMANALES POR CIUDAD:")
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for s in range(num_semanas):
        print(f"  Semana {s+1}: {promedios[i][s]:.2f} °C")

# 7️⃣ Guardar resultados en CSV
rows = []
for i, ciudad in enumerate(ciudades):
    for s in range(num_semanas):
        rows.append({
            "Ciudad": ciudad,
            "Semana": s+1,
            "Promedio_C": round(promedios[i][s], 2)
        })

df = pd.DataFrame(rows)
csv_path = "promedios.csv"
df.to_csv(csv_path, index=False, encoding="utf-8")
print(f"\nArchivo CSV guardado como '{csv_path}'")

# 8️⃣ Crear gráfica de barras
pivot = df.pivot(index="Semana", columns="Ciudad", values="Promedio_C")
ax = pivot.plot(kind="bar", figsize=(8,5), rot=0, title="Promedio semanal por ciudad (°C)")
ax.set_xlabel("Semana")
ax.set_ylabel("Temperatura promedio (°C)")
plt.tight_layout()
fig_path = "promedios.png"
plt.savefig(fig_path)
plt.show()
print(f"Gráfica guardada como '{fig_path}'")

