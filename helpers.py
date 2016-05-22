from selenium import webdriver
from strings import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

'''Returns the first available browser which can be used as a driver.'''
def get_first_available_browser(verbose=False):
    browsers = [
        ('PhantomJS', webdriver.PhantomJS),
        ('Chrome', webdriver.Chrome),
        #('Firefox', webdriver.Firefox), 
        ('Opera', webdriver.Opera),
        ('Ie', webdriver.Ie)
    ]
    
    for browser in browsers:
        try:
            if verbose: print(I_GET_BROWSER_PROG % browser[0])
            result = browser[1](service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']) if browser[0] is 'PhantomJS' else browser[1]()
            print(I_GET_BROWSER_SUPPORT % browser[0])
            result.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
            return result
        except:
            print(I_GET_BROWSER_NSUPPORT % browser[0])
            continue
    print(E_GET_BROWSER_NONE)
    for browser in browsers: print(browser[0])
    return None
