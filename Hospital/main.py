from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from patients import get_random_patients, choice_patients
from datetime import datetime, time
from distance import dist_location
from send_email import send_email
from hospital_info import *




get_random_patient = get_random_patients(choice_patients) # select a random patients
print(get_random_patient) # print the patients details
print("************************xXx***********************")



suggested_hospital = check(get_random_patient) # Get list of hospitals (Public or Private) depaend on time

get_min_distance, min_dis = get_small_distance(suggested_hospital) # from list hospital get the hospital of min distance


print(get_min_distance) # print details for hospital 

print('small distance is ',min_dis) # print the distance 

send_email(get_min_distance[0][6], "There is a patient in the location " +
           str(get_random_patient[1]) + " "+str(get_random_patient[2]))
# send email to hospital 