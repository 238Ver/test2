# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time


# 伪装成浏览器获取网页文本
# 接受URL/返回网页文本
#http://yx.dlut.edu.cn/index/yjsbd.htm
def get_html(url):
    try:
        send_headers = {
            "Host": "yx.dlut.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'Connection': 'close'
        }
        response = requests.get(url, headers=send_headers)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(e)


# 解析主页面提取链接属性
# 接受主页面/返回书本链接
def get_bookurl(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    urllist = []
    # 提取出图书的href属性
    for x in soup.find_all('a'):
        url = x['href']
        #http://yx.dlut.edu.cn/info/9991
        if re.match(r'http://yx.dlut.edu.cn/info/9991/\d{8}/\Z', url):
            urllist.append(url)
    urllist = urllist[::2]
    return urllist


# 利用bs4解析书本页面
# 接受书本页面/返回书本信息
# get_text()是获取标签之间的文本
def get_bookdata(html):
    book_data = []
    # soup = BeautifulSoup(html, 'lxml')
    soup = BeautifulSoup(html, 'html.parser')
    # 提取书名
    title = soup.find('h1').get_text(strip=True)
    book_data.append(title)
    # 提取图片
    img = soup.find(class_='nbg')['href']
    book_data.append(img)
    i = soup.find('div', id='info').get_text(strip=True)
    # 去掉空格
    info = re.sub(r'\s+', '', i)
    #提取作者
    pattern = re.match(r'作者:(.*)出版社.*ISBN:(.*)', info)
    book = pattern.groups()
    book_data.extend(book)
    related_info = soup.find('div', class_='related_info')
    indentlist = related_info.find_all(attrs={'class': 'indent'})

    # 提取简介
    iro = indentlist[0].get_text('|', strip=True)
    intro = re.sub(r'\s+', '', iro)
    book_data.append(intro)
    # 提取豆瓣评分
    douban_score = soup.find(class_='ll rating_num').get_text(strip=True)
    book_data.append(douban_score)
    return book_data


# 插入数据到文本文档中
def intofile(data, file):
    file = open(file, 'a', encoding='utf-8')
    for i in data:
        file.write(str(i))
        file.write('\t')
    file.write('\n')
    file.close()
    return True

def main():
    # 第一步：构造出主页面的url，获得所有图书链接
    book_url = []
    for a in [0, 10, 20]:
        # url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=' + str(a) + '&type=T'
        # url = 'https://book.douban.com/tag/%E6%A0%A1%E5%9B%AD?start=' + str(a) + '&type=T'
        url = 'https://book.douban.com/tag/%E6%A0%A1%E5%9B%AD?start=' + str(a) + '&type=T'

        book_url.extend(get_bookurl(get_html(url)))
        # 去除重复的链接
    book_url = list(set(book_url))
    print(book_url)

    # 第二步：根据图书链接爬取图书信息
    book_data = []
    for u in book_url:
        book_data = get_bookdata(get_html(u))
        time.sleep(1)  # 定义时间间隔
        intofile(book_data, 'book.txt')

if __name__ == '__main__':
    main()
