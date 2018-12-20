import requests
import json
input_url = input('输入URL：')
params = input_url[input_url.rindex('/')+1:input_url.rindex('.')]
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+params+'&filename=C400'+params+'.m4a&guid=9082027038'
response = requests.get(url)    # 访问加密的网址
response = json.loads(response.text)
vkey = response['data']['items'][0]['vkey'] # 加密的参数
music_url = 'http://dl.stream.qqmusic.qq.com/C400'+params+'.m4a?vkey='+vkey+'&guid=9082027038&uin=0&fromtag=66'
response = requests.get(url=music_url, stream=True)
with open('new_music.mp3', 'wb') as f:
    for chunk in response.iter_content(1024):
        f.write(chunk)
