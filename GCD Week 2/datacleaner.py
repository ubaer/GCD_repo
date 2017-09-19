import pandas as pd

data = pd.read_csv("dirtydata.csv")
gender_column = data['What is your gender?']
# Capitalisation is irrelevant because it will be transformed to lower case
accepted_genders = ['male', 'female']
rename_genders_male = ['m', 'man']
rename_genders_female = ['f', 'v', 'vrouw']
rownumber = 0
for row in gender_column:
    gender = str(row).lower()

    if (gender in rename_genders_male):
        gender = 'male'
    if (gender in rename_genders_female):
        gender = 'female'

    if (gender in accepted_genders):
        data.set_value(rownumber, 'What is your gender?', gender)
    else:
        data.set_value(rownumber, 'What is your gender?', 'NAN')
    rownumber = rownumber + 1

data.to_csv("cleaneddata.csv")
