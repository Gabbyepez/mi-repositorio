import pandas as pd

# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

temperaturas = [
    [   # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ]
    ],
    [   # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 52},
            {"day": "Miércoles", "temp": 55},
            {"day": "Jueves", "temp": 58},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 62},
            {"day": "Domingo", "temp": 65}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 54},
            {"day": "Miércoles", "temp": 57},
            {"day": "Jueves", "temp": 59},
            {"day": "Viernes", "temp": 61},
            {"day": "Sábado", "temp": 63},
            {"day": "Domingo", "temp": 66}
        ]
    ]
]

# Lista para guardar resultados
resultados = []

# Calcular promedio de cada ciudad por semana usando bucles anidados
for i, ciudad in enumerate(temperaturas, start=1):
    for j, semana in enumerate(ciudad, start=1):
        suma = 0
        for dia in semana:
            suma += dia["temp"]
        promedio = suma / len(semana)
        resultados.append({"Ciudad": f"Ciudad {i}", "Semana": f"Semana {j}", "Promedio": promedio})

# Mostrar resultados en consola
print("Promedio de temperaturas por ciudad y semana:")
for r in resultados:
    print(r)

# Guardar en un archivo CSV
df = pd.DataFrame(resultados)
df.to_csv("promedios.csv", index=False, encoding="utf-8")

print("\nArchivo 'promedios.csv' creado con éxito ✅")

