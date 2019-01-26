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


class NewsApiHandle:

    """
    This class contains methods to handle everything related to the use of news api
    """
    def __init__(self,API_Key):
        """
        This method inititalizes the news api
        """

        #initialize news client with the api key
        self.news_api = NewsApiClient(api_key=API_Key)

    def request_news_URLs(self,keyword_list):

        """
        This method takes in a list of keywords as the argument and applies AND operation between them and queries it 
        with the help of news api and returns a maximum of 5 related Urls (list)

        :type keyword_list: list
        :param keyword_list: list of keywords to query the api
        """

        # the sting to be appended in the middle
        AND = " AND "

        # initialize an empty list which will hold the URLs
        list_of_URLs =[]
        
        # add AND in between the keywords in the list
        query_string = AND.join(keyword_list)

        # query the api
        all_articles = self.news_api.get_everything(q=query_string)

        # get the number of articles given by the api
        # for each article returned get the corresponding URL and append it to list_of_URLs
        # if the size of list_of_URLs is more than 5 break the loop and return the URLs
        for i in range(0,len(all_articles['articles'])):
            list_of_URLs.append(all_articles["articles"][i]["url"])

            if len(all_articles) > 5:
                break

        return list_of_URLs





                
        











        

