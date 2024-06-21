coke_price = 50

def main():
    collect_coin()

def collect_coin():
    print(f"Amount due: {coke_price}")

    coin = int(input("Insert coin: "))

    print(coin)

main()
