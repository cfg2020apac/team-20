#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np
from operator import itemgetter
import random
import json
import loader

def return_json_var(json_var):
  #json_list = loader.load(json_var)
  return json_var


def build_cats_dict(cats, cats_abbr):
  cats_dict = {cats_abbr[i]:cats[i] for i in range(len(cats))}
  return cats_dict


'''
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
'''


def import_csv(file_path):
  return pd.read_csv(file_path)


def map_oppo_name_cat(program_df):
  program_cat_match = program_df[['impact_area','opportunity_name']]
  program_cat_match = program_cat_match.dropna(how='all')
  program_cat_match = program_cat_match.drop_duplicates()
  return program_cat_match

def oppo_map_to_dict(oppo_map):
  program_cat_match_dict = program_cat_match.set_index('opportunity_name').T.to_dict('list')
  return program_cat_match_dict



def build_feature_matrix(user_df, cats_abbr, cats_dict, feature):
  # Construct features from user data
  user_matrix_id = user_f.connection_id
  user_matrix_gender_female = user_f.gender.str.contains('Female')
  user_matrix_gender_male = user_f.gender.str.contains('Male')
  user_matrix_employment_others = user_f.employment_status.fillna(True)
  d = {'Other': True, 'Not Employed': True, 'Full Time': False, 'Part Time': False}
  user_matrix_employment_others = user_matrix_employment_others.map(d)
  #user_matrix_employment_pt = user_f.employment_status.str.contains('Part Time')
  user_matrix_employment_pt = user_f.employment_status.astype(str).str.contains('Part Time')
  user_matrix_employment_ft = user_f.employment_status.astype(str).str.contains('Full Time')
  user_matrix_employment_retired = user_f.employment_status.astype(str).str.contains('Retired')
  user_matrix_hours_served_total = user_f.hours_served_all
  user_matrix_hours_served_oppo = user_f.hours_served_opportunity
  user_matrix_oppo_cat = user_f.opportunity_name.map(program_cat_match_dict).rename('oppo_cat')

  # Construct features from user interest
  for cat_abbr in cats_abbr:
    tmp_pdseries = user_f.interest_list.str.contains(cats_dict[cat_abbr])
    tmp_pdseries = tmp_pdseries.fillna(False)
    tmp_pdseries = tmp_pdseries.rename('interest_'+cat_abbr)
    vars()['user_matrix_'+'interest_'+cat_abbr] = tmp_pdseries

  # Construct feature matrix from user last joined program
  for cat_abbr in cats_abbr:
    tmp_pdseries = user_matrix_oppo_cat.str.contains(cats_dict[cat_abbr])
    tmp_pdseries = tmp_pdseries.fillna(False)
    tmp_pdseries = tmp_pdseries.rename('oppo_cat_'+cat_abbr)
    vars()['user_matrix_'+'oppo_cat_'+cat_abbr] = tmp_pdseries

  # Construct dummy click response for feedback reinforcement
  dummy_list = [0]*int(len(user_matrix_id)/2)+[1]*(len(user_matrix_id)-int(len(user_matrix_id)/2))
  random.shuffle(dummy_list)
  user_matrix_click_response = pd.Series(dummy_list)
  
  # Build feature matrix for user
  user_matrix = pd.DataFrame(user_matrix_id)
  for attr in feature:
    user_matrix = pd.concat([user_matrix,vars()['user_matrix_'+attr]],axis=1)
    #user_matrix.join(vars()['user_matrix_'+attr])

  # From True/False to 1/0
  user_matrix = user_matrix.replace({True: 1, False: 0}).drop(columns='oppo_cat')
  return user_matrix


## Build Transform matrix
# Can be updated with NN training
def build_transform_matrix(cats, feature):
  transform_mat = np.random.rand(len(cats),len(feature)-1)
  return transform_mat


