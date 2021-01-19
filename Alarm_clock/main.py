# from datetime import datetime
# from playsound import playsound
# alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
# alarm_hour=alarm_time[0:2]
# alarm_minute=alarm_time[3:5]
# alarm_seconds=alarm_time[6:8]
# alarm_period = alarm_time[9:11].upper()
# print("Setting up alarm..")
# while True:
#     now = datetime.now()
#     current_hour = now.strftime("%I")
#     current_minute = now.strftime("%M")
#     current_seconds = now.strftime("%S")
#     current_period = now.strftime("%p")
#     if(alarm_period==current_period):
#         if(alarm_hour==current_hour):
#             if(alarm_minute==current_minute):
#                 if(alarm_seconds==current_seconds):
#                     print("Wake Up!")
#                     while True:
#                         playsound('ringtone.mp3')
#
#                     break


from playsound import playsound
from datetime import datetime

time = input("Enter the time in the format HH:MM:SS:(AM/PM): ")
set_hrs = time[0:2]
set_min = time[3:5]
set_sec = time[6:8]
set_period = time[9:11].upper()

while True:
	now = datetime.now()
	cur_hrs = now.strftime("%I")
	cur_min = now.strftime("%M")
	cur_sec = now.strftime("%S")
	cur_period = now.strftime("%p")
	if cur_hrs == set_hrs:
		if cur_min == set_min:
			if cur_sec == set_sec:
				if cur_period == set_period:
					print("Wake up")
					playsound('ringtone.mp3')
					break
