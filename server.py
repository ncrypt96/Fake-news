from abstractor import with_keywords,without_keywords
from abstractor2 import with_keywords,without_keywords
from flask import Flask , jsonify,request


app = Flask(__name__)

@app.route('/api/without',methods=['GET','POST'])
def without_k():

    if(request.method =='POST'):

        url = request.get_json()['users_link']

        return jsonify(without_keywords(url,"3689abcc32e2468abb4eed31af2115c0"))


@app.route('/api/with',methods=['GET', 'POST'])
def with_k():

    if(request.method == 'POST'):

        url_and_keywords = request.get_json()

        url = url_and_keywords['users_link']

        keywords = url_and_keywords['keywords']


        return jsonify(with_keywords(url,keywords,"3689abcc32e2468abb4eed31af2115c0"))


if (__name__ =="__main__"):

    app.run()