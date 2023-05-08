import requests
#通过headers对程序进行伪装
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 "}
response=requests.get('https://movie.douban.com/top250',headers=headers)
#状态码为4开头表示请求存在问题
print(response)
print(response.text)
