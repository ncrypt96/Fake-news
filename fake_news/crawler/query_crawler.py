from newsapi.newsapi_client import NewsApiClient
import requests
import json
from newsplease import NewsPlease
from goose3 import Goose
import lassie
from fake_news.preprocessor.error_handle import highlight_back , line_loc

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
            
            # initialize Goose
            goose = Goose()

            # initialize the goose article object
            goose_article = goose.extract(self.URL)

            # assign title
            self.title = goose_article.title

            # assign content
            self.content = goose_article.cleaned_text

            # assign meta keywords (str) and split it to form a list
            self.meta_keywords = goose_article.meta_keywords.split(',')

            # assign meta description
            self.meta_description = goose_article.meta_description

        except Exception as exception:
            
            highlight_back("[Crawler] Crawler migrated from Goose to News-Please and Lassie due to an exception: {}".format(exception),'G')
            line_loc()
            
            try:
            
                # initialize news please object
                news_please_article = NewsPlease.from_url(self.URL)

                # set title
                self.title = news_please_article.title

                # set content
                self.content = news_please_article.text

                # set meta keywords
                self.meta_keywords = lassie.fetch(self.URL)["keywords"]

                # set meta description
                self.meta_description = news_please_article.description
            
            except Exception as exception:

                highlight_back("[Crawler] An exception has occured in News Please and Lassie method: {}".format(exception),'R')
                line_loc()
      

    def get_title(self):
        """
        This method returns the title of the article (str)
        """
        return self.title

    def get_content(self):
        """
        This method returns the content from the article (str)
        """
        return self.content

    def get_meta_keywords(self):
        """
        This method returns the list of the meta keywords in the page (list)
        """
        return self.meta_keywords

    def get_meta_description(self):
        """
        This method returns the list of the meta keywords in the page (str)
        """
        return self.meta_description

class ContentCrawler:
    """
    This class contains methods that crawls only the content from the given link
    """

    def extract_content(self,URL):
        """
        This method returns the main content from the given URL
        """
        try:
            # Extract content
            content = Goose().extract(URL).cleaned_text
        except Exception as exception:
            highlight_back("[ContentCrawler] Crawler migrated from Goose to News-Please due to an exception: {}".format(exception),'G')

            try:
                # Extract content usinf NewsPleas
                content = NewsPlease.from_url(URL).text
            except Exception as exception:
                highlight_back("[ContentCrawler] An exception has occured in News Please and Lassie method: {}".format(exception),'R')

        return content



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

        # initialize an empty list of sources
        self.sources_list = []

        # query the api
        response = self.news_api.get_everything(q=query_string,sort_by='relevancy')

        # if the size of list_of_URLs is more then 5 set parse_length to 5 else according to its size
        parse_length = 5  if len(response['articles']) >= 5 else len(response['articles'])

        # for each article returned get the corresponding URL and append it to list_of_URLs
        for item in range(parse_length):

            # append every title to title list
            self.title_list.append(response["articles"][item]["title"])

            # append every description to description_list
            self.descriptions_list.append(response["articles"][item]["description"])

            # append every Urls to Urls_list
            self.Urls_list.append(response["articles"][item]["url"])

            # append every source to source list
            self.sources_list.append(response["articles"][item]['source']['name'])



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
        
    def get_sources(self):
        """
        This method returns the source of 
        """
        return self.sources_list







                
        











        

