![header_github](https://bestestimate.nl/static/images/header_github.png)

Reliability analyses can range from small to large. Engineering can be based on statistics from start to finish.
But most likely (and sometimes preferably) at critical intermediate steps in between. *MOLE* is a tailor made API specifically developed to suit such demands. Please read more in detail on [this page](https://bestestimate.nl/api.html).

#### BEFORE YOU START
This public repository shows several examples of how different analyses can be performed using the currently released web-API. To execute these examples (or even better, your own reliability analysis) please follow these steps:

1. Subscribe on [this page](https://bestestimate.nl/api.html)
2. Receive access codes and guidance for use of MOLE
3. Fill in your input file and run the analysis in only 5 lines of code

The public version of *MOLE* can be used for many examples. However, in some cases adaptations might be required (for instance adding a limit state for direct reliability analyses). Please [reach out](https://bestestimate.nl/reach_out.html) in case you would like an added functionality or an update to the API.

#### REQUIREMENTS
*MOLE* is a web-API which means there are very little dependencies. The examples provided in this repository use Python (any other language can be used as well). In Python the following packages are required for running the analyses (and retrieving the output).
* Requests
* JSON
* Base64

#### HOW DOES IT WORK?
Every analysis works in the same way using simple steps:
1. Fill out the input file
1. Login to the API with your [login details](https://bestestimate.nl/api.html)
1. Receive your authorization token for further works
1. Send your input to the API endpoint and wait for the results
1. Save your output reports, logfiles or work further with the outcomes  

See the folders with examples to check login and API procedures.

#### FEATURES
The following features are currently available through the public version of *MOLE*:
1. Soil profile layer identification based on CPT data
1. Bootstrap analysis
1. Distribution fitting
1. Parameter estimation over depth with quantile regression
1. Direct reliability analysis
1. Copula analysis (beta)

Works is continuously being improved and developed. Please [check out this page](https://bestestimate.nl/disclaimer.html) for more information.

#### CONTACT & LICENSE
Created by [@joostremmers](https://bestestimate.nl/reach_out.html). For information and license agreements reference is made to [this page](https://bestestimate.nl/index_disclaimer.html).
