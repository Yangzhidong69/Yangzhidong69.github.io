# import requests
# import re
# import json
# import time
# import csv
# # 爬取网页数据源码
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
#     'Cookie': 'guid=a3c8b82754108c2c31c3fbdf6d2656b4; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; ssxmod_itna=Yq+xnDyDBjitGHKRwDjOAtG8KwFq7If5==3D/YQxnqD=GFDK40EvHqPD7zKR5nR2BeiiWnYSm+3Kb1jRoe87IMnUoDU4i8DCqnD3sxenQD5xGoDPxDeDADYE6DAqiOD7qDdfhTXtkDbxi3fxiaDGeDeEKODY5DhxDC6mPDwx0CfaxYgA9hO6BCTK5Y5bDxfxG1a40H8ASINU8LgmyhwFSdqGDDUnwUemTtS9iPdxBomx0kYq0Oc=vzk=EU66v1DRqTq70qMG2qGCbxYBTq3Aw4rW8t8AD5aGDPeA0DzExx=lceF2=DioPyWiDD==; ssxmod_itna2=Yq+xnDyDBjitGHKRwDjOAtG8KwFq7If5==G9QamDBkDhD7P63D7Gao8hx8xWU8pX1qGhiyi7FFrY9t48b8j4NIox4cE=4K=i=99aYe9Dxjdd2t0Fwpe1tp0Ga=AbWgWvpxymGFw99htpDjd0YQfpb4IxQiheV+I5T4mec4AIjwbhGboyf4Ql7nfGB2Pe1+5inR2z3Zd=FxEhlkPDaqrDoiiFgTN7ua0VA4tGRaNhv=oFM3XrgT0+grhrxjQ9f+Yi0YFsenG7o7Ska8vEBeYW6uA7Sfq9lhAcalGw/R2CTSHzGqgE=m3dadf0oe74DQFmD08DiQ8YD==='
# }
# for page in range(1,1042):
#     url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(page)
#     response = requests.get(url=url,headers=headers).text
#     time.sleep(0.3)
#     #正则查找
#     r = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>',response,re.S)
#     string = ''.join(r)
#     infodict = json.loads(string)
#     #字典的键获取 对应的值
#     engine_search_result = infodict['engine_search_result']
#     for i in engine_search_result:
#         #公作名字
#         job_name = i['job_name']
#         #详细信息网页地址
#         job_href = i['job_href']
#         #公司名字
#         company_name = i['company_name']
#         #公司福利
#         jobwelf = i['jobwelf']
#         #工作地址
#         workarea_text = i['workarea_text']
#         #公司性质
#         companytype_text = i['companytype_text']
#         #薪资待遇
#         providesalary_text = i['providesalary_text']
#         # 文聘要求
#         attribute_text = i['attribute_text']
#         f = open('51job.csv','a')
#         f.write('{},{},{},{},{},{},{},{}\n'.format(job_name,job_href,company_name,jobwelf,workarea_text,companytype_text,providesalary_text,attribute_text))
#         f.close()






import time
import requests
from lxml import etree
# if __name__ == __main__:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
url = 'https://cd.58.com/ershoufang/?utm_source=sem-sales-baidu-pc&spm=83028910845.21475390032&utm_campaign=sell&utm_medium=cpc&showpjs=pc_fg&bd_vid=8320809163272762952'
page_text = requests.get(url=url,headers=headers,).text
tree = etree.HTML(page_text)
# print(page_text)
li_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
fp = open('58.text','w',encoding='utf-8')
time.sleep(0.3)
for li in li_list:
    title = li.xpath('./a/div[2]/div/div/h3/text()')[0]
    size = li.xpath('./a/div[2]/div/section/div/p[2]/text()')[0]
    print(title,)
    fp.write(title+'\n')

