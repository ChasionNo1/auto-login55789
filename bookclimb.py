#encording='utf-8'
import requests
import json
import urllib

headers = {"Referer": "https://view57.book118.com/pdf/dXAxNC0zLmJvb2sxMTguY29tLjgwXDQ1NzA4NzItNWJiNWI4MThlMGNjNi5wZGY%3d?readpage=0OEvuD5bBUBfS0xmxbdZqA%3D%3D&furl=o4j9ZG7fK94Tv49GtkfHI01km8IDSWfGjKmxOx3L7c3Kn5qq4ouSX0qQHYTn6i8xx4wux2Vr_RAkbukPHFu9pJRQlYKmlAU1ZyBpmNIt%40n_jwrEkW221jA%3D%3D&token=PDWfni5ovTuPlmy9LSwwpBMbk5TNAo4t",
           "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
param = "7o@o7xcocmkBL1fhqhpnSoO7TLfS_J@EPUHaYhyl1CWngmIalFIvfwocQIH_0oxhWMpXtMXk7r0="
for i in range(0,176,1):
    first_url = "https://view57.book118.com/img/?img={}"
    first_url = first_url.format(param)
    print(first_url)
    response = requests.get(first_url,headers=headers)
    NextPageUrl = "https://view57.book118.com/pdf/GetNextPage/?f=dXAxNC0zLmJvb2sxMTguY29tLjgwXDQ1NzA4NzItNWJiNWI4MThlMGNjNi5wZGY%3D&img={}&isMobile=true&isNet=True&readLimit=0OEvuD5bBUBfS0xmxbdZqA%3D%3D&furl=o4j9ZG7fK94Tv49GtkfHI01km8IDSWfGjKmxOx3L7c3Kn5qq4ouSX0qQHYTn6i8xx4wux2Vr_RAkbukPHFu9pJRQlYKmlAU1ZyBpmNIt%40n_jwrEkW221jA%3D%3D"
    NextPageUrl = NextPageUrl.format(param)
    response1 = requests.get(NextPageUrl,headers=headers)
    param = json.loads(response1.content)['NextPage']
    print(param)
    with open("D:\\an\\page={}.png".format(i), "wb")as f:
        f.write(response.content)
