from selenium import webdriver
from strings import *
from helpers import *

def main():
    driver = getFirstAvailableBrowser()
    if (driver is None): return -1
main()