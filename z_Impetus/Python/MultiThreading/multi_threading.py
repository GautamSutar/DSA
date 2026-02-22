import threading 
import time 
def func(second):
    print(f"sleeping for {second} second")
    time.sleep(second)

time1 = time.perf_counter()

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()


time2 = time.perf_counter()
print(time2 - time1)
