import requests
import datetime
import functools

def bench_count(cnt):

    def timer(func):

        @functools.wraps(func)
        def wrapper(url):
            begin = datetime.datetime.now()

            for i in range(cnt):
                func(url)

            end = datetime.datetime.now()
            second = (end - begin).total_seconds()

            print(f'Выполнено {cnt} запросов за {second:.2f} ({cnt/second:.2f} rps) - {url}')

        return wrapper

    return timer

@bench_count(1000)
def req(url):
    requests.get('http://gitsrv01:5050/' + url)

req('ping')
# req('find?collect=test')
