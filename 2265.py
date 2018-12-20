import requests


url = 'http://img.tukuppt.com/origin_music/00/06/18/pd-5b7a133e4a45c868.mp3'
headers = {'authority': 'u.y.qq.com',
           'method': 'GET',
           # 'path': '/cgi-bin/musicu.fcg?callback=getplaysongvkey09829986857353257&g_tk=897183151&jsonpCallback=getplaysongvkey09829986857353257&loginUin=1051459470&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%225445473344%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%225445473344%22%2C%22songmid%22%3A%5B%2YjvJ11vued88%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221051459470%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A1051459470%2C%22format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D',
           'scheme': 'https',
           'accept': '*/*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9',
           'cookie': 'pgv_pvid=5445473344; tvfe_boss_uuid=56fdfcdaada6f420; pgv_pvi=1255536640; RK=iGAg0uQUPJ; ptcz=d9bcd472d062e8220d9ca2f67e23a372914a2078c0a57ad567ed07a2c2f97cf0; o_cookie=185897780; ts_uid=2805663344; ptui_loginuin=1051459470; pt2gguin=o1051459470; luin=o1051459470; lskey=00010000f78fb167a8f45b5b54ccc547ac4a84252eae333f9cc075b2749a75c50ed92fc0904299af76f0f56c; p_luin=o1051459470; p_lskey=00040000011b7e4b92addd33d010a5a6561ef5cf0765d1900550c4bf4ee7a0a7c5830adf7d9ada4f9df5ae0d; ts_refer=www.baidu.com/link; pgv_si=s1745353728; pgv_info=ssid=s316746010; yqq_stat=0; player_exist=1; qqmusic_fromtag=66; ts_last=y.qq.com/portal/player.html; yplayer_open=1; yq_index=0',
           'referer': 'https://y.qq.com/portal/player.html',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
response = requests.get(url, headers=headers)
with open('zengxiaoxian.WAV', 'wb') as f:
    f.write(response.content)
