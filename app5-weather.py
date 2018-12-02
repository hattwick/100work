# Playing with Build 10 Applications from Talk Python Training.  This is App 5 from that course
# Program is a web scraping weather puller.
# Tested in Python 3.7
# Current test result: <Response [200]>

import sys
import requests
# import beautifulsoup4 as bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def program_header():
    print('--------------------------------------------')
    print('           WEATHER SCRAPER                  ')
    print('--------------------------------------------')
    print()

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    print(response)
    return response.text


version = sys.version
print(version)


def main():
    program_header()

    zip = input('What zipcode do you want the weather for (01463)? ')

    html = get_html_from_web(zip)


if __name__ == "__main__":
    main()