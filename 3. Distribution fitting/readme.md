### **DISTRIBUTION FITTING**

This readme provides a description of the bootstrapping functionality.

#### **1. DESCRIPTION**

Performs a distribution fitting analysis based on provided input data and
a bootstrap and quantile quantile analysis.

#### **2. INPUT**

The following input is required from the user in a .JSON file. Examples can be   
found in the JSON files in this folder.

##### **2.1 REQUIRED**

The following input is required to run the analysis:

**data :**  data array with values   
**bootstrap_total :** number of bootstraps to be performed   
**boostrap_single :** amount of samples per bootstrap analysis

Example input files are provided in *input.json*.

##### **2.2 OPTIONAL**

The following input is optional and improves or completes the analysis:

**selected_dist :** pre-selected distribution (uniform, normal, exponential)
**parname :** name of the parameter   
**parunit :** unit of the parameter   
**confidence_interval :** confidence interval used as integer (standard 95%)   
**title :** title of the analysis provided by user     
**ref1:** reference provided by the user    
**made_by :** name of the user  

More references can be provided by keywords **ref2**, **ref3** (and onwards).

#### **3. RETURNS**

If the input is passed to the API correctly the following items will return:

**results :** Library with the results of the analysis   
**report_1_png :** PNG output report in bytes (to be converted by user)   
**report_1_pdf :** PDF output report in bytes (to be converted by user)   
**report_2_png :** PNG output report in bytes (to be converted by user)   
**report_2_pdf :** PDF output report in bytes (to be converted by user)   
**report_3_png :** PNG output report in bytes (to be converted by user)   
**report_3_pdf :** PDF output report in bytes (to be converted by user)   
**log_string :** Logfile with the computational steps and details (see example)

The reports and logfiles are passed in bytes. Conversion functions are provided   
in *example.py*.
