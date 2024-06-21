coke_price = 50

def main():
    print(collect_coin())

def collect_coin():
    coin_received = 0

    while True:
        print(f"Amount due: {coke_price - coin_received}")

        coin = int(input("Insert coin: "))

        if coin != 25 or coin != 10 or coin != 5:
            continue

        coin_received = coin_received + coin

        if coin_received >= coke_price:
            return coin_received

main()
