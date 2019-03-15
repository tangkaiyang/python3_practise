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
# 在调用with cond之后才能调用wait或者notify方法
# condition有两层锁,一把底层锁会在线程调用了wait方法的时候释放,上面的锁会在每次调用wait的时候分配一把并放入cond的等待对列中,等待notify方法的唤醒