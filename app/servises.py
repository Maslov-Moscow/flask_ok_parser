import re

import requests
from bs4 import BeautifulSoup


def parse_site(login, password):
    url = 'https://ok.ru/dk?cmd=AnonymLogin&st.cmd=anonymLogin'
    headers = {'origin': 'https://ok.ru',
               'referer': 'https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
               'content-type': 'application/x-www-form-urlencoded'}
    data = {'st.email': {login}, 'st.password': {password}, 'st.iscode': 'false', 'st.st.flashVer': '0.0.0',
            'st.fJS': 'on', 'st.posted': 'set', 'st.asr': '', 'st.redirect': ''}
    with requests.Session() as s:
        response = s.post(url=url, headers=headers, data=data)
        return response


def get_name(site):
    soup = BeautifulSoup(site.text, 'html.parser')
    div = soup.find('div', class_='ucard-mini_cnt_i')
    name = div.text

    href = soup.find('a', class_='toolbar_nav_a toolbar_nav_a__friends')
    id = re.search('(\d+)', href['href'])[0]

    return (name, id)

