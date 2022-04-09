import re

pattern = r'>>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)'
spent_money = 0

text = input()
product_list = []

while not text == "Purchase":
    result = re.match(pattern, text)
    if result is not None:
        product = result[1]
        price = float(result[2])
        quantity = float(result[3])
        spent_money += price * quantity
        product_list.append(product)

    text = input()
print("Bought furniture:")

if spent_money > 0:
    print("\n".join(product_list))
print(f"Total money spend: {spent_money:.2f}")

