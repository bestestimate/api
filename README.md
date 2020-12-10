![header_github](https://bestestimate.nl/images/header_github.png)

Reliability analyses can range from small to large. Engineering can be based on statistics from start to finish.
But most likely (and sometimes preferably) at critical intermediate steps in between. *MOLE* is a tailor made toolbox specifically developed to suit such demands. Please read more in detail on [this page](https://bestestimate.nl/menu_mole.html).

#### BEFORE YOU START
This public repository shows several examples of how different analyses can be performed using the currently released web-API. To execute these examples (or even better, your own reliability analysis) please follow these steps:

1. Subscribe on [this page](https://bestestimate.nl/menu_mole.html)
2. Receive access codes and guidance for use of MOLE
3. Fill in your input file and run the analysis in only 5 lines of code

The public version of *MOLE* can be used for many examples. However, in some cases adaptations might be required (for instance adding a limit state for direct reliability analyses). Please [reach out](https://bestestimate.nl/menu_reach_out.html) in case you would like an added functionality or an update to the API.

#### REQUIREMENTS
*MOLE* is a web-API which means there are very little dependencies. The examples provided in this repository use Python (any other language can be used as well). In Python the following packages are required for running the analyses (and retrieving the output).
* Requests
* JSON
* Base64

#### HOW DOES IT WORK?
Every analysis works in the same way using 3 simple steps:
1. Fill out the input file (see example pages)
1. Login to the API with your received details (http://mole.bestestimate.nl/)
1. Send your input to the API, run the analysis and save output!

#### FEATURES
The following features are currently available through the public version of *MOLE*:
* Bootstrap analysis
* Distribution fitting (Uniform, Gaussian, Exponential)
* Direct reliability analysis (*[reach out](https://bestestimate.nl/menu_reach_out.html) for custom limit states*)
* Soil profile layer identification based on CPT data
* Parameter estimation over depth with quantile regression

Works are ongoing to expand the amount of features. Please [check out this page](https://bestestimate.nl/ex_to_be_developed.html) for more information.

#### CONTACT
Created by [@joostremmers](https://bestestimate.nl/index_myself.html) - reach out in case of questions, bugs or errors.
