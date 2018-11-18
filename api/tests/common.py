import os
import json


class MockBitFinexProvider:
    def __init__(self, dirname):
        self._dirname = dirname

    async def get_tickers(self):
        filename = os.path.join(self._dirname, 'provider-tickers.json')
        with open(filename) as h:
            return json.load(h)

    async def get_ticker(self, ticker):
        assert ticker == 'BTCUSD'
        filename = os.path.join(self._dirname, 'provider-ticker.json')
        with open(filename) as h:
            return json.load(h)

    async def get_candles(self, ticker):
        assert ticker == 'BTCUSD'
        filename = os.path.join(self._dirname, 'provider-candles.json')
        with open(filename) as h:
            return json.load(h)
