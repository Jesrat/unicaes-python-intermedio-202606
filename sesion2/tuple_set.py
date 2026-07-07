tuple()
set()

data_list = ["Perro", "Gato", "Ave", "Vaca"]
data_tuple = ("Perro", "Gato", "Ave", "Vaca")

students = [
    ("Student1", False, "Data Analysis", "M"),
    ("Student2", False, "Data Analysis", "F"),
    ("Student3", False, "Programador", "M"),
    ("Student4", True, "Gerente General", "M"),
    ("Student5", False, "Data Analysis", "F"),
    ("Student6", True, "Ing Industrial", "M"),
    ("Student6", False, "Ciberseguridad", "M"),
]


# Comprehension
len([i for i in students if i[1]])


def get_week_days():
    return "Lunes", \
        "Martes", \
        "Miércoles", \
        "Jueves", \
        "Viernes", \
        "Sábado", \
        "Domingo"



def get_week_days():
    return (1, "Lunes"), \
        (2, "Martes"), \
        (3, "Miércoles"), \
        (4, "Jueves"), \
        (5, "Viernes"), \
        (6, "Sábado"), \
        (7, "Domingo")


def convert_cron_date(day):
    return [i[1] for i in get_week_days() if i[0] == day][0]


# ISO

data_list = ["Perro", "Gato", "Ave", "Vaca", "Perro"]
data_tuple = ("Perro", "Gato", "Ave", "Vaca", "Perro")
data_set = {"Perro", "Gato", "Ave", "Vaca", "Perro"}


backend_devs = {"Luis", "Maria", "Carlos"}
frontend_devs = {"Maria", "Ana", "Carlos"}

# operadores (&, |, -, ^)

# lo que se encuentra en ambos
backend_devs & frontend_devs

# union completa
backend_devs | frontend_devs

# lo que solo está en backends
backend_devs - frontend_devs

# lo que solo está en frontends
frontend_devs - backend_devs

# lo que no está en ambos forma correcta
frontend_devs ^ backend_devs

# lo que no está en ambos forma incorrecta
set(list(backend_devs - frontend_devs) + list(frontend_devs - backend_devs))

# lo que no está en ambos forma incorrecta
backend_devs - frontend_devs | frontend_devs - backend_devs


# Pythonic

students_from_previous_course = []
for student in students:
    if student[1]:
        students_from_previous_course.append(student)

students_from_previous_course = [student[2] for student in students if student[1] and student[3] == "F"]

# [student[2] for student in students if student[1] and student[3] == "M"]

# operador de asignación =
# operadores aritméticos + - * /
# operadores lógicos/comparación <> != == or not and


emails = ['luis@gmail.com', 'maria@empresa.com', 'pedro@gmail.com', 'ana@hotmail.com']

counter = 0
for email in emails:
    spliced = email.split('@')
    domain = spliced[1]
    if domain == "gmail.com":
        counter += 1


sum([1 for email in emails if email.split('@')[1] == "gmail.com"])


nombres_sucios = ['  Luis ', 'MARIA  ', ' carlos']

# strip() -> remover espacios en blanco
# lower(), upper() -> convertir a minúsculas o mayúsculas
# title() -> Capitalizar

nombres_limpios = []
for nombre in nombres_sucios:
    paso1 = nombre.strip()
    paso2 = paso1.title()
    nombres_limpios.append(paso2)


nombres = [
        "Ana",
        "Carlos",
        "María",
        "José",
        "Luis",
        "Ana",
        "Sofía",
        "Miguel",
        "Valeria",
        "Carlos",
        "Andrés",
        "Daniela",
        "Javier",
        "Fernanda",
        "María",
        "Alejandro",
        "Camila",
        "Diego",
        "Isabella",
        "Luis",
        "Ricardo",
        "Natalia",
        "Eduardo",
        "Gabriela",
        "José",
        "Fernando",
        "Paula",
        "Roberto",
        "Lucía",
        "Ana",
        "David",
        "Elena",
        "Carlos",
        "Manuel",
        "Patricia",
        "Jorge",
        "Carolina",
        "Sofía",
        "Diego",
        "María"
    ]

def my_iterator():
    counter = len(nombres)
    while counter:
        yield nombres[counter-1]
        counter -= 1


# ventaja legibilidad
nombres_limpios = [nombre.strip().title() for nombre in nombres_sucios]



nombres_mayuscula_y_unicos = []
for nombre in nombres:
    paso1 = nombre.strip()
    paso2 = paso1.lower()
    if paso2 not in nombres_mayuscula_y_unicos:
        nombres_mayuscula_y_unicos.append(paso2)


nombres_mayuscula_y_unicos = {nombre.strip().lower() for nombre in nombres}

# enumerate()
for idx, nombre in enumerate(nombres):
    print(f"{idx} - {nombre}")


counter = 0
for nombre in nombres:
    print(f"{counter} - {nombre}")
    counter += 1


# inicializar en 1
counter = 1
for nombre in nombres:
    print(f"{counter} - {nombre}")
    counter += 1


for idx, nombre in enumerate(nombres):
    print(f"{idx + 1} - {nombre}")


for idx, nombre in enumerate(nombres, start=1):
    print(f"{idx} - {nombre}")



