#### Description

This repo contains the python code to generate the csv data and anonymise the pii data such as first_name, last_name and the address.
Faker Python library is used to genrate the data and Anonympy Python library is used to anonymise the data.

#### Script Name

Anonymise_Customer_information.py

#### Details.
This script when run produces 2 files.
1) input_pii_data_file.csv is genrated with sample data using Faker Library
2) anonymised_pii_data_file.csv is generated with the anonymised data using anonympy library

#### Detailed Steps

1) Sample data is generated and saved to input_pii_data_file.csv.
2) The sample data generated in above step is loaded, then anonymised and written to the anonymised_pii_data_file

#### Run Instructions

This script can be run in any Editor like pycharm.
Also it can be run in the command Prompt,

Download the code to the local machine and run the below command in the command prompt in the directory where the script is downloaded.

python Anonymise_Customer_information.py