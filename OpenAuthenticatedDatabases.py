import requests
import webbrowser
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL = 'https://www5.elawsoftware.com/eLawSecure.nsf/SecureLogin?ReadForm'

# This URL is the page you actually want to pull down with requests.
REQUEST_URL = 'https://www5.elawsoftware.com/1217/1217_Criminal.nsf/Docket?OpenForm'

values = {'username': 'Leonard.martinez',
          'password': '51698'}

r = requests.post(POST_LOGIN_URL, data=values)
print(r.content)
webbrowser.get(chrome_path).open(REQUEST_URL)


