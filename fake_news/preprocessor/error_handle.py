# This module deals with highlighting all the messases

from colorama import Fore,Back,Style,init
# initialize colorama
init()

def highlight_back(text,color='Y'):
    """
    This method highlights the background of the text in the console
    this method is only for strings and list

    :type text: string
    :param text: the text to be colored

    :type color: string
    :param color: The color to be used (R,G,B,Y) 
    """

    if(type(text)!=str):
        text = " , ".join(text)
        
    if color == 'R':
        print(Back.RED+ text)
    elif color == 'G':
        print(Back.GREEN+Fore.BLACK+ text)
    elif color == 'B':
        print(Back.BLUE+Fore.BLACK+text)
    else:
        print(Back.YELLOW+Fore.BLACK+text)

    # reset styles
    print(Style.RESET_ALL)

def highlight_fore(text,color='Y'):
    """
    This method highlights the foreground of the text in the console
    this method is only for strings and list

    :type text: string or list
    :param text: the text to be colored

    :type color: string
    :param color: The color to be used (R,G,B,Y) 
    """

    if(type(text)!=str):
        text = " , ".join(text)

    if color == 'R':
        print(Fore.RED+ text)
    elif color == 'G':
        print(Fore.GREEN+ text)
    elif color == 'B':
        print(Fore.BLUE+text)
    else:
        print(Fore.YELLOW+text)

    # reset styles
    print(Style.RESET_ALL)






