url = 'http://net2.sharif.ir/logout?'


def logOut_webbot():
    # from webbot import *
    web = Browser()
    web.go_to('http://net2.sharif.edu/status')
    web.click(classname="login100-form-btn")

def logOut_requests():
    import requests
    with requests.Session() as s:
        p = s.get(url)
