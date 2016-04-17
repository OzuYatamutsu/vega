from selenium import webdriver
from strings import *

'''Returns the first available browser which can be used as a driver.'''
def get_first_available_browser(verbose=False):
    browsers = {
        'PhantomJS': lambda: webdriver.PhantomJS(),
        'Chrome': lambda: webdriver.Chrome(),
        #'Firefox': lambda: webdriver.Firefox(), 
        'Opera': lambda: webdriver.Opera(),
        'Ie': lambda: webdriver.Ie()
    }
   
    for browser in browsers:
        try:
            if verbose: print(I_GET_BROWSER_PROG % browser)
            browsers[browser]().quit()
            print(I_GET_BROWSER_SUPPORT % browser)
            return browsers[browser]()
        except:
            print(I_GET_BROWSER_NSUPPORT % browser)
    print(E_GET_BROWSER_NONE)
    for browser in browsers: print(browser)
    return None
