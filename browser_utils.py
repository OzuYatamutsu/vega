## Useful aliases for selenium functions.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def inject_jquery_if_needed(browser):
    browser.execute_script('''if (typeof(jQuery) === "undefined") { 
    var script = document.createElement("script"); 
    script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
    document.getElementsByTagName("head")[0].appendChild(script);
    }''')
def set_text(browser, selector, text):
    inject_jquery_if_needed(browser);
    browser.execute_script("""jQuery("%s").text("%s")""" % (selector, text))
def set_value(browser, selector, value):
    inject_jquery_if_needed(browser);
    browser.execute_script("""jQuery("%s").val("%s")""" % (selector, value))
def wait_for_id(browser, id, timeout=10):
    WebDriverWait(browser, timeout).until(lambda browser: browser.find_element_by_id(id))
def wait_for_class(browser, class_name, timeout=10):
    WebDriverWait(browser, timeout).until(lambda browser: browser.find_element_by_class_name(class_name))
def get_text_from_id(browser, id):
    return browser.find_element_by_id(id).text
def get_text_from_class(browser, class_name):
    return browser.find_element_by_class_name(class_name).text
def get_value_from_id(browser, id):
    return browser.find_element_by_id(id).get_attribute('value')
def get_value_from_class(browser, class_name):
    return browser.find_element_by_class_name(class_name).get_attribute('value')