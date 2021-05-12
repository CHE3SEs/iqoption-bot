import time
import logging
from iqoptionapi.stable_api import IQ_Option

#conectar
Iq=IQ_Option("julio8martins@gmail.com","julio123!@#.")
check_connect=Iq.connect()
if check_connect:
    print("conectado")
else:
    print("nao conectado")

#carteira
balance_type="PRACTICE" 
Iq.change_balance(balance_type)
print("você tem: ", Iq.get_balance(), "R$")
wallet=Iq.get_balance()


#comprar btc
print("comprar crypto-moeda")

instrument_type="crypto"
instrument_id="BTCUSD"
goal=instrument_id
side="buy"
amount=wallet/2
leverage=3
type="market"
limit_price=None
stop_price=None
stop_lose_kind="percent"
stop_lose_value=95
take_profit_kind="percent"
take_profit_value=2
use_trail_stop=False
auto_margin_call=True
use_token_for_commission=False


#pegar candles
Iq.subscribe_top_assets_updated(instrument_type)


while True:
    if Iq.get_top_assets_updated(instrument_type)!=None:
        list=(Iq.get_top_assets_updated(instrument_type))
        btc_price=(list[0]["cur_price"]['value'])
        print("BTC custa:", btc_price)
        time.sleep(900)
        if Iq.get_top_assets_updated(instrument_type)!=None:
                list2=(Iq.get_top_assets_updated(instrument_type))
                btc_price2=(list2[0]["cur_price"]['value'])
                print("BTC custa:", btc_price2)


                if btc_price>btc_price2 and wallet>10:

                    check,order_id=Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
                    side=side, amount=amount,leverage=leverage,
                    type=type,limit_price=limit_price, stop_price=stop_price,
                    stop_lose_kind=stop_lose_kind,
                    stop_lose_value=stop_lose_value,
                    take_profit_kind=take_profit_kind,
                    take_profit_value=take_profit_value,
                    use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
                    use_token_for_commission=use_token_for_commission)

                    if check:
                        print(instrument_id, "comprado! ", amount)
                    else:
                        print("compra mal-sucedida")
                
                if btc_price<btc_price2:
                        print("nao comprar bitcoin agora")


                time.sleep(900)
            
        

      

#if wallet >= btc:
    
