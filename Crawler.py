#抓取網頁原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立request物件，附加headers資訊
request=req.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)    

#解析
import bs4
root=bs4.BeautifulSoup(data,"html.parser")#用beautifulsoup解析html
#print(root.title.string)"標籤"裡的"文字"
titles=root.find_all("div",class_="title")#尋找"所有(all)" class=title的div標籤
#print(titles)抓到所有標籤，輸出列表
for title in titles:
    if title.a !=None:  #如果有a(不是"已刪除文章")
        print(title.a.string)