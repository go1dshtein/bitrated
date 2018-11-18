from tornado import web

from .api import TickersHandler
from .api import CandlesHandler


def make_router(**kwargs):
    return web.Application([
        (r'/v1/tickers/?', TickersHandler, kwargs),
        (r'/v1/tickers/(?P<ticker>\w+)/?', TickersHandler, kwargs),
        (r'/v1/tickers/(?P<ticker>\w+)/candles?', CandlesHandler, kwargs),
    ])
