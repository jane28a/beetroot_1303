from multiprocessing import Process
import time

from datetime.datetime import now
from here import my_decorator

def sleep_and_print(num):
    time.sleep(num/10)
    print(num)

# print("hello world") * 100 times
# request.get("https://python.org") * 100 times
# list current directory * 100 times
# counts 1001 prime number

def main():
    processes = list()
    for i in range(5):
        process = Process(target=sleep_and_print, args=(i,))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()