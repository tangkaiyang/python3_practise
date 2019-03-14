from threading import Condition
import threading
# 条件变量,用于复杂的线程间同步
# class XiaoAi(threading.Thread):
#     def __init__(self):
#         super().__init__(name="小爱")
#
#     def run(self):
#         print("{} : 在".format(self.name))
#
# class TianMao(threading.Thread):
#     def __init__(self):
#         super().__init__(name="天猫精灵")
#     def run(self):
#         print("{} : 小爱同学".format(self.name))

# 通过condition完成协同读诗
from threading import Condition
if __name__ == "__main__":
    xiaoai = XiaoAi()
    tianmao = TianMao()

    xiaoai.start()
    tianmao.start()
# condition启动顺序很重要
# 在调用