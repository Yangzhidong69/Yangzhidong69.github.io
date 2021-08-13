# Yangzhidong69.github.io
#生成词云图片
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import pymysql
#准备词云数据
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    db='jobsan',
    charset='utf8'
)
sql = 'SELECT job_welfare from works where job_welfare is not null'
cursor = conn.cursor()
#执行sql
cursor.execute(sql)
#采集数据量
result = cursor.fetchall()
text = ""
for item in result:
    text = text+item[0]
    #print(text)
cursor.close()
conn.close()
#分词
cut = jieba.cut(text)
string = ''.join(cut)
#print(string)
print(len(string))
#导入需要遮罩的图片
img = Image.open(r'./static/assets/img/leaf.jpg')
img_array = np.array(img)
#词云参数
wc = WordCloud(
    mask=img_array,
    background_color='white',
    # 报错为：OSError: cannot open resource意思就是电脑没有字体，换一种就是了
    font_path = "C:\Windows\Fonts\Deng.ttf",
)
wc.generate_from_text(string)
fig = plt.figure(1)
# plt.rcParams["figure.figsize"] = (6.0,4.0)#设置figure_size尺寸
plt.imshow(wc)
plt.axis('off')
# plt.show()
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)
