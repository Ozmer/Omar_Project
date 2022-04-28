import pywhatkit

from datetime import datetime, time


# def whatsapp_sms(phone_number,message,hour,minute):
#     # Same as above but Closes the Tab in 2 Seconds after Sending the Message
#     # pywhatkit.sendwhatmsg(phone_number, message, hour, minute, 15, True,30)
#     pywhatkit.sendwhatmsg_instantly(phone_number, message, 10, 20)

    




# phone_number='+9647713061075'
# message = 'this is a test message '















date_now = datetime.now()
time = date_now.strftime("%H:%M:%S")
time_now = time.split(':')
print(time_now)

hour=int(time_now[0])
print(hour)


minute = (int(time_now[1])+1)
print(minute)

print("*********xXx**************")
whatsapp_sms(phone_number, message, hour, minute)



# Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)
# Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")


