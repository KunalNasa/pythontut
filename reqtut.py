import requests
# r = requests.get("https://site.financialmodelingprep.com/financial-summary/AAPL")
# print(r.text)
# print(r.status_code)

# url = "www.kunalnasa.com"
# data = {
#     "p":4,
#     "p2":8
# }
#
# r2 = requests.post(url= url, data=data)


# x = requests.get('https://w3schools.com/python/demopage.htm')
#
# print(x.text)

# r = requests.get("https://xkcd.com/353/")
# print(dir(r))
# print(help(r))
# print(r.content)
# print(r.text)

# r = requests.get("https://imgs.xkcd.com/comics/python.png")
# with open('comic.png', 'wb') as c:  #wb - write bytes mode
#     c.write(r.content)


# r = requests.get("https://imgs.xkcd.com/comics/python.png")
# print(r.status_code)
# print(r.ok)
# print(r.headers)

# r = requests.get('https://httpbin.org/get?page=2&count=25') #we can also add data after get in parameters(it also reduces chances of error).
# payload  = {'page':2, 'count':25}
# r = requests.get("https://httpbin.org/get", params= payload)
# print(r.url)


# payload  = {'username':'Kunal', 'password':'kannu'}
# r = requests.post("https://httpbin.org/post", data= payload)
# # print(r.text)
# r_dict = r.json()
# print(r_dict['form'])


# r = requests.get("http://httpbin.org/basic-auth/kannu/Kunal", auth = ('kannu', 'Kunal'))
# print(r.text)


r = requests.get("http://httpbin.org/delay/6", timeout = 5)
print(r)
