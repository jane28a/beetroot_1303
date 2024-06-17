from threading import Thread

counter = 0

def increase():
    global counter
    for i in range(100_000):
        counter += 1

if __name__ == "__main__":
    threads = []
    for i in range(400):
        thread = Thread(target=increase)
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(counter)