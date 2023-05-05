import requests
import re
import datetime

url = "https://www.example.com/time" # 你想要爬取的网页URL
response = requests.get(url) # 发送HTTP GET请求

if response.status_code == requests.codes.ok: # 如果请求成功
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}" # 正则表达式匹配时间格式
    
    match = re.search(pattern, response.text) # 在网页内容中搜索时间
    
    if match:
        time_str = match.group() # 获取到时间字符串
        time_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S") # 将时间字符串转化为datetime对象
        print("现在的时间是：", time_obj)
