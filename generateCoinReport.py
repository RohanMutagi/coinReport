from binance.client import Client

from binance.enums import *



#### CHANGES #######

# percent of balance

# timeout





from time import sleep







###### Read all trade data from Exchange (Binance) ###########

def get_all_trades_binance():

	trades = 1

	return trades



###### Get balances from Exchange ###########

###### For each coin with non-zero balance, get trades ###########

###### Calculate cost of purchasing the coins ###########

###### Get latest cost of the coin ###########

###### ###########

###### ###########

###### ###########

###### ###########

###### ###########

###### ###########













testing = False



scoin="ETH"

percent_of_balance=0.90



api_key = ""

api_secret = ""



client = Client(api_key, api_secret)



####### Get account balance for source coin ###################

eth=client.get_asset_balance(asset=scoin)

eth_balance = float(eth["free"])

print("%s balance = %f" % (scoin, eth_balance))



tcoin = raw_input('Enter the symbol: ')

tsymbol=tcoin+scoin

print ("Using %s" % tcoin)

print ("Symbol %s" % tsymbol)



####### Get Symbol Price ###################

symbol_history=client.get_recent_trades(symbol=tsymbol)

symbol_last_tick=symbol_history[-1]

symbol_last_price_str=symbol_last_tick["price"]

symbol_last_price=float(symbol_last_price_str)



print symbol_last_tick

print("symbol_last_price = %f" % symbol_last_price)

print("symbol_last_price_str = %s" % symbol_last_price_str)





####### Calculate how many coins to buy with all source coins ###################

tquantity=int(eth_balance/symbol_last_price*percent_of_balance)

print("Coins to buy = %f" % tquantity)





####### Make the purchase  ###################

print("Purchasing [%s] at [%s]. Quantity = [%f]" % (tsymbol,symbol_last_price_str,tquantity))

if testing == False:

	order = client.create_order( symbol=tsymbol, side=SIDE_BUY, type=ORDER_TYPE_MARKET, quantity=tquantity)

	print order





####### Get account balance for coin to sell ###################

coin=client.get_asset_balance(asset=tcoin)

print("[%s] account balance - [%s]" % (tcoin, coin))

coin_balance = float(coin["free"])

print("quantity selling = %f" % coin_balance)





####### Sell  ###################

sleep(300)

print("Selling [%s] at [%s]. Quantity = [%f]" % (tsymbol,symbol_last_price_str,coin_balance))

if testing == False:

	order = client.create_order( symbol=tsymbol, side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity=tquantity)

	print order
