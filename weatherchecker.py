#!/usr/bin/env python3
""" Download stuff I want to know from around the internet and display it in one screen, also
    add a search the internet button. """

import bs4
import requests
print()
ZIPCODE = input("Enter a zip code to check the weather: ")
WEATHERADDRESS = "https://weather.com/weather/today/l/" + ZIPCODE + ":4:US"

GETTINGWEATHER = requests.get(WEATHERADDRESS)
GETTINGWEATHER.raise_for_status()
WEATHERPAGE = bs4.BeautifulSoup(GETTINGWEATHER.text, "lxml")

LOCATION = WEATHERPAGE.select('.today_nowcard-location')[0].getText()
TEMP = WEATHERPAGE.select('.today_nowcard-temp')[0].getText()
CONDITION = WEATHERPAGE.select('.today_nowcard-phrase')[0].getText()

print()
print("The current weather in " + LOCATION + " is " + TEMP + " degrees, and "
      + CONDITION + ".")
print()
