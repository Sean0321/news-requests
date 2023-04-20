import tkinter as tk
import requests
import datetime
from bs4 import BeautifulSoup

def showTime():
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')  # 取得目前的時間，格式使用 H:M:S
    a.set(now)                    # 設定變數內容
    win.after(1000,showTime)    # 視窗每隔 1000 毫秒再次執行一次 showTime()

def _hit1():
    if val.get() == '1':##自由時報
        urL="https://news.ltn.com.tw/list/breakingnews/"
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")        
        soupS=souP.find("ul","list")            
        for mySoup in soupS.find_all("li"):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a["title"].strip())
                listbox.insert(tk.END,mySoup.a["href"].strip())
                listbox.insert(tk.END,"-"*90)
            except:
                continue
    
    elif val.get() == '2':##聯合新聞網
        urL='https://udn.com/news/breaknews/1'
        q1 = requests.get(urL).text
        bs1 = BeautifulSoup(q1,'html5lib')
        soups = bs1.find('div','context-box__content story-list__holder story-list__holder--full')
        for data in soups.find_all('div','story-list__news'):
            try:
                listbox.insert(tk.END,data.h2.a.text.strip())
                listbox.insert(tk.END,'https://udn.com'+data.p.a['href'].strip())
                listbox.insert(tk.END,data.find('time','story-list__time').text)
                listbox.insert(tk.END,'-'*90)
            except:
                continue
            
    elif val.get() == '3':##ETtoday
        urL='https://www.ettoday.net/news/focus/%E7%84%A6%E9%BB%9E%E6%96%B0%E8%81%9E/'
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")
        soupS=souP.find('div','block_content')        
        for mySoup in soupS.find_all('div','piece clearfix'):
            try:
                listbox.insert(tk.END,mySoup.find('h3').a.text.strip())
                listbox.insert(tk.END,'https://www.ettoday.net'+mySoup.find('h3').a['href'])
                listbox.insert(tk.END,"-"*90)
            except:
                continue
            
def _hit2():
    if val.get() == '1':##自由時報
        urL="https://news.ltn.com.tw/list/breakingnews/popular"
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")        
        soupS=souP.find("ul","list")            
        for mySoup in soupS.find_all("li"):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a["title"].strip())
                listbox.insert(tk.END,mySoup.a["href"].strip())
                listbox.insert(tk.END,"-"*90)
            except:
                continue
    
    elif val.get() == '2':##聯合新聞網
        listbox.insert(tk.END,'聯合新聞無 【熱門】 新聞版面...')
            
    elif val.get() == '3':##ETtoday
        urL='https://www.ettoday.net/news/hot-news.htm'
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")
        soupS=souP.find('div','block_content')        
        for mySoup in soupS.find_all('div','piece clearfix'):
            try:
                listbox.insert(tk.END,mySoup.find('h3').a.text.strip())
                listbox.insert(tk.END,'https://www.ettoday.net'+mySoup.find('h3').a['href'])
                listbox.insert(tk.END,"-"*90)
            except:
                continue
            
        
def _hit3():
    if val.get() == '1':##自由時報
        urL="https://news.ltn.com.tw/list/breakingnews/politics"
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")        
        soupS=souP.find("ul","list")            
        for mySoup in soupS.find_all("li"):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a["title"].strip())
                listbox.insert(tk.END,mySoup.a["href"].strip())
                listbox.insert(tk.END,"-"*90)
            except:
                continue
    
    elif val.get() == '2':##聯合新聞網
        urL='https://udn.com/news/cate/2/6638'
        q1 = requests.get(urL).text
        bs1 = BeautifulSoup(q1,'html5lib')
        soups = bs1.find('div','context-box__content story-list__holder story-list__holder--full')
        for data in soups.find_all('div','story-list__news'):
            try:
                listbox.insert(tk.END,data.h2.a.text.strip())
                listbox.insert(tk.END,'https://udn.com'+data.p.a['href'].strip())
                listbox.insert(tk.END,data.find('time','story-list__time').text)
                listbox.insert(tk.END,'-'*90)
            except:
                continue
            
    elif val.get() == '3':##ETtoday
        urL='https://www.ettoday.net/news/news-list-'+y[0]+'-1.htm'
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")
        soupS=souP.find('div','part_list_2')        
        for mySoup in soupS.find_all('h3'):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a.text.strip())
                listbox.insert(tk.END,'https://www.ettoday.net'+mySoup.a['href'])
                listbox.insert(tk.END,"-"*90)
            except:
                continue

