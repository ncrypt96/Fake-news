import requests

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

        if (" http://" or  " https://") in URL:

            pass
        
        else:

            URL =  "http://" + URL


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


 







