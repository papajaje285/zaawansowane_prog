class Property:
    def __init__(self, area: int, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"powierzchnia: {self.area}, pokoje: {self.rooms}, cena: {self.price}, adres: {self.address}"


class House(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}, rozmiar działki: {self.plot}"


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}, piętro: {self.floor}"