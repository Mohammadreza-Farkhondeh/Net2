
url = 'https://net2.sharif.edu/login'
payload  = {'username': 'matin.mirzaei926', 'password': 'Matin926'}


def logIn_requests():
    import requests
    with requests.Session () as s:
        p = s.post(url, data=payload)


def logIn_webbot():
    import webbot
    web = browser()
    web.go_to(url)
    web.click(name="username")
    web.type(payload[username], name="username")
    web.click(name="password")
    web.type(payload[password], name="password")
    web.click(classname="login-form-btn")


def logIn_PyQuery():
    from pyquery import PyQuery
    q = PyQuery(content)
    title = q("title").text()

