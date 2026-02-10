import random

# Function that mimics the change in stock prices
def get_stock_price():
    return random.randint(1, 100)

# INPUT
stock_list = ['APPL', 'META', 'GOOGL'] #
portfolio = {'APPL': 10, 'GOOGL': 50, 'META': 40}
iterations = 4
initial_capital = 1000

############# START PROCESS ################

# Verify portfolio is properly created
contador_percentage = 0
for stock in portfolio:
    contador_percentage += portfolio[stock]

if contador_percentage != 100:
    raise 'Portfolio does not add up to 100'

d_prices = {}
contador = 0

# Get the initial stock prices
for stock in stock_list:
    d_prices[stock] = {}
    d_prices[stock][0] = get_stock_price()
    print(f'{stock} stock price ({contador}): {d_prices[stock][0]}')

print(f'Capital ({contador}): {initial_capital}')

# Get te initial quantity of every stock
d_quantity = {}

for stock in stock_list:
    d_quantity[stock] = {}
    d_quantity[stock][0] = initial_capital*portfolio[stock]/100/d_prices[stock][0]
    print(f'{stock} stock quentity ({contador}): {d_quantity[stock][0]}')

# Start the iterations

while contador < iterations:

    contador += 1

    print(f'{contador}-----------------')

    # Get the new prices per stock
    for stock in stock_list:
        d_prices[stock][contador] = get_stock_price()
        print(f'{stock} stock price ({contador}): {d_prices[stock][contador]}')

    # Get the new capital
    new_caital = 0
    for stock in stock_list:
        new_caital += d_prices[stock][contador]*d_quantity[stock][contador-1]

    print(f'Capital ({contador}): {new_caital}')

    # Get the new quantity of every stock

    for stock in stock_list:
        d_quantity[stock][contador] = new_caital*portfolio[stock]/100/d_prices[stock][contador]
        print(f'{stock} stock quentity ({contador}): {d_quantity[stock][contador]}')

    # Go short or go long

    for stock in stock_list:

        if d_quantity[stock][contador] < d_quantity[stock][contador-1]:
            go_short = d_quantity[stock][contador-1]-d_quantity[stock][contador]
            print(f'{stock} GO SHORT {go_short}')
        elif d_quantity[stock][contador] == d_quantity[stock][contador-1]:
            print(f'{stock} DO NOTHING')
        else:
            go_long = d_quantity[stock][contador] - d_quantity[stock][contador-1]
            print(f'{stock} GO LONG {go_long}')

print('Finish!!')