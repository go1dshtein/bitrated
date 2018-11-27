import logging


from tornado import web
from prometheus_client import REGISTRY
from prometheus_client import exposition
from prometheus_client import Histogram


logger = logging.getLogger(__name__)


REQUEST_TIME = Histogram(
    'api_request_processing_seconds',
    'Number of seconds that request takes',
    ['path', 'method', 'status'])


class MetricsHandler(web.RequestHandler):
    async def get(self):
        accept = self.request.headers.get('Accept')
        encoder, content_type = exposition.choose_encoder(accept)
        self.set_header('Content-type', content_type)
        data = encoder(REGISTRY)
        self.finish(data)


class RequestTimeMixin:
    def log_request(self, handler):
        request = handler.request
        method = request.method
        status = handler.get_status()
        path = request.uri
        REQUEST_TIME.labels(
            method=method, status=status, path=path).observe(
            request.request_time())
        return super().log_request(handler)


def make_router(**kwargs):
    return web.Application([
        (r'/metrics/?', MetricsHandler, kwargs),
    ])
