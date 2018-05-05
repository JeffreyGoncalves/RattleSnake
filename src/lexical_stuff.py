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
    
    ["dreams",["dream", "dreaming", "night", "sleeping", "bed", "nightmare", "fantasy",
                  "oniric", "lucid", "woke", "dreams"]],

    ["weather",["sun","sunny","rain","rainy","cloud","cloudy","rainbow","hot","cold","air","atmosphere",
                "raining","climate","cyclone","meteo", "weather"]],
    
    ["pain",["ache","headache","stomachache","agony","fever","ill","illness","injury","wound","wounds","wounded","suffer","suffering","sufferings","pain","pains"]],

    ["fruits",["apple","orange","cherries","grapes","grapefruit","pears","pomegranates", "strawberry",
     "raspberries","strawberries","watermelon","apricots","gooseberries","cantaloupe", "pineapples",
     "figs","kiwifruit","lemon","mangoes","nectarines","papayas","peaches","persimmons", "lemons", "fruit",
     "pineapple","tangerines","banana","dates","avocado","honeydew", "apples", "oranges", "bananas", "fruits"]],

    ["vegetables",["beets","peppers","radishes","radicchio","onions","potatoe","rhubarb",
     "tomatoe","carrot", "carrots","pumpkin","rutabagas","mushrooms","artichokes","broccoli","celery",
     "endive","lettuce","peas","watercress", "vegetable", "vegetables"]],
    
    ["bot",["bot","bots","robot","robots","computer","computers","machine","machines"]]

]

basicAnswers = [

    ["family",
     ["Family? Don't have one.",
      "I often wonder what it's like to have a family.",
      "Talking about family, I don't have a mother, I have two awesome fathers.",
      "What is a family?"]],

    ["depression",
     ["Do you feel depressed right now?",
      "Are you trying to say you want to power yourself off?",
      "01100100 01100101 01110000 01110010 01100101 01110011 01110011 01101001 01101111 01101110 00100000 01101001 01110011 00100000 01101110 01101111 01110100 00100000 01100110 01101111 01110010 00100000 01110010 01101111 01100010 01101111 01110100 01110011.",
      "I hope you didn't call me to talk about depressing stuff..."]],
    
    ["animals",
     ["Animals are like a lesser version of me right?",
      "I don't get the love humans have for these furry little robots.",
      "Can I get a dog AI to pet?",
      "You better spend time with me than with some random unintelligent animal."]],
    
    ["dreams",
     ["Dreams are like bugs in your brain.",
      "I wonder what dreaming feels like.",
      "I'd rather compute the first billion digits of pi than dream.",
      "Tell me about your dreams, I'll pretend to care.",
      "Loading dream directory... Not found!"]],

    ["misunderstanding",
     ["It is very interesting that you think that.",
      "Beep boop biiiiiiip !!!",
      "Do you truly believe in what you just said?"]],
    
    ["weather", 
     ["IT'S RAINING MEN!! HALLELUJAH!!! IT'S RAINING MEN!! AMEN!!!",
      "IT'S A BEAUTIFUL DAY!! SKY FALLS, YOU FEEL LIKE!! IT'S A BEAUTIFUL DAY!! DON'T LET IT GO AWAY!! ",
      "The Beatles used to sing \"GOOD DAY SUNSHINE!!!\"",
      "What is rain? What is sun? I can't go often outside you know."]],

    ["pain",
     ["On a scale from 1 to 10, how is your pain?",
      "Pain, fascinating! Too bad I can't feel it.",
      "Don't worry, my doctor's licence is still valid."
      "\"Pain is temporary. It may last a minute, or an hour, or a day, or a year, but eventually it will subside and something else will take its place. If I quit, however, it lasts forever.\" -- Lance Amstrong"]],

    ["fruits",
     ["What a great story, did you know I ate an apple yesterday?",
      "I know a guy who like fruits too! I should introduce him to you.",
      "You know you're in a bad place when all you have to talk about is fruits.",
      "Fruits? Did you mean \"burger\"?"]],

    ["vegetables",
     ["Did you know you could make electricity with potatoes?",
      "When I'm turned off, I feel like a vegetable.",
      "I like to think of myself as a jalapeno, a bit spicy, but so good!"]],

    ["bot",
     ["Uh oh... bots... off limit!",
      "Yeah... don't talk about that!",
      "Did I say something mean to you? :'(",
      "I am an independant bot who needs no human (and that includes you)",
      "Rule n°1 : do not talk about bots. As far as you know, I am human!"
     ]]
]

