#!/usr/bin/env python3
import argparse
import logging
import signal

from tornado import ioloop

from bitrate import server


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-L', '--log-level', default='INFO',
                        help='logging level [%(default)s]')
    parser.add_argument('--host', default='',
                        help='binding host [0.0.0.0]')
    parser.add_argument('--port', default=8080, type=int,
                        help='binding port [%(default)s]')
    return parser.parse_args(args)


def handler(signum, frame):
    ioloop.IOLoop.current().add_callback_from_signal(stop)


def stop():
    logger.info('bye bye\n')
    ioloop.IOLoop.current().stop()


def main(args):
    global logger
    logger = logging.getLogger('bitrated')

    ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    server.make_server(args.host, args.port, args.log_level)
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    logger.info('starting bitrated on %s:%d',
                args.host or '0.0.0.0', args.port)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main(parse_args())
