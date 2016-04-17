from __future__ import with_statement
import logging
import psycopg2
import psycopg2.pool

__author__ = 'leandroloi'

logger = logging.getLogger(__name__)


def initial_config(settings):
    """Called by the app on startup to setup bindings to the DB
    :param settings: Database settings, like database,port, user, password
    """
    try:

        conn = psycopg2.pool.ThreadedConnectionPool(1, 10, database=settings.get('database'), user=settings.get('user'),
                                                  password=settings.get('password'), host=settings.get('host'),
                                                  port=settings.get('port'))

        return conn

    except Exception, e:
        logger.error('The system is having problem to connect. Exception {exception}'.format(exception=e))