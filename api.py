from flask import Flask, g
from yjx_project.proxypool.db import RedisClient


__all__ = ['app']
app = Flask(__name__)


def get_coon():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def hello():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return:随机代理
    """
    coon = get_coon()
    return coon.random()


@app.route('/count')
def get_count():
    """
    Get the count of proxies
    :return: 代理数量
    """
    coon = get_coon()
    return str(coon.count())


if __name__ == '__main__':
    app.run()
