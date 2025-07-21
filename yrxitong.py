import requests,csv
from lxml import etree
#xpath方法进行爬取
headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
url='https://www.yrxitong.com/h-nr--0_406_2.html'

#发送请求
response=requests.get(url,headers=headers)
#编码转换
content=response.content.decode('utf8')
#网页解析
html=etree.HTML(content)
#提取各个元素
softs=[]
# softhrefs=html.xpath('//div[@topclassname="top1"]//a[@hidefocus="true"]/@href')
softhrefs=html.xpath('//div[@topclassname="top1"]//a[@class="J_articlePicHref"]/@href') #更换url地址

for softhref in softhrefs:
    soft={}  #新建空字典
    softurl='https://www.yrxitong.com'+softhref
    soft_html=etree.HTML(requests.get(softurl,headers=headers).content.decode('utf-8'))
    soft_title=soft_html.xpath('//h1/text()')[0]
    #简介
    # soft_jianjie=soft_html.xpath('//div[@class="jz_fix_ue_img"]/p[1]')
    soft_jj=soft_html.xpath('//div[@class="jz_fix_ue_img"]//p[1]/text()')[0]
    '''
       # 百度盘地址
    soft_baidu=soft_html.xpath('//div/p[3]/a/@href')
    # 啊里云盘
    soft_ali=soft_html.xpath('//div/p[4]/a/@href')
    # onedrive地址
    soft_one=soft_html.xpath('//div/p[5]/a/@href')
    '''
    soft_baidu=soft_html.xpath('//div[@class="jz_fix_ue_img"]//p/a/@href')[-3]
    soft_ali=soft_html.xpath('//div[@class="jz_fix_ue_img"]//p/a/@href')[-2]
    soft_one=soft_html.xpath('//div[@class="jz_fix_ue_img"]//p/a/@href')[-1]
   #附件下载地址
    #soft_attachdown=soft_html.xpath('//a[@class="attachName"]/@href')[0]
    soft={
        '软件名':soft_title,
        '软件简介':soft_jj,
        #'软件附件地址':soft_attachdown,
        '百度地址':soft_baidu,
        '阿里地址':soft_ali,
        'onedrive地址':soft_one,
        }
    print(soft)
    softs.append(soft)





