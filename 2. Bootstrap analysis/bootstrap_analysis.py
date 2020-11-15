import requests
import json
import base64

# ----------------------------------------------------------------------------
# 1. FUNCTION TO CREATE IMAGE
# ----------------------------------------------------------------------------

def create_image(filename,image_string):
    image_bytes = image_string.replace("'", '""').encode('utf8')
    with open(filename+".png", "wb") as fh:
        fh.write(base64.decodebytes(image_bytes))
    return()

# ----------------------------------------------------------------------------
# 1. LOGIN
# ----------------------------------------------------------------------------

url = "https://be-mole.herokuapp.com/"

# LOGIN TO THE MOLE WEB-API
r = requests.post(url+"login",json={"username":"username","password":"password"})
print('\nIf this value: '+str(r.status_code)+' is equal to 200 you are logged in.\n')

# VALIDATE YOUR ACCESS TOKEN FOR THIS SESSION
access_token = r.json()['access_token']
r = requests.get(url+"validate",headers={"Authorization":"Bearer "+str(access_token)})
print('Request made by: '+r.json()['logged_in_as'])

# ----------------------------------------------------------------------------
# 2. BOOTSTRAP ANALYSIS
# ----------------------------------------------------------------------------

# 2.1 Data import
bootstrap_data = json.load(open('./input.json', 'r'))

# 2.2 Validate and analyse data
r = requests.post(url+"bootstrap",json=bootstrap_data,headers={"Authorization":"Bearer "+str(access_token)})
print('\nIf this value: '+str(r.status_code)+' is equal to 200 your analysis is completed.\n')

# 2.3 Convert string to bytes value and save
create_image("./output",r.json()["image"])
