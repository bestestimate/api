# DATA STUDY - CONE PENETRATION TEST DATA

This readme describes how to use the cone penetration test data study
functionality in *MOLE*. Refer to the main page for a generic introduction to
usage of the API.

### GOAL OF FUNCTIONALITY

Performs Robertson classification and layer identification based on the
user input of CPT data.

#### INPUT

The following input is required from the user in a .JSON file. Examples can
be found in the JSON files in this folder.

## Required

The following input is required to run the analysis:

* d: Depth array in m
* qc: Cone resistance array in MPa (same length as d)
* fs: Shaft resistance array in MPa (same length as d)

## Optional

The following input is optional and improves or completes the analysis:

* title: Title of the analysis provided by user
* ref1: Reference provided by the user
* made_by: Users name
* layers: Array with depth points of layers identified in m

When the user provides layers the layer identification step of the algorithm
is skipped. This allows for correction as well as skipping this part.

#### RETURNS

If the input is passed to the API correctly the following items will return:

* results: Library with the results of the analysis
* report_1_png: PNG output report in bytes (to be converted by user)
* report_1_pdf: PDF output report in bytes (to be converted by user)
* log_file: Logfile with the computational steps and details (see example)

#### NOTES

Please note that the xx
