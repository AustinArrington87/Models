import requests
import json

# Load in MRV Data to Translator
mrv_Data = open('DataModel_Test.json')
mrv_Data = json.load(mrv_Data)

# Project Overview 
def ProjectOverview(mrvData):
	#print(mrv_Data['id'])
	# unique identifier for export from ESMC MRV
	mrv_export_id = mrvData['id']
	# mrv version
	mrv_vers = mrvData['version']
	# project name 
	project = mrvData['project']
	# year enrolled 
	year_enrolled = mrvData['producers'][0]['year_enrolled']
	# user by project id
	user_by_p = mrvData['producers'][0]['user_by_project_id']
	# impact unit types 
	assets = mrvData['assets']
	# anonymized producer_list
	producer_list = []
	producers = mrv_Data['producers']

	for prod in producers:
		producer_list.append(prod['id'])

	return ({
		"exportID": mrv_export_id,
		"project": project,
		"version": mrv_vers,
		"assets": assets,
		"producers": producer_list,
		"year_enrolled": year_enrolled,
		"user_by_p": user_by_p
		})

# Give Project Overview 
p_overview = ProjectOverview(mrv_Data)

# load 1 Producer (set of fields) at a Time 
producer_id = mrv_Data["producers"][0]['id']
fields = mrv_Data["producers"][0]['fields']

# DEFINE Time window
# year enrolled
year_enrolled = int(p_overview['year_enrolled'])
# 3 year lookback date
lookback_year = year_enrolled - 3

# Management Practice dictionaries
field_dic = {"id": [], "acres": [], "units": [], "practice_changes": [], "history": [], "coord": []}
baseline_dic = {"id": [], "history": []}
planting_dic = {"id": [], "history": []}


for f in fields:
	#field_ids.append(f['id'])
	field_dic['id'].append(f['id'])
	#acres.append(f['area']['value'])
	field_dic['acres'].append(f['area']['value'])
	#units.append(f['area']['unit'])
	field_dic['units'].append(f['area']['unit'])
	#prac_changes.append(f['field_practice_changes'][0]['name'])
	field_dic['practice_changes'].append(f['field_practice_changes'][0]['name'])
	field_dic['history'].append(f['history'])
	# replace this with centroid value - for now just choose any coord from field
	field_dic['coord'].append(f['boundary']['coordinates'][0][0][0])


print(field_dic)

# Test - Total Acres for this producer 
print("Project: ", str(p_overview['project']), "|Year Enrolled",p_overview['year_enrolled'], "| Assets:", str(p_overview['assets']), "| Export ID: ", str(p_overview["exportID"]), "| This is using MRV version ", str(p_overview['version']))
print("Number of Producers: ", str(len(p_overview["producers"])))
print("Producer ID: ", producer_id, "| Alias: ", p_overview['user_by_p'])
print("Number of Fields", len(fields))
print("Year Enrolled: ", str(year_enrolled))
print("Lookback Year: ", str(lookback_year))
print("Total Acres: ", sum(field_dic['acres']))
print("Practice Changes: ", field_dic['practice_changes'])

