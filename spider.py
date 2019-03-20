from yjx_project.proxypool.utils import get_page
from pyquery import PyQuery as pq
from lxml import etree
from bs4 import BeautifulSoup


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # print(cls)
        # print(name)
        # print(bases)
        count = 0
        attrs['__CrawlFunc__'] = []

        for k, v in attrs.items():
            print(k, v)
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        # print(attrs)
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_xici(self, page_coumt=4):
        """
        获取西次代理
        :param page: 页码
        :return: 代理
        """
        start_url = 'https://www.xicidaili.com/nn/{0}'
        urls = [start_url.format(page) for page in range(1, page_coumt)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('table tr').items()
                next(trs)
                for tr in trs:
                    tds = list(tr('td'))
                    # print(tds)
                    yield tds[1].text+':'+tds[2].text

    def crawl_kuaidaili(self, page_count=4):
        """
        快代理
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'https://www.kuaidaili.com/free/inha/{0}/'
        urls = [start_url.format(page) for page in range(1, page_count)]
        for url in urls:
            print('快代理Crawling', url)
            html = get_page(url)
            if html:
                doc = etree.HTML(html)
                trs = doc.xpath('//tbody/tr')
                for tr in trs:
                    td = tr.xpath('./td')
                    yield td[0].text + ':' + td[1].text

    def crawl_ip3366(self, page_count=4):
        """
        云代理
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.ip3366.net/free/?page={0}'
        urls = [start_url.format(page) for page in range(1, page_count)]
        for url in urls:
            print('云代理Crawling', url)
            html = get_page(url)
            if html:
                doc = BeautifulSoup(html, 'lxml')
                trs = doc.select('tbody tr')
                for tr in trs:
                    td = tr.select('td')
                    yield td[0].text + ':' + td[1].text
