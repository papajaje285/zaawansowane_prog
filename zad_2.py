# a
print("Zadanie a")


def a(lista):
    print(lista)


lista_a = ["Tomek", "Kasia", "Marek", "Ala", "Jan"]
a(lista_a)


# b
print("\nZadanie b")


def b(lista):
    o = []
    for i in lista:
        o.append(i*2)
    return o


def b2(lista):
    return [i * 2 for i in lista]


lista_b = [1, 2, 3, 4, 5]
print(b(lista_b))
print(b2(lista_b))

# c
print("\nZadanie c")


def c(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)


lista_c = range(10)
c(lista_c)

# d
print("\nZadanie d")


def d(lista):
    o = []
    for i in range(len(lista)):
        if i % 2 == 1:
            o.append(lista[i])
    return o


lista_d = range(10)
print(d(lista_d))
