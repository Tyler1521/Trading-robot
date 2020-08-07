import random
import requests
import ccxt
import pandas as pd

apiKey = 'tyler1521' 
secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
test_exchange = getattr(ccxt,"bytetrade") ({
    'apiKey': apiKey,
    'secret':secret
     })

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












