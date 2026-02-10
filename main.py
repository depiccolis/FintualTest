import random

def get_stock_price():
    return random.randint(1, 100)

# INPUT
stock_list = ['APPL', 'META']
portfolio = {'APPL': 40, 'META': 60}
iterations = 4
initial_capital = 1000

# PROCESS

d_prices = {}
contador = 0

for stock in stock_list:
    d_prices[stock] = {}
    d_prices[stock][0] = get_stock_price()
    print(f'{stock} stock price ({contador}): {d_prices[stock][0]}')

print(f'Capital ({contador}): {initial_capital}')

d_quantity = {}

for stock in stock_list:
    d_quantity[stock] = {}
    d_quantity[stock][0] = initial_capital*portfolio[stock]/100/d_prices[stock][0]
    print(f'{stock} stock quentity ({contador}): {d_quantity[stock][0]}')

# Start process

while contador < iterations:

    contador += 1

    print(f'{contador}-----------------')

    for stock in stock_list:
        d_prices[stock][contador] = get_stock_price()
        print(f'{stock} stock price ({contador}): {d_prices[stock][contador]}')

    new_caital = 0
    for stock in stock_list:
        new_caital += d_prices[stock][contador]*d_quantity[stock][contador-1]

    print(f'Capital ({contador}): {new_caital}')

    for stock in stock_list:
        d_quantity[stock][contador] = new_caital*portfolio[stock]/100/d_prices[stock][contador]
        print(f'{stock} stock quentity ({contador}): {d_quantity[stock][contador]}')

    # Go short or go long

    for stock in stock_list:

        if d_quantity[stock][contador] < d_quantity[stock][contador-1]:
            go_short = d_quantity[stock][contador-1]-d_quantity[stock][contador]
            print(f'Vender {go_short} {stock}')
        elif d_quantity[stock][contador] == d_quantity[stock][contador-1]:
            print('Do nothing')
        else:
            go_long = d_quantity[stock][contador] - d_quantity[stock][contador-1]
            print(f'Comprar {go_long} {stock}')

print('Finish!!')