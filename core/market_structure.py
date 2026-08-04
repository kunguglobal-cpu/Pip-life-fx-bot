class MarketStructure:
    def __init__(self):
        self.swing_highs = []
        self.swing_lows = []

    def detect_swing_high(self, highs, index):
        if index < 2 or index > len(highs) - 3:
            return False
        return (
            highs[index] > highs[index - 1]
            and highs[index] > highs[index - 2]
            and highs[index] > highs[index + 1]
            and highs[index] > highs[index + 2]
        )

    def detect_swing_low(self, lows, index):
        if index < 2 or index > len(lows) - 3:
            return False
        return (
            lows[index] < lows[index - 1]
            and lows[index] < lows[index - 2]
            and lows[index] < lows[index + 1]
            and lows[index] < lows[index + 2]
        )

    def analyze(self, highs, lows):
        self.swing_highs.clear()
        self.swing_lows.clear()

        for i in range(2, len(highs) - 2):
            if self.detect_swing_high(highs, i):
                self.swing_highs.append((i, highs[i]))

            if self.detect_swing_low(lows, i):
                self.swing_lows.append((i, lows[i]))

        return {
            "swing_highs": self.swing_highs,
            "swing_lows": self.swing_lows,
        }
+ao

