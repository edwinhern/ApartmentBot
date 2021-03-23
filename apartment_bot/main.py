from selenium import webdriver
import time

'''
    Name: Edwin Hernandez
    Project Name: Apartment_Bot
    Description: Allows users who use "apartmentpermits.com/guest" to register their guests with one execution of this program.
    Doing so will save users time and be convenient if guests tend to show up multiple times.
'''


class Bot:
    # Setter function to allow the information given to be entered into the "name" variables
    def __init__(self, apartment_name, suite_number, four_digit_number, car_model, car_color, license_plate, chrome_path):
        # Takes a parameter and assigns it to the 'name' variable so we can access different 'names'
        self.apartment_name = apartment_name
        self.suite_number = suite_number
        self.four_digit_number = four_digit_number
        self.car_model = car_model
        self.car_color = car_color
        self.license_plate = license_plate
        self.driver = webdriver.Chrome(chrome_path)
        # Open website
        self.driver.get("https://app.apartmentpermits.com/guest")
        
    # Auto completes the apartment information
    def add_unit_details(self):    
        # Xpath for the box "Apartment Name" to be filled
        apartName = ('//*[@id="vs1__combobox"]/div[1]/input')
        # Xpath for "Apartment Name" inside the listed apartment names to be clicked
        Box = ('//*[@id="vs1__listbox"]')
        # Xpath for "Suite Number" to be entered
        suiteNumber = ('//*[@id="input-9"]')
        # Xpath for the last "four digit numbers" in your phone number to be entered
        four_Number = ('//*[@id="input-10"]')
        # Xpath to click on the "next step" button
        next_Step= ('//*[@id="kt_form"]/div[5]/button[3]')

        # Finds the Xpath of "apartName" and access the string stored in "apartment_name"
        self.enterData(apartName, self.apartment_name)
        # Waits for the ListBox to be shown
        time.sleep(.4)
        # Finds the Xpath of "Box" and clicks to object 
        self.clickButton(Box)
        # Finds the Xpath of "suiteNumber" and access the string stored in "suite_number"
        self.enterData(suiteNumber, self.suite_number)
        # Finds the Xpath of "four_Number" and access the string stored in "four_digit_number"
        self.enterData(four_Number, self.four_digit_number)
        # Finds the Xpath of "next_Step" and clicks to object 
        self.clickButton(next_Step)

    # Auto completes the Car information
    def add_vehicle_details(self):
        # Xpath for the box "make" to be filled
        make = ('//*[@id="kt_form"]/div[2]/div[2]/div/div[1]/div/div/button')
        # Xpath for "make" inside the listed make names to be clicked
        Box1 = ('//*[@id="bs-select-1"]/ul/li[1]')
        # Xpath for the box "vehicle color" to be filled with "car_color"
        vehicle_color = ('//*[@id="vs2__combobox"]/div[1]/input')
        # Xpath for "vehicle color" inside the listed make names to be clicked
        Box2 = ('//*[@id="vs2__listbox"]') 
        # Xpath for the box "license plate" to be filled
        License1 = ('//*[@id="input-20"]')
        # Xpath for the box "confirm license plate" to be filled
        License2 = ('//*[@id="input-21"]')
        # Finds the Xpath of "next_Step" and clicks to object 
        next_step = ('//*[@id="kt_form"]/div[5]/button[3]')

        # Finds the Xpath of "make" and access the string stored in "car_model"
        self.enterData(make, self.car_model)
        # Waits for the ListBox to be shown
        time.sleep(.2)
        # Finds the Xpath of "make" and clicks to object 
        self.clickButton(Box1)
        # Finds the Xpath of "vehicle_color" and access the string stored in "car_color"
        self.enterData(vehicle_color, self.car_color)
        # Waits for the ListBox to be shown
        time.sleep(.2)
        # Finds the Xpath of "car_color" and clicks to object 
        self.clickButton(Box2)
        # Finds the Xpath of "License1" and access the string stored in "license_plate"
        self.enterData(License1, self.license_plate)
        # Finds the Xpath of "License1" and access the string stored in "license_plate"
        self.enterData(License2, self.license_plate)
        # Finds the Xpath of "next_Step" and clicks to object 
        self.clickButton(next_step)
        
    # Auto Confirms the "confirm" button
    def confirm(self):
        # Xpath to click on the "Confirm" button
        confirm = ('//*[@id="kt_form"]/div[5]/button[2]')
        # Finds the Xpath of "confirm" and clicks to object 
        self.clickButton(confirm)

    # Clicks Button function
    def clickButton(self, xpath):
        try:
            # Finds the xpath and clicks on the object
            self.driver.find_element_by_xpath(xpath).click()
        except Exception:
            time.sleep(1)
            self.clickButton(xpath)
    # Enter Data 
    def enterData(self, field, data):
        try:
            self.driver.find_element_by_xpath(field).send_keys(data)
            pass
        except Exception:
            time.sleep(1)
            self.enterData(field, data)


# Enter Information
if __name__ == "__main__":
    personal_info = dict(
        apartment_name = input("Enter apartment name: "),
        suite_number = input("Enter suite number: "),
        four_digit_number = input("Enter your last four-digit numbers to your phone number: "),
        car_model = input("Enter car model: "),
        car_color = input("Enter car color: "),
        license_plate = input("Enter your license plate: "),
        chrome_path = "Enter Chrome_path in the string"
    )

bot = Bot(**personal_info)
bot.add_unit_details()
bot.add_vehicle_details()
bot.confirm()
