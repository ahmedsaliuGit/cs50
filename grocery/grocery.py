def main():
    items = get_order("")

    for i in range(len(items)):
        print(f"{i}. {items[i].upper()}")

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
