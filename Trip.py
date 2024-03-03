PUZZLES_PRICE = 2.6
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.1
MINIONS_PRICE = 8.2
TRUCKS_PRICE = 2

trip_price = float(input())

puzzles_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price = (
    puzzles_count * PUZZLES_PRICE +
    talking_doll_count * TALKING_DOLL_PRICE +
    teddy_bear_count * TEDDY_BEAR_PRICE +
    minions_count * MINIONS_PRICE +
    trucks_count * TRUCKS_PRICE
)

total_count = (
    puzzles_count +
    talking_doll_count +
    teddy_bear_count +
    minions_count +
    trucks_count
)

if total_count >= 50:
    total_price -= total_price * 0.25

total_price -= total_price * 0.1

if total_price >= trip_price:
    print(f"Yes! {total_price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_price:.2f} lv needed.")
