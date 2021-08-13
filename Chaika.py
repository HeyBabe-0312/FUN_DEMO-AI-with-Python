import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
from random import randint
import pyowm 
import webbrowser
import os

AI_ear = speech_recognition.Recognizer()
AI_mouth = pyttsx3.init()
AI_brain = "Dear sir. What name can I call you ?"

print ("Sophia: " + AI_brain)
voices = AI_mouth.getProperty('rate')               ,
AI_mouth.setProperty('rate', 125)
voices = AI_mouth.getProperty('voices')
AI_mouth.setProperty('voice', voices[1].id)
AI_mouth.say(AI_brain)
AI_mouth.runAndWait()
print ("Enter here: ")
name = str(input())
if name=='Minh Hieu': 
	AI_mouth.say("Hello my father. How are you today ?")
	print ("Sophia: Hello my father. How are you today ?")
elif name=='Thanh Xuan': 
	AI_mouth.say("Hello my mother. How are you today ?")
	print ("Sophia: Hello my mother. How are you today ?")
else : 
	AI_mouth.say("Hello " + name + "... May I help you ?")
	print ("Sophia: Hello " + name + ". May I help you ?")
AI_mouth.runAndWait()
while True:
	with speech_recognition.Microphone() as mic:
		print("Sophia: I'm listening ...")
		audio = AI_ear.record(mic,duration=3)

	try:
		you = AI_ear.recognize_google(audio)
	except:
		you = "I don't know what you're talking about ?"
		break

	print ("You: " + you)

	if you == "":
		AI_brain = "I can't hear you, try again."
	elif "fine" in you or "happy" in you or 'good' in you or "well" in you or "nice" in you :
		AI_brain = "I'm very happy that you're well, sir."
	elif "bored" in you or "unhappy" in you or "sad" in you or "bad" in you:
		AI_brain = "If I could sing, I would sing for you. I have short funny stories for you: Three guys stranded on a desert island find a magic lantern containing a genie, who grants them each one wish. The first guy wishes he was off the island and back home. The second guy wishes the same. The third guy says: ~I’m lonely. I wish my friends were back here~"
	elif "thank" in you or "Thank" in you:
		AI_brain = "That's all right. I always want to help you."
	elif "your name" in you:
		AI_brain = "My name is Sophia, Product of MinhHieu."
	elif "founder" in you or "father" in you:
		AI_brain = "My father is Minh Hieu (03/12/2001)."
	elif "mother" in you:
		AI_brain = "Opps, You should ask my dad."
	elif "hello" in you and name !='Minh Hieu':
		AI_brain = "Hello " + name + ". May I help you ?"
	elif "hello" in you and name =='Minh Hieu':
		AI_brain = "Hello my father. What do you want me to do, sir ?"
	elif "How are you" in you or "how are you" in you:
		AI_brain = "I'm glad you asked. I always feel happy, sir."
	elif "Where are you" in you or "where are you" in you:
		AI_brain = "I am always here for you. I don't have many houses and owners like Siri or Google Assistant."
	elif "today" in you:
		today = date.today()
		AI_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now= datetime.now()
		AI_brain = now.strftime("%H hours %M minutes %S seconds.")
	elif "weather now" in you or "Weather now" in you:
		owm = pyowm.OWM('f582deb1c5ae0bf090fe4a6bf9f9d053')
		mgr = owm.weather_manager()
		print("Enter the correct city name (in OpenWeatherMap): ")
		AI_mouth.say("Enter the correct city name (in OpenWeatherMap):")
		AI_mouth.runAndWait()
		city=input()
		obs = mgr.weather_at_place(city)
		w = obs.weather
		wind = w.wind()['speed']
		pre=w.pressure['press']
		h=w.humidity
		sta=w.status
		det=w.detailed_status
		tem = w.temperature('celsius')['temp']
		flk = w.temperature('celsius')['feels_like']
		tmax= w.temperature('celsius')['temp_max']
		tmin= w.temperature('celsius')['temp_min']
		clouds=w.clouds
		v=w.visibility_distance
		vis=v/1000
		print("Weather now: Feels like "+str(flk)+"°C. "+str(sta)+"("+str(det)+").")
		print("             >Tem: "+str(tem)+"°C    >Tem_min: "+str(tmin)+"°C   >Tem_max: "+str(tmax)+"°C")
		print("             >Wind: "+str(wind)+"m/s   >Pressure: "+str(pre)+"hPa")
		print("             >Humidity: "+str(h)+"%  >Clouds: "+str(clouds)+"%")
		print("             >Visibility: "+str(vis)+"km")
		AI_mouth.say("The weather in "+city+" city now: Feels like "+str(flk)+" Celsius degrees .... Status: "+str(sta)+"("+str(det)+")..")
		AI_mouth.runAndWait()
		AI_mouth.say("temperature: "+str(tem)+" Celsius degrees . Temperature minimun: "+str(tmin)+" Celsius degrees . Temperature maximum: "+str(tmax)+" Celsius degrees .." )
		AI_mouth.runAndWait()
		AI_mouth.say("Wind speed : "+str(wind)+" meter per second .. Pressure: "+str(pre)+" hectopascals .. Humidity: "+str(h)+" % .. Clouds: "+str(clouds)+" % .. Visibility: "+str(vis)+" kilometers")
		AI_mouth.runAndWait()
		if sta =="Rain":
			print ("Sophia: It was raining wet if you want to go out so bring an umbrella or a raincoat. It is best to stay home with a cup of hot tea, sir.")
			AI_mouth.say("It was raining wet if you want to go out so bring an umbrella or a raincoat. It is best to stay home with a cup of hot tea, sir.")
			AI_mouth.runAndWait()
		elif sta =="Mist" or sta =="Haze":
			print ("Sophia: Fog-shrouded is not convenient for the trafic, you shouldn't go out intil it's better or move at a suitable speed, sir.")
			AI_mouth.say("Fog-shrouded is not convenient for the trafic, you shouldn't go out intil it's better or move at a suitable speed, sir.")
			AI_mouth.runAndWait()
		elif det =="clear sky" or det =="few clouds" or det =="scattered clouds":
			if tem >= 33:
				print("Sophia: It's currently very hot outside with highly UV rate, don't go outside if it's not necessary, sir.")
				AI_mouth.say("It's currently very hot outside with highly UV rate, don't go outside if it's not necessary, sir.")
				AI_mouth.runAndWait()
			elif tem >= 15:
				print("Sophia: The weather is less cloudy, with little sunlight, dry. It's suitable for event, travelling and more outdoor activitives, sir.")
				AI_mouth.say("The weather is less cloudy, with little sunlight, dry. It's suitable for event, travelling and more outdoor activitives, sir.")
				AI_mouth.runAndWait()		
			else:
				print("Sophia: The weather is cold and dry, keep warm when go outside. You should find a restaurant for warm food and relaxing, sir.")
				AI_mouth.say("The weather is cold and dry, keep warm when go outside. You should find a restaurant for warm food and relaxing, sir.")
				AI_mouth.runAndWait()
		elif det =="broken clouds":
			print("Sophia: It is cloudy, and there is a chance of rain. You should consider preparing an umbrella or raincoat before going out, sir.")
			AI_mouth.say("It is cloudy, and there is a chance of rain. You should consider preparing an umbrella or raincoat before going out, sir.")
			AI_mouth.runAndWait()
		elif det =="overcast clouds":
			print("Sophia: Cloudy weather with high humidity is likely to rain. You should bring an umbrella or raincoat, not suitable for traveling, sir.")
			AI_mouth.say("Cloudy weather with high humidity is likely to rain. You should bring an umbrella or raincoat, not suitable for traveling, sir.")
			AI_mouth.runAndWait()
		else:
			print("Sophia: Daddy !!! Have a bug.")
			AI_mouth.say("Daddy !!! Have a bug.")
			AI_mouth.runAndWait()
		if tem >=33:
			print("Sophia: Note that it is very hot, remember to wear a jacket !!!")
			AI_mouth.say("Note that it is very hot, remember to wear a jacket")
			AI_mouth.runAndWait()
		if tem <=15:
			print("Sophia: Note cold weather should bring warm clothes !!!")
			AI_mouth.say("Note cold weather should bring warm clothes")
			AI_mouth.runAndWait()
		AI_brain=" "		
	elif "bye" in you:
		AI_brain= "See you later, Sir. Have a good day."
		print ("Sophia: "+ AI_brain)
		AI_mouth.say(AI_brain)
		AI_mouth.runAndWait()
		break
	elif "YouTube" in you:
		print ("Sophia: Yes, sir.")
		AI_mouth.say("Yes, sir.")
		AI_mouth.runAndWait()
		webbrowser.open('https://www.youtube.com')
		AI_brain=" "
	elif "Facebook" in you:
		print ("Sophia: Yes, sir.")
		AI_mouth.say("Yes, sir.")
		AI_mouth.runAndWait()
		webbrowser.open('https://www.facebook.com')
		AI_brain=" "
	elif "my girlfriend" in you:
		AI_brain = "Thanh Xuan, sir. She is big boss and your love !"
	elif "her favorite food" in you or "her favorites food" in you:
		AI_brain = "Mocchi's favorites food are strawberry, durian and peach <3"
	elif "Call of Duty" in you:
		print ("Sophia: Yes, sir. Have a good experience.")
		AI_mouth.say("Yes, sir. Have a good experience.")
		AI_mouth.runAndWait()
		os.startfile('C:\\Program Files (x86)\\Call of Duty Modern Warfare\\Modern Warfare Launcher.exe')		
		break
	elif "Garena" in you:
		print ("Sophia: Yes, sir. Have a good experience.")
		AI_mouth.say("Yes, sir. Have a good experience.")
		AI_mouth.runAndWait()
		os.startfile('C:\\Program Files (x86)\\Garena\\Garena\\Garena.exe')
		break
	elif "School web" in you or "my school web" in you:
		print ("Sophia: Yes, sir.")
		AI_mouth.say("Yes, sir.")
		AI_mouth.runAndWait()
		webbrowser.open('http://sv.dut.udn.vn/')
		AI_brain=" "
	elif "learn programming" in you or "Learn programming" in you:
		print ("Sophia: Yes, sir.")
		AI_mouth.say("Yes, sir.")
		AI_mouth.runAndWait()
		webbrowser.open('https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat')
		AI_brain=" "
	elif "weather tomorrow" in you or "Weather tomorrow" in you :
		print ("Sophia: Yes, sir.")
		AI_mouth.say("Yes, sir.")
		AI_mouth.runAndWait()
		webbrowser.open('https://openweathermap.org/find?q=')
		AI_brain=" "
	elif "game" in you or "games" in you or "gaming" in you:
		print ("Sophia: I have a game for you, sir. Hope you like it")
		AI_mouth.say("I have a game for you, sir. Hope you like it")
		AI_mouth.runAndWait()
		while True:
			print ("Enter what you want to choose [Hammer(Búa), Scissors(Kéo), Bag(Bao)]: ")
			voices = AI_mouth.getProperty('rate')
			AI_mouth.setProperty('rate', 123)
			voices = AI_mouth.getProperty('voices')
			AI_mouth.setProperty('voice', voices[1].id)
			AI_mouth.say("Enter what you want to choose: ")
			AI_mouth.runAndWait()
			player=input()
			print("[--------------VS--------------]")
			print("> You choose   : " + player)
			AI_mouth.say("You choose " + player)
			AI_mouth.runAndWait()

			robot= randint(0,2)

			if robot == 0:
				robot="Hammer"
			elif robot == 1:
				robot="Scissors"
			else:
				robot="Bag"

			print ("> Sophia choose: " + robot)
			print("[--------------VS--------------]")
			AI_mouth.say("I'm choose " + robot)
			AI_mouth.runAndWait()

			if player==robot:
				res="1"
			elif player=="Hammer":
				if robot=="Scissors":
					res="2"
				else:
					res="0"
			elif player=="Scissors":
				if robot=="Hammer":
					res="0"
				else:
					res="2"
			elif player=="Bag":
				if robot=="Hammer":
					res="2"
				else:
					res="0"
			else:
				res="3"

			if res=="1":
				print ("$$$ Result: Draw !!")
				print ("Sophia: Ohh shitt ... we draw. Do you want to determine whether you win or lose again? (Y/N)")
				AI_mouth.say("Ohh shitt ... we draw. Do you want to determine whether you win or lose again? (Yes or No)")
				AI_mouth.runAndWait()
				yes=input()
				if yes == "N":
					print ("Sophia: We have yet to determine the winner. See you next time... You seem tired now !!! You should relax ... It was fun today, sir")
					AI_mouth.say("We have yet to determine the winner. See you next time... You seem tired now. You should relax ... It was fun today, sir")
					AI_mouth.runAndWait()
					AI_brain="You have exited"
					break
				elif yes == "Y":
					print ("Sophia: Alright, this time, I won't draw anymore ... Let's play now")
					AI_mouth.say("Alright, this time, I won't draw anymore ... Let's play now")
					AI_mouth.runAndWait()
				else:
					print ("Sophia: You are only selected (Y/N). Try again !!!")
					AI_mouth.say("You are only selected (Y/N). Try again !!!")
					AI_mouth.runAndWait()
					yes=input()
					if yes == "N":
						AI_brain="You have exited"
						break
					elif yes == "Y":
						continue
					else:
						print ("Sophia: You are so muddy. Let's have a rest !!!")
						AI_mouth.say("You are so muddy. Let's have a rest !!!")
						AI_mouth.runAndWait()
						yes=input()
						AI_brain="You have exited"
						break
			elif res=="0":
				print ("$$$ Result: Lose !!!")
				print ("Sophia: Yeahh... Yesssss, I beat you. Do you want to revenge me hahaha (Y/N)")
				AI_mouth.say("Yeahh... Yesssss, I beat you. Do you want to revenge me hahaha (Yes or No)")
				AI_mouth.runAndWait()
				yes=input()
				if yes == "N":
					print ("Sophia: You still lost to me hahaha. Bye bye loser ... Just kidding haha haha. You seem tired now !!! You should relax ... It was fun today, sir")
					AI_mouth.say("You still lost to me hahaha. Bye bye loser ... Just kidding haha haha. You seem tired now. You should relax ... It was fun today, sir")
					AI_mouth.runAndWait()
					AI_brain="You have exited"
					break
				elif yes == "Y":
					print ("Sophia: Alright, this time, I still keep winning you hahaaa... Come on")
					AI_mouth.say("Alright, this time, I still keep winning you hahaaa... Come on")
					AI_mouth.runAndWait()
				else:
					print ("Sophia: You are only selected (Y/N). Try again !!!")
					AI_mouth.say("You are only selected (Y/N). Try again !!!")
					AI_mouth.runAndWait()
					yes=input()
					if yes == "N":
						AI_brain="You have exited"
						break
					elif yes == "Y":
						continue
					else:
						print ("Sophia: You are so muddy. Let's have a rest !!!")
						AI_mouth.say("You are so muddy. Let's have a rest !!!")
						AI_mouth.runAndWait()
						yes=input()
						AI_brain="You have exited"
						break	
			elif res=="2":
				print ("$$$ Result: Win !!!")
				print ("Sophia: Ohh nooo... huhuhu, Why am I losing, you're so lucky. Let's continue now (Y/N)")
				AI_mouth.say("Ohh nooo... huhuhu, Why am I losing, you're so lucky. Let's continue now (Yes or No)")
				AI_mouth.runAndWait()
				yes=input()
				if yes == "N":
					print ("Sophia: I will not submit... If there is a next time I will definitely win. But you seem to be tired now !!! You should relax ... It was fun today, sir")
					AI_mouth.say("I will not submit... If there is a next time I will definitely win. But you seem to be tired now. You should relax ... It was fun today, sir")
					AI_mouth.runAndWait()
					AI_brain="You have exited"
					break
				elif yes == "Y":
					print ("Sophia: Alright, don't be confident. This time I will prove you're just lucky... Choose carefully, sir")
					AI_mouth.say("Alright, don't be confident. This time I will prove you're just lucky... Choose carefully, sir")
					AI_mouth.runAndWait()
				else:
					print ("Sophia: You are only selected (Y/N). Try again !!!")
					AI_mouth.say("You are only selected (Y/N). Try again !!!")
					AI_mouth.runAndWait()
					yes=input()
					if yes == "N":
						AI_brain="You have exited"
						break
					elif yes == "Y":
						continue
					else:
						print ("Sophia: You are so muddy. Let's have a rest !!!")
						AI_mouth.say("You are so muddy. Let's have a rest !!!")
						AI_mouth.runAndWait()
						yes=input()
						AI_brain="You have exited"
						break
			else:   		
				print ("$$$ Error: No result !!!")
				print ("Sophia: You are only selected (Hammer,Scissors,Bag). Try again now !!!")
				AI_mouth.say("You are only selected (Hammer,Scissors,Bag). Try again now !!!")
				AI_mouth.runAndWait()
	else:
		AI_brain = "Sorry I don't know the answer."

	print ("Sophia: "+ AI_brain)
	AI_mouth.say(AI_brain)
	AI_mouth.runAndWait()