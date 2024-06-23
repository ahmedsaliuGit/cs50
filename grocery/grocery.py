def main():
    for i in range(len(get_order(""))):
        print()

def get_order(prompt):
    items = []

    while True:
        try:
            item_name = input(prompt)
        except EOFError:
            return items
        else:
            if item_name not in items:
                items.append(item_name)

main()
