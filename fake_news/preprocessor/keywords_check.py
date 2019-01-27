import spacy

class KeyWordCheck:
    """
    This class contains methods to process keyword before it is applied to the api
    """

    def eir_reduction(self,text,other_list_of_keywords):
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
           

        return final_keyword_list

                    
