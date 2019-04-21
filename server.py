from fake_news.preprocessor.error_handle import line_loc,highlight_back
from abstractor2 import with_keywords,without_keywords
from flask import Flask , jsonify,request


API_KEY =""

if(len(API_KEY)<=1):
    highlight_back("ENTER YOUR API KEY ABOVE ON LINE 6 OF THIS FILE","R")
    line_loc()


app = Flask(__name__)

@app.route('/api/without',methods=['GET','POST'])
def without_k():

    if(request.method =='POST'):

        url = request.get_json()['users_link']

        return jsonify(without_keywords(url,API_KEY))


@app.route('/api/with',methods=['GET', 'POST'])
def with_k():

    if(request.method == 'POST'):

        url_and_keywords = request.get_json()

        url = url_and_keywords['users_link']

        keywords = url_and_keywords['keywords']


        return jsonify(with_keywords(url,keywords,API_KEY))


if (__name__ =="__main__"):

    app.run()