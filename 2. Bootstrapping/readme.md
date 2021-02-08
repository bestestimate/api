![header_github](https://bestestimate.nl/images/header_github.png)

### **BOOTSTRAPPING**

This readme provides a description of the bootstrapping functionality.

#### **1. DESCRIPTION**

Performs bootstrap analysis based on provided input data array and user
specific sampling requests.

*API ENDPOINT : http://mole.bestestimate.nl/bootstrap*

#### **2. INPUT**

The following input is required from the user in a .JSON file. An example can be   
found in the JSON file in this folder.

##### **2.1 REQUIRED**

The following input is required to run the analysis:

**data :**  data array with values   
**bootstrap_total :** number of bootstraps to be performed   
**boostrap_single :** amount of samples per bootstrap analysis

Example input files are provided in *input.json*.

##### **2.2 OPTIONAL**

The following input is optional and improves or completes the analysis:

**parname :** name of the parameter   
**parunit :** unit of the parameter   
**confidence_interval :** confidence interval used as integer (standard 95%)   
**title :** title of the analysis provided by user     
**ref1:** reference provided by the user    
**made_by :** name of the user  

More references can be provided by keywords **ref2**, **ref3** (and onwards).

#### **3. RETURNS**

If the input is passed to the API correctly the following items will return:

**results :** library with the results of the analysis   
**report_1_png :** PNG output report in bytes (to be converted by user)   
**report_1_pdf :** PDF output report in bytes (to be converted by user)   
**log_string :** logfile with the computational steps and details (see example)

The reports and logfiles are passed in bytes. Conversion functions are provided   
in *example.py*.
