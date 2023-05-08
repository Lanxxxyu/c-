import requests
response=requests.get('http://books.toscrape.com/')
if response.ok:
    #200为请求成功 
    print(response)
    print(response.text)#爬取的为该网页的源码
else:
    print("请求失败")
