# -*- coding:utf-8 -*- 
"""
fileName: fictiondownload.py
Created Time: 2017年09月29日 星期五 14时58分57秒
description:
"""


__author__ = 'yi_Xu'


from bs4 import BeautifulSoup
import urllib.request
import os, re
import sys, time, random


def getsoup(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('gbk', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def progressBar(count, total, message=None, interval = None):
    if not interval:
        interval = 1+ (random.randint(1,9)/10)
    i = int((count/total)*100)
    k = i + 1
    
    ProgressBar = '>'*(i//2)+' '*((100-k)//2)
    sys.stdout.write('\r'+ProgressBar+'[%s%%]'%(i+1)+' '*100)
    sys.stdout.flush()
    sys.stdout.write('\r'+ProgressBar+'[%s%%]'%(i+1)+message+'  稍等'+str(interval)+'秒！')
    sys.stdout.flush()
    time.sleep(interval)


def main():
    download_path = os.path.join('.', 'result')
    original_url = 'http://www.ranwena.com/files/article/0/167/'
    original_url_soup = getsoup(original_url)
    with open(os.path.join(download_path,'希灵帝国.txt'), mode='w', encoding='utf-8') as f:
        f.write("《希灵帝国》\n")
    for i, a in enumerate(original_url_soup.find(id='list').find_all('a')):
        chaptername = a.string
        chaptername = re.sub('[\\\\|:"<>?*./]', '_',chaptername).replace(' ', '')
        
        url = str(a.get('href'))
        fileName = '希灵帝国' + chaptername + '.txt'
        filePath = os.path.join(download_path,fileName)
        if os.path.isfile(filePath):
            message = chaptername + '已经下载过了！'
            progressBar(i, len(original_url_soup.find(id='list').find_all('a')), message, interval=0.001)
            continue
        with open(filePath, mode='w', encoding='utf-8') as f:
            f.write('\n' + chaptername + '\n')
        condition = True
        while condition:
            try:
                chapter_url_soup = getsoup(url)
                for each in chapter_url_soup.find(id='content').strings:
                    with open(filePath, mode='a', encoding='utf-8') as f:
                        f.write('%s%s' % (each.replace('\xa0', ''), os.linesep))
            except urllib.error.HTTPError:
                message = 'wait 403 拒接访问！'
            else:
                condition = False
                message = '正在下载：' + chaptername
            finally:
                progressBar(i, len(original_url_soup.find(id='list').find_all('a')), message)
    else:
        print('下载完成！')
            #print('%s%s' % (each.replace('\xa0', ''), os.linesep))
if __name__ == '__main__':
    main()
