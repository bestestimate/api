![header_github](https://bestestimate.nl/images/header_github.png)

### **RELIABILITY ANALYSIS**

This readme provides a description of the direct reliability analysis.

#### **1. DESCRIPTION**

Performs a direct reliability analysis for a limit state function based   
on the input of the user provided and the parametric variabilities.

#### **2. INPUT**

The following input is required from the user in a .JSON file. Examples can be   
found in the JSON files in this folder.

##### **2.1 REQUIRED**

The following input is required to run the analysis:

**parameters :**  parametric distributions provided (see *input.json*)  
**analysis_type :** type of analysis (specific name to be performed)   
**amount_of_simulations :** amount of simulations to be performed

An example input file is provided in *input.json*.

##### **2.2 OPTIONAL**

The following input is optional and improves or completes the analysis:

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

The reports and logfiles are passed in bytes. Conversion functions are provided   
in *example.py*.

#### **4. NOTES**

It is possible to add customized **analysis_types**. Please [reach out](https://bestestimate.nl/menu_reach_out.html) if needed.
