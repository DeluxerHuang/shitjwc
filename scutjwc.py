from urllib import request, parse
import codecs
from bs4 import BeautifulSoup

class HtmlDownloader(object):
    '''
    网页下载器
    '''
    def download(self, url):
        if url is None:
            return None
        res = request.urlopen(url)
        if res.getcode() != 200:
            return None
        return res.read().decode('utf-8')

class HtmlParser():
    '''
    解析器
    '''
    def _getHighligthInfo(self, page_url, soup):
        '''
        page_url: 原网页
        soup: bs对象
        教务处网站上的通知最上面一条的样式不一致
        单独提取
        div class='index-content-infos-tab-ad-info pt20 pl20 pr20'
        '''
        highNode = soup.find_all('div', class_="index-content-infos-tab-ad-info pt20 pl20 pr20")
        res_data = []
        res_link = []
        for i in highNode:
            res_data.append(i.a.get_text())
            res_link.append(parse.urljoin(page_url, i.a['href']))
        return res_data, res_link

    def _getNewsData(self, page_url, soup):
        '''
        目前教务的主页分为5个板块，每个板块上面有12条消息
        只抓取标题-链接-时间
        '''
        title_node = soup.find_all('li', class_="oh")
        res_data = []
        res_link = []
        res_time = []
        #print(len(title_node))
        for i in title_node:
            res_data.append(i.a.get_text())
            res_link.append(parse.urljoin(page_url, i.a['href']))
            res_time.append(i.find("span", class_="fr").get_text())
        return res_data, res_link, res_time

class GetInfo():
    '''
    all datas are encapsulated in one member
    对HtmlParser的封装
    '''
    def __init__(self, url):
        self.url = url
        self.down = HtmlDownloader()
        self.cont = self.down.download(url)
        self.soup = BeautifulSoup(self.cont, 'html.parser')
        self.par = HtmlParser()
        self.category = ['教务通知', '交流交换', '新闻动态', '学院通知', '媒体关注']

    def getHighlightString(self):
        '''
        数据格式为 类别&&标题&&链接
        置顶消息无时间字段
        返回值为list
        顺序为category顺序
        '''
        data, link = self.par._getHighligthInfo(self.url, self.soup)
        datas = []
        for ca, k, c in zip(self.category, data, link):
            i = ca + "&&" + k + "&&" + c
            datas.append(i)
        return datas

    def getAllCatagory(self):
        '''
        return a dict
        keys are category 5
        values a list 12
        '''
        data, link, time = self.par._getNewsData(self.url, self.soup)
        datas = {}
        count = 0
        while count<5:
            i = 0
            #print("*"+category[count]+"*")
            datas[self.category[count]] = []
            while i<12:
                nums = 12*count+i
                try:
                    s = data[nums] + "&&" + link[nums] + "&&" + time[nums]
                    datas[self.category[count]].append(s)
                    i+=1
                except:
                    print("error")
            count+=1
        return datas

    '''
    all the data are like 
    title&&link&&time
    以下返回的都是list
    '''
    def getAffairs(self):
        return self.getAllCatagory()['教务通知']

    def getChange(self):
        return self.getAllCatagory()['交流交换']
    
    def getNews(self):
        return self.getAllCatagory()['新闻动态']

    def getAcademic(self):
        return self.getAllCatagory()['学院通知']

    def getMedia(self):
        return self.getAllCatagory()['媒体关注']