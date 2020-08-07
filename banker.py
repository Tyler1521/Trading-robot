
import random
import requests
import ccxt
import pandas as pd
import json
import time

apiKey = 'tyler1521' 
secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
test_exchange = getattr(ccxt,"bytetrade") ({
    'apiKey': apiKey,
    'secret':secret
     })


max = 500 # max price
min = 100  # min price

while True:
######maker_bid
    apiKey = 'maker_bid' 
    secret = 'ffdc95ac5e87113ee4bb93c661aa464e3f4455fb91e6960202aae169649c1242'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
         })

    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)
   

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'maker_bid')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'maker_bid')
        
        print(transfer_USDG)
    else:
        pass
    
     
   

     









    #####maker_ask
    apiKey = 'maker_ask' 
    secret = '2141671874fa0fd529c5149bb86d79f22c3babbf812587741276a30678a3493e'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })
        
    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)

     

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'maker_ask')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'maker_ask')
        
        print(transfer_USDG)
    else:
        pass

    



         


    #####taker_ask
    apiKey = 'taker_ask' 
    secret = 'e12064c75d59e2c527062db2fa45283afa190b86943b23fd60b79d0437d26bb3'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)

     

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'taker_ask')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'taker_ask')
        
        print(transfer_USDG)
    else:
        pass

     



        


    #####taker_bid
    apiKey = 'taker_bid' 
    secret = 'ef2e00e85bc5fa8cd706bffef37d0450d460e1517ebf3509a26c4e8900f86ed7'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)

     

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'taker_bid')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'taker_bid')
        
        print(transfer_USDG)
    else:
        pass

     



        


    #####taker_bidask
    apiKey = 'taker_bidask' 
    secret = '23201aa119d943fda547abd785b3ab965bac8758bbf5253c710d18004907ec85'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)

     

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'taker_bidask')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'taker_bidask')
        
        print(transfer_USDG)
    else:
        pass

     


        


    #####hater_ask
    apiKey = 'hater_ask' 
    secret = '5af740acb1d10a7cc8286e8ab82e406e242c806979f3e184cf9941475867e972'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)

     

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'hater_ask')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'hater_ask')
        
        print(transfer_USDG)
    else:
        pass

     



         


    #####hater_bid
    

    apiKey = 'hater_bid' 
    secret = '7bdf2cb11106e1f2d76cdad26593798d9561164f619090c2fa32a5a070c8d5ad'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    balance = test_exchange.fetch_balance()
    total_USDG = balance['USDG']['total']
    #print(total_USDG)

    total_DGT = balance['DGT']['total']
    #print(total_DGT)

     

    apiKey = 'tyler1521' 
    secret = 'b7ff34f7feeabd8816b92a9f34bffa5109ec96d7110d3122e8d9b5d4f2b6c228'
    test_exchange = getattr(ccxt,"bytetrade") ({
        'apiKey': apiKey,
        'secret':secret
        })

    if total_DGT < min:
        am = max - total_DGT
        amount = am - max/2
        transfer_DGT = test_exchange.transfer('DGT', amount , 'hater_bid')
        
        print(transfer_DGT)
    if total_USDG < min:
        am = max - total_USDG
        amount = am -max/2
        transfer_USDG = test_exchange.transfer('USDG', amount , 'hater_bid')
        
        print(transfer_USDG)
    else:
        continue

     
    time.sleep(5)







