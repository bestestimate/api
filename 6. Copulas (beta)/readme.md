![header_github](https://bestestimate.nl/images/header_github.png)

### **COPULA ASSESSMENT (BETA)**

This readme provides a description of the joint variability assessment with copulas.

#### **1. DESCRIPTION**

Performs a distribution fitting analysis of copulas based on two provide input
datasets.

*API ENDPOINT : http://mole.bestestimate.nl/copulas*

#### **2. INPUT**

The following input is required from the user in a .JSON file. Examples can be   
found in the JSON files in this folder.

##### **2.1 REQUIRED**

The following input is required to run the analysis:

**parameter_1 :**  dictionary with data input for parameter 1  
**parameter_2 :**  dictionary with data input for parameter 2

Each parameter dataset can be provided with the following sub-entries:

**data :**  samples   
**parname :**  name of the parameter   
**parunit :**  unit of the parameter   
**selected_dist :** pre-selected distribution (uniform, normal, lognormal, exponential)     

Example input files are provided in *input.json*.

##### **2.2 OPTIONAL**

The following input is optional and improves or completes the analysis:

**selected_copula :** pre-selected copula (gaussian, clayton, frank, gumbel)   
**title :** title of the analysis provided by user     
**ref1:** reference provided by the user  
**made_by :** name of the user  

More references can be provided by keywords **ref2**, **ref3** (and onwards).

#### **3. RETURNS**

If the input is passed to the API correctly the following items will return:

**results :** library with the results of the analysis   
**report_1_png :** PNG output report in bytes (to be converted by user)   
**report_1_pdf :** PDF output report in bytes (to be converted by user)   
**report_2_png :** PNG output report in bytes (to be converted by user)   
**report_2_pdf :** PDF output report in bytes (to be converted by user)   
**log_string :** logfile with the computational steps and details (see example)

The reports and logfiles are passed in bytes. Conversion functions are provided in *example.py*.

#### **4. NOTES**

It is possible to add additional distributions. Please [reach out](https://bestestimate.nl/menu_reach_out.html) if needed.
