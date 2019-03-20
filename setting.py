"""存储模块"""
# 代理最高分
MAX_SCORE = 100
# 代理最低分
MIN_SCORE = 0
# 代理初始分
INITIAL_SCORE = 10
# redis地址
REDIS_HOST = 'localhost'
# redis端口号
REDIS_PORT = 6379
# redis密码
REDIS_PASSWORD = None
# redis集合名
REDIS_KEY = 'proxies'

"""getter"""
# 代理池数量界限
POOL_UPPER_THRESHOLD = 1000

"""tester"""
# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://m.weibo.cn/api/container/getIndex?uid=1783286485&type=uid&value=1783286485&containerid=1005051783286485'
# 请求成功的状态码
VALID_STATUS_CODES = [200, 302]
# 批量测试的最大值 (步长)
BATCH_TEST_SIZE = 10

"""scheduler"""
# tester开关
TESTER_ENABLED = True
# getter开关
GETTER_ENABLED = True
# api开关
API_ENABLED = True
# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300
# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

