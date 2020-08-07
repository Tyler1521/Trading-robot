
import random
import time
import requests
import ccxt
import pandas as pd
from time import sleep
from random import randint

a = 4   #range of random amount
b = 8   #range of random amount
amount = random.randint(a,b)
c = 2   #range of order time
d = 6   #range of order time

apiKey = 'taker_ask' 
secret = 'e12064c75d59e2c527062db2fa45283afa190b86943b23fd60b79d0437d26bb3'
test_exchange = getattr(ccxt,"bytetrade") ({
    'apiKey': apiKey,
    'secret':secret
     })

data = requests.get("https://api-v2-test.bytetrade.com/depth?symbol=161061273596").json()
calls = data["asks"]
price_amount = min(calls)
best_ask1 = list(filter(lambda x : len(x) == 7 , price_amount))
best_ask2 = filter(None, best_ask1) 
for best_ask in best_ask2: 
    #print(best_ask)

     
    new_order = test_exchange.create_order(symbol='DGT/USDG', type='limit',side='buy',amount=amount, price=best_ask)
sleep(randint(c,d))
print(new_order) 




























'''
max = 500 # max price
min = 100  # min price

while True:

    apiKey = 'taker_ask' 
    secret = 'e12064c75d59e2c527062db2fa45283afa190b86943b23fd60b79d0437d26bb3'
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

 