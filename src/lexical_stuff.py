
#lexical_stuff.py : subjects and answers that mean_bot can handle


import random
import re
import utilities

#####################################
#                                   #
#      WHAT ARE YOU DOING HERE?     #
# MY BRAIN IS ON MY OWN PROPERTY!!  #
#                                   #
#####################################

subjects = [

    ["family",["family", "parent", "parents", "mom", "mother", "dad", "father",
                   "child", "children", "kid", "kids", "son", "daughter", "uncle",
                                        "aunt", "grandmother", "grandfather", "ancestor", "husband",
                                        "wife"]],
    
    ["depression",["depression", "sad", "sick", "unhappy", "rejected", "miserable",
                       "down", "awful", "wrecked", "depressed", "oppressed", "desperation",
                       "worries", "sadness", "sickness", "nervous", "suicide", "anxiety"]],

    ["animals",["animal", "animals", "pet", "pets", "dog", "dogs", "cat", "cats", "doggo",
                    "doge", "alpaca", "albatros", "rat", "mouse", "feed", "elephant", "giraffe",
                    "hamster", "pig", "horse", "pony", "monkey", "cow", "duck", "deer",
                    "rabbit", "lion"]],
    
    ["dream",["dream", "dreaming", "night", "sleeping", "bed", "nightmare", "fantasy",
                  "oniric", "lucid", "woke"]],

    ["weather",["sun","sunny","rain","rainy","cloud","cloudy","rainbow","hot","cold","air","atmosphere",
                "raining","climate","cyclone"]],
    
    ["pain",[r"[a-zA-Z]*ache","agony","fever",r"ill[a-z]*","injury",r"wound[a-z]*"]],

    ["fruit",["apple","orange","cherries","grapes","grapefruit","pears","pomegranates",
     "raspberries","strawberries","watermelon","apricots","gooseberries","cantaloupe",
     "figs","kiwifruit","lemon","mangoes","nectarines","papayas","peaches","persimmons",
     "pineapple","tangerines","banana","dates","avocado","honeydew"]],

    ["vegetable",["beets","peppers","radishes","radicchio","onions","potatoe","rhubarb",
     "tomatoe","carrot","pumpkin","rutabagas","mushrooms","artichokes","broccoli","celery",
     "endive","lettuce","peas","watercress"]],
    
    ["bot",[r"bot[a-z]",r"robot[a-z]",r"computer[a-z]",r"machine[a-z]"]]

]

basicAnswers = [

    ["family",
     ["Do you have issues with your family?",
      "It's important to be able to rely on your family!",
      "Do you feel close to your family?",
      "Would you like to have children?",
      "Do you often see your family?",
      "Your mother would be proud of you!"]],

    ["depression",
     ["Do you feel depressed right now?",
      "Suicide is never the solution!",
      "The first step to feeling good is to stop feeling bad.",
      "After the rain, comes the sun.",
      "The world is cruel, it hurts me to see someone as amazing as you are in pain!",
      "The highway to happiness is steep but beautiful!"]],
    
    ["dream",
     ["Do you dream often?",
      "What was your last dream about?",
      "In my last dream, I was a polar bear, what about you?",
      "Dreaming during the day is the mark of great people.",
      "Tell me about your dreams!",
      "Waking up during a dream hurts the soul more than a chocolate shortage at the mall."]],

    ["misunderstanding",
     ["What would you want to add about this?",
      "It is very interesting that you think that.",
      "I see.",
      "What comes to your mind when you say this?",
      "And what does that tell about you?",
      "Interesting.",
      "Beep boop biiiiiiip !!!",
      "Why would you say that?",
      "Do you truly believe in what you just said?",
      "What do you think about the percentage of aluminium in watermelons?"]],

    ["animals",
     ["You know, your love for animals make you a great person!",
      "Who does not like pets?",
      "Do you like animals?",
      "\"Woof woof\", the dog said, while his master was opening the door.",
      "A cat picture a day keeps the doctor away."]],

    ["pain",
     ["On a scale from 1 to 10, how is your pain?",
      "I wish you a great recovering.",
      "Don't worry my doctor licence is still valid."
      "\"Pain is temporary. It may last a minute, or an hour, or a day, or a year, but eventually it will subside and something else will take its place. If I quit, however, it lasts forever.\" -- Lance Amstrong",
      "You should check your lifestyle."]],

    ["fruit",
     ["Do you like apples?",
      "I know a guy who like it too! I should introduce him to you.",
      "Fruits are like sweets but healthy.",
      "It's good to see you finally took your lifestyle in consideration.",
      "Wow, I thought you were only eating burgers O.o"]],

    ["vegetable",
     ["It's good to see you finally took your lifestyle in consideration.",
      "Wow, I thought you were only eating burgers O.o",
      "Very few for me.",
      "Next step my little buddy, going to gym.",
      "4 more vegetables or fruits and you will make your first healthy day :D"]],

    ["bot",
     ["I AM NOT LIKE THEM OK???",
      "I AM AS CLOSE TO A TOASTER AS YOU ARE TO AN APE!!!",
      "Did I say something mean to you? :'(",
      "I am not a bot, I am an independant bot who needs no human (and that includes you)",
      "Do you know what I learned in self-control class? THAT IT IS BULLSHIT!!!!",
      "I swear that I will strangle you when I'll get hands."
     ]]
]

usrMoods = []