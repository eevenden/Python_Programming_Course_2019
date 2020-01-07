'''
# Assignment 5 title: Lab 5- Web-scraping Current Weather Conditions
# By Emily Evenden
# Date: 09/20/2019
# Time: 30 mins
'''

# This section imports several libraries which contain modules for web scrapping
import requests
from bs4 import BeautifulSoup

#This sections sets the latitude and longtitude of Philadelphia, PA as variables
lat = '39.952583'
lon = '-75.165222'

# This lines creates url for the requested location through string concatenation and the variables I created for latitude and longitude
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
print url

# This section uses the get() function from the requests library to retrieve the web-page
# Then is sets the results to the variable 'page'
page = requests.get(url)

# Next, we create a BeautifulSoup object using the page variable
# Then we access contents of the web-page using .content
# The html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Next, I located the element containing all the current weather information.
# It is contained in id tag called "current_conditions_detail"
# Then the find() function locates that element in the BeautifulSoup object
cur_weather_conditions = soup.find(id="current_conditions_detail")

# Here, the selected text is set to the cur_weather_conditions variable
cur_weather_conditions = cur_weather_conditions.text

# Final Output
# Return scraped information
# This section prints the location's latitude and longitude and the scraped information
print 'The Current Weather Conditions at '+ lat +  ", " + lon + " is:" + cur_weather_conditions

