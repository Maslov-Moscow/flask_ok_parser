from bs4 import BeautifulSoup
import requests
import re


def parse_site(login,password):
    url = 'https://ok.ru/dk?cmd=AnonymLogin&st.cmd=anonymLogin'
    headers = {'origin': 'https://ok.ru',
               'referer': 'https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
               'content-type': 'application/x-www-form-urlencoded'}
    data = {f'st.email': {login}, f'st.password': {password}, 'st.iscode': 'false', 'st.st.flashVer': '0.0.0',
            'st.fJS': 'on', 'st.posted': 'set', 'st.asr': '', 'st.redirect': ''}
    response = requests.post(url=url, allow_redirects=False, headers=headers, data=data)
    cookie = response._next.headers['Cookie']
    site = requests.get('https://ok.ru', headers={'Cookie': cookie, 'user-agent': response._next.headers['user-agent'],
                                                  'referer': 'https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose'})
    return site

def get_name(site):
    soup = BeautifulSoup(site.text, 'html.parser')
    div = soup.find('div', class_='ellip')
    name = div.text

    href = soup.find('a', class_='toolbar_nav_a toolbar_nav_a__friends')
    id = re.search('(\d+)',href['href'])[0]


    return (name,id)

