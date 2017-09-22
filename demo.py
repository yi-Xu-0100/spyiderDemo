# -*- coding: utf-8 -*-


__author__ = 'yi_Xu'

import urllib
import urllib.request


def main():
    data = {}
    data['word'] = 'Python 爬虫'
    urlValues = urllib.parse.urlencode(data, encoding = 'utf-8')
    url = "http://www.baidu.com/s?"
    fullUrl = url + urlValues
    data = urllib.request.urlopen(fullUrl).read()
    data =data.decode('utf-8')
    print(data)

if __name__ == '__main__':
    main()