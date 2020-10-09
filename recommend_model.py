#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np
from operator import itemgetter
import random
import json



## Construct category list
cats = ['Assistance and Support for Elderly',
        'Disaster & Emergency Services',
        'Education and Empowerment for Children and Youth',
        'Empowerment and Support for Domestic and Migrant Workers', 
        'Environmental Conservation',
        'Education and Empowerment for Refugees and Asylum Seekers',
        'Health and Wellness',
        'Hunger & Homelessness', 
        'Support for Homeless People',
        'Adult Education',
        'International Service',
        'Internships & Employment',
        'Justice & Legal Services',
        'Refugee & Asylum Seekers Services',
        'Schools',
        'Sports & Recreation',
        'Technology',
        'Family Services',
        'Arts & Culture',
        'Civic & Community']
print(len(cats))
cats_abbr = ['elderly','disaster','education_young',
             'worker','environment','education_refugee',
             'health','hunger','homeless',
             'education_adult','international','internship',
             'justice','refugee','school','sports',
             'tech','family','arts','civic']
cats_dict = {cats_abbr[i]:cats[i] for i in range(len(cats))}




## construct skill set
skills = ['Accounting / finance',
          'Administrative/general office support',
          'Communications and marketing',
          'Fundraising',
          'Gardening',
          'Graphic design',
          'Health / medical',
          'Event management',
          'Human resources',
          'IT',
          'Legal',
          'Photography',
          'Project management',
          'Teaching/Training/Fine arts',
          'Teaching/Training/Fitness/sports',
          'Teaching/Training/Music/drama',
          'Teaching/Training/Health',
          'Teaching/Training/IT',
          'Translation',
          'Videography']




## Construct feature map for user
feature = ['gender_female','gender_male',
           'employment_pt','employment_ft','employment_retired','employment_others',
           'hours_served_total','hours_served_oppo','oppo_cat',
           'interest_elderly','interest_disaster','interest_education_young',
           'interest_worker','interest_environment','interest_education_refugee',
           'interest_health','interest_hunger','interest_homeless',
           'interest_education_adult','interest_international','interest_internship',
           'interest_justice','interest_refugee','interest_school','interest_sports',
           'interest_tech','interest_family','interest_arts','interest_civic',
           'oppo_cat_elderly','oppo_cat_disaster',
           'oppo_cat_education_young','oppo_cat_worker',
           'oppo_cat_environment','oppo_cat_education_refugee',
           'oppo_cat_health','oppo_cat_hunger',
           'oppo_cat_homeless','oppo_cat_education_adult',
           'oppo_cat_international','oppo_cat_internship',
           'oppo_cat_justice','oppo_cat_refugee',
           'oppo_cat_school','oppo_cat_sports',
           'oppo_cat_tech','oppo_cat_family',
           'oppo_cat_arts','oppo_cat_civic',
           'click_response']




## Import user & program data
user_f = pd.read_csv('data/volunteer_profile.csv')
program_f = pd.read_csv('data/handson_program.csv')

## Clean user data
# sort column names
user_f_columns = ['first_name','last_name','interest_list','gender','employment_status','mobile','connection_id','email','attend_status','hours_served_opportunity','hours_served_all','opportunity_name','opportunity_org','opportunity_type','employer','contact_id']
user_f.columns = user_f_columns
# Reform the interests to list
user_f.interest_list = user_f.interest_list.str.replace('?','')
user_f.interest_list = user_f.interest_list.str.split(';')
## Remove weird characters from opportunity_org
user_f.opportunity_org = user_f.opportunity_org.str.replace('?','')


## Map between event name and cat
program_cat_match = program_f[['impact_area','opportunity_name']]
program_cat_match = program_cat_match.dropna(how='all')
program_cat_match = program_cat_match.drop_duplicates()


## Turn map to dict
program_cat_match_dict = program_cat_match.set_index('opportunity_name').T.to_dict('list')



## Construct feature matrix from user data
user_matrix_id = user_f.connection_id
user_matrix_gender_female = user_f.gender.str.contains('Female')
user_matrix_gender_male = user_f.gender.str.contains('Male')
user_matrix_employment_pt = user_f.employment_status.str.contains('Part Time')
user_matrix_employment_ft = user_f.employment_status.str.contains('Full Time')
user_matrix_employment_retired = user_f.employment_status.str.contains('Retired')
d = {'Other': True, 'Not Employed': True, 'Full Time': False, 'Part Time': False}
user_matrix_employment_others = user_f.employment_status.map(d)
user_matrix_employment_others = user_matrix_employment_others.fillna(True)
user_matrix_hours_served_total = user_f.hours_served_all
user_matrix_hours_served_oppo = user_f.hours_served_opportunity
user_matrix_oppo_cat = user_f.opportunity_name.map(program_cat_match_dict).rename('oppo_cat')



## Construct feature matrix from user interest
for cat_abbr in cats_abbr:
    tmp_pdseries = user_f.interest_list.str.contains(cats_dict[cat_abbr])
    tmp_pdseries = tmp_pdseries.fillna(False)
    tmp_pdseries = tmp_pdseries.rename('interest_'+cat_abbr)
    vars()['user_matrix_'+'interest'+cat_abbr] = tmp_pdseries




## Construct feature matrix from user last joined program
for cat_abbr in cats_abbr:
    tmp_pdseries = user_matrix_oppo_cat.str.contains(cats_dict[cat_abbr])
    tmp_pdseries = tmp_pdseries.fillna(False)
    tmp_pdseries = tmp_pdseries.rename('oppo_cat_'+cat_abbr)
    vars()['user_matrix_'+'oppo_cat_'+cat_abbr] = tmp_pdseries


## Construct dummy click response for feedback reinforcement
user_matrix_click_response = pd.Series([random.shuffle([0]*int(len(user_matrix_id)/2))+[1]*(len(user_matrix_id)-int(len(user_matrix_id)/2))])


## Build feature matrix for user
user_matrix = pd.DataFrame(user_matrix_id)
for attr in feature:
    user_matrix = pd.concat([user_matrix,vars()['user_matrix_'+attr]],axis=1)
    
user_matrix = user_matrix.replace({True: 1, False: 0}).drop(columns='oppo_cat')



## Build Transform matrix
transform_mat = np.random.rand(len(cats),len(feature)-1)



## Generate prediction result
pred_result_cats = []
for i in range(len(user_matrix)):
    pred_result_one = np.matmul(transform_mat,np.array(user_matrix.iloc[i].fillna(0).drop('connection_id')))
    highest_three_cat_num = pred_result_one.argsort()[-3:]
    highest_three_cat = itemgetter(*highest_three_cat_num)(cats_abbr)
    pred_result_cats.append(highest_three_cat)


user_recommend_opportunity = []
for j in range(len(user_matrix_id):
    for cat in pred_result_cats[j]:
        if program_f['impact_area'].str.contains(cat).value_counts(False) == len(program_f):
          continue 
        opportunities = program_f[program_f['impact_area'].str.contains(cat)]
        user_recommend_opportunity.append(opportunities.iloc[random.randint(0,len(opportunities)-1)])

    user_recommend_opportunity = pd.concat(user_recommend_opportunity,axis=1).T

    ## Save to JSON
    user_recommend_opportunity.to_json(r'user_recommend_program_{j}.json'.format(j=j))

