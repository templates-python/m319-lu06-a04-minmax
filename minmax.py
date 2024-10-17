import random


def main():
    # Akzeptiere die Eingabe des Benutzers für die Anzahl der Zufallszahlen
    num_count = int(input('Anzahl Zufallszahlen: '))
    # Basis Version
    # num_count = 15

    # Erzeuge eine Liste von Zufallszahlen zwischen -999 und 999
    numbers = random.sample(range(-999, 1000), num_count)

    # Definiere die Variablen 'smallest' und 'biggest' zum Finden der min/max-Werte
    smallest = 10000  # Wert, der größer als der größte mögliche Zufallswert ist
    biggest = -10000  # Wert, der kleiner als der kleinste mögliche Zufallswert ist

    # Iteration über alle Zahlen in der Liste, um die kleinste und größte Zahl zu finden
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > biggest:
            biggest = number

    # Ausgabe der kleinsten und größten Zahl
    print(f'{smallest}\n{biggest}')

    # Rückgabe der Liste
    return numbers


if __name__ == '__main__':
    main()