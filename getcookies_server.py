import requests
import re
import urllib
from pytesser import *

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
def find_code():
    impath = './codePhoto/the_code_photo.png'
    im = Image.open(impath)
    text = image_to_string(im)
    text = text.strip('\n')
    print text
    return text
def find_select(text):
    new_str = text[6:14]
    return new_str

def init_main():

    url_test = "http://202.97.210.38:9002/usr_cardb_main.ktcl"
    html = getHtml(url_test)
    getImg(html)

    card_id = "card_id="+"4510002509618"
    password ="&password="+"oruec8pu"
    code ="&code="+find_code()
    key = "&key="+get_key_value(html)

    payload = card_id+password+code+key
    print payload

    url_post = "http://202.97.210.38:9002/usr_cardb_proc.ktcl"
    response = requests.request("POST",url_post,data=payload)
    user_cookie = response.headers['Set-Cookie']
    user_cookie = user_cookie.strip(';')
    print user_cookie

    url_select = "http://202.97.210.38:9002/cardb_acct_bal.ktcl"
    select = {'select':find_select(user_cookie)}
    headers = {'Cookie':user_cookie}
    response = requests.request("POST",url_select,data=select,headers=headers)
    print response.text
    return response.text
