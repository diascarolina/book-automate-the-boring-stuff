def collatz(number):
    if number % 2:
        print(3 * number + 1)
        return 3 * number + 1

    else:
        print(number // 2)
        return number // 2

if __name__ == "__main__":
    print(f'Type an integer.')
    number = input()

    try:
        number = int(number)
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("You must enter an integer.")