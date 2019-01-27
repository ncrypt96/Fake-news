import requests
from urllib.parse import urlparse

class PreCheck:

    """
    This class contains methods for checking the validity
    """

    def check_if_website_exists(self,URL):

        """
        This method is used to check if the given URL exists or if its unreachable

        Returns: True if the website exists and False if it dosen't

        :type URL: string
        :param URL: The URL of the website
        """

        # Remove leading and ending white spaces if there are any
        URL = URL.strip()

        if ("http://" in URL) or  ("https://" in URL):

            pass
        
        else:

            URL =  "http://" + URL

        print(URL)


        try:
            # apply a get request on the URL
            request = requests.get(URL)


            # if the status code is equal to 200 return True else return False
            if request.status_code == 200:

                return True
            else:

                return False

        except Exception as exception:

            # If there arises an exception print the exception and return False
            print("There was a problem: {}".format(exception))

            return False


    def check_if_secure(self,URL):

        """
        This method checks if the given site is secure or not 

        Returns False if not secure else if secure return True if not either return None

        :type URL: string
        :param URL: The URL of the Website
        """
        # if the url is not secure return False else if secure return True if not either return None
        if (urlparse(URL).scheme == 'http'):

            return False

        elif( urlparse(URL).scheme == 'https'):

            return True

        else:
            
            return None








 







