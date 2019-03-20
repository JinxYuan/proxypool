import requests
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent

base_headers = {
    'User-Agent': UserAgent(verify_ssl=False).random,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7'
}


def get_page(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    headers = dict(base_headers, **options)
    print(headers)
    print('正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取失败', url)
        return None
