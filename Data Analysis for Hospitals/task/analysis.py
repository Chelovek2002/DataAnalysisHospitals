import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', 8)
df_general = pd.read_csv('test/general.csv')
df_prenatal = pd.read_csv('test/prenatal.csv')
df_sports = pd.read_csv('test/sports.csv')
df_prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
df_sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

df_agg = (pd.concat([df_general, df_prenatal, df_sports], ignore_index=True)
          .drop(columns='Unnamed: 0')
          .dropna(axis='rows', how='all'))

df_agg.gender.replace(['female', 'woman', 'male', 'man'], ['f', 'f', 'm', 'm'], inplace=True)


def hospital(name):
    return df_agg.hospital == name


def diagnosis(diagnosis):
    return df_agg.diagnosis == diagnosis


def count_cond(condition):
    return df_agg.loc[condition].value_counts()


df_agg.loc[hospital('prenatal'), 'gender'] = df_agg.loc[hospital('prenatal'), 'gender'].fillna('f')
df_agg.iloc[:, 5:] = df_agg.iloc[:, 5:].fillna(0)

sns.histplot(data=df_agg, x='age', kde=True, binwidth=5)
first = '15-35'
plt.show()
df_agg.diagnosis.value_counts().plot.pie()
second = 'pregnancy'
plt.show()
sns.violinplot(y=df_agg["height"], x=df_agg["hospital"])
plt.show()

print("""The answer to the 1st question: 15-35
The answer to the 2nd question: pregnancy
The answer to the 3rd question: It's because for general and prenatal hospitals height is measured in meters, while for sports hospitals it's measured in foots""")
# first = df_agg.hospital.describe()['top']
#
# second = round(count_cond(diagnosis('stomach') * hospital('general')) / count_cond(hospital('general')), 3)
#
# third = round(count_cond(hospital('sports') * diagnosis('dislocation')) / count_cond(hospital('sports')), 3)
#
# fourth = df_agg.loc[hospital('general'), 'age'].median() - df_agg.loc[hospital('sports'), 'age'].median()
#
# fifth_1 = df_agg[df_agg.blood_test == 't'].groupby('hospital').count().idxmax('rows')[0]
# fifth_2 = count_cond((df_agg.blood_test == 't')*hospital(fifth_1))
# print(f"""The answer to the 1st question is {first}
# The answer to the 2nd question is {second}
# The answer to the 3rd question is {third}
# The answer to the 4th question is {fourth}
# The answer to the 5th question is {fifth_1}, {fifth_2} blood tests""")
