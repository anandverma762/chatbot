from datetime import datetime
#import urllib.request
#import requests
#from googlesearch import search as sr
#import re
import botapi as key

def srepo(user_input):
    reply_text=str(user_input).lower()
   
    if reply_text in ("hello","hi"):
        return "Hey! How can help you?"

    if reply_text in ("time","time?"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you. Go with www.google.com ."


            
    
       
