from multiprocessing import Process
from yjx_project.proxypool.setting import TESTER_ENABLED, GETTER_ENABLED, API_ENABLED, TESTER_CYCLE, GETTER_CYCLE, API_HOST, API_PORT
from yjx_project.proxypool.tester import Tester
from yjx_project.proxypool.getter import Getter
from yjx_project.proxypool.api import app
import time


class Scheduler(object):
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle: 检查周期
        """
        tester = Tester()
        while True:
            print('测试模块')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时更新代理
        :param cycle: 获取周期
        """
        getter = Getter()
        while True:
            print('抓取模块')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """api"""
        print('接口模块')
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()


a = Scheduler()
a.run()
