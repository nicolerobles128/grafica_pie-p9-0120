# Nombre: [Tu Nombre Completo Aquí]
# NC: 0777

import matplotlib.pyplot as plt

# 1. Nombre de 5 materias en lugar de categorías
materias = ['Matemáticas', 'Física', 'Química', 'Programación', 'Inglés']

# 2. Calificaciones (una por materia) en lugar de sales
calificaciones = [85, 90, 78, 95, 88]

# Crear gráfica de pastel basada en la estructura del min 21:49
plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')

# 3 y 4. Uso de title (con NC 0777), xlabel y ylabel
plt.title("Calificaciones por Materia - NC: 0120")
plt.xlabel("Distribución de Materias")
plt.ylabel("Calificación Relativa")

# Mostrar la gráfica
plt.show()

# 6. Imprimir al final nombre completo y número de control
print("Nombre Completo: [Tu Nombre Completo Aquí]")
print("Número de Control: 0120")