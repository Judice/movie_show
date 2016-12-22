# _*_ coding: utf-8 _*_
import urllib2
from bs4 import BeautifulSoup
from mongoengine import connect, Document, StringField, IntField, ListField
from movie.utils import time as time_utils
import config


class Movie(Document):
    name = StringField(required=True, unique=True)
    year = IntField()
    month = IntField()
    day = IntField()
    img_url = StringField()
    download_links = ListField()
    date = IntField()

url_movie_list = 'http://www.6vhao.com/gvod/zx.html'


def get_html(url):
    """获取指定url web内容

    :param url:
    :return:
    """
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except ValueError, urllib2.URLError:
        html = ''
    return html


def get_movie_list():
    """针对url_movie_list，返回所有电影链接、更新时间、名称的数组

    :return:
    """
    html = get_html(url_movie_list)
    soup = BeautifulSoup(html, 'html5lib')
    lis = soup.select('ul[class="list"] li')
    movie_list = []
    for li in lis:
        month = int(li.span.string[1:3])
        day = int(li.span.string[4:6])
        url = li.a.get('href')
        try:
            name = li.a.span.string
        except AttributeError:
            name = li.a.string
        movie_list.append({
            'month': month,
            'day': day,
            'url': url,
            'name': name,
        })
    return movie_list


def get_movie_detail(url):
    """获取电影详情

    :param url:
    :return:
    """
    html = get_html(url)
    soup = BeautifulSoup(html, 'html5lib')
    img_url = soup.select_one('div[id="endText"] p img').get('src')
    download_links = [str(td.contents[0].encode('utf-8')) for td in soup.select('div[id="endText"] td')]
    return {'img_url': img_url, 'download_links': download_links}


def start_job():
    movie_list = get_movie_list()
    for movie in movie_list:
        name = movie.get('name')
        url = movie.get('url')
        movie_detail = get_movie_detail(url)
        month = movie.get('month')
        year = time_utils.current_year - 1 if time_utils.current_month - month < 0 else time_utils.current_year
        day = movie.get('day')
        date = time_utils.prc_int_day(time_utils.format_arrow_time(year, month, day))
        img_url = movie_detail.get('img_url')
        download_links = movie_detail.get('download_links')
        Movie(name=name, year=year, month=month, day=day, img_url=img_url, download_links=download_links, date=date).\
            save()
        print 'movie {0} is saved'.format(name.encode('utf-8'))

if __name__ == '__main__':
    connect(config.MONGODB_SETTINGS['db'], host=config.MONGODB_SETTINGS['host'], port=config.MONGODB_SETTINGS['port'])
    start_job()
