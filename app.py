print("Title of program: CCA Matching Personality test") 
print() 
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest a CCA for you!") 
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.") 


print("What are you skilled at?")

tech2 = input("I know how to build apps and websites.")

outdoor2 = input("I'm good with tying knots and ropes.")

music2 = input("I can play a musical instrument well.")

sports2 = input("I am good at playing ball games.")

print("Which of these applies to you best?") 

tech1 = input("I like building and fixing things.")

outdoor1 = input("I'll go mad if I do not go out of the house for the whole day.")

music1 = input("I can see colours in my mind when i hear music.")

sports1 = input("I am able to transfer skills that I learnt from one sport to another sport.")


print("What are you most interested in?")

tech3 = input("I prefer creating apps")

outdoor3 = input("I prefer going for an adventure")

music3 = input("I prefer listening to music")      

sports3 = input("I prefer playing sports")
tech_final = int(tech1) + int(tech2) + int(tech3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1)+ int(music2) + int(music3)

print("Are you excited to know your results?") 
print("Here it is!")

if tech_final > outdoor_final and tech_final > music_final and tech_final > sports_final: print("You might be suitable for Infocomm club!") 
elif outdoor_final > music_final and outdoor_final > sports_final: print("You might be stuiable for ODAC!") 
elif sports_final > music_final: print("You might be suitable for Basketball, Volleyball or Netball!") 
else: print("You might be suitable for Band!")
