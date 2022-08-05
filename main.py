import json
import requests
from webbot import Browser

zCalendarPage = "https://northwestbadmintonacademy.sites.zenplanner.com/calendar.cfm"
zLoginPage = "https://northwestbadmintonacademy.sites.zenplanner.com/login.cfm"
zTestPage = "https://northwestbadmintonacademy.sites.zenplanner.com/calendar.cfm?DATE=2022%2D08%2D07&VIEW=LIST"
zUserProfilePage = "https://northwestbadmintonacademy.sites.zenplanner.com/person.cfm"
zFamilyPage = "https://northwestbadmintonacademy.sites.zenplanner.com/family.cfm"

urlDate = "?DATE="
urlEnd = "&VIEW=LIST"
urlCalendarPerson = "&calendarType=PERSON:"
urlPerson = "&personId="

def getUserEndlink(name, browser):

    link = ""
    browser.go_to(zFamilyPage)

    if (browser.exists(name)):
        browser.click(name)
        link = browser.get_current_url()
        return(link[link.index("=") + 1:])

    else:
        print("Family member not found: " + name + ".")


username = ""
password = ""

with open("login.json", "r") as f:
    data = json.load(f)
    username = data["username"]
    password = data["password"]

web = Browser()

print("Navigating to zenplanner.")

web.go_to(zCalendarPage)
web.go_to(zLoginPage)


if (web.exists("Log In")):
    print("Not logged in, logging in...")
    web.go_to(zLoginPage)
    web.type(username , into='username', id='idUsername')
    web.type(password , into='Password' , id='idPassword')
    web.click('Log In' , tag='input')

if (web.exists("My Profile")):
    print("Successfully logged in.")

else:
    print("An error occurred.")
    quit()


commands = []

with open("commands.json", "r") as f:
    data = json.load(f)
    commands = data["scheduled"]


for x in commands:

    userId = getUserEndlink(x["name"], web)
    web.go_to(zCalendarPage + urlDate + x["date"] + urlEnd)

    if (web.exists(x["time"])):
        web.click(x["time"])

        if (web.exists("All available spots for this class session are now taken.")):
            print("Time slot found at " + x["time"] + " on " + x["date"] + " is full.")
        
        else:
            web.go_to(web.get_current_url() + urlPerson + userId)
            web.click("Reserve")

            if (web.exists(x["name"] +  " is registered for this class.")):
                print("Sucessfully registered " + x["name"] + " for the time slot found at " + x["time"] + " on " + x["date"])

            else:
                print("An error may have occurred when trying to register " + x["name"] + "for the time slot found at " + x["time"] + " on " + x["date"])

    else:
        print("No time slot found at " + x["time"] + " on " + x["date"])


web.quit()