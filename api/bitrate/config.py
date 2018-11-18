import logging.config
import os
import sys

from raven.transport.tornado import TornadoHTTPTransport


ENVIRONMENT = os.getenv('BITRATE_ENVIRONMENT', 'local')
SENTRY_DSN = os.getenv('BITRATE_SENTRY_DSN', '')


def setup_logging(level):
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s: %(levelname)s %(name)s] %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'stream': sys.stderr,
                'formatter': 'default'
            },
            'sentry': {
                'level': 'WARNING',
                'class': 'raven.handlers.logging.SentryHandler',
                'dsn': SENTRY_DSN,
                'transport': TornadoHTTPTransport,
            },
        },
        'root': {
            'handlers': ['console', 'sentry'],
            'level': level.upper(),
        },
    }
    logging.config.dictConfig(config)
