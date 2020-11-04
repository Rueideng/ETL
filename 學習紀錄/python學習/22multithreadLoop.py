#import multiprocessing as mp
import  threading
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


    mp_list=[]
    for p in range(0,4):
        mp_list.append(threading.Thread(target=longTimeTask, args=(p, )))

    for p in range(0,4):
        mp_list[p].start()

    for p in range(0, 4):
        mp_list[p].join()


    end_time=time.time()
    print(end_time - start_time)