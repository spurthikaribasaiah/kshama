import csv
import pandas as pd
from faker import Faker
from anonympy.pandas import dfAnonymizer


def generate_data():
    fake = Faker()
    data = []
    for val in range(2):
        data.append([fake.first_name(),fake.last_name(),fake.address().replace('\n',' '),fake.date_of_birth()])
    return data

def generate_csv(mylist):
    data_header = ['first_name','last_name','address','date_of_birth']
    with open('input_pii_data_file.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data_header)
        writer.writerows(mylist)

def anonymise_data(df):
    anonym = dfAnonymizer(df)
    anonym.anonymize({'first_name': 'categorical_fake',
                      'last_name': 'categorical_fake',
                      'address': 'categorical_fake'})
    anonymised_df = anonym.to_df()
    return anonymised_df

def write_to_csv(df, path):
    df.to_csv(path, index=False, encoding='UTF8')

if __name__ == '__main__':
### below code to generate dummy csv data using Fake library
    dummy_data = generate_data()
    generate_csv(dummy_data)

### below code to anonymise the data generated in previous step
    df = pd.read_csv('input_pii_data_file.csv')
    anonymised_df = anonymise_data(df)
##### removing the new line charecter from anonymised dataset's address column
    anonymised_df['address'] = anonymised_df['address'].str.replace('\n',' ',regex=True)

### below code to write the anonymised data to the new file.
    write_to_csv(anonymised_df, 'anonymised_pii_data_file.csv')
