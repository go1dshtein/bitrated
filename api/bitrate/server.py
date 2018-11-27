import logging

from tornado import routing
from tornado import httpserver

from .config import setup_logging
from .provider import BitFinexProvider
from .handlers.v1 import make_router as make_v1_router
from .metrics import make_router as make_metrics_router

logger = logging.getLogger(__name__)


def make_router(provider=None):
    if provider is None:
        provider = BitFinexProvider()

    router = routing.RuleRouter([
        (r'/api/v1/.*', make_v1_router(provider=provider)),
        (r'/metrics.*', make_metrics_router()),
    ])

    return router


def make_server(host, port, level):
    setup_logging(level)
    router = make_router()
    server = httpserver.HTTPServer(router)
    server.listen(port, address=host)
    return server
