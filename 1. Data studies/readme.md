![header_github](https://bestestimate.nl/images/header_github.png)

### **DATA STUDY - CONE PENETRATION TEST DATA**

This readme provides a description of the CPT data study functionality.

#### **1. DESCRIPTION**

Performs Robertson classification and layer identification based on the input   
of CPT data and returns reports and identified layers.

*API ENDPOINT : http://mole.bestestimate.nl/cpt_data*

#### **2. INPUT**

The following input is required from the user in a .JSON file. Examples can be   
found in the JSON files in this folder.

##### **2.1 REQUIRED**

The following input is required to run the analysis:

**d :**  depth array in m   
**qc :** cone resistance array in MPa (same length as d)   
**fs :** shaft resistance array in MPa (same length as d)

Example input files are provided in:

* *input_with_specified_layers.json* (excluding layer identification)
* *input_withouth_specified_layers.json* (including layer identification)

##### **2.2 OPTIONAL**

The following input is optional and improves or completes the analysis:

**title :** title of the analysis provided by user  
**ref1:** reference provided by the user  
**made_by :** name of the user  
**moving_box :** height of the moving box for the filtering algorithm in m
**layers :** array with depth points of layers identified in m

More references can be provided by ref2, ref3 (and onwards).

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

* The moving bandwidth window applied is standard 0.5 m
* The layers smaller than 0.2 m are ignored in the analysis
* Correction of the analysis is possible via the input argument **layers**
