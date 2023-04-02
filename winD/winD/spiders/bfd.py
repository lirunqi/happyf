import requests
from bs4 import BeautifulSoup

url = "http://odds.gooooal.com/fb_detail.html?mid=1868860&cid=19&type=0&ms=0&lang=cn"

# 获取网页内容
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 获取赔率表格
table = soup.find_all('table', {'class': 'pankou_table'})[0]

# 解析赔率数据
for tr in table.tbody.find_all('tr'):
    # 获取公司名称
    company_name = tr.th.a.text.strip()

    # 获取时间和赔率
    for td in tr.find_all('td')[1:]:
        time = td.get('data-time')
        odds = td.get('data-odds')

        print(time, company_name, odds)