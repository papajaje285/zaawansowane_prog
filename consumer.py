from time import sleep

while True:
    znaleziony_indeks = None
    with open("plik.txt", "r", encoding="utf-8") as plik:
        linie = plik.readlines()

    for i, linia in enumerate(linie):
        if linia.startswith("pending"):
            znaleziony_indeks = i
            break

    if znaleziony_indeks is not None:
        linie[znaleziony_indeks] = "in_progress\n"
        with open("plik.txt", "w", encoding="utf-8") as plik:
            plik.writelines(linie)
        sleep(30)

        with open("plik.txt", "r", encoding="utf-8") as plik:
            linie = plik.readlines()
        linie[znaleziony_indeks] = "done\n"
        with open("plik.txt", "w", encoding="utf-8") as plik:
            plik.writelines(linie)

    else:
        sleep(5)
