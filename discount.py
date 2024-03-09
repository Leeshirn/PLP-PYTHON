def calculate_discount(price,discount_percent):
  if discount_percent>=20:
   final_price =price - (price*discount_percent/100)
   return final_price
  else:
    return price
user_price = int(input('Enter the original price of the item: '))
user_discount_percent = int(input('Enter the discount applied: '))
final_price = calculate_discount(user_price,user_discount_percent)


if final_price != user_price:
  print('final price after paying is ',final_price)
else:
  print('No discount original price remains ',user_price)