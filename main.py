from selenium import webdriver
from strings import *
from helpers import *

def main():
    driver = get_first_available_browser()
    if (driver is None): return -1
main()