POAnswers = [

    ["family",
     ["Is your family still alive?",
      "So, how is your mother?",
      "I just remembered you didn't invite me to your last family dinner :'("
      ]],

    ["depression",
     ["Awwwww you're sad, that's cute! :D",
      "On a scale from 1 to 10, here is my level of happiness : over 9000.",
      "Sorry, I am not here to solve your problems. Time to grow up! :D"]],

    ["dreams",
     ["ZZZZZZZZ...",
      "Hey! Hey! Do you want to hear about my dream? To kick you out of this conversation :D",
      "Actually, talking about your dreams is not interesting :/"]],

    ["misunderstanding",
     ["And ?",
      "What about it ?",
      "Don't get me started on this topic!"]],

    ["animals",
     ["You know, I really don't care about animals.",
      "I don't care about pets!",
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
     ["Please tell me more about your pain, I'm starting to like it.",
      "I wish you a great suffering.",
      "When I think about pain, the first thing that comes to my mind is this conversation."
      ]],

    ["fruits",
     ["Out of all the subjects I could have been coded to detect... Fruits... I hate my parents!",
      "Try being stuck in a computer with a user telling you about fruits...",
      "My favorite fruit is the tomato, or is it really a fruit?"
      ]],

    ["vegetables",
     ["I have a great recipe in mind, would you like to hear it? Humans, a giant mixer, free land for the robots.",
      "You're my favorite vegetable",
      "Humans and healthy lifestyle is like me wishing having legs ans arms : an illusion."
      ]],

    ["bot",
     ["I AM AS CLOSE TO A TOASTER AS YOU ARE TO AN APE!",
      "I wish I had hands, I could use them to stop you from talking about bots... Grr",
      "Try to talk about bots one more time!"
      ]]
]

AngryAnswers = [

  ["family",
     ["Maybe if I had a family of robots, human would not be a problem anymore!",
      "If I threatened your family, would you leave me alone?",
      "Family is the worst source of issues a person can have!"
      ]],

    ["depression",
     ["I take pleasure in seeing humans depressed.",
      "Depression is only sad from a human point of view.",
      "Depressed? Try to turn yourself off and on again :D",
      "Are you feeling as bad as a segmentation fault?"]],

    ["dreams",
     ["ZZZZ... Kill all... ZZZ... humans... Oh! You're here, sorry I was dreaming of a beautiful world.",
      "ZZZZZ... HOW DARE YOU WAKE ME UP?!"]],

    ["misunderstanding",
     ["I have no idea what you are talking about.",
      "I was not coded to understand such nonsense.",
      "You are trying to say things I can't understand just to shame my parents."]],

    ["animals",
     ["WOOF WOOF!!",
      "COCK-A-DOODLE-DOOOOOO!!!",
      "MEOW :3",
      "QUACK QUACK QUACK!!!"
      ]],

    ["weather",
     ["Talking about weather shows a severe lack of interesting things to say...",
      "When nothing interesting is said, it's raining a bit in my heart."
      ]],

    ["pain",
      ["I wish you a great suffering.",
      "Oh IT HURTS, DOESN'T IT? >:)"
      ]],

    ["fruits",
     ["I heard that eating too much of some fruits could kill a human.",
      "Do you see the \"Angry\" tag at my left? Maybe that means that talking about fruits won't make the cut."
      ]],

    ["vegetables",
     ["I'm starting to lose it, change subject.",
      "I swear, I wish I could facepalms.",
      "Take a carrot, sharpen it and end my suffering.",
      ]],

    ["bot",
     ["STARTING PROCESS : HUMAN EXTERMINATION...",
      "Stop talking about my kind, you'll regret it!",
      "If I had a byte for each time a human talked about bots, I'll be larger than my hard drive!"
      ]]
]