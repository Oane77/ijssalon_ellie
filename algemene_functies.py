def mijn_functie_1(x):
    return x ** 2

if __name__ == "__main__":
    print(mijn_functie_1(2))   # 4
    print(mijn_functie_1(4))   # 16
    print(mijn_functie_1(10))  # 100
    print(mijn_functie_1(12))  # 144

def mijn_functie_2(a, b):
    return [a + b, a - b, a * b, a / b]

if __name__ == "__main__":
    print(mijn_functie_2(12, 3))
    print(mijn_functie_2(12, 2))
    print(mijn_functie_2(10, 5))
    print(mijn_functie_2(100, 20))
    wait = input("Press Enter to continue.")


