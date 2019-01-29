import spacy

class KeyWordCheck:
    """
    This class contains methods to process keyword before it is applied to the api
    """

    def eir_intersection_reduction(self,text,other_list_of_keywords):
        """
        This method uses spacys entity recogintion to recognize entities and applies intersection between the meta keywords to get most relevant keywords
        it returns a list of possible keywords

        :type text: string
        :param string: The text from which the keywords must be extracted

        :type other_list_of_keywords: list
        :param other_list_of_keywords: other keywords for the intersection

        """
        # load the english module
        # install 'en' model (python3 -m spacy download en)
        nlp = spacy.load('en')
        
        # process the doc
        doc  = nlp(text)

        # get the entities 
        keywords = doc.ents

        # initialize an empty list for the keywords
        list_of_intermediate_keywords = []

        # final keywords list to be returned
        final_keyword_list = []

        # intersect with other list of keywords
        for word in keywords:

            for item in other_list_of_keywords:

                if(str(word) in item) or (item in str(word)):

                    if(len(str(word))<=len(item)):

                        list_of_intermediate_keywords.append(str(word))
                    else:
                        list_of_intermediate_keywords.append(item)

        #----------------------------------------------
        print("from keyword_check.py")
        print(set(list_of_intermediate_keywords))
        #----------------------------------------------

        # assign final_keyword_list
        final_keyword_list = list_of_intermediate_keywords
        
        # remove partial duplicates from the final list
        for word in list_of_intermediate_keywords:

            for item in list_of_intermediate_keywords:

                if(word != item):

                    if((word in item) or (item in word)):

                        if(len(word)<=len(item)):

                            final_keyword_list.remove(item)

                        else:

                            final_keyword_list.remove(word)
        #---------------------------------------
        print(final_keyword_list)
        print("from keyword_check.py")
        #---------------------------------------
        return set(final_keyword_list)


    def keyword_reducer(self,keywords):
        """
        This method removes the repetitive keywords and reduces them to a single entity

        :type keywords: list
        :param keywords: the list of properly sortred and lower case keywords
        """

        #initialize check as flase
        check = False
        
        # for each word in keywords if they have their substrings present in other members of the list then remove the larger string from the list
        for word in keywords:
            
            for item in keywords:
            
                if(word!=item):
                    
                    if(word in item):
                    
                        keywords.remove(item)
                
                
        # check if word still have their substrings in the list
        for word in keywords:
            
            for item in keywords:
            
                if(word!=item):
                
                    if(word in item):
                
                        check = True
        
        # if there are still substrings repeat the above procedure
        # else return the keywords        
        if(check == True):
            
            return self.keyword_reducer(keywords)
        
        else:
            return keywords

    
    def eir_keywords(self,text):
        """
        This method uses named entity recognition for the extraction of keywords from the given text
        returns a list of keywords

        :type text: string
        :param text: The text from where keywords need to be extracted
        """
        #initialize empty
        keywords_list = []

        # load the english module
        # install 'en' model (python3 -m spacy download en)
        nlp = spacy.load('en')
        
        # process the doc
        doc  = nlp(text)

        # get the entities 
        keywords = doc.ents

        # convert each entity to string and apend
        for word in keywords:

            keywords_list.append(str(word))
        
        return keywords_list

    def keyword_formatter(self,keywords):
        """
        This method takes in keyword as an argument then makes each keyword lower case and sorts them according to their length and returns them

        :type keywords: list
        :param keywords: all the keywords found
        """

        # initialize empty
        formatted_keywords = []

        # lower case each keyword and append
        for word in keywords:

            formatted_keywords.append(word.lower())

        # sort the keywords according to their length
        formatted_keywords = sorted(formatted_keywords,key=len)

        return formatted_keywords




                    
