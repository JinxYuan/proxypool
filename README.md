# proxypool
代理池（随机取出一个代理ip）
# setting.py
- 可以修改自己本地或者远程的redis地址和端口号
我这里使用的是默认的
- TEST_URL 建议爬取那个网址 设置为那个网站
- API地址可以根据自己的情况配置(API_HOST、API_PORT)
# scheduler.py
- 使用时，运行该文件就行
- 建议让代理池跑一会再开始运行自己的爬虫
# 自己的项目使用代理池

```
def get_proxy():
  try:
      # 这里的127.0.0.1:5555是你自己配置的API_HOST、API_PORT
      # random 随机获取一个代理ip
      proxy_response = requests.get('http://127.0.0.1:5555/random', headers=headers, verify=False)
      if proxy_response.status_code == 200:
          return proxy_response.text
  except ConnectionError:
      return None

def get_playlist_page(page):
        proxy = get_proxy()
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        url = 'https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD&offset=' + str(page)
        # print(url)
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            return response.text
```
