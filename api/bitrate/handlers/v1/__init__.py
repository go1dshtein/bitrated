from tornado import web

from bitrate.metrics import RequestTimeMixin

from .api import TickersHandler
from .api import CandlesHandler


class Application(RequestTimeMixin, web.Application):
    pass


def make_router(**kwargs):
    return Application([
        (r'/api/v1/tickers/?', TickersHandler, kwargs),
        (r'/api/v1/tickers/(?P<ticker>\w+)/?', TickersHandler, kwargs),
        (r'/api/v1/tickers/(?P<ticker>\w+)/candles?', CandlesHandler, kwargs),
    ])
