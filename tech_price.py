budget = float(input())

graphics_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

GRAPHICS_CARD_PRICE = 250

graphics_card_price = graphics_cards_count * GRAPHICS_CARD_PRICE
processor_price = processors_count * graphics_card_price * 0.35
ram_price = ram_count * graphics_card_price * 0.10

total_price = (
    graphics_card_price +
    processor_price +
    ram_price
)

if graphics_cards_count > processors_count:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")