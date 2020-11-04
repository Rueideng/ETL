#from multiprocessing import  Pool
from multiprocessing.dummy import  Pool
import time
import os

def longTimeTask(i):
    print('task:{},PID:{}'.format(i, os.getpid()))
    time.sleep(5)
    result = 10**30
    print("result: ", result)
    return result

if __name__ == "__main__":
    start_time = time.time()
    print("母程序PID:", os.getpid())

    p=Pool(4)
    data= p.map(longTimeTask, iterable=range(0,4))
    p.close()
    p.join()

    print("data=",data)

    end_time=time.time()
    print(end_time - start_time)