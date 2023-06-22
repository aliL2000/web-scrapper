from RPA.Browser.Selenium import Selenium
from datetime import datetime
import re

br = Selenium()

class Robot:

    BIRTHDAY_LOCATOR="class:bday"
    DEATHDAY_LOCATOR="xpath://div[@class='deathplace']/../span"
    FIRST_PARAGRAPH_LOCATOR="css:div.mw-parser-output > p:not([class])"
    IMAGE_LOCATOR="xpath://td[@class='infobox-image']/a/img"

    DATE_REGEX="(\d{4})-(\d{2})-(\d{2})"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("\nGoodbye, my name is " + self.name)

    def say_updates(self,current_work):
        print(f"\nWorking on {current_work}'s information currently...")

    def open_webpage(self, webpage):
        return br.open_available_browser(webpage)

    def get_birth_date(self):
        return self.date_formatter(br.find_element(self.BIRTHDAY_LOCATOR).get_attribute("innerHTML"))
    
    def get_death_date(self):
        return self.date_formatter(br.find_element(self.DEATHDAY_LOCATOR).get_attribute("innerHTML"))
    
    def get_first_paragraph(self):
        return br.find_element(self.FIRST_PARAGRAPH_LOCATOR).text
    
    def get_image(self):
        return br.find_element(self.IMAGE_LOCATOR).get_attribute("src")
    
    @staticmethod
    def age_calculator(birthday:str,deathday:str):
        '''
        Calculates the age from given strings 
        Accepts a birthday string, and a deathday string.
        Returns the age of a person between these two dates as an Integer
    
        '''
        birthdate = datetime.strptime(birthday, '%Y-%m-%d').date()
        deathdate = datetime.strptime(deathday, '%Y-%m-%d').date()
        return int(deathdate.year - birthdate.year - ((deathdate.month, deathdate.day) < (birthdate.month, birthdate.day)))

    @staticmethod
    def date_formatter(input_date):
        '''
        Formats the date given from Wikipedia in a filtered format using regex
        Accepts a input_date string
        Returns a properly formatted string in this format: "YYYY-MM-DD"
    
        '''
        return re.search(r"(\d{4})-(\d{2})-(\d{2})", input_date).group()
