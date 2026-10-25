def a(i1: int) -> bool:
    return i1 % 2 == 0


w = a(4)
if w:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
