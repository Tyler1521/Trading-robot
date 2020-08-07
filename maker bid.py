import random
import requests
import ccxt
import pandas as pd
import time

apiKey = 'maker_bid' 
secret = 'ffdc95ac5e87113ee4bb93c661aa464e3f4455fb91e6960202aae169649c1242'
test_exchange = getattr(ccxt,"bytetrade") ({
    'apiKey': apiKey,
    'secret':secret
     })
'''
a = 5       #order times
b = 100     #amount

data = requests.get("https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/quotes?pairs=XAUUSD_Group.fix&api_key=%22df8db708-c9d2-443c-8f55-08cff55d3fec%22").json()
calls = data["prices"]
for el in calls:
    ask = el["ask"]
    bid = el["bid"] 


for ask in range(a):
    bid_price = el["bid"]/31.1035 - random.uniform(0.00032,0.00035)
    #print("bid price:",bid)

array = []

for i in range(a):
    array.append(0)

while sum(array) != b:
    for i in range(len(array)):
        array[i] = random.randint((b/a-5),(b/a+5))
    
for no in array:
    amount = no
    #print("amount:",amount)

    new_order = test_exchange.create_order(symbol='DGT/USDG', type='limit', side='sell',amount=amount, price=bid_price)
    print(new_order) 
'''

max = 500 # max price
min = 100  # min price

while True:

    apiKey = 'maker_bid' 
    secret = 'ffdc95ac5e87113ee4bb93c661aa464e3f4455fb91e6960202aae169649c1242'
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



 