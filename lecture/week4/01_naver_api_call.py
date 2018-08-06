import os
import sys
import urllib.request
import json

client_id = "JyP8ZGwBvgwzajxGWs7m"
client_secret = "WC3_t8TCMu"
encText = urllib.parse.quote("에어컨")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    json_obj = json.loads(response_body)

    for item in json_obj['items']:
        print(item['title'])

else:
    print("Error Code:" + rescode)