import multiprocessing as mp
import time
import os

def longTimeTask(i):
    print('task:{},PID:'.format(i, os.getpid()))
    time.sleep(5)
    result = 10**30
    print("result:", result)

if __name__ == "__main__":
    start_time = time.time()
    print("母程序PID:", os.getpid())

    work1 = mp.Process(target=longTimeTask, args=(1, ))
    work2 = mp.Process(target=longTimeTask, args=(2, ))
    work3 = mp.Process(target=longTimeTask, args=(3, ))
    work4 = mp.Process(target=longTimeTask, args=(4, ))

    work1.start()
    work2.start()
    work3.start()
    work4.start()

    work1.join()
    work2.join()
    work3.join()
    work4.join()
    end_time=time.time()
    print(end_time - start_time)