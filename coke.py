coke_price = 50

def main():
    collect_coin()

def collect_coin():
    amount_due = 0

    while True:
        print(f"Amount due: {coke_price - amount_due}")

        coin = int(input("Insert coin: "))

        amount_due = amount_due + coin

        if amount_due >= coke_price:
            return amount_due

main()
