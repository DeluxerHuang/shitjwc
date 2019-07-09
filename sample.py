from scutjwc import *

if __name__ == '__main__':
    category = ['教务通知', '交流交换', '新闻动态', '学院通知', '媒体关注']
    url = 'http://jwc.scuteo.com/jiaowuchu/cms/index.do'
    info = GetInfo(url) #获取info对象
    
    #以学院通知为例
    s = info.getAcademic() #获取学院通知信息
    for li in s:
        print(li)
    
    #提取标题和时间
    for li in s:
        tu = li.split("&&")
        print(tu[0]) #标题
        print(tu[1]) #链接
        print(tu[2]) #时间


    #获取指定消息
    print("highLight")
    t = info.getHighlightString()
    for i in t:
        print(i)

    #分割信息同上
    for i in t:
        tm = i.split("&&")
        print(tm[0]) #类别
        print(tm[1]) #标题
        print(tm[2]) #链接