## Generate prediction result
def gen_pred_result(user_matrix, transform_mat, cats_abbr):
  pred_result_cats = []
  for i in range(len(user_matrix)):
    pred_result_one = np.matmul(transform_mat,np.array(user_matrix.iloc[i].fillna(0).drop('connection_id')))
    highest_three_cat_num = pred_result_one.argsort()[-3:]
    highest_three_cat = itemgetter(*highest_three_cat_num)(cats_abbr)
    pred_result_cats.append(highest_three_cat)
  return pred_result_cats


## Generate recommendation result
def gen_recom_result(user_matrix, pred_result_cats, program_f):
  user_recommend_opportunities_json = []
  for j in range(len(user_matrix)):
    user_recommend_opportunity = []
    blank = 0
    for cat in pred_result_cats[j]:
      #print(cat)
      if program_f['impact_area'].str.contains('Hunger').value_counts(False).iloc[0] == len(program_f):   #'Hungry' as a demo. Can do real search with large enough dataset
        blank += 1
        continue 
      opportunities = program_f[program_f['impact_area'].str.contains('Hunger')]
      user_recommend_opportunity.append(opportunities.iloc[random.randint(0,len(opportunities)-1)])

    if blank == len(pred_result_cats[j]):
      continue

    user_recommend_opportunity = pd.concat(user_recommend_opportunity,axis=1).T
    #print(user_recommend_opportunity)
    user_recommend_opportunity_json = user_recommend_opportunity.to_json(orient='records')
    #user_recommend_opportunities.append(user_recommend_opportunity)
    user_recommend_opportunities_json.append(user_recommend_opportunity_json)
  ## Save to JSON variable
  #user_recommend_opportunities_json = user_recommend_opportunities.to_json(orient='records')
  return user_recommend_opportunities_json
    #user_recommend_opportunity.to_json(r'user_recommend_program_{j}.json'.format(j=j))
    #return user_recommend_opportunity

if __name__ == '__main__':
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
  cats_abbr = ['elderly','disaster','education_young',
               'worker','environment','education_refugee',
               'health','hunger','homeless',
               'education_adult','international','internship',
               'justice','refugee','school','sports',
               'tech','family','arts','civic']
  cats_dict = build_cats_dict(cats, cats_abbr)

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
  user_f = import_csv('handson_data/dummy_volunteer_profile_one.csv')
  program_f = import_csv('handson_data/handson_program.csv')

  ## Uncomment if data is in raw .xlsx
  '''
  ## Clean user data
  # sort column names
  user_f_columns = ['first_name','last_name','interest_list','gender','employment_status','mobile','connection_id','email','attend_status','hours_served_opportunity','hours_served_all','opportunity_name','opportunity_org','opportunity_type','employer','contact_id']
  user_f.columns = user_f_columns
  # Reform the interests to list
  user_f.interest_list = user_f.interest_list.str.replace('?','')
  user_f.interest_list = user_f.interest_list.str.split(';')
  ## Remove weird characters from opportunity_org
  user_f.opportunity_org = user_f.opportunity_org.str.replace('?','')
  '''

  ## Map between event name and cat
  program_cat_match = map_oppo_name_cat(program_f)

  ## Turn map to dict
  program_cat_match_dict = oppo_map_to_dict(program_cat_match)

  ## Build feature matrix
  user_matrix = build_feature_matrix(user_f, cats_abbr, cats_dict, feature)

  ## Build Transform matrix
  transform_mat = build_transform_matrix(cats, feature)

  ## Generate prediction result
  pred_result_cats = gen_pred_result(user_matrix, transform_mat, cats_abbr)

  ## Generate recommendation result
  user_recommend_opportunities_json = gen_recom_result(user_matrix, pred_result_cats, program_f)
  #print(user_recommend_opportunities_json)

  #json_string = json.dumps([ob.__dict__ for ob in user_recommend_opportunities_json])
  #print(json_string)

  ## Return JSON object
  return_json_var(user_recommend_opportunities_json)

