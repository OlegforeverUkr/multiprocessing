import time
from threading import Thread
import multiprocessing
import requests


url_google = "https://google.com"
url_rozetka = "https://rozetka.com.ua/"
url_microsoft = "https://microsoft.com"


def get_status(url):
    requests.get(url)


def func_sinh_response(url):
    start_time = time.time()
    requests.get(url[0])
    requests.get(url[1])
    requests.get(url[2])
    end_time = time.time()
    return end_time - start_time




def func_sinh_five_response(url):
    start_time = time.time()
    for i in range(5):
        requests.get(url[0])
        requests.get(url[1])
        requests.get(url[2])
    end_time = time.time()
    return end_time - start_time




def tread_func_response(url):
    start_time = time.time()
    threads = []

    for i in url:
        thread = Thread(target=get_status, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time




def tread_func_five_response(url):
    start_time = time.time()

    for i in range(5):
        threads = []

        for y in url:
            thread = Thread(target=get_status, args=(y,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    end_time = time.time()
    return end_time - start_time




def multiprocessing_func_response(url):
    start_time = time.time()
    processes = []

    for i in url:
        process = multiprocessing.Process(target=get_status, args=(i,))
        process.start()
        processes.append(process)

    for process in processes:
            process.join()

    end_time = time.time()
    return end_time - start_time


def multiprocessing_func_five_response(url):
    start_time = time.time()
    processes = []

    for i in range(5):
        for y in url:
            process = multiprocessing.Process(target=get_status, args=(y,))
            process.start()
            processes.append(process)

        for process in processes:
                process.join()

    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    result_sinhron = func_sinh_response([url_google, url_rozetka, url_microsoft])
    result_sinhron_five = func_sinh_five_response([url_google, url_rozetka, url_microsoft])
    result_threaded = tread_func_response([url_google, url_rozetka, url_microsoft])
    result_threaded_five_times = tread_func_five_response([url_google, url_rozetka, url_microsoft])
    result_multiprocessing = multiprocessing_func_response([url_google, url_rozetka, url_microsoft])
    result_multiprocessing_five_times = multiprocessing_func_five_response([url_google, url_rozetka, url_microsoft])


    print('Usuall - ', result_sinhron,
          '\nFive times - ', result_sinhron_five,
          '\nMultithreaded - ', result_threaded,
          '\nMultithreaded five times - ', result_threaded_five_times,
          '\nMultiprocessing - ', result_multiprocessing,
          '\nMultiprocessing five times - ', result_multiprocessing_five_times,)
