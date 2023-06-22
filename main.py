from robotics import Robot
from validation import Validator
from image_processing import ImageProcessing
import pandas as pd


SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
ROOT_URL = "https://en.wikipedia.org/wiki/"

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()

def communicate_work(scientist_worked_on):
    robot.say_updates(scientist_worked_on)

def say_bye():
    robot.say_goodbye()

def main():

    introduce_yourself()
    try:
        #Create lists to store data
        birthdays=[]
        deathdays=[]
        ages=[]
        first_paragraphs=[]
        images=[]
        
        #Traverse through each site using the robot, and obtain data (validate data and formats)
        for scientist in SCIENTISTS:
            robot.say_updates(scientist)
            robot.open_webpage(url_formatter(ROOT_URL,scientist))
            birthdays.append(Validator.not_null(robot.get_birth_date(),"Birthday"))
            deathdays.append(Validator.not_null(robot.get_death_date(),"Deathday"))
            first_paragraphs.append(Validator.not_null(robot.get_first_paragraph(),"First paragraph"))
            images.append(Validator.not_null(robot.get_image(),"Image"))
            ages.append(Validator.check_age(robot.age_calculator(birthdays[-1],deathdays[-1]),"Scientist"))
            
            
            print(f"\nName: {scientist}, Age: {ages[-1]}, Birthday: {birthdays[-1]}, Deathday: {deathdays[-1]}\n{first_paragraphs[-1]}")
            # Commented out below line because code doesn't currently work
            #ImageProcessing.download_image_as_txt(images[-1],scientist)
        #Output data to .csv file for access once terminal is closed
        output_data("data/scientist_data.csv", birthdays, deathdays, ages, first_paragraphs, images)
    except Exception as e:
        print(f"Error occured when parsing through {scientist}(s):{str(e)}")
    say_bye()



#Self-made UTIL Methods Below
def output_data(path, bd_list, dd_list, age_list, first_paragraph_list, image_list):
    '''
    Creates a .csv file that can be easily read and accessed by the user
    Takes in a path to where .csv file will be outputted to, and takes in lists of data to 
    
    '''
    output_dataframe = pd.DataFrame(data={'Scientist': SCIENTISTS, 'Birthday': bd_list, 'DeathDate':dd_list, 'Age':age_list, 'First_Paragraph':first_paragraph_list, 'Images':image_list})
    output_dataframe.to_csv(path,index=False)


def url_formatter(prefix,suffix):
    '''
    Creates a proper URL that the Robot can use to open the website
    Takes a prefix string and a suffix string and converts it into a valid ASCII String
    
    '''
    return prefix+suffix.replace(" ","_")

if __name__ == "__main__":
    main()
