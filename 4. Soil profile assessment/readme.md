![header_github](https://bestestimate.nl/static/images/header_github.png)

### **SOIL PROFILE ASSESSMENT**

This readme provides a description of the soil profile assessment functionality.

#### **1. DESCRIPTION**

Performs soil profiling based on a quantile regression analysis and    
provided parametric correlations with CPT data provided.

*API ENDPOINT : https://bestestimate.nl/profile_analysis*

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
**moving_box :** height of the moving box for the filtering algorithm in m   
**layers :** array with depth points of layers identified in m   
**undrained_shear_strength_factor :** array with undrained shear strength factor per layer   
**critical_volume_angle :** array with critical volume angle per layer

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

* Correction of the analysis is possible via the input argument **layers**
* The moving bandwidth window applied is standard 0.5 m
* The layers smaller than 0.2 m are ignored in the analysis
* Density estimated according to Robertson (2010)
* Undrained shear strength estimated with factor (Nk) of 14
* Friction angle estimated based on Jefferies and Been (2006)

It is possible to add customized formulations. Please [reach out](https://bestestimate.nl/reach_out.html) if needed.
