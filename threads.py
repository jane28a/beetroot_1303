import time
import threading

def sleep_and_print(num):
    time.sleep(num/10)
    print(num)

def main():
    for i in range(1, 11):
        sleep_and_print(i)

def main_with_threads():
    for i in range(1, 11):
        thread = threading.Thread(target=sleep_and_print, args=(i,))
        thread.start()
        thread.join()

if __name__ == "__main__":
    main()
    main_with_threads()
