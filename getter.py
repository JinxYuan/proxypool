from yjx_project.proxypool.spider import Crawler
from yjx_project.proxypool.db import RedisClient
import sys
from yjx_project.proxypool.setting import POOL_UPPER_THRESHOLD


class Getter(object):
    def __init__(self):
        self.crawler = Crawler()
        self.redis = RedisClient()

    def is_over_threshold(self):
        """
        判断是否达到代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                print(proxies)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)

#
# a = Getter()
# a.run()