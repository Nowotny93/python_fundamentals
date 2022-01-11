price_without_tax = input()

total_prices_without_taxes = 0
taxes = 0

while price_without_tax != "special" and price_without_tax != "regular":
    price_without_tax_int = float(price_without_tax)
    if price_without_tax_int < 0:
        print('Invalid price!')
        price_without_tax = input()
        continue
    total_prices_without_taxes += price_without_tax_int
    taxes += price_without_tax_int * 0.2
    price_without_tax = input()

if price_without_tax == "special":
    total_price = total_prices_without_taxes + taxes
    discount = total_price * 0.1
    discounted_total_price = total_price - discount
    if discounted_total_price == 0:
        print('Invalid order!')
    else:
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total_prices_without_taxes:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print('-----------')
        print(f'Total price: {discounted_total_price:.2f}$')
elif price_without_tax == "regular":
    total_price = total_prices_without_taxes + taxes
    if total_price == 0:
        print('Invalid order!')
    else:
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total_prices_without_taxes:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print('-----------')
        print(f'Total price: {total_price:.2f}$')
