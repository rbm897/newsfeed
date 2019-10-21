from flask import Flask, render_template, request
from timeloop import Timeloop
from datetime import timedelta
import requests
app = Flask(__name__)

pages = 0
page = 0
prevCategory = '''https://newsapi.org/v2/top-headlines?country=in&language=en
&category=business&category=entertainment&category=general
&category=health&category=science&category=sports&category=technology
&pageSize=20&apiKey=888fa0f55948429f8ec40e15d69cf9a0'''
@app.route('/',methods = ['GET','POST'])
def news_feed():
    api_url = 'https://newsapi.org/v2/top-headlines'
    PARAMS = {
                'country':'in',
                'language':'en',
                'category':'business',
                'category':'entertainment',
                'category':'general',
                'category':'health',
                'category':'science',
                'category':'sports',
                'category':'technology',
                'pageSize':'20',
                'apiKey':'888fa0f55948429f8ec40e15d69cf9a0'}
    r = requests.get(url = api_url, params = PARAMS)
    global pages
    global page
    page=0
    pages = r.json().get("totalResults") / 20
    temp = r.json()
    if temp is None:
        temp['articles'] = []
    return render_template("News_feed.html",name = temp)


@app.route('/category',methods = ['GET','POST'])
def category():
    global page
    global prevCategory
    
    category = request.form['category']
    if category is not None and category != '':
        prevCategory = category
    if request.form['refresh'] == 'True':
        api_url = 'https://newsapi.org/v2/top-headlines?' + prevCategory
        res = requests.get(url = api_url)
        if page >= 4 :
            page = 0
        else:
            page = page + 1
        api_url = 'https://newsapi.org/v2/top-headlines?' + prevCategory + '&page=' + str(page)
    else:
        page = 0
        api_url = 'https://newsapi.org/v2/top-headlines?' + category + '&page=' + str(page)
    
    r = requests.get(url = api_url)
    temp = r.json()
    if temp is None:
        temp['articles'] = []
    return render_template("News_feed.html",name = temp)

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0')

