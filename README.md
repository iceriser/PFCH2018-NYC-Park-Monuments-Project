# PFCH2018-NYC-Park-Monuments-Project
Repository of files for PFCH final project based on NYC park monuments.

Description:
These scripts are designed to pull information from a publically available csv about New York park
monuments and combine that information with data harvested from wikidata into a single file. The goal is to 
produce a file containing all this information that can be easily analyzed and used to expose interesting correlations 
between information about the artist and information about the artwork. The csv is first used to compile a list 
of artist names. Those names are then associated with information about what borough and park the artist's works are 
located in, the materials those monuments are made of, and the cost of the monuments themselves. All 
of this information is taken from the csv. Then, the list of names is resolved with page names on
wikidata. Pages that match based on name, aliases, and occupation have the artist's birthdate, birthplace,
death date, and place of death information harvested and associated with the corresponding entry on the 
list of names. Once all the information is together, it is output in the form of a json file, which can
then be run through another script to put the information in a form more suitable for data visualization
through programs like Tableau Public.


Instructions:
If you wish to test the functioning of the script it is important that you download the following files:

NYC_Parks_Monuments.csv: This is used to create the list of artist names and also contains important data
for harvesting.

monumentdata.py: this is the script that runs all of the functions and outputs the first json file. This
is the script you actually run to test everything as a whole.

namelistfunction.py: this script contains the function that compiles the name list from the csv.

csvdatafunction.py: this script contains the function that harvests necessary data from the csv.

wikidatafunction.py: this script contains the function that harvests data from wikidata.

filetransformation.py: after you run monumentdata.py, you run this script on the json file it produced
to create a file more suitable for use with data visualization programs.


Optional Downloads:
functiontest.py: this script is set up to test the three functions used in monumentdata.py without having
to run monumentdata.py every time. It could be useful if you'd like to test the functions yourself.

monumentdata.json: this is an example of the product of monumentdata.py. If you'd like to test 
filetransformation.py without running monumentdata.py first, feel free to download this file.

monumentdatafix.json: this is an example of the product of filetransformation.py. If you'd like to try
creating your own data visualizations without running the scripts first, you could download this file.


Data Visualizations:
Some examples of data visualizations created from analysis of monumentdatafix.json can be found on this github, 
listed as "Sheet 1.png", "Sheet 2.png", and "Sheet 3.png". 

Please also download "NYC Park Monuments Visualization Companion Document.docx" for explanations of and commentary 
on these visualizations.
