import MetaTrader5 as mt5


class TradeExecutor:
    def __init__(self):
        pass

    def market_order(self, symbol, lot, order_type, sl, tp):
        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            return None

        price = tick.ask if order_type == mt5.ORDER_TYPE_BUY else tick.bid

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 20,
            "magic": 123456,
            "comment": "Pip Life FX Bot",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        return mt5.order_send(request)
