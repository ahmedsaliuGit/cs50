def main():
    print(get_input("Level: "))

def get_input(prompt):
    while True:
        try:
            num = int(input(prompt))

            if num <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return num

main()
