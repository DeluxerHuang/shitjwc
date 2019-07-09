# holy shit scutjwc

![scutjwc](./template/scutjwc.png)

## 文件结构

- scutjwc.py 爬虫模块
- smtp.py 邮件发送模块
- parseContent.py html内容处理模块
- template文件夹存放html模板
- conn数据库连接模块

## 注意

- parseContent.py使用比较固定，需要根据给定模板的html样式进行处理
- 使用smtp发送邮件，邮件服务器必须支持SMTP/IMAP
- 数据库相关代码请放在conn文件夹下
- 文本文件使用utf-8编码
