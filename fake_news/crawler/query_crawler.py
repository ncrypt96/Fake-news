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

        # initialize an object from the Article class and provide the URL in the constructor  
        try:
            self.article = Article(self.URL)
        except Exception as exception:
            print("There was a problem while initializing the article object: {}".format(exception))
        
        # download and parse
        try:
            self.article.download()
        except Exception as exception:
            print("There was a problem while downloading the article: {}".format(exception))

        try:
            self.article.parse()
        except Exception as exception:
            print("There was a problem while parsing the article: {}".format(exception))
        

    def get_title(self):
        """
        This method returns the title of the article (str)
        """
        return self.article.title

    def get_content(self):
        """
        This method returns the content from the article (str)
        """
        return self.article.text

    def get_meta_keywords(self):
        """
        This method returns the list of the meta keywords in the page (list)
        """
        return self.article.meta_keywords

    def get_meta_description(self):
        """
        This method returns the list of the meta keywords in the page (str)
        """
        return self.article.meta_description
                
        











        

