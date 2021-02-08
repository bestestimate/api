![header_github](https://bestestimate.nl/images/header_github.png)

### **SOIL PROFILE ASSESSMENT**

This readme provides a description of the distribution fitting functionality.

#### **1. DESCRIPTION**

Performs soil profiling based on a quantile regression analysis and    
provided parametric correlations with CPT data provided.

#### **2. INPUT**

The following input is required from the user in a .JSON file. Examples can be   
found in the JSON files in this folder.

##### **2.1 REQUIRED**

The following input is required to run the analysis:

**d :**  depth array in m   
**qc :** cone resistance array in MPa (same length as d)   
**fs :** shaft resistance array in MPa (same length as d)   

Example input files are provided in *input.json*.

##### **2.2 OPTIONAL**

The following input is optional and improves or completes the analysis:

**layers :** layers provided by the user (corresponding to depth array in m)   
**title :** title of the analysis provided by user     
**ref1:** reference provided by the user    
**made_by :** name of the user  
**confidence_interval :** confidence interval used as integer (standard 95%)   

More references can be provided by keywords **ref2**, **ref3** (and onwards).

#### **3. RETURNS**

If the input is passed to the API correctly the following items will return:

**results :** library with the results of the analysis   
**report_1_png :** PNG output report in bytes (to be converted by user)   
**report_1_pdf :** PDF output report in bytes (to be converted by user)   
**log_string :** logfile with the computational steps and details (see example)

The reports and logfiles are passed in bytes. Conversion functions are provided   
in *example.py*.


#### **4. NOTES**

Please note the following regarding the analysis:

* If layers are not provided the layer identification algorithm is used
* Density estimated according to Robertson 1990
* Undrained shear strength estimated with factor (Nk) of 14
* Friction angle estimated based on Bolton XXX???

It is possible to add customized formulations. Please [reach out](https://bestestimate.nl/menu_reach_out.html) if needed.
