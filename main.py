import string


def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum())
    return text == text[::-1]


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


def count_vowels(text: str) -> int:
    vowels = 'aeiouyąęó'
    text = text.translate(str.maketrans('', '', string.punctuation))
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("znizka musi być między 0 a 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def word_frequencies(text: str) -> dict:
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
