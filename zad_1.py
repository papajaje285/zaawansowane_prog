from klasy.Student import Student

st1 = Student("Bob", [40, 50, 60])
st2 = Student("Alice", [30, 70, 40])

print(f"st1: {st1.is_passed()}")
print(f"st2: {st2.is_passed()}")
