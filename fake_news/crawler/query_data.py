from fake_news.crawler.query_crawler import Crawler,NewsApiHandle,ContentCrawler
from fake_news.preprocessor.keywords_check import KeyWordCheck
from fake_news.preprocessor.error_handle import highlight_fore,highlight_back

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

        :type keyword_extraction_algo: string
        :param keyword_extraction_algo : The algorithm to be used to extract the keywords
        """
        # initialize NewApi object
        
        
        # get data from the user provided link
        user_news_content = self.user_news_crawler.get_content()

        user_news_title  = self.user_news_crawler.get_title()

        user_news_meta_keywords = self.user_news_crawler.get_meta_keywords()

        user_news_meta_description = self.user_news_crawler.get_meta_description()

        #--------------------------------------------------
        print("from query_data.py")
        print(user_news_meta_keywords)
        print(user_news_meta_description)
        print(user_news_title)
        print("from query_data.py")
        #---------------------------------------------------
        #-------------keyword processing START--------------

        # initialize an empty list 
        keywords = []
        # use to get unique kewords to query the api
        keywords_manager = KeyWordCheck()

        intermediate_keywords = user_news_meta_keywords

        # for named enitities as keywords
        eir_keywords = []

        if(len(intermediate_keywords)<=3):
            # assign meta keywords to keywords
            keywords = intermediate_keywords
            print("here 1")
        elif(len(intermediate_keywords)==4):
            # pop the last element from the list
            intermediate_keywords.pop(-1)
            keywords = intermediate_keywords
            print("here 2")            
        elif(len(intermediate_keywords)==5):
            intermediate_keywords.pop(-1)
            intermediate_keywords.pop(-1)
            keywords = intermediate_keywords
            print("here 3")
        else:
            # lower case the meta keywords and sort them according to their length
            intermediate_keywords = keywords_manager.keyword_formatter(intermediate_keywords)
            # reduce the number of keywords 
            intermediate_keywords = keywords_manager.keyword_reducer(intermediate_keywords)
            # remove irrevelent keywords which are put for seo purposes
            intermediate_keywords = keywords_manager.remove_irrelevant_keywords(intermediate_keywords)
            # check if now keywords are less than or equal to 4
            if(len(intermediate_keywords)<=3):
                keywords = intermediate_keywords
                print("here 4")
            elif(len(intermediate_keywords)==4):
                intermediate_keywords.pop(-1)
                keywords = intermediate_keywords
                print("here 5")
            elif(len(intermediate_keywords)==5):
                intermediate_keywords.pop(-1)
                intermediate_keywords.pop(-1)
                keywords = intermediate_keywords
                print("here 6")
            else:
                # import named entities from the description and the title as keywords
                eir_keywords = keywords_manager.eir_keywords(user_news_meta_description) + keywords_manager.eir_keywords(user_news_title)
                # lower case and sort
                print(eir_keywords)
                eir_keywords = keywords_manager.keyword_formatter(eir_keywords)
                print(eir_keywords)
                # reduce smilar keywords
                eir_keywords = keywords_manager.keyword_reducer(eir_keywords)
                print(eir_keywords)
                # remove irrelevent
                eir_keywords = keywords_manager.remove_irrelevant_keywords(eir_keywords)
                print("here 7")
                print(eir_keywords)
                # check if there are more than one keywords but less than 3
                if(len(eir_keywords)>1 and len(eir_keywords)<=3):
                    keywords = eir_keywords
                    print("here 8")
                elif(len(eir_keywords)==4):
                    eir_keywords.pop(-1)
                    keywords = eir_keywords
                    print("here 9")
                elif(len(eir_keywords)==5):
                    eir_keywords.pop(-1)
                    eir_keywords.pop(-1)
                    keywords = eir_keywords
                    print("here 10")
                else:
                    # perform intersection between named entities and meta keywords
                    keywords = keywords_manager.eir_intersection_reduction(user_news_meta_description,user_news_meta_keywords)
                    print("here 11")
                    if(len(keywords)<=1):
                        print("here 12")
                        highlight_back("There was a problem while extracting the keywords",'R')
                        highlight_fore("Please input unique keywords relevent to the article separated by ','","B")
                        highlight_fore("Suggested Keywords: ",'Y')
                        highlight_fore(list(set(intermediate_keywords+eir_keywords)),'G')
                        # get keywords from the user
                        keywords = input().split(',')

        #-------------keyword processing END--------------
        print(keywords)

        #--------------------News api related stuff START--------------------

        #initialize empty list for the content
        api_news_contents = []
        
        # initialize the client with an api key
        api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords) 

        api_news_titles = api_news_handler.get_titles()

        api_news_Urls = api_news_handler.get_URLs()

        api_news_descriptons = api_news_handler.get_descriptions()

        all_news_sources = api_news_handler.get_sources()

        # get only the content from the given Urls
        api_news_crawler = ContentCrawler()

        for url in api_news_Urls:

            api_news_contents.append(api_news_crawler.extract_content(url))
        

        all_news_titles = api_news_titles

        all_news_descriptions = api_news_descriptons

        all_news_content = api_news_contents

        #--------------------News api related stuff END--------------------

        # insert the information from the user at the first of the index
        all_news_titles.insert(0,user_news_title)

        all_news_descriptions.insert(0,user_news_meta_description)

        all_news_content.insert(0,user_news_content)



        # return all data as dictionary and later can be converted into a json object
        return {"all":[all_news_sources,all_news_titles,all_news_descriptions,all_news_content],"sources":all_news_sources,"titles":all_news_titles,"descriptons":all_news_descriptions,"contents":all_news_content}



        
        

        