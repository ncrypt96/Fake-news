from fake_news.crawler.query_crawler import Crawler,NewsApiHandle,ContentCrawler
from fake_news.preprocessor.keywords_check import KeyWordCheck
from fake_news.preprocessor.error_handle import highlight_fore,highlight_back,line_loc
from fake_news.preprocessor.nlp_preprocessor import NlpPreprocessing

class Data:
    """
    This class contains all the methods to get data from various other classes
    """

    def get_user_data(self,URL):
        """
        This method returns the data from the users link
        :type URL: string
        :param URL: The Url of the website

        returns a dictionary with keys all, title,description, content , meta_keywords ,top_img_URL,users_link
        """
        # initialize the crawler for crawling the news form the users URL
        user_Crawler = Crawler(URL)

        # get title
        title = user_Crawler.get_title()

        # get description
        description = user_Crawler.get_meta_description()

        # get content
        content = user_Crawler.get_content()

        # get all the meta_ keywords
        meta_keywords = user_Crawler.get_meta_keywords()

        # get top image
        top_img_URL = user_Crawler.get_top_image_URL()

        return {"title":title,"description":description,"content":content,"meta_keywords":meta_keywords,"top_img_URL": top_img_URL,"users_link":URL}


    def get_data_wo_user_help(self,user_link_data,no_of_keywords=6):
        """
        This method returns all data without the user giving the keywords

        :type user_link_data: dict
        :param user_link_data: the data retreived from the users link including titlesc contents etc

        :type no_of_keywords: int
        :param no_of_keywords: the number of keywords for AND operation

        """
        # if true let the user enter the keywords
        ask_keywords_from_user = False

        # get title from the users link
        user_link_title = user_link_data['title']

        # get description from the users link
        user_link_description = user_link_data['description']

        # get the content from users link
        user_link_content = user_link_data['content']

        # get the meta keywords
        user_link_meta_keywords  = user_link_data['meta_keywords']

        # link to the top image
        user_link_top_img_url = user_link_data['top_img_URL']

        # url of the users link
        user_link_URL = user_link_data['users_link']

        line_loc()
        print(user_link_title)
        print(user_link_description)
        print(user_link_content)
        print(user_link_meta_keywords)
        print(user_link_top_img_url)
        line_loc()

        # KEYWORD MANAGEMENT STARTS HERE--------------------

        # initialize empty keywords
        keywords = []

        # initialize empty entity keywords
        eir_keywords = []

        # KeyWordCheck contains methods for processing keywords
        keyword_manager = KeyWordCheck()

        # remove duplicated and sort the user meta keywords according to the length
        intermediate_keywords = sorted(list(set(user_link_meta_keywords)),key=len)

        if((len(intermediate_keywords)<=1)):

            # recoginze keywords from users title and the description and add them and remove duplicates
            no_meta_eir_keywords = list(set(keyword_manager.eir_keywords(user_link_title)+keyword_manager.eir_keywords(user_link_description)))

            print(no_meta_eir_keywords)

            # sort and lower case keywords
            no_meta_eir_keywords = keyword_manager.keyword_formatter(no_meta_eir_keywords)

            print(no_meta_eir_keywords)

            # reduce similar keywords
            no_meta_eir_keywords = keyword_manager.keyword_reducer(no_meta_eir_keywords)

            print(no_meta_eir_keywords)

            # remove irrevelant keywords
            no_meta_eir_keywords = keyword_manager.remove_irrelevant_keywords(no_meta_eir_keywords)

            print(no_meta_eir_keywords)

            print("HERE 1")
            line_loc()

            # check if the number of keywords is greater than 1 but less than the number of keywords
            if(len(no_meta_eir_keywords)>1 and len(no_meta_eir_keywords)<=no_of_keywords):

                keywords = no_meta_eir_keywords
                print("HERE 2")
                line_loc()

            elif(len(no_meta_eir_keywords)==no_of_keywords+1):

                no_meta_eir_keywords.pop(-1)
                # pop the last keyword
                keywords = no_meta_eir_keywords
                print("HERE 3")
                line_loc()

            elif(len(no_meta_eir_keywords)==no_of_keywords+2):

                no_meta_eir_keywords.pop(-1)
                no_meta_eir_keywords.pop(-1)

                keywords = no_meta_eir_keywords
                print("HERE 4")
                line_loc()

            else:
                # skip the current method and ask the user for keywords
                ask_keywords_from_user = True

                highlight_back("Asking the user for keywords",'R')

        # check if the length of meta keywords are greater than or equal to 2 but less than  no_of_keywords
        elif(len(intermediate_keywords)>=2 and len(intermediate_keywords)<=no_of_keywords):

            keywords = intermediate_keywords

            print("HERE 5")
            line_loc()

        elif(len(intermediate_keywords)==no_of_keywords+1):

            intermediate_keywords.pop(-1)
            keywords = intermediate_keywords

            print("HERE 6")
            line_loc()

        elif(len(intermediate_keywords)==no_of_keywords+2):

            intermediate_keywords.pop(-1)
            intermediate_keywords.pop(-1)
            keywords = intermediate_keywords
            print(keywords)
            print("HERE 7")
            line_loc()
        else:

            # lower case and sort keywords
            intermediate_keywords = keyword_manager.keyword_formatter(intermediate_keywords)

            # remove duplicate keywords
            intermediate_keywords = keyword_manager.keyword_reducer(intermediate_keywords)

            # remove irrevelent keywords
            intermediate_keywords = keyword_manager.remove_irrelevant_keywords(intermediate_keywords)

            if(len(intermediate_keywords)>1 and len(intermediate_keywords)<=no_of_keywords):

                keywords = intermediate_keywords

                print("HERE 8")
                line_loc()

            elif(len(intermediate_keywords)==no_of_keywords+1):

                intermediate_keywords.pop(-1)
                keywords = intermediate_keywords

                print("HERE 9")
                line_loc()

            elif(len(intermediate_keywords)==no_of_keywords+2):

                intermediate_keywords.pop(-1)
                intermediate_keywords.pop(-1)
                keywords = intermediate_keywords

                print("HERE 10")
                line_loc()

            else:
                # use named entities in description and description as keywords
                eir_keywords = list(set(keyword_manager.eir_keywords(user_link_title)+keyword_manager.eir_keywords(user_link_description)))
                print(eir_keywords)
                # lower case
                eir_keywords = keyword_manager.keyword_formatter(eir_keywords)
                print(eir_keywords)
                # remove duplicates
                eir_keywords = keyword_manager.keyword_reducer(eir_keywords)
                print(eir_keywords)
                # remove irrevelent
                eir_keywords = keyword_manager.remove_irrelevant_keywords(eir_keywords)
                print(eir_keywords)
                line_loc()

                if(len(eir_keywords)>1 and len(eir_keywords)<=no_of_keywords):

                    keywords = eir_keywords

                    print("HERE 11")
                    line_loc()

                elif(len(eir_keywords)==no_of_keywords+1):

                    eir_keywords.pop(-1)
                    keywords = eir_keywords

                    print("HERE 12")
                    line_loc()

                elif(len(eir_keywords)==no_of_keywords+2):

                    eir_keywords.pop(-1)
                    eir_keywords.pop(-1)
                    keywords = eir_keywords

                    print("HERE 13")
                    line_loc()

                else:
                    # apply intersection between keywords in the description and keywords in the meta tag
                    eir_intersection_keywords = keyword_manager.eir_intersection_reduction(user_link_description,user_link_meta_keywords)
                    print(eir_intersection_keywords)

                    # lower case and sort
                    eir_intersection_keywords = keyword_manager.keyword_formatter(eir_intersection_keywords)
                    print(eir_intersection_keywords)

                    # remove duplicates
                    eir_intersection_keywords = keyword_manager.keyword_reducer(eir_intersection_keywords)
                    print(eir_intersection_keywords)

                    # remove irrevelent
                    eir_intersection_keywords = keyword_manager.remove_irrelevant_keywords(eir_intersection_keywords)
                    print(eir_intersection_keywords)
                    line_loc()

                    if(len(eir_intersection_keywords)<=1):

                        ask_keywords_from_user = True

                        print("HERE 14")
                        line_loc()
                        highlight_back("Asking the user for keywords",'R')

                    elif(len(eir_intersection_keywords)>1 and len(eir_intersection_keywords)<no_of_keywords):

                        keywords = eir_intersection_keywords

                        print("HERE 15")
                        line_loc()

                    elif(len(eir_intersection_keywords)==no_meta_eir_keywords+1):

                        eir_intersection_keywords.pop(-1)
                        keywords = eir_intersection_keywords

                        print("HERE 16")
                        line_loc()

                    elif(len(eir_intersection_keywords)==no_meta_eir_keywords+2):

                        eir_intersection_keywords.pop(-1)
                        eir_intersection_keywords.pop(-1)
                        keywords = eir_intersection_keywords

                        print("HERE 17")
                        line_loc()

                    else:

                        ask_keywords_from_user = True

                        print("HERE 18")
                        line_loc()
                        highlight_back("Asking the user for keywords",'R')


        print(keywords)
        line_loc()

        # KEYWORD MANAGEMENT ENDS HERE-------------------


        if(ask_keywords_from_user==True):

            # return failed status and ask the user to give the keywords
            return {"status":"fail","suggestions":sorted(list(set(user_link_meta_keywords+keyword_manager.eir_keywords(user_link_description))),key=len),"users_link":user_link_URL}

        else:

            api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords)

            # initialize empty list for api content
            api_news_contents = []

            # get titles
            api_news_titles = api_news_handler.get_titles()

            # get sources
            all_news_sources = api_news_handler.get_sources()

            # get URLs
            api_news_Urls = api_news_handler.get_URLs()

            # get descriptions
            api_news_descriptons = api_news_handler.get_descriptions()

            # get only the content from the given urls
            api_news_crawler = ContentCrawler()

            # extract content from each URL and append
            for url in api_news_Urls:

                api_news_contents.append(api_news_crawler.extract_content(url))

            all_news_titles = api_news_titles

            all_news_descriptions = api_news_descriptons

            all_news_contents = api_news_contents

            # insert users news title on to the first element
            all_news_titles.insert(0,user_link_title)

            all_news_descriptions.insert(0,user_link_description)

            all_news_contents.insert(0,user_link_content)

            return ({"status":"success","sources":all_news_sources,"titles":all_news_titles,"descriptions":all_news_descriptions,"contents":all_news_contents,"suggestions":sorted(list(set(user_link_meta_keywords+keyword_manager.eir_keywords(user_link_description))),key=len),"top_img_URL": user_link_top_img_url,"users_link":user_link_URL,"api_news_urls":api_news_Urls})


    def get_data_with_users_help(self,user_link_data,keywords):

        """
        This method takes in keywords and the data from the users link and uses the keywords to  find content
        It returns all data in the form of a dictionary

        :type keywords: list
        :param keywords: list of keywords by the user
        """
        # get users link title
        user_link_title = user_link_data['title']

        # get description
        user_link_description = user_link_data['description']

        # get content
        user_link_content = user_link_data['content']

        # link to the top image
        user_link_top_img_url = user_link_data['top_img_URL']

        api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords)

        # initialize empty
        api_news_contents = []

        # get sources
        all_news_sources = api_news_handler.get_sources()

        # get api titles
        api_news_titles = api_news_handler.get_titles()

        api_news_descriptions = api_news_handler.get_descriptions()

        api_news_Urls = api_news_handler.get_URLs()

        # for only crawling the content from the url
        api_news_crawler = ContentCrawler()

        # for each url extract the content and append
        for url in api_news_Urls:

            api_news_contents.append(api_news_crawler.extract_content(url))

        all_news_titles = api_news_titles

        all_news_descriptions = api_news_descriptions

        all_news_contents = api_news_contents

        # insert all the data from users link on to the first element on the list
        all_news_titles.insert(0,user_link_title)

        all_news_descriptions.insert(0,user_link_description)

        all_news_contents.insert(0,user_link_content)

        return {"sources":all_news_sources,"titles":all_news_titles,"descriptions":all_news_descriptions,"contents":all_news_contents,"top_img_URL": user_link_top_img_url,"api_news_urls":api_news_Urls}



    def get_all_data(self,URL,no_of_keywords=6):
        """
        This method returns all the data in the form of a python dictionary which can be converted inti json
        passing the parameter ['all'] in the returns all of the information
        passing the parameters like ['titles'], ['descriptions'], ['contents'] return that specific data

        This method should only be used while testing in cli mode

        :type URL: string
        :param URL: the url of the website

        :type no_of_keywords: int
        :param no_of_keywords : the number of keywords considered
        """
        # initialize Crawler
        user_news_crawler = Crawler(URL)

        # get data from the user provided link
        user_news_content = user_news_crawler.get_content()

        user_news_title  = user_news_crawler.get_title()

        user_news_meta_keywords = user_news_crawler.get_meta_keywords()

        user_news_meta_description = user_news_crawler.get_meta_description()

        #--------------------------------------------------
        line_loc()
        print(user_news_meta_keywords)
        print(user_news_meta_description)
        print(user_news_title)
        line_loc()
        #---------------------------------------------------
        #-------------keyword processing START--------------

        # use to get unique kewords to query the api
        keywords_manager = KeyWordCheck()

        # initialize an empty list
        keywords = []

        intermediate_keywords = sorted((list(set(user_news_meta_keywords))),key=len)

        # for named enitities as keywords
        eir_keywords = []

        # if the length of the meta keywords is less tha or equal to 2
        if(len(user_news_meta_keywords)<=1):
            no_meta_eir_keywords = list(set(keywords_manager.eir_keywords(user_news_meta_description) + keywords_manager.eir_keywords(user_news_title)))
            # lower case and sort
            print(no_meta_eir_keywords)
            no_meta_eir_keywords = keywords_manager.keyword_formatter(no_meta_eir_keywords)
            print(no_meta_eir_keywords)
            # reduce smilar keywords
            no_meta_eir_keywords = keywords_manager.keyword_reducer(no_meta_eir_keywords)
            print(no_meta_eir_keywords)
            # remove irrelevent
            no_meta_eir_keywords = keywords_manager.remove_irrelevant_keywords(no_meta_eir_keywords)
            print("here 13")
            line_loc()
            print(no_meta_eir_keywords)
            # check if there are more than one keywords but less than 3
            if(len(no_meta_eir_keywords)>1 and len(no_meta_eir_keywords)<=no_of_keywords):
                keywords = no_meta_eir_keywords
                print("here 14")
                line_loc()
            elif(len(no_meta_eir_keywords)==(no_of_keywords+1)):
                no_meta_eir_keywords.pop(-1)
                keywords = no_meta_eir_keywords
                print("here 15")
                line_loc()
            elif(len(no_meta_eir_keywords)==(no_of_keywords+2)):
                no_meta_eir_keywords.pop(-1)
                no_meta_eir_keywords.pop(-1)
                keywords = no_meta_eir_keywords
                print("here 16")
                line_loc()
            else:
                print("here 17")
                highlight_back("There was a problem while extracting the keywords",'R')
                highlight_fore("Please input unique keywords relevent to the article separated by ','","B")
                highlight_fore("Suggested Keywords: ",'Y')
                highlight_fore(list(set(no_meta_eir_keywords)),'G')
                # get keywords from the user
                keywords = input().split(',')
                line_loc()
        elif(len(intermediate_keywords)>=2 and len(intermediate_keywords)<=no_of_keywords):
            # assign meta keywords to keywords
            keywords = intermediate_keywords
            print("here 1")
            line_loc()
        elif(len(intermediate_keywords)==(no_of_keywords+1)):
            # pop the last element from the list
            intermediate_keywords.pop(-1)
            keywords = intermediate_keywords
            print("here 2")
            line_loc()
        elif(len(intermediate_keywords)==(no_of_keywords+2)):
            intermediate_keywords.pop(-1)
            intermediate_keywords.pop(-1)
            keywords = intermediate_keywords
            print("here 3")
            line_loc()
        else:
            # lower case the meta keywords and sort them according to their length
            intermediate_keywords = keywords_manager.keyword_formatter(intermediate_keywords)
            # reduce the number of keywords
            intermediate_keywords = keywords_manager.keyword_reducer(intermediate_keywords)
            # remove irrevelent keywords which are put for seo purposes
            intermediate_keywords = keywords_manager.remove_irrelevant_keywords(intermediate_keywords)
            # check if now keywords are less than or equal to 4
            if(len(intermediate_keywords)<=no_of_keywords):
                keywords = intermediate_keywords
                print("here 4")
                line_loc()
            elif(len(intermediate_keywords)==(no_of_keywords+1)):
                intermediate_keywords.pop(-1)
                keywords = intermediate_keywords
                print("here 5")
                line_loc()
            elif(len(intermediate_keywords)==(no_of_keywords+2)):
                intermediate_keywords.pop(-1)
                intermediate_keywords.pop(-1)
                keywords = intermediate_keywords
                print("here 6")
                line_loc()
            else:
                # import named entities from the description and the title as keywords
                eir_keywords = list(set(keywords_manager.eir_keywords(user_news_meta_description) + keywords_manager.eir_keywords(user_news_title)))
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
                line_loc()
                print(eir_keywords)
                # check if there are more than one keywords but less than 3
                if(len(eir_keywords)>1 and len(eir_keywords)<=no_of_keywords):
                    keywords = eir_keywords
                    print("here 8")
                    line_loc()
                elif(len(eir_keywords)==(no_of_keywords+1)):
                    eir_keywords.pop(-1)
                    keywords = eir_keywords
                    print("here 9")
                    line_loc()
                elif(len(eir_keywords)==(no_of_keywords+2)):
                    eir_keywords.pop(-1)
                    eir_keywords.pop(-1)
                    keywords = eir_keywords
                    print("here 10")
                    line_loc()
                else:
                    # perform intersection between named entities and meta keywords
                    keywords = keywords_manager.eir_intersection_reduction(user_news_meta_description,user_news_meta_keywords)
                    print("here 11")
                    line_loc()
                    if(len(keywords)<=1):
                        print("here 12")
                        line_loc()
                        highlight_back("There was a problem while extracting the keywords",'R')
                        highlight_fore("Please input unique keywords relevent to the article separated by ','","B")
                        highlight_fore("Suggested Keywords: ",'Y')
                        highlight_fore(list(set(intermediate_keywords+eir_keywords)),'G')
                        # get keywords from the user
                        keywords = input().split(',')
                    elif(len(keywords)>no_of_keywords):
                        print("here 12")
                        line_loc()
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


    def get_titles_from_query(self,text):
        """
        This method is incomplete
        """

        sources = []

        titles = []

        success = True

        keyword_manager = KeyWordCheck()


        tokenizer_preprocessor = NlpPreprocessing(text)

        keywords = tokenizer_preprocessor.word_lem_tokenize()

        keywords = keyword_manager.keyword_formatter(keywords)

        keywords = keyword_manager.keyword_reducer(keywords)

        keywords = keyword_manager.remove_irrelevant_keywords(keywords)

        keywords = sorted(list(set(keywords)),key=len)


        if(len(keywords)!=0):

            if(len(keywords)<=3):

                api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords)

            else:

                for i in range(1,(len(keywords)-3)):

                    api_news_handler = NewsApiHandle(API_Key="3689abcc32e2468abb4eed31af2115c0",keyword_list=keywords[0:len(keywords-i)])

                    if(len(api_news_handler.get_sources())>0):
                        break


        if(len(api_news_handler.get_sources())>0):

            sources = api_news_handler.get_sources()

            titles = api_news_handler.get_titles()

        else:

            success = False

        # get sources
        sources = api_news_handler.get_sources()

        # get api titles
        titles = api_news_handler.get_titles()


        if(success==True):

            return {"status":"success","sources":sources,"titles":titles}
        else:

            return{"status":"fail"}
