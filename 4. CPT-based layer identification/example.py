import requests
import json
import base64

# ----------------------------------------------------------------------------
# 1. FUNCTION TO CREATE IMAGE (ONLY DEFINE ONCE IN YOUR PROJECT)
# ----------------------------------------------------------------------------

def create_image(filename,image_png,image_pdf):
    image_bytes = image_png.replace("'", '""').encode('utf8')
    with open(filename+".png", "wb") as fh:
        fh.write(base64.decodebytes(image_bytes))
    image_bytes = image_pdf.replace("'", '""').encode('utf8')
    with open(filename+".pdf", "wb") as fh:
        fh.write(base64.decodebytes(image_bytes))
    return()

# ----------------------------------------------------------------------------
# 2. FUNCTION TO CREATE LOGFILE (ONLY DEFINE ONCE IN YOUR PROJECT)
# ----------------------------------------------------------------------------

def create_logfile(filename,log_string):
    with open(filename+".txt", "w") as fh:
        fh.write(log_string)
    return()

# ----------------------------------------------------------------------------
# 3. LOGIN (ONLY REQUIRED ONCE IN YOUR PROJECT)
# ----------------------------------------------------------------------------

# 3.1 Define login requirement
url = "https://bestestimate.nl/"
username = 'USERNAME'
password = 'PASSWORD'

# 3.2 Login
login = requests.post(url+"login",json={"username":username,"password":password})
print(login.json()["message"]) # Can always be requested to check the API response

# 3.3 Validate access token
validate = requests.get(url+"validate",headers={"Authorization":str(login.json()['access_token'])})
print(validate.json()["message"]) # Can always be requested to check the API response

# ----------------------------------------------------------------------------
# 4. CPT ANALYSIS (INCLUDING LAYER IDENTIFICATION)
# ----------------------------------------------------------------------------

# 4.1 Data import
cpt_data = json.load(open('./input_identification.json', 'r'))

# 4.2 Validate and analyse data
analysis = requests.post(url+"cpt_data",json=cpt_data,headers={"Authorization":str(login.json()['access_token'])})

# 4.3 Convert strings to bytes value and save
create_image("./example_identification",analysis.json()["report_1_png"],analysis.json()["report_1_pdf"])
create_logfile("./logfile_identification",analysis.json()["log_string"])

# ----------------------------------------------------------------------------
# 5. CPT ANALYSIS (WITH YOUR OWN LAYER IDENTIFICATION)
# ----------------------------------------------------------------------------

# 5.1 Data import
cpt_data = json.load(open('./input_no_identification.json', 'r'))

# 5.2 Validate and analyse data
analysis = requests.post(url+"cpt_data",json=cpt_data,headers={"Authorization":str(login.json()['access_token'])})

# 5.3 Convert strings to bytes value and save
create_image("./example_no_identification",analysis.json()["report_1_png"],analysis.json()["report_1_pdf"])
create_logfile("./logfile_no_identification",analysis.json()["log_string"])
