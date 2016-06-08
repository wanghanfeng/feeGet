#coding=utf-8
import re
import urllib

url = "http://202.97.210.38:9002/usr_cardb_proc.ktcl"
payload = "card_id=4510002509618&password=oruec8pu&code=4736&key=d40e24bdf45fc904a1e4490a1bb9cc225e8851874b12face"
cookies = ""

card_id = "4510002509618"
password = "oruec8pu"
code = "5954"
key = "f92c6d1254a029a4179d66afd3b9e5425e8851874b12face"

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_key_value(html):
    reg = r'name=.key. value=.(.+?).>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for key_value in imglist:
        return key_value

def getImg(html):
    reg = r'img src=(.+?\.png)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        imgurl = 'http://202.97.210.38:9002/' + imgurl
        urllib.urlretrieve(imgurl,'./codePhoto/the_code_photo.png')
        print imgurl

if __name__ == '__main__':
    url_test = "http://202.97.210.38:9002/usr_cardb_main.ktcl"
    html = getHtml(url_test)
    getImg(html)
    key_value = get_key_value(html)
    print key_value

# response = requests.request("POST",url,data = payload)

# set_cookie = requests.post(url,payload).cookies

# print(response.text)
# print("\n")
# print(response.headers)

# print (set_cookie['Set-Cookie'])

# set_cookie = requests.get('http://www.baidu.com')
# print (set_cookie['BAIDUID'])
# if len(set_cookie)>1:
#     print('login school return cookies...')
# else:
#     print('login failed ...')
