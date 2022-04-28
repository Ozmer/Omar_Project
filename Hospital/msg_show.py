import PySimpleGUI as SG



# sms for hospital with patient's details 
def hospital_Msg(name , health,diagnosed):
    SG.popup_ok(f' You have a new case : \n Patien Name :{name}' 
                f'\n Health Condition : {health} \n Diagnosed : {diagnosed}')
#####################################################################################


# sms for patient's family
def patientFamily_Msg(name, health, hopital_name):
    SG.popup_ok(f' Please note that {name} health condition is {health} , and going to sent to \n '
                f'{hopital_name}')

#########################################################################

# sms for patient and sent umbulance
def patient_Msg_umbulance(name, health, diagnosed, hopital_name):
    SG.popup_ok(f' {name} \n Unfortunately , you have {diagnosed} \n '
                f'\n your health Condition is {health} \n a call for an umbulance has been sent '
                'the umbulance will reach the location you provided , and \n'
                f'it will transport you to the hospitall {hopital_name}')


# sms for patient and sent umbulance
def patient_Msg_case2(name, health, diagnosed, hopital_name):
    SG.popup_ok(f' {name} \n '
                f'\n your have High  {diagnosed} \n and your health condition is {health} \n'
                f' Please you have to go to the hospitall '
                f'suggested {hopital_name}')




def patient_Msg_case3(name, health, hopital_name):
    SG.popup_ok(f' {name} \n Unfortunately , we could not diagnose your disease \n'
                f'\n but your health condition is {health} \n'
                f' Please go to the nearest hospital  {hopital_name}')
