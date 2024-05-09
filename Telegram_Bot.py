import telebot
from telebot import types 
import random

TOKEN = '6428597142:AAFWwL5h9Ww-uDRp2XgU-mAjxPnKTohtjsw'

ABOUT_TEXT = """Its a Health Companion Bot"""
    

#Init the  bot with token
bot = telebot.TeleBot(TOKEN)

#This will generate buttons for us in more elegant way
def generate_buttons(bts_names, markup):
    for button in bts_names:
        markup.add(types.KeyboardButton(button))
    return markup

#To catch the message you need to use this decorator. 
@bot.message_handler(commands=['705852'])
def send_hello(message):
    #Init keyboard markup
    markup = types.ReplyKeyboardMarkup(row_width=2)
    #Add to buttons by list with ours generate_buttons function.
    markup = generate_buttons(['Reports', 'About', 'Patient Profile'], markup) 
    message = bot.reply_to(message, """Hi there! What you want to do?""",
                 reply_markup=markup)
    
    #Here we assign the next handler function and pass in our response from the user. 
    bot.register_next_step_handler(message, play_or_about)

#Here we no longer need to specify the decorator function
def play_or_about(message):
    if message.text in ['Reports']:
        global daily_data
        global water_data
        daily_data = []
        with open('dailyreport.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            daily_data.append(line.strip().split(',')) 
            
        water_data = []
        with open('water_data.txt', 'r') as file: 
             water_report = file.readlines() 
        for line in water_report: 
            water_data.append(line.strip().split(',')) 
         
        #Generating keyboard markup for user guess
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup = generate_buttons(['Food Report', 'Water Report', 'Exercise Report', 'Medication Report'], markup)
        guess = bot.reply_to(message, 
                             "Select a report",
                             reply_markup=markup)
        bot.register_next_step_handler(guess, win_or_not)
    elif message.text == 'About':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup = generate_buttons(['Reports', 'About'], markup)
        message = bot.reply_to(message,
                               ABOUT_TEXT,
                               reply_markup=markup)
        bot.register_next_step_handler(message, play_or_about)
    
    elif message.text == 'Patient Profile':
        text=""
        profile=[]
        with open('profile.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            profile.append(line) 
        print(profile)
        for element in profile:
            text=text+element[:]
            
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup = generate_buttons(['Reports', 'Patient Profile'], markup) 
        message = bot.reply_to(message,
            "Here's it :\n" + text,
                               reply_markup=markup)
        bot.register_next_step_handler(message, play_or_about)
    else: 
        #Sometimes user dont want to use keyboard markup, so we need to deal with it
    
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup = generate_buttons(['Get reports', 'About'], markup)
        message = bot.reply_to(message,
                               "Invalid Command",
                               reply_markup=markup)
        bot.register_next_step_handler(message, play_or_about)
        
def win_or_not(guess):
    text=""
    if guess.text == "Food Report":
        
        for element in daily_data:
            text=text+element[0]+" at "+element[3]+"\n"
        
    elif guess.text == "Water Report":
        for element in water_data:
            text=text+element[0]+"ml at "+element[1]+"\n"
            
    elif guess.text == "Exercise Report":
        exercise=[]    
        with open('exercise.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            exercise.append(line) 
        print(exercise)
        for element in exercise:
            text=text+element[:]
            
        
      
    
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = generate_buttons(['Reports', 'Patient Profile'], markup) 
    message = bot.reply_to(guess,
        "Here's it :\n" + text,
                           reply_markup=markup)
    bot.register_next_step_handler(guess, play_or_about)
        
#Launches the bot in infinite loop mode with additional
#...exception handling, which allows the bot
#...to work even in case of errors. 
bot.infinity_polling()
