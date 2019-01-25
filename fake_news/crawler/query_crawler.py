from newspaper import Article
from urllib.parse import urlparse
from newsapi import NewsApiClient
import requests

class Crawler:

    def check_if_website_exists(self,URL):

        try:

            requests = requests.get(URL)

        except Exception as exception:

            print(exception)

            raise 










        

