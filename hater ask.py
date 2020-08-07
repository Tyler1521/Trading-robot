import ccxt
import pandas as pd
import time
from time import sleep
from random import randint


apiKey = 'hater_ask' 
secret = '5af740acb1d10a7cc8286e8ab82e406e242c806979f3e184cf9941475867e972'
test_exchange = getattr(ccxt,"bytetrade") ({
    'apiKey': apiKey,
    'secret':secret
     })
'''
data = requests.get("https://api-v2-test.bytetrade.com/depth?symbol=161061273596").json()
calls = data["asks"]
price_amount = min(calls)
best_ask1 = list(filter(lambda x : len(x) == 7 , price_amount))
best_ask2 = filter(None, best_ask1) 
for best_ask in best_ask2: 
    #print(best_ask)


    new_best_ask = best_ask - 0.0001
new_order = test_exchange.create_order(symbol='DGT/USDG', type='limit',side='buy',amount= 1 , price= new_best_ask)

if best_ask not from bot:
    print(new_order) 
else:
    pass
'''

max = 500 # max price
min = 100  # min price

while True:

    apiKey = 'hater_ask' 
    secret = '5af740acb1d10a7cc8286e8ab82e406e242c806979f3e184cf9941475867e972'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
         })

    balance = test_exchange.fetch_balance()
    total_DGT = balance['DGT']['total']
    #print(total_DGT)
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

 
    if total_DGT > max:
        am = total_DGT - max
        amount = am + max/2
        transfer_DGT = test_exchange.transfer('DGT', amount, 'tyler1521')

        print(transfer_DGT)
    if total_USDG > max:
        am = total_USDG - max
        amount = am + max/2
        transfer_USDG = test_exchange.transfer('USDG', amount, 'tyler1521')

        print(transfer_USDG)
    else:
        continue

    time.sleep(10)



