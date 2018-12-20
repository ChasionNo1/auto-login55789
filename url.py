import requests

url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey8320475868222292&g_tk=897183151&jsonpCallback=getplaysongvkey8320475868222292&loginUin=1051459470&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"5445473344","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"5445473344","songmid":["004DXFlC0nsTCZ"],"songtype":[0],"uin":"1051459470","loginflag":1,"platform":"20"}},"comm":{"uin":1051459470,"format":"json","ct":20,"cv":0}}'

headers = {'authority': 'u.y.qq.com',
           'method': 'GET',
           # 'path': '/cgi-bin/musicu.fcg?callback=getplaysongvkey09829986857353257&g_tk=897183151&jsonpCallback=getplaysongvkey09829986857353257&loginUin=1051459470&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"5445473344","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"5445473344","songmid":[%2YjvJ11vued88"],"songtype":[0],"uin":"1051459470","loginflag":1,"platform":"20"}},"comm":{"uin":1051459470,"format":"json","ct":20,"cv":0}}',
           'scheme': 'https',
           'accept': '*/*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9',
           'cookie': 'pgv_pvid=5445473344; tvfe_boss_uuid=56fdfcdaada6f420; pgv_pvi=1255536640; RK=iGAg0uQUPJ; ptcz=d9bcd472d062e8220d9ca2f67e23a372914a2078c0a57ad567ed07a2c2f97cf0; o_cookie=185897780; ts_uid=2805663344; ptui_loginuin=1051459470; pt2gguin=o1051459470; luin=o1051459470; lskey=00010000f78fb167a8f45b5b54ccc547ac4a84252eae333f9cc075b2749a75c50ed92fc0904299af76f0f56c; p_luin=o1051459470; p_lskey=00040000011b7e4b92addd33d010a5a6561ef5cf0765d1900550c4bf4ee7a0a7c5830adf7d9ada4f9df5ae0d; ts_refer=www.baidu.com/link; pgv_si=s1745353728; pgv_info=ssid=s316746010; yqq_stat=0; player_exist=1; qqmusic_fromtag=66; ts_last=y.qq.com/portal/player.html; yplayer_open=1; yq_index=0',
           'referer': 'https://y.qq.com/portal/player.html',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.content.decode())

