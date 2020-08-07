import ccxt
import requests
import pandas as pd
import time
from time import sleep
from random import randint

apiKey = 'hater_bid' 
secret = '7bdf2cb11106e1f2d76cdad26593798d9561164f619090c2fa32a5a070c8d5ad'
test_exchange = getattr(ccxt,"bytetrade") ({
    'apiKey': apiKey,
    'secret':secret
     })

data = requests.get("https://api-v2-test.bytetrade.com/depth?symbol=161061273596").json()
calls = data["bids"]
price_amount = max(calls)
best_bid1 = list(filter(lambda x : len(x) == 7 , price_amount))
best_bid2 = filter(None, best_bid1) 
for best_bid in best_bid2: 
    #print(best_bid)


    data = requests.get("https://api-v2-test.bytetrade.com/orders/closed?userid=hater_bid").json()
calls = data["id"]  







'''
    new_best_bid = best_bid + 0.0001
new_order = test_exchange.create_order(symbol='DGT/USDG', type='limit',side='sell',amount= 1 , price = new_best_bid)

if best_bid not from bot:
    print(new_order) 
else:
    pass
'''
'''
max = 500 # max price
min = 100  # min price

while True:

    apiKey = 'hater_bid' 
    secret = '7bdf2cb11106e1f2d76cdad26593798d9561164f619090c2fa32a5a070c8d5ad'
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
'''


 