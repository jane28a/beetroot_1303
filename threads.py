import time
import threading

def sleep_and_print(num):
    time.sleep(num/10)
    print(num)

def main():
    for i in range(1, 11):
        sleep_and_print(i)

def main_with_threads():
    threads = list()
    for i in range(5):
        thread = threading.Thread(target=sleep_and_print, args=(i,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    main_with_threads()
