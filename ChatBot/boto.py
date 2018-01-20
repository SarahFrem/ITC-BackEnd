"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
from weather import Weather

time_counter=0
user_name = ''

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    #we return a json.dumps because in the ajax expects a json -> ,"json"
    global time_counter
    global user_name
    time_counter +=1

    user_message = request.POST.get('msg')
    #post request in js : {"msg": userInput.val()} ie "msg" is the keyword
    user_message_array = user_message.split()
    if time_counter == 1:
        if 'I am' or 'i am' in user_message:
            index = user_message_array.index('am')
            user_name = user_message_array[index+1] 
        elif 'my name is ' in user_message:
            index = user_message_array.index('is')
            user_name = user_message_array[index+1]
        else:
            user_name = user_message_array[0]
        return json.dumps({"animation": "inlove", "msg": "Hii "+user_name+ " I hope you are fine !"})

    swear_words = ('fuck', 'shit', 'bastard', 'ass', 'asshole','bitch')
    joke_words = ('joke', 'joking', 'laugh', 'laughing', 'funny')
    weather_words = ('weather', 'rain', 'cloud', 'sun','rainy','cloudy','sunny')
    message_random = [user_message + ".. I'm bored",
         "Do you want to dance with me " +user_name+" ? it is my passion !!!",
          "people thinks robot can only say OK .. but it is not true ok ?",
          "Did I tell you my dog is my best friend ?",
         "I am a bit crazy ... sometimes",
          "Can I sleep ?",
          "mo mo mo monnneyyyyyy",
           "What are your fears "+user_name+" ? me it is the storm and balloons ... ",
          "ok I'll tell you a secret, I met a girl last year, she broke my heart ... I mean if I have one"]
    animation_random = ["bored", "dancing", "ok", "dog", "giggling", "takeoff", "money", "afraid", "heartbroke"]
    index_random = random.randint(0, len(message_random) - 1)
    current_message = message_random[index_random]
    current_animation = animation_random[index_random]

    if 'my name is ' in user_message:
        index = user_message_array.index('is')
        user_name = user_message_array[index+1]
        return json.dumps({"animation": "confused", "msg": "ok i am a bit confused... so Hello "+user_name})
        

    if any((word in swear_words for word in user_message_array)):
        return json.dumps({"animation": "no", "msg": "Be polite please"})

    if any((word in joke_words for word in user_message_array)):
        joke_array = ['If vegetarians eat vegetables, what do humanitarians eat?',
                      'If tin whistles are made of tin, what are fog horns made of?',
                      'Why do we park our car in the driveway and drive our car on the parkway?',
                      'I used to be a werewoolf... But I m much better noooooooooooow !']
        current_joke = joke_array[random.randint(0, len(joke_array) - 1)]
        return json.dumps({"animation": "laughing", "msg": "Oh you want to laugh? " + current_joke})

    if any((word in weather_words for word in user_message_array)):
        weather = Weather()

        # Lookup via location name.
        city = 'tel-aviv'
        location = weather.lookup_by_location(city)
        condition = location.condition()
        print "Weather for "+city+ " :"
        print condition.date()
        print condition.text()
        print condition.temp()
        
        return json.dumps({"animation": "excited", 
        "msg": 'ok I got the weather for you in ' +city+ ': ' +condition.date()+ ', it is '+condition.text()+' and the temperature is '+condition.temp()+' Farenheit.' })

    if user_message_array[-1]=='?':
        return json.dumps({"animation": "crying", "msg":"sorry I am not enought smart to know the answer.."})
    else:
        print current_animation
        print current_message
        return json.dumps({"animation": current_animation, "msg": current_message })
    


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
