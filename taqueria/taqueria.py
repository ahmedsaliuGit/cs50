def main():
    get_order("Item: ")

def get_order(prompt):
    total = 0

    while True:
        try:
            item_name = input(prompt)
        except EOFError:
            break
        else:
            if item_name.title() in menu_items:
                total += menu_items[item_name.title()]

                print(f"Total: ${round(total, 2)}" {:0.2f}ºC.\n".format(answer))

menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()
