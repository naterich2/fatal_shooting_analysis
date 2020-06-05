### Written by Nate Richman
### 2020-06-04

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from scipy.stats import fisher_exact


data = pd.read_csv('data-police-shootings/fatal-police-shootings-data.csv',index_col=0)
total_by_race = data.loc[:,'race'].value_counts()


############Armed or not
armed = data[data['armed'] != 'unarmed']
unarmed = data[data['armed'] == 'unarmed']

###########Armed/unarmed contingency
armed_nums = armed.loc[:,'race'].value_counts()
unarmed_nums = unarmed.loc[:,'race'].value_counts()

# Give columns names
armed_nums.name = 'armed'
unarmed_nums.name = 'unarmed'
#Join into race x armed table
cont_table = armed_nums.to_frame().join(unarmed_nums.to_frame()).T
chi2,p,dof,expected = chi2_contingency(cont_table.loc[:,['W','B','H']].values)

oddsratio,p = fisher_exact(cont_table.loc[:,['W','B']].values)


############Mental Illness or not
ment_ill = data[data['signs_of_mental_illness']]
not_ment_ill = data[~data['signs_of_mental_illness']]

###########Ill/not contingency
ment_ill_nums = ment_ill.loc[:,'race'].value_counts()
ment_ill_nums.name = 'ment_ill'
not_ment_ill_nums = not_ment_ill.loc[:,'race'].value_counts()
not_ment_ill_nums.name = 'not_ment_ill'

ment_cont_table = ment_ill_nums.to_frame().join(not_ment_ill_nums.to_frame()).T
chi2,p,dof,expected = chi2_contingency(ment_cont_table.loc[:,['W','B','H']].values)

oddsratio,p = fisher_exact(ment_cont_table.loc[:,['W','B']].values)


############Threat or not
threat = data[data['threat_level'] == 'attack']
not_threat = data[data['threat_level'] != 'attack']

###########threat/not contingency
threat_nums = threat.loc[:,'race'].value_counts()
threat_nums.name = 'threat'
not_threat_nums = not_threat.loc[:,'race'].value_counts()
not_threat_nums.name = 'not_threat'

threat_cont_table = threat_nums.to_frame().join(not_threat_nums.to_frame()).T
chi2,p,dof,expected = chi2_contingency(threat_cont_table.loc[:,['W','B','H']].values)

oddsratio,p = fisher_exact(threat_cont_table.loc[:,['W','B']].values)

