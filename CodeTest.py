"""
커피포트는 N개 1 10,000
주문수량은 M개 길이 1 300,000 원소 100,000,000
입출력 예시
N   coffie_times    result
3   [4,2,2,5,3]     [2,3,1,5,4]
"""
from threading import Thread
from threading import Lock
from collections import deque
import time

N = input("커피머신 개수는?: ")
coffie_times = [4,2,2,5,3]
result = []
class OrderedCoffie:
    def __init__(self,N,coffie_times):
        self.N = N
        self.coffie_times = coffie_times

    def startMakeCoffie(self):
        print("N: ",self.N)
        print("coffie_times: ",self.coffie_times)

class MakingCoffie(Thread):
    def __init__(self):
        super().__init__
        self.testTime = 1

    def callMaking(self):
        time.sleep(3)
        print("sleep: done")
        return self.testTime

orderCoffie = OrderedCoffie(N,coffie_times)
orderCoffie.startMakeCoffie()
coffie_times.pop()
orderCoffie.startMakeCoffie()
threads = MakingCoffie()
threads.callMaking()


