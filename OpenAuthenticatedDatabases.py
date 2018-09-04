import requests
import webbrowser
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL_ELAW = 'https://www5.elawsoftware.com/eLawSecure.nsf/SecureLogin?ReadForm'

# This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL_AMP = 'https://courts.co.travis.tx.us/amp/'

# This URL is the page you actually want to pull down with requests.
REQUEST_URL_CreateNewFile = 'https://www5.elawsoftware.com/1217/1217_Criminal.nsf/Docket?OpenForm'
REQUEST_URL_AMP1 = 'https://courts.co.travis.tx.us/AMP/Cases/Search'
REQUEST_URL_Sherrif = 'https://public.co.travis.tx.us/sips/default.aspx'
REQUEST_URL_TravisDocket = 'https://publiccourts.co.travis.tx.us/dsa/'

#auth_value
values_ELAW = {'username': 'Leonard.martinez',
          'password': ''}
values_AMP = {'username': '',
          'password': ''}

r = requests.post(POST_LOGIN_URL_ELAW, data=values_ELAW)
amp = requests.post(POST_LOGIN_URL_AMP, data=values_AMP)

print(r.content)
webbrowser.get(chrome_path).open(REQUEST_URL_CreateNewFile)
webbrowser.get(chrome_path).open(REQUEST_URL_AMP1)
webbrowser.get(chrome_path).open(REQUEST_URL_Sherrif)
webbrowser.get(chrome_path).open(REQUEST_URL_TravisDocket)
