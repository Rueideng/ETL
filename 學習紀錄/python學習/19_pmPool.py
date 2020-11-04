from multiprocessing import  Pool
import time
import os

def longTimeTask(i):
    print('task:{},PID:{}'.format(i, os.getpid()))
    time.sleep(5)
    result = 10**30
    print("result:", result)

if __name__ == "__main__":
    start_time = time.time()
    print("母程序PID:", os.getpid())


    p=Pool(4)
    for i in range(0,8):
       p.apply_async(longTimeTask,args=(1, ))
    p.close()
    p.join()

    end_time=time.time()
    print(end_time - start_time)