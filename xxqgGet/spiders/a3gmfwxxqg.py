# -*- coding: utf-8 -*-
import scrapy
from xxqgGet.items import XxqggetItem

class A3gmfwxxqgSpider(scrapy.Spider):
    name = '3gmfwxxqg'
    allowed_domains = ['3gmfw.cn']
    start_urls = []
    start_urls.append('https://3gmfw.cn/article/html2/2019/09/09/486867.html')
    for i in range(45,47):
        url = 'https://3gmfw.cn/article/html2/2019/09/09/486867_'+str(i)+'.html'
        start_urls.append(url)
    def parse(self, response):
        subSelector = response.xpath('//div[@class="mainNewsContent NewsContent"]')
        items = []
        #初始化item
        item = XxqggetItem()
        #获取html数据
        htmlValueOri=subSelector.extract()[0]
        #去掉非法的&nbsp字符
        #htmlValue = "".join(htmlValueOri.split())
        htmlValue = htmlValueOri
        #进行分割
        qsItemsOri= htmlValue.split('<br>')
         #删除第一项和最后一项
        qsItemsOri.remove(qsItemsOri[0])
        qsItemsOri.remove(qsItemsOri[-1])
        #将列表元素中的换行和空格删除掉
        qsItemsOri1 = [ x.strip() for x in qsItemsOri]
        #删除列表为空的元素
        while '' in qsItemsOri1:
            qsItemsOri1.remove('')
        #将列表合并为字符串
        qsStrOri = '^'.join(qsItemsOri1)
        item['question'] = qsStrOri
        items.append(item)
        return items
