# Hi there

This is a list of my changes to the repository you've shared with me, I've also decided to make some interesting changes to the project. Aside from the required outlined requirements, I've added some additional features that I will elaborate on.

## Changes

- Added code to [main.py](main.py) so that we obtain the birth date, death date, first paragraph, and the **image link** from the robot. 
    - Obtains the correct Wikipedia URL to the scientist page using the **url_formatter()** method. (Not necessary, as Wikipedia automatically re-directs, but would be good to maintain proper standards).
    - Updates the user which scientist they are currently working on.
    - Stores the information into lists, so that we can save the date in an easily readable format for future access and so we don't have re-run the script, see **output_data()** method.
    - Prints data to console/terminal so that the users can view data instantaneously, and also provides users with the data located in the [scientist_data.csv](data/scientist_data.csv) located in the data folder for future access (Two options!)

- Added code to [robotics.py](robotics.py) so that the Robot obtains the requested information from the main.py file.
  - Created a set of **constants** that are the locating strategies that the rpa framework uses to obtain the data.
  - Created **get_birth_date()** that obtains the scientist's birth date.
  - Created **get_death_date()** that obtains the scientist's death date.
  - Created **get_first_paragraph()** that obtains the scientist's first paragraph on their Wikipedia page.
  - Created **get_image()** that obtains the image from the scientist's Wikipedia page.
  - Created **age_calculator()** that calculates the age of a person from two dates given in strings (made a docstring to explain the method).
  - Created **date_formatter()** that returns a properly formatted string that can be used in the age_calculator() method (made a docstring to explain the method). 

## Additions

- Created [validation.py](validation.py) that contains methods that validates data obtained from the robot, the methods created are:
    - **not_null** that checks to see if the Robot actually returned a value from scraping the site.
    - **check_age** that checks to see if the age calculation makes logical sense and is calculated properly.

- Created [image_processing.py](image_processing.py) that takes the image links from the Robot, downloads the images, and outputs the image in a .txt file that looks like this:
![image](https://miro.medium.com/v2/resize:fit:750/format:webp/1*SkSXpy88uqu-7Kr8XU80aA.jpeg) 
It's more cool than it is actually functional, and whether or not it's a business-oriented feature is up to debate to be honest.

- Created [test.py](test.py) that contains unit tests that check the correct behaviour of methods that I've created. Each test contains test cases for the following methods:
    - **age_calculator()**
    - **date_formatter()**
    - **not_null()**
    - **check_age()**
    - **url_formatter()**

## Final Thoughts/Conclusion
The list of changes I've made add functionality and support the script by adding levels of industry standard convention. For example, the inclusion of a [test](test.py) file ensures that further development/new changes to this script operate as expected and **are not** breaking old code. Also, creating a [validator](validation.py) class means that we check that data from the Robot is in a format we expect and it works in tandem with the test class to ensure proper output from the script. After all, we don't want our users to be obtaining data that doesn't make sense to them.

I also obtained the images from each scientist's respective URL page, it's a new feature that I thought was cool and found about recently. But it needs some future work, in the meantime, the robot obtains the image urls as an additional feature.

I also add output in two formats: (1) Through the console/terminal, and more tech-savvy individuals/users can navigate through the terminal and comprehened the data immediately and (2) Output data to the data/scientist_data.csv file, for less computer-savvy users, and the added advantage is that the data persists after closing the script and .csv is a common file format that most of your clients should be familiar with. 
