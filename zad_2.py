from klasy.Biblioteka import Library, Book, Employee, Order

bib1 = Library("Warszawa", "ul. Książkowa 1", "00-001", "9:00-17:00", "123456789")
bib2 = Library("Kraków", "ul. Czytelnicza 2", "30-002", "10:00-18:00", "987654321")
ks1 = Book(bib1, "2020-01-01", "Jan", "Kowalski", 300)
ks2 = Book(bib2, "2021-05-15", "Anna", "Nowak", 400)
ks3 = Book(bib1, "2019-09-10", "Piotr", "Wiśniewski", 250)
ks4 = Book(bib2, "2022-03-20", "Katarzyna", "Lewandowska", 350)
ks5 = Book(bib1, "2023-07-05", "Michał", "Zieliński", 280)
pr1 = Employee(
    "Jan",
    "Kowalski",
    "2020-01-01",
    "1990-05-15",
    "Warszawa",
    "ul. Kowalska 1",
    "00-001",
    "123456789",
)
pr2 = Employee(
    "Anna",
    "Nowak",
    "2021-05-15",
    "1992-08-20",
    "Kraków",
    "ul. Nowaka 2",
    "30-002",
    "987654321",
)
st1 = "Adam Nowak"
st2 = "Ewa Kowalska"
zm1 = Order(pr1, st1, [ks1, ks3], "2026-07-01")
zm2 = Order(pr2, st2, [ks2, ks4, ks5], "2026-06-02")

print(zm1)
print(zm2)
