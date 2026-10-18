#a
print("Zadanie a")
def a(l):
        print(l)

lista_a=["Tomek", "Kasia", "Marek","Ala","Jan"]
a(lista_a)


#b
print("\nZadanie b")
def b(l):
    o=[]
    for i in l:
        o.append(i*2)
    return o

def b2(l):
    return [i*2 for i in l]

lista_b=[1,2,3,4,5]
print(b(lista_b))
print(b2(lista_b))


print("\nZadanie c")
#c
def c(l):
    for i in l:
        if i%2==0:
            print(i)

lista_c = range(10)
c(lista_c)

#d
print("\nZadanie d")
def d(l):
    o=[]
    for i in range(len(l)):
        if i%2==1:
            o.append(l[i])
    return o

lista_d = range(10)
print(d(lista_d))