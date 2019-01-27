from newspaper import Article
from newsapi import NewsApiClient
import requests
import json

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
    def __init__(self,API_Key,keyword_list):
        """
        This method inititalizes the news api and also takes in a list of keywords as the argument and applies AND operation between them and queries it 
        and stores it in the variable response

        :type keyword_list: list
        :param keyword_list: list of keywords to query the api
        """

        #initialize news client with the api key
        self.news_api = NewsApiClient(api_key=API_Key)

        # the sting to be appended in the middle
        AND = " AND "
        
        # add AND in between the keywords in the list
        query_string = AND.join(keyword_list)

        # initialize an empty list of titles
        self.title_list = []

        # initialize an empty list of meta descriptions
        self.descriptions_list = []

        # initialize an empty list of Urls
        self.Urls_list = []

        # query the api
        response = self.news_api.get_everything(q=query_string)

        # if the size of list_of_URLs is more then 5 set parse_length to 5 else according to its size
        parse_length = 5  if len(response['articles']) >= 5 else len(response['articles'][0])

        # for each article returned get the corresponding URL and append it to list_of_URLs
        for item in range(parse_length):

            # append every title to title list
            self.title_list.append(response["articles"][item]["title"])

            # append every description to description_list
            self.descriptions_list.append(response["articles"][item]["description"])

            # append every Urls to Urls_list
            self.Urls_list.append(response["articles"][item]["url"])



    def get_URLs(self):
        """
        This method returns a maximum of 5 news Urls to extract content from (list)
        """
        return self.Urls_list

    def get_titles(self):
        """
        This method returns a maximum of 5 news titles (list)
        """
        return self.title_list

    def get_descriptions(self):
        """
        This method returns a maximum of 5 descriptions (list)
        """
        return self.descriptions_list
        







                
        











        

