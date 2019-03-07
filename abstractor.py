from fake_news.crawler.query_data import Data
from fake_news.preprocessor.error_handle import highlight_back
from fake_news.nlp.cosine_bow import cosine_similartity_bow

def without_keywords(url):
    
    """
    :type url: string
    :param url: url of the website

    This method returns two types of dictionary
    if the algorithm manages to find relevent articlesit returns a dictionary with keys

    status: string, similarity:list, sources :list, suggestions: list , titles: list, contents: list, top_image_URL:string, users_link:string

    if the algorithm fails it returns 
    status: string ,suggestions: list ,user_link : string

    """
    # initialize data object
    d = Data()

    # get the data  from the link (dict)
    p = d.get_user_data(url)

    # initialize empty
    data = {}

    for keys in range(6,2,-1):

        k = d.get_data_wo_user_help(p,keys)

        highlight_back(str(keys),'Y')

        if(k['status'] == "fail"):

            break
        
        elif(k['status']=='success'):

            if(len(k['titles'])>1):

                break
    
    if(k['status']=="success"):

        if(len(k['titles'])<=1):

            k['status'] = 'fail'

    if(k['status']=='success'):

        data = k

        return {"similarity":cosine_similartity_bow(data["contents"]),**data}

    if(k['status']=='fail'):

        return {"status":"fail","suggestions":k['suggestions'],"user_link":k['users_link']}



def with_keywords(url,keywords):

    """
    :type url: string
    :param keywords: list

    This method returns a dctionary with following keys

    contents:list, descriptions: list , similarity:list, sources: list, titles: list ,top_img_URL :string


    """

    # initialize data
    d = Data()

    user_link_data_wo = d.get_user_data(url)

    data = d.get_data_with_users_help(user_link_data=user_link_data_wo,keywords=keywords)

    return {"similarity":cosine_similartity_bow(data["contents"]),**data}

