MedPack is a python script used to create and search a JSON file derived of all medications downloaded directly from the United States’ OpenFDA.gov website. This does so without using their API is split into two parts. One part is the python script which can be called upon as a module. This script will allow the user to generate lists in python of medications fitting their search criteria. This is useful for a pipelined project. Included as well is a widget function included in a Jupyter-Notebook. This allows the user to explore the contents of the OpenFDA medications without the need for coding.

To run the MedPack Script, it is recommended to use Python version 3. The libraries used are available in the requirements.txt

The installation of Anaconda is highly recommended. Anaconda is a free open source project by the Anaconda Inc. Upon installing it, Jupyter Notebook and several basic Python Data Science libraries wil be installed.

For more information on Anaconda, please see their official documentation:
https://media.readthedocs.org/pdf/anaconda-installer/latest/anaconda-installer.pdf

For more information on Jupyter Notebook, please see their official documentation:
https://media.readthedocs.org/pdf/jupyter-notebook/latest/jupyter-notebook.pdf

First Launch and MedPack.update()
The most important part of this module is the update() function. Running this function is essential if you are beginning with the MedPack.py module. It will set up your environment for you. 
Please keep in mind that all work done by the function will be in the same immediate directory. Therefore, please keep MedPack.py and your working Jupyter Notebook or Python folder in the same directory. 
 

Running the MedPack.update() function begins to download directly from the Open FDA website. This may take around 10 minutes depending on your computer speed.

If “Clean up Complete” is shown, your environment has successfully been set up in your folder.

 
During the running of the update() function, MedPack:
1.	Calls upon the OpenFDA documentation for available downloads.
2.	Creates downloads lists.
3.	Downloads Zip files for each of the list.
4.	Unzips the JSON files within the zip files and compiles them into one JSON file specific to MedPack.
5.	Creates supporting documentation in the form of lists for each categorical variable of the medications.
6.	Deletes the original JSON files and relevant zip files downloaded from OpenFDA

The main JSON containing all medications is titled FDAdrugs.json

Supporting Documents:

•	rxcui.txt

•	pharm_classes product_types routes.csv

•	substance_name.txt

•	product_ncd.txt


The supporting documents all list out all categorical variables from our FDAdrugs.json file. This file contains all the medication information that will be used later.
 

Structuring of Drugs JSON
During the update() function, MedPack downloads and extracts the following from the original Open FDA data:

•	indications_and_usage

•	pharm_class_epc

•	pharm_class_moa

•	product_ndc

•	product_type

•	route

•	rxcui

•	substance_name




**Jupyter Notebook Widgets**

For simple code free browsing of the medications available, the Jupyter Notebook MedPackwidgets.ipynb was created. If you do not have this file, the code to produce the widgets is shown in the images. This must be run on a jupyter notebook in order to work.


Here is the basic search widget produced. The inputs for each are as follows:

•	indications_and_usage 

•	pharm_class_epc 

•	pharm_class_pe 

•	product_ndc  

•	product_type 

•	route

•	rxcui 

•	substance_name

•	pharm_class_moa 

The second widget searches categorical variables from our supporting files.
Fill in text under any criteria and hit run interact. 
 
The options for this are:

•	pharm_class_epc

•	pharm_class_pe

•	pharm_class_moa

•	route

•	product_type



**Search Drugs Function**

MedPack.py contains a search_drug function which is meant for integrating directly into a workflow.

The function for search drugs is structures as:
search_drugs(name = 'no_name', indications_and_usage = None, pharm_class_epc = None, pharm_class_pe = None, product_ndc  = None, product_type = None, route = None, rxcui = None, substance_name = None, pharm_class_moa = None, JSON = False, CSV = False, pretty_list = False):
	
name : str, optional, default ‘no_name’

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When outputting a file, the string entry becomes the file’s name. 

indications_and_usage : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under indications_and_usage parameter for items in the FDA drug database.

pharm_class_epc : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under pharm_class_epc parameter (Established Pharmacologic Class) for items in the FDA drug database.

pharm_class_pe :  str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under pharm_class_pe parameter (Physiologic Effect) for items in the FDA drug database.

product_ndc  : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under product_ndc parameter (Product National Drug Code) for items in the FDA drug database.

product_type  : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under product_type parameter (Human prescription drug or Human over the counter drug) for items in the FDA drug database.

route : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under route parameter (route of administration) for items in the FDA drug database.

rxcui : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under rxcui parameter (RxNorm concept unique identifer for the clinical drug or substance) for items in the FDA drug database.

substance_name : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under substance_name (Name of the main substance in the drug) parameter for items in the FDA drug database.

pharm_class_moa : str, optional, default None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entry searches under pharm_class_moa (Drug’s method of action) parameter for items in the FDA drug database.

JSON : str, optional, default False

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When True, this tells the function to create a JSON file containing the results with the name under the name input.

CSV : bool, optional, default False

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When True, this tells the function to create a CSV file containing the results with the name under the name input.

pretty_list : bool, optional, default False

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When True, this takes the original return of the list function and returns only unique entries from the results.

Note that all of the entries must be string and in parenthesis “”

