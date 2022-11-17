import urllib3
import requests

# 设置连接池
def get_html_by_urllib(url):
    pool_manager = urllib3.PoolManager()
    r = pool_manager.request('get',url)
    return r.data.decode('utf-8')
def get_html_by_requests(url):
    r = requests.get(url)
    return r.content