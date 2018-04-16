# coding: utf-8
def cal(price, tax):
    total = price + (price * tax)
    global my_price
    print('my_price inside func=', my_price)
    return total


my_price = float(raw_input('Enter a price'))

total_price = cal(my_price, 0.06)
print('price =', my_price, 'total price = ', total_price)
print('my price outside = ', my_price)
