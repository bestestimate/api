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
key = 'FILL_IN_API_KEY_HERE'

# 3.2 Login
login = requests.post(url+"login",json={"key":key})
print(login.json()["message"]) # Can always be requested to check the API response

# 3.3 Validate access token
validate = requests.get(url+"validate",headers={"Authorization":str(login.json()['access_token'])})
print(validate.json()["message"]) # Can always be requested to check the API response

# ----------------------------------------------------------------------------
# 4. DISTRIBUTION FITTING
# ----------------------------------------------------------------------------

# 4.1 Data import
dist_data = json.load(open('./input_fit.json','r'))

# 4.2 Validate and analyse data
analysis = requests.post(url+"distribution",json=dist_data,headers={"Authorization":str(login.json()['access_token'])})

# 4.3 Convert strings to bytes value and save
create_image("example_fit_1",analysis.json()["report_1_png"],analysis.json()["report_2_pdf"])
create_image("example_fit_3",analysis.json()["report_2_png"],analysis.json()["report_2_pdf"])
create_image("example_fit_2",analysis.json()["report_3_png"],analysis.json()["report_3_pdf"])
create_logfile("logfile_fit",analysis.json()["log_string"])

# ----------------------------------------------------------------------------
# 5. DISTRIBUTION FITTING (WITH DISTRIBUTION ALREADY SELECTED)
# ----------------------------------------------------------------------------

# 5.1 Data import
dist_data = json.load(open('./input_selected.json','r'))

# 5.2 Validate and analyse data
analysis = requests.post(url+"distribution",json=dist_data,headers={"Authorization":str(login.json()['access_token'])})

# 5.3 Convert strings to bytes value and save
create_image("example_selected",analysis.json()["report_2_png"],analysis.json()["report_2_pdf"])
create_logfile("logfile_selected",analysis.json()["log_string"])

# ----------------------------------------------------------------------------
# 6. DISTRIBUTION FITTING (TRUNCATED)
# ----------------------------------------------------------------------------

# 6.1 Data import
dist_data = json.load(open('./input_truncated.json','r'))

# 6.2 Validate and analyse data
analysis = requests.post(url+"distribution",json=dist_data,headers={"Authorization":str(login.json()['access_token'])})

# 6.3 Convert strings to bytes value and save
create_image("example_truncated",analysis.json()["report_2_png"],analysis.json()["report_2_pdf"])
create_logfile("logfile_truncated",analysis.json()["log_string"])

