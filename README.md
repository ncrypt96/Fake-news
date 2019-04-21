
  

# Welcome to Fake news

  

  

This project aims to detect **Fake news**

We take the URL from the user-> Extract Keywords->Crawl the web for related articles->Comapre the similarity with each article

# Installation

  
> git clone https://github.com/ncrypt96/Fake-news.git<br>
> cd Fake-news<br>
> pip install -r requirements.txt

### Also

> import nltk<br>
> nltk.download('punkt')<br>
> nltk.download('stopwords')<br>
> nltk.download('averaged_perceptron_tagger')<br>
> nltk.download('wordnet')<br>

  

## Usage
### Go to https://newsapi.org/ and get the **free API key** under the Developer Plan
#### make a python file inside the cloned folder Fake-news<br>
#### for example some_file.py
#### now run python3 some_file.py with the following code in it
## Set a thershold value to the score returned for classification
### the reccomended threshold is **0.4**

  

  

```python
from abstractor2 import with_keywords,without_keywords

print("Enter the URL")

url = input()

results = without_keywords(url,"<YOUR API KEY HERE>")

if(results["status"]=="fail"):

    print("Enter the keywords seperated by ',' \n")
    print("Suggested keywords:")
    print(results["suggestions"])

    keywords = input().split(',')

    print(keywords)


    print(with_keywords(url,keywords,"<YOUR API KEY HERE>")["similarity"])

else:

    print(results["similarity"])

``` 

  