def _hit4():
    if val.get() == '1':##自由時報
        urL="https://news.ltn.com.tw/list/breakingnews/society"
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")        
        soupS=souP.find("ul","list")            
        for mySoup in soupS.find_all("li"):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a["title"].strip())
                listbox.insert(tk.END,mySoup.a["href"].strip())
                listbox.insert(tk.END,"-"*90)
            except:
                continue
    
    elif val.get() == '2':##聯合新聞網
        urL='https://udn.com/news/cate/2/6639'
        q1 = requests.get(urL).text
        bs1 = BeautifulSoup(q1,'html5lib')
        soups = bs1.find('div','context-box__content story-list__holder story-list__holder--full')
        for data in soups.find_all('div','story-list__news'):
            try:
                listbox.insert(tk.END,data.h2.a.text.strip())
                listbox.insert(tk.END,'https://udn.com'+data.p.a['href'].strip())
                listbox.insert(tk.END,data.find('time','story-list__time').text)
                listbox.insert(tk.END,'-'*90)
            except:
                continue
            
    elif val.get() == '3':##ETtoday
        urL='https://www.ettoday.net/news/news-list-'+y[0]+'-6.htm'
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")
        soupS=souP.find('div','part_list_2')        
        for mySoup in soupS.find_all('h3'):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a.text.strip())
                listbox.insert(tk.END,'https://www.ettoday.net'+mySoup.a['href'])
                listbox.insert(tk.END,"-"*90)
            except:
                continue

def _hit5():
    if val.get() == '1':##自由時報
        urL="https://news.ltn.com.tw/list/breakingnews/life"
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")        
        soupS=souP.find("ul","list")            
        for mySoup in soupS.find_all("li"):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a["title"].strip())
                listbox.insert(tk.END,mySoup.a["href"].strip())
                listbox.insert(tk.END,"-"*90)
            except:
                continue
    
    elif val.get() == '2':##聯合新聞網
        urL='https://udn.com/news/cate/2/6649'
        q1 = requests.get(urL).text
        bs1 = BeautifulSoup(q1,'html5lib')
        soups = bs1.find('div','context-box__content story-list__holder story-list__holder--full')
        for data in soups.find_all('div','story-list__news'):
            try:
                listbox.insert(tk.END,data.h2.a.text.strip())
                listbox.insert(tk.END,'https://udn.com'+data.p.a['href'].strip())
                listbox.insert(tk.END,data.find('time','story-list__time').text)
                listbox.insert(tk.END,'-'*90)
            except:
                continue
    elif val.get() == '3':##ETtoday        
        urL='https://www.ettoday.net/news/news-list-'+y[0]+'-5.htm'
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")
        soupS=souP.find('div','part_list_2')        
        for mySoup in soupS.find_all('h3'):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a.text.strip())
                listbox.insert(tk.END,'https://www.ettoday.net'+mySoup.a['href'])
                listbox.insert(tk.END,"-"*90)
            except:
                continue

def _hit6():
    if val.get() == '1':##自由時報
        urL="https://news.ltn.com.tw/list/breakingnews/world"
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")        
        soupS=souP.find("ul","list")            
        for mySoup in soupS.find_all("li"):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a["title"].strip())
                listbox.insert(tk.END,mySoup.a["href"].strip())
                listbox.insert(tk.END,"-"*90)
            except:
                continue
    
    elif val.get() == '2':##聯合新聞網
        urL='https://udn.com/news/cate/2/7225'
        q1 = requests.get(urL).text
        bs1 = BeautifulSoup(q1,'html5lib')
        soups = bs1.find('div','context-box__content story-list__holder story-list__holder--full')
        for data in soups.find_all('div','story-list__news'):
            try:
                listbox.insert(tk.END,data.h2.a.text.strip())
                listbox.insert(tk.END,'https://udn.com'+data.p.a['href'].strip())
                listbox.insert(tk.END,data.find('time','story-list__time').text)
                listbox.insert(tk.END,'-'*90)
            except:
                continue
            
    elif val.get() == '3':##ETtoday
        urL='https://www.ettoday.net/news/news-list-'+y[0]+'-2.htm'
        rQ=requests.get(urL).text
        souP=BeautifulSoup(rQ,"html5lib")
        soupS=souP.find('div','part_list_2')        
        for mySoup in soupS.find_all('h3'):
            try:
                listbox.insert(tk.END,mySoup.span.text.strip())
                listbox.insert(tk.END,mySoup.a.text.strip())
                listbox.insert(tk.END,'https://www.ettoday.net'+mySoup.a['href'])
                listbox.insert(tk.END,"-"*90)
            except:
                continue

def _hit7():
    listbox.delete(0,tk.END)
#------------------------------------------------------------#
win = tk.Tk()
win.title('新聞搜尋')
win.iconbitmap('012.ico')
win.geometry('800x500+500+300')
win.resizable(False,False)
#------------------------------------------------------------#
GMT = datetime.timezone(datetime.timedelta(hours=8))
a = tk.StringVar()
#------------------------------------------------------------#
val = tk.StringVar()
val.set(0)
#------------------------------------------------------------#
x = datetime.datetime.today()
y=str(x).split(' ')


#------------------------------------------------------------#
f1 = tk.Frame(win) #,width=550,height=300,bg='#daa520'
f1.pack(side='left',fill='y')#top

f2 = tk.Frame(win,bg='#4682b4',width=300) #,width=530,height=600
f2.pack(side='bottom',expand=1,fill='both')#right

f3 = tk.Frame(win,bg='#3cb371')
f3.pack(side='top',expand=1,fill='both')
#------------------------------------------------------------#
btn1 = tk.Radiobutton(f2,text='自由時報',relief='solid',
                font=('微軟正黑體 Light',15,'bold'),variable=val,value=1)
btn1.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

btn2 = tk.Radiobutton(f2,text='聯合新聞',relief='solid',
                font=('微軟正黑體 Light',15,'bold'),variable=val,value=2)
btn2.grid(row=1,column=0,padx=10,pady=10,columnspan=2)

btn3 = tk.Radiobutton(f2,text='ETtoday',relief='solid',
                font=('微軟正黑體 Light',15,'bold'),variable=val,value=3)
btn3.grid(row=3,column=0,padx=10,pady=10,columnspan=2)
#------------------------------------------------------------#
btn4 = tk.Button(f2,text='焦點',relief='solid',command=lambda:_hit1(), ##因為command函數帶有參數,故前面加lambda:解決
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn4.grid(row=4,column=0,padx=7,pady=10)

btn5 = tk.Button(f2,text='熱門',relief='solid',command=lambda:_hit2(),
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn5.grid(row=4,column=1,padx=7,pady=10)

btn6 = tk.Button(f2,text='政治',relief='solid',command=lambda:_hit3(),
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn6.grid(row=5,column=0,padx=7,pady=10)

btn7 = tk.Button(f2,text='社會',relief='solid',command=lambda:_hit4(),
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn7.grid(row=5,column=1,padx=7,pady=10)

btn8 = tk.Button(f2,text='生活',relief='solid',command=lambda:_hit5(),
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn8.grid(row=6,column=0,padx=7,pady=10)

btn9 = tk.Button(f2,text='國際',relief='solid',command=lambda:_hit6(),
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn9.grid(row=6,column=1,padx=7,pady=10)

btn10 = tk.Button(f2,text='清除',relief='solid',command=lambda:_hit7(),
                font=('微軟正黑體 Light',15,'bold'),
                activeforeground='#a9a9a9')
btn10.grid(row=7,column=0,padx=10,pady=10,columnspan=2)
#------------------------------------------------------------#
sbar = tk.Scrollbar(f1)
sbar.pack(side='right',fill='y')

listbox = tk.Listbox(f1,font=('微軟正黑體 Light',10),width=90,height=80,yscrollcommand = sbar.set)
listbox.pack()
sbar.config(command = listbox.yview)
#------------------------------------------------------------#
tk.Label(f3,text='現在時間',font=('微軟正黑體 Light',15,'bold'),bg='#3cb371').pack()
tk.Label(f3,textvariable=a,font=('微軟正黑體 Light',24,'bold'),bg='#3cb371').pack()

showTime()

#print(font.families())

win.mainloop()

