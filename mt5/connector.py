import MetaTrader5 as mt5


class MT5Connector:
    def __init__(self):
        self.connected = False

    def connect(self):
        if not mt5.initialize():
            print("MT5 initialization failed")
            return False

        self.connected = True
        print("Connected to MetaTrader 5")
        return True

    def disconnect(self):
        if self.connected:
            mt5.shutdown()
            self.connected = False

    def get_symbol_tick(self, symbol="XAUUSD"):
        if not self.connected:
            return None

        return mt5.symbol_info_tick(symbol)

    def get_price(self, symbol="XAUUSD"):
        tick = self.get_symbol_tick(symbol)

        if tick is None:
            return None

        return {
            "bid": tick.bid,
            "ask": tick.ask,
            "time": tick.time,
        }
