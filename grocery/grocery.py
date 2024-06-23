def main():
    items = get_order("")

    print()
    
    for item in items:
        print(f"{items[item]} {item.upper()}")

def get_order(prompt):
    items = {}

    while True:
        try:
            item_name = input(prompt)
        except EOFError:
            return items
        else:
            if item_name not in items:
                items[item_name] = 1
            else:
                items[item_name] = items[item_name] + 1

main()
