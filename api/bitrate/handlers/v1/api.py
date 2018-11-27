import logging
import traceback
import json

from tornado import web

from bitrate.config import ENVIRONMENT

logger = logging.getLogger(__name__)


class BaseHandler(web.RequestHandler):
    def send(self, data, status_code=200):
        self.set_status(status_code)
        self.write(json.dumps({'data': data}))

    def write_error(self, status_code, **kwargs):
        result = {'error': {'status': status_code}}
        if 'reason' in kwargs:
            result['error']['reason'] = kwargs['reason']

        if ENVIRONMENT != 'prod' and 'exc_info' in kwargs:
            trace = result['error']['traceback'] = []
            for line in traceback.format_exception(*kwargs['exc_info']):
                trace.append(line)

        self.write(json.dumps(result))

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Origin', '*')


class TickersHandler(BaseHandler):
    def initialize(self, provider=None):
        self.provider = provider

    async def get(self, ticker=None):
        if ticker:
            result = await self.provider.get_ticker(ticker)
        else:
            result = await self.provider.get_tickers()

        if not result:
            self.send_error(503, reason='service temporary unavailable')
            return

        self.send(result)


class CandlesHandler(BaseHandler):
    def initialize(self, provider=None):
        self.provider = provider

    async def get(self, ticker):
        result = await self.provider.get_candles(ticker)

        if not result:
            self.send_error(503, reason='service temporary unavailable')
            return

        self.send(result)
