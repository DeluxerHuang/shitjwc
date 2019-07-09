import codecs
from bs4 import BeautifulSoup
from scutjwc import GetInfo
import os

class parseContent():
    def __init__(self):
        pass
    
    def parseHightlight(self, soup, datas):
        '''
        in html, highlight message are used id hightlightNews
        默认存在五个节点，所以只需要替换内容
        '''
        tag = soup.find('ul', id='hightlightNews')
        li = tag.find_all('li')
        loop = 0
        while loop < 5:
            k = datas[loop].split("&&")
            if k[0] == '' or k[1] == '' or k[2] == '':
                li[loop].decompose()
            else:
                li[loop].p.b.string = k[0]
                li[loop].a.string = k[1]
                li[loop].a['href'] = k[2]
            loop += 1
    
    def parseNormalInfo(self, soup, datas, htmlid):
        '''
        选择插入节点的方式来修改数据，只添加新的数据进<ul>
        对于无更新数据直接删除对应div块，分割线在div块中
        '''
        tag = soup.find('div', id=htmlid)
        #print(len(tag))
        #print(tag)
        if datas == []:
            tag.decompose()
        else:
            ul = tag.find('ul')
            for data in datas:
                da = data.split("&&")
                new_li_tag = soup.new_tag("li")
                new_li_tag["id"] = htmlid
                #插入节点
                new_a_tag = soup.new_tag("a", href=da[1])
                new_a_tag.string = da[0] + " [" + da[2] + "]"
                #new_li_tag.insert(0, new_a_tag)
                new_li_tag.append(new_a_tag)
                ul.append(new_li_tag)

if __name__ == '__main__':
    '''
    如何进行替换节点后并且写回文档
    '''
    test = codecs.open('./template/content.html', 'r', 'utf-8')
    soup = BeautifulSoup(test.read(), 'html.parser')
    news = codecs.open('news.html', 'w', 'utf-8')
    s = GetInfo('http://jwc.scuteo.com/jiaowuchu/cms/index.do')
    cata = ["affairs", "change", "news", "academic", "media"]
    try:
        cont = test.read()
        part = parseContent()
        part.parseHightlight(soup, s.getHighlightString())
        for name in cata:
            part.parseNormalInfo(soup, s.getAffairs(), name)
        strs = soup.prettify()
        news.write(strs)
    finally:
        news.close()
        test.close()