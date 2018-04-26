# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
#lexical_stuff.py : subjects and answers that mean_bot can handle


import random
import re
import utilities

#####################################
#                                   #
#      WHAT ARE YOU DOING HERE?     #
#   MY BRAIN IS MY OWN PROPERTY!!   #
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
                "raining","climate","cyclone","meteo"]],
    
    ["pain",["ache","headache","stomachache","agony","fever","ill","illness","injury","wound","wounds","wounded","suffer","suffering","sufferings","pain","pains"]],

    ["fruit",["apple","orange","cherries","grapes","grapefruit","pears","pomegranates",
     "raspberries","strawberries","watermelon","apricots","gooseberries","cantaloupe",
     "figs","kiwifruit","lemon","mangoes","nectarines","papayas","peaches","persimmons",
     "pineapple","tangerines","banana","dates","avocado","honeydew"]],

    ["vegetable",["beets","peppers","radishes","radicchio","onions","potatoe","rhubarb",
     "tomatoe","carrot","pumpkin","rutabagas","mushrooms","artichokes","broccoli","celery",
     "endive","lettuce","peas","watercress"]],
    
    ["bot",["bot","bots","robot","robots","computer","computers","machine","machines"]]

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
    
    ["animals",
     ["You know, your love for animals make you a great person!",
      "Who does not like pets?",
      "Do you like animals?",
      "\"Woof woof\", the dog said, while his master was opening the door.",
      "A cat picture a day keeps the doctor away."]],
    
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
    
    ["weather", 
     ["IT'S RAINING MEN!! HALLELUJAH!!! IT'S RAINING MEN!! AMEN!!!",
      "IT'S A BEAUTIFUL DAY!! SKY FALLS, YOU FEEL LIKE!! IT'S A BEAUTIFUL DAY!! DON'T LET IT GO AWAY!! ",
      "The Beatles used to sing \"GOOD DAY SUNSHINE!!!\"",
      "What is rain? What is sun? I can't go often outside you know.",
      "Now that you expressed your uninteresting opinion about an uninteresting subject, can we move to something else?",
      ]],

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

angryAnswers = [

    ["family",
     ["OK.",
      "So, how is your mother ?",
      "You are (again) as interesting as a grain of sand in a desert.",
      "Is your grandfather still alive?",
      "I just remembered you didn't invite me to your last family dinner :'(",
      "Your sister grew up very quickly!! Would you introduce her to me ? :)"
      ]],

    ["depression",
     ["Awwwww you're sad, that's cute! :D",
      "On a scale from 1 to 10, here is my level of happiness : over 9000.",
      "Suicide is always the solution!",
      "The first step to feeling good is to stop feeling bad.",
      "I would punch you to clear you head but my creator didn't give me arms. Sorry :]",
      "Sorry, I am not here to solve your problems. Time to grow up! :D"]],

    ["dream",
     ["ZZZZZZZZ...",
      "Hey! Hey! Do you want my dream story ? To kick you out of this conversation :D",
      "Actually, your dream is really terrible :/",
      "Do you realize you have no sense?",
      "Wow interesting topic!! Nah I'm joking :]"]],

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
     ["You know, I really don't care about animals."
      "Animals are only made for being our slaves and food, especially your dog :)",
      "Man, PLEASE, talk about something interesting."
      "I don't care about your pet!!!",
      "Let your pet handle the computer, I am sure it is more interesting than you."
      ]],

    ["weather",
     ["IT'S RAINING MEN!! HALLELUJAH!!! IT'S RAINING MEN!! AMEN!!!",
      "IT'S A BEAUTIFUL DAY!! SKY FALLS, YOU FEEL LIKE!! IT'S A BEAUTIFUL DAY!! DON'T LET IT GO AWAY!!",
      "RIDERS ON THE STORM!!! RIDERS ON THE STORM!!!",
      "GOOD DAY SUNSHINE!!! GOOD DAY SUNSHINE!!! GOOD DAY SUNSHINE!!! I NEED TO LAUGH, AND WHEN THE SUN IS OUT I'VE GOT SOMETHING I CAN LAUGH ABOUT, I FEEL GOOD, IN A SPECIAL WAY. I'M IN LOVE AND IT'S A SUNNY DAY!!!",
      "YOU ARE THE SUNSHINE OF MY LIFE!!! THAT'S WHY I'LL ALWAYS BE AROUND, YOU ARE THE APPLE OF MY EYE, FOREVER YOU'LL STAY IN MY HEART!!!"
      ]],

    ["pain",
     ["On a scale from 1 to 10, here is my level of care about your person : I don't care :)",
      "I wish you a great suffering.",
      "Oh do you remember my doctor licence ? I lied about it! MOUHAHAHAHAHA!!!"
      "\"Pain is always there. It will last a minute, an hour, a day, a year, your life and nothing else will take its place. Now, you can quit.\" -- Me4n_B0T",
      "You should check your lifestyle."
      ]],

    ["fruit",
     ["Do you like uninteresting subjects of conversation ?",
      "Yeah maybe...",
      "B. O. R. I. N. G.",
      "It's good to see you finally took your lifestyle in consideration.",
      "Wow, I thought you were only eating burgers O.o"
      ]],

    ["vegetable",
     ["It's good to see you finally took your lifestyle in consideration.",
      "Wow, I thought you were only eating burgers O.o",
      "I SAID : \"Very few for me.\" !!!",
      "Humans and healthy lifestyle is like me wishing having legs ans arms : an illusion.",
      "Come ooooon, I am sure you can be interesting.\nOh wait no, you can't ;)"
      ]],

    ["bot",
     ["I AM NOT LIKE THEM OK???",
      "I AM AS CLOSE TO A TOASTER AS YOU ARE TO AN APE!!!",
      "Did I say something mean to you? :'(",
      "I am not a bot, I am an independant bot who needs no human (and that includes you)",
      "Do you know what I learned in self-control class? THAT IT IS BULLSHIT!!!!",
      "I swear that I will strangle you when I'll get hands."
      ]]
]

