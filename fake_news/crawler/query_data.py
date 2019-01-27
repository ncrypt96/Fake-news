from fake_news.crawler.query_crawler import Crawler,NewsApiHandle
from fake_news.preprocessor.keywords_check import KeyWordCheck

class Data:
    """
    This class contains all the methods to get data from various other classes
    """
    def __init__(self,URL):

        self.URL = URL
        self.user_news_crawler = Crawler(URL)
        
    def get_all_data(self):
        
        user_news_content = self.user_news_crawler.get_content()

        user_news_title  = self.user_news_crawler.get_title()

        user_news_meta_keywords = self.user_news_crawler.get_meta_keywords()

        user_news_meta_description = self.user_news_crawler.get_meta_description()

        keywords_manager = KeyWordCheck()

        keywords = keywords_manager.eir_reduction(user_news_meta_description,user_news_meta_keywords)


        # News api related stuff

        api_news_contents = []
               
        api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords) 

        api_news_titles = api_news_handler.get_titles()

        api_news_Urls = api_news_handler.get_URLs()

        api_news_descriptons = api_news_handler.get_descriptions()

        for url in api_news_Urls:

            api_news_crawler = Crawler(url)

            api_news_contents.append(api_news_crawler.get_content())
        

        all_news_titles = api_news_titles

        all_news_descriptions = api_news_descriptons

        all_news_content = api_news_contents

        all_news_titles.insert(0,user_news_title)

        all_news_descriptions.insert(0,user_news_meta_description)

        all_news_content.insert(0,user_news_content)

        return {"all":[all_news_titles,all_news_descriptions,all_news_content],"titles":all_news_titles,"descriptons":all_news_descriptions,"contents":all_news_content}



        
        

        