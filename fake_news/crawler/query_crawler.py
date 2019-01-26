from newspaper import Article
from newsapi import NewsApiClient
import requests

class Crawler:
    """
    This class contains all the methods to extract the content from the given link
    """

    def __init__(self,URL):
        """
        This method initializes the URL in the class

        :type URL: string
        :param URL: The URL of the Website
        """
        self.URL = URL

        try:
            article = Article(self.URL)
        except Exception as exception:
            print("There was a problem while initializing the article object: {}".format(exception))
        
        try:
            article.download()
        except Exception as exception:
            print("There was a problem while downloading the article: {}".format(exception))

        try:
            article.parse()
        except Exception as exception:
            print("There was a problem while parsing the article: {}".format(exception))
        

    def get_title(self):
        """
        This method returns the title from the given URL 
        """
        
        











        

