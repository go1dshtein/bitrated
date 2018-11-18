import logging
import json

from tornado import httpclient
from tornado import httputil

logger = logging.getLogger(__name__)


class BitFinexProvider:
    def __init__(self, base_url=None):
        self._base_url = base_url or 'https://api.bitfinex.com/v2/'

    async def get_tickers(self):
        data = await self._make_request('tickers', {'symbols': 'ALL'})
        if not data:
            return

        return self._convert_tickers_list(data)

    async def get_ticker(self, ticker):
        _ticker = 't%s' % ticker.upper()
        data = await self._make_request(f'ticker/{_ticker}')
        if not data:
            return

        return self._convert_ticker(data, ticker)

    async def get_candles(self, ticker):
        _ticker = 't%s' % ticker.upper()
        data = await self._make_request(
            f'candles/trade:30m:{_ticker}/hist', {'limit': 48})
        if not data:
            return

        return self._convert_candles(data)

    async def _make_request(self, path, params=None):
        url = self._base_url + path
        if params:
            url = httputil.url_concat(url, params)

        logger.debug('send request to bitfinex: %s', url)
        response = await httpclient.AsyncHTTPClient().fetch(
            url, raise_error=False)

        if response.code != 200:
            logger.error(
                'invalid response: %s status_code = %s\n%s',
                url, response.code, response.body)
            return None

        return json.loads(response.body)

    def _convert_tickers_list(self, data):
        return [
            {'ticker': e[0][1:].upper()} for e in data if e[0].startswith('t')
        ]

    def _convert_ticker(self, data, ticker):
        keys = [
            'bid', '_', 'ask', '_',
            '_', '_', 'price', 'daily_volume',
            'daily_high', 'daily_low',
        ]
        result = {
            k: float(v) for k, v in zip(keys, data) if not k.startswith('_')
        }
        result['ticker'] = ticker
        return result

    def _convert_candles(self, data):
        keys = [
            'timestamp',
            'open', 'close',
            'high', 'low',
            'volume',
        ]

        elem = (lambda x: {k: v for k, v in zip(keys, x)})
        return [elem(x) for x in reversed(data)]
