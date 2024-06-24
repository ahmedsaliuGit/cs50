def main():
    print(get_input("Level "))

def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
