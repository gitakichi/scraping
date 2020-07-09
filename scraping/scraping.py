import requests
from bs4 import BeautifulSoup


load_url = "http://opinion.people.com.cn/GB/8213/49160/49217/index.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

for news_list in soup.find_all(class_="abl"):    # すべてのxxタグを検索して表示
    detail_url = load_url+news_list.get('href')
    
    html = requests.get(detail_url)
    detail = BeautifulSoup(html.content, "html.parser",from_encoding="gb18030")
    con = detail.find(class_="box_con")

    det = 0
    for element in con.find_all("p"):
        #if '习近平总书记强调：' in element.text:
        if '强调：' in element.text:
            if det == 0:#初回だけニュースタイトル、発行日を表示
                print(news_list.text)   
                #print(detail.find(id="paper_num").text)
                print(detail.find(class_="box01").find(class_="fl").text[:16])
                det = 1;
            print(element.text[1:] + "\n")#必ず改行が入るので取り除く
    if det == 1:
        print(detail.find(class_="edit clearfix").text + "\n")
        

#reference
#https://codezine.jp/article/detail/12230
#https://tonari-it.com/python-html-get-text-attr/#toc8