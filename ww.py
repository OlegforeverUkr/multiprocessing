import time
import multiprocessing
from threading import Thread


def base_power(num, power):
    return num ** power


def sync_power():
    start_time = time.time()
    base_power(2, 10_000_000)
    base_power(3, 10_000_000)
    base_power(5, 10_000_000)
    end_time = time.time()
    return end_time - start_time


def multi_tread():
    start_time = time.time()

    threads = []

    for i in [2, 3, 5]:
        thread = Thread(target=base_power, args=(i, 10_000_000))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


def multi_process():
    start_time = time.time()

    processes = []

    for i in [2, 3, 5]:
        process = multiprocessing.Process(target=base_power, args=(i, 10_000_000))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    sync = sync_power()
    multi_tr = multi_tread()
    multi_proc = multi_process()

    print('Usuall - ', sync,
          '\nMulti tread - ', multi_tr,
          '\nMulti process - ', multi_proc)

