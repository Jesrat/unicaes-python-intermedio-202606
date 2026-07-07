
# name is the parameter
def who_am_i(name):
    # F-strings
    print(f"my name is {name}")
    print("my name is {0}".format(name))
    print("my name is {namex}".format(namex=name))
    print("my name is %s" % (name,))
    print("my name is " + name)


# "Josue" is the argument
who_am_i("Josue")


def who_am_i(name, last_name):
    # F-strings
    print(f"my name is {name} and last name is {last_name}")


who_am_i("Josue", "Gomez")


# *args **kwargs

# list
data = ["Josue", "Gomez"]
who_am_i(*data)

# unpack, iterable

# tuple
data = ("Josue", "Gomez")
who_am_i(*data)


# set
data = {"Josue", "Gomez"}
who_am_i(*data)


# KEYWORD ARGUMENT
def who_am_i(name, last_name, age=0):
    # F-strings
    print(
        f"my name is {name} "
        f"and last name is {last_name} "
        f"and age is {age}"
    )


who_am_i("Josue", "Gomez", age=33)
who_am_i("Josue", "Gomez", 33)


def who_am_i(name, last_name, age=0, height=0):
    # F-strings
    print(
        f"my name is {name} "
        f"and last name is {last_name} "
        f"and age is {age} "
        f"and height is {height}"
    )


who_am_i("Josue", "Gomez", age=33, height=175)
who_am_i("Josue", "Gomez", height=175, age=33)


def who_am_i(
        name,
        last_name,
        age=0,
        height=0,
        **kwargs
):
    # F-strings
    my_data = f"my name is {name} and last name is {last_name} and age is {age} and height is {height}"
    if kwargs:
        for k, v in kwargs.items():
            my_data += f" and {k} {v}"
    print(my_data)


who_am_i("Josue", "Gomez")
who_am_i("Josue", "Gomez", age=33)
who_am_i("Josue", "Gomez", age=33, height=175)
who_am_i("Josue", "Gomez", height=175, age=33)
who_am_i("Josue", "Gomez", height=175, age=33, work="COO")


def record_sale(customer_name, *args):
    print(f"customer is {customer_name}")
    if not args:
        raise Exception("por lo menos un item debe comprar")
    print(f"invoice for {args}")


record_sale("Josue", "Leche", "Pan", "Frijoles", "Arroz")

products = ["Leche", "Pan", "Frijoles", "Arroz"]
record_sale("Josue", products)
record_sale("Josue", *products)


