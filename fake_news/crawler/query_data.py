from fake_news.crawler.query_crawler import Crawler,NewsApiHandle
from fake_news.preprocessor.keywords_check import KeyWordCheck

class Data:
    """
    This class contains all the methods to get data from various other classes
    """
    def __init__(self,URL):
        """
        This method is used to initialize self.URL
        :type URL: string
        :param URL: Url of thr website
        """
        # Initialize the variables
        self.URL = URL
        self.user_news_crawler = Crawler(URL)
        
    def get_all_data(self):
        """
        This method returns all the data in the form of a python dictionary which can be converted inti json
        passing the parameter ['all'] in the returns all of the information
        passing the parameters like ['titles'], ['descriptions'], ['contents'] return that specific data
        """
        
        # get data from the user provided link
        user_news_content = self.user_news_crawler.get_content()

        user_news_title  = self.user_news_crawler.get_title()

        user_news_meta_keywords = self.user_news_crawler.get_meta_keywords()

        user_news_meta_description = self.user_news_crawler.get_meta_description()

        #--------------------------------------------------
        print("from query_data.py")
        print(user_news_meta_keywords)
        print(user_news_meta_description)
        print("from query_data.py")
        #---------------------------------------------------

        # use to get unique kewords to query the api
        keywords_manager = KeyWordCheck()

        # returns a list of unique keywords
        keywords = keywords_manager.eir_intersection_reduction(user_news_meta_description,user_news_meta_keywords)


        # News api related stuff

        #initialize empty list for the content
        api_news_contents = []
        
        # initialize the client with an api key
        api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords) 

        api_news_titles = api_news_handler.get_titles()

        api_news_Urls = api_news_handler.get_URLs()

        api_news_descriptons = api_news_handler.get_descriptions()

        # get all the contents from the given Url
        for url in api_news_Urls:

            api_news_crawler = Crawler(url)

            api_news_contents.append(api_news_crawler.get_content())
        

        all_news_titles = api_news_titles

        all_news_descriptions = api_news_descriptons

        all_news_content = api_news_contents

        # insert the information from the user at the first of the index
        all_news_titles.insert(0,user_news_title)

        all_news_descriptions.insert(0,user_news_meta_description)

        all_news_content.insert(0,user_news_content)

        # return all data as dictionary and later can be converted into a json object
        return {"all":[all_news_titles,all_news_descriptions,all_news_content],"titles":all_news_titles,"descriptons":all_news_descriptions,"contents":all_news_content}



        
        

        