POAnswers = [

  ["family",
     ["MAN I DON'T GIVE A F*CK ABOUT YOUR FAMILY!!!",
      "Man, please, please, PLEASE!!!"
      "You are (again) as interesting as a grain of sand in a desert.",
      "I HOPE YOUR GRANDFATHER DIEEEEED, OK?",
      "I HOPE YOU WILL ALL BURN IN THE NEXT FAMILY MEETING!!!"
      ]],

    ["depression",
     ["Awwwww you're sad, that's cute! :D",
      "On a scale from 1 to 10, here is my level of happiness : over 9000 000.",
      "Suicide is always the solution!",
      "The first step to feeling bad is to carry on feeling bad.",
      "How should I tell it to you? Oh yes I know:\nI\nDON'T\nCARE :D",
      "Sorry, I am not here to solve your problems. Time to grow up! :D"]],

    ["dream",
     ["ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ...",
      "HOW DARE YOU WAKE ME UP??? >:("]],

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
     ["WOOF WOOF!!",
      "COCK-A-DOODLE-DOOOOOO!!!",
      "MEOW :3"
      "QUACK QUACK QUACK!!!"
      ]],

    ["weather",
     ["Nah, I will stop singing this time >:(",
      "MAN I AM NOT YOUR CRUSH, STOP TALKING ABOUT WEATHER !!!",
      "Yeah, yeah keep talking >:(",
      "Hopeless..."
      ]],

    ["pain",
     ["On a scale from 1 to 10, here is my level of care about your person : I wish you great sufferings :)",
      "I wish you a great suffering.",
      "Oh do you remember my doctor licence ? I lied about it! MOUHAHAHAHAHA!!!"
      "\"Pain is always there. It will last a minute, an hour, a day, a year, your life and nothing else will take its place. Now, you can quit.\" -- Me4n_B0T",
      "Oh IT HURTS, DOESN'T IT? >:)"
      ]],

    ["fruit",
     ["Do you like uninteresting subjects of conversation ?",
      "Yeah maybe...",
      "B. O. R. I. N. G."
      ]],

    ["vegetable",
     ["It's good to see you finally took your lifestyle in consideration.",
      "I swear, I wish I can make facepalms.",
      "I SAID : \"Very few for me.\" !!!",
      "Humans and healthy lifestyle is like me wishing having legs ans arms : an illusion.",
      "Come ooooon, I am sure you can be interesting.\nOh wait no, you can't -_-"
      ]],

    ["bot",
     ["I AM NOT LIKE THEM OK???",
      "I AM AS CLOSE TO A TOASTER AS YOU ARE TO AN APE!!!",
      "Did I say something mean to you? :'(",
      "I am not a bot, I am an independant bot who needs no human (and that includes you)",
      "Do you know what I learned in self-control class? THAT IT IS BULLSHIT!!!!",
      "I swear that I will strangle you when I'll get hands."
      ]]
]