def main():
    get_order("Item: ")

def get_order(prompt):
    items = []

    while True:
        try:
            item_name = input(prompt)
        except EOFError:
            break
        else:
            if item_name.title() not in menu_items:
                total += menu_items[item_name.title()]

                print("Total: ${:0.2f}".format(total))

main()
