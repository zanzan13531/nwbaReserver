import json
import requests
from webbot import Browser

zenPlannerMainPage = "https://northwestbadmintonacademy.sites.zenplanner.com/calendar.cfm"
zenPlannerLoginPage = "https://northwestbadmintonacademy.sites.zenplanner.com/login.cfm"

username = ""
password = ""

with open("login.json", "r") as f:
    data = json.load(f)
    username = data["username"]
    password = data["password"]


web = Browser()

print("Navigating to zenplanner")

web.go_to(zenPlannerMainPage)
web.go_to(zenPlannerLoginPage)


if (web.exists("Log In")):
    print("Not logged in, logging in...")
    web.go_to(zenPlannerLoginPage)
    web.type(username , into='username', id='idUsername')
    web.type(password , into='Password' , id='idPassword')
    web.click('Log In' , tag='input')

if (web.exists("My Profile")):
    print("Successfully logged in")
else:
    print("An error occurred")




# web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')

"""web.press(web.Key.ENTER)
web.go_back()
web.click('Sign in')
web.type('mymail@gmail.com' , into='Email')
web.click('NEXT' , tag='span')
web.type('mypassword' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') # you are logged in . oohoooo


zenPlannerMainPage = "https://northwestbadmintonacademy.sites.zenplanner.com/calendar.cfm"
page = requests.get(zenPlannerMainPage)

print(page.text)

"""