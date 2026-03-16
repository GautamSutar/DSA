import threading 
import time 
from concurrent.futures import ThreadPoolExecutor
def func(second):
    print(f"sleeping for {second} second")
    time.sleep(second)
    return second

def threadPoolExecutor():
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 2, 4]
        results = executor.map(func, l)
        for result in results:
            print(result)
            
            
threadPoolExecutor()