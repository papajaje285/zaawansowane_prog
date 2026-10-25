class Library:
    def __init__(self, city: str, street: str, zip_code: str, opening_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.opening_hours = opening_hours
        self.phone = phone

    def __str__(self):
        return f"biblioteka w {self.city}, {self.street}, {self.zip_code}, godziny otwarcia: {self.opening_hours}, tel: {self.phone}"

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, zatrudniony: {self.hire_date}, urodzony: {self.birth_date}, mieszka w: {self.city}, {self.street}, {self.zip_code}, tel: {self.phone}"

class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"autor: {self.author_name} {self.author_surname}, Opublikowano: {self.publication_date}, {self.number_of_pages} stron, dostepny w {self.library.city}"

class Order:
    def __init__(self, employee: Employee, student: str, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Student: {self.student} data: {self.order_date} pracownik: {self.employee.first_name} {self.employee.last_name}. Autorzy: {[book.author_name + ' ' + book.author_surname for book in self.books]}"

bib1 = Library("Warszawa", "ul. Książkowa 1", "00-001", "9:00-17:00", "123456789")
bib2 = Library("Kraków", "ul. Czytelnicza 2", "30-002", "10:00-18:00", "987654321") 
ks1 = Book(bib1, "2020-01-01", "Jan", "Kowalski", 300)
ks2 = Book(bib2, "2021-05-15", "Anna", "Nowak", 400)
ks3 = Book(bib1, "2019-09-10", "Piotr", "Wiśniewski", 250)
ks4 = Book(bib2, "2022-03-20", "Katarzyna", "Lewandowska", 350)
ks5 = Book(bib1, "2023-07-05", "Michał", "Zieliński", 280)
pr1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-15", "Warszawa", "ul. Kowalska 1", "00-001", "123456789")
pr2 = Employee("Anna", "Nowak", "2021-05-15", "1992-08-20", "Kraków", "ul. Nowaka 2", "30-002", "987654321")
st1="Adam Nowak"
st2="Ewa Kowalska"
zm1 = Order(pr1, st1, [ks1, ks3], "2026-07-01")
zm2 = Order(pr2, st2, [ks2, ks4, ks5], "2026-06-02")

print(zm1)
print(zm2)