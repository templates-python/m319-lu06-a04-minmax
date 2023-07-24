import random


def main():
    numbers = random.sample(range(-999, 999), 15)
    smallest = 2147483647
    biggest = -2147483648
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > biggest:
            biggest = number
    print(smallest)
    print(biggest)
    return numbers

if __name__ == '__main__':
    main()
