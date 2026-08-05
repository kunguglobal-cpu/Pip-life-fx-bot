class RiskManager:
    def __init__(self, risk_percent=1.0, max_open_trades=1):
        self.risk_percent = risk_percent
        self.max_open_trades = max_open_trades

    def calculate_lot_size(self, balance, stop_loss_pips, pip_value=1.0):
        if stop_loss_pips <= 0:
            return 0.01

        risk_amount = balance * (self.risk_percent / 100)
        lot = risk_amount / (stop_loss_pips * pip_value)

        return round(max(0.01, lot), 2)

    def can_open_trade(self, open_positions):
        return open_positions < self.max_open_trades
