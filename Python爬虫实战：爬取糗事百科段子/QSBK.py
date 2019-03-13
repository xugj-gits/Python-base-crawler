#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   QSBK.py
@Time    :   2019/03/13 09:58:59
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''
from urllib import request, error
import ssl
import re

class QSBK:

    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.hosts = 'www.qiushibaike.com'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent, 'Host' : self.hosts}
        # 存放段子的变量，每一个元素就是一页的段子
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False
        self.contextes = ssl._create_unverified_context()

    # 获取传入索引页面的Html代码
    def getPage(self, pageIndex):
        try:
            url = 'https://www.qiushibaike.com/hot/page/' + str(pageIndex)
            req = request.Request(url=url, headers=self.headers)
            response = request.urlopen(req, context=self.contextes)
            pageCode = response.read().decode('UTF-8')
            return pageCode
        except error.URLError as e:
            if hasattr(e, "reason"):
                print('连接糗事百科失败,错误原因:%s' % e.reason)
                return None



    # 获取传入索引页面不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('页面加载失败...')
            return None

        pattern = re.compile('<div.*?content">.*?<span>.*?(.*?)</span>.*?</div>', re.S)
        pageStories = re.findall(pattern, pageCode)
        return pageStories

    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    
    # 调用该方法，每次回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            inputs = input()
            self.loadPage()
            if inputs == 'Q':
                self.enable = False
                return
            print(story)

    
    # 开始方法
    def start(self):
        print('正在读取糗事百科,按回车查看新段子，Q退出')
        self.enable = True
        self.loadPage()

        nowPage = 0
        while self.enable:
            if len(self.stories) > 0 :
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)



spider = QSBK()
spider.start()