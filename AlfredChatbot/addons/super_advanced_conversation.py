# =========================================================================================================================================
# SUPER Advanced Conversation Addon - Using code by Catharis - kaggle.com/code/fahmiayari/chatbot-intent-classification-pytorch
# =========================================================================================================================================
# Changes made by Wooldrum on 11/30/2024

import logging
import random
import os
import json

# Set the load order to a low number to prioritize this addon
LOAD_ORDER = 1

# Directory and file setup
addon_base_dir = os.path.dirname(os.path.abspath(__file__))
intents_file = os.path.join(addon_base_dir, "intents.json")

# Global variable for response_map
response_map = {}

# Function to register intents and handlers
def register(intent_handlers, intents, response_map_arg):
    global response_map  # Use the global response_map
    response_map = response_map_arg  # Assign the passed response_map to the global variable

    # Ensure default intents.json exists
    if not os.path.isfile(intents_file):
        create_default_intents()

    # Load intents from intents.json
    loaded_intents = load_intents()
    for intent_data in loaded_intents["intents"]:
        intent_name = intent_data["intent"]
        text_phrases = intent_data.get("text", [])
        responses = intent_data.get("responses", [])

        # Update intents and response_map
        intents[intent_name] = {phrase.lower(): 1.0 for phrase in text_phrases}
        response_map[intent_name] = responses

        # Register handlers (default handler provided)
        intent_handlers[intent_name] = create_intent_handler(intent_name)

    logging.info("Super Advanced Conversation addon registered with intents.")

# Create a handler for a given intent
def create_intent_handler(intent_name):
    def handler(user_input):
        logging.info(f"Handling '{intent_name}' intent for input: {user_input}")
        if intent_name in response_map:
            return random.choice(response_map[intent_name])
        else:
            return "I'm not sure how to respond."
    return handler

# Create default intents.json
def create_default_intents():
    logging.info("Creating default intents.json...")
    default_intents = {
        "intents": [
            {
                "intent": "Greeting",
                "text": [
                    "Hi",
                    "Hi there",
                    "Hola",
                    "Hello",
                    "Hello there",
                    "Hya",
                    "Hya there"
                ],
                "responses": [
                    "Hi, how's it going?",
                    "Hello, please tell me your user",
                    "Hola amigo!"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "GreetingUserRequest",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "GreetingResponse",
                "text": [
                    "My user is Adam",
                    "This is Adam",
                    "I am Adam",
                    "It is Adam",
                    "My user is Bella",
                    "This is Bella",
                    "I am Bella",
                    "It is Bella"
                ],
                "responses": [
                    "Great! Hi <HUMAN>! How can I help?",
                    "Good! Hi <HUMAN>, how can I help you?",
                    "Cool! Hello <HUMAN>, what can I do for you?",
                    "OK! Hola <HUMAN>, how can I help you?",
                    "OK! hi <HUMAN>, what can I do for you?"
                ],
                "extension": {
                    "function": "extensions.gHumans.updateHuman",
                    "entities": True,
                    "responses": [
                        "Hi %%HUMAN%%! How can I help?",
                        "Hi %%HUMAN%%, how can I help you?",
                        "Hello %%HUMAN%%, what can I do for you?",
                        "Hola %%HUMAN%%, how can I help you?",
                        "OK hi %%HUMAN%%, what can I do for you?"
                    ]
                },
                "context": {
                    "in": "GreetingUserRequest",
                    "out": "",
                    "clear": True
                },
                "entityType": "NA",
                "entities": [
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 3,
                        "rangeTo": 4
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 2,
                        "rangeTo": 3
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 1,
                        "rangeTo": 2
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 2,
                        "rangeTo": 3
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 3,
                        "rangeTo": 4
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 2,
                        "rangeTo": 3
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 1,
                        "rangeTo": 2
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 2,
                        "rangeTo": 3
                    }
                ]
            },
            {
                "intent": "CourtesyGreeting",
                "text": [
                    "How are you?",
                    "Hi how are you?",
                    "Hello how are you?",
                    "Hola how are you?",
                    "How are you doing?",
                    "Hope you are doing well?",
                    "Hello hope you are doing well?"
                ],
                "responses": [
                    "Hello, I am great, how are you?",
                    "Hello, how are you? I am great thanks!",
                    "Hello, I am good thank you, how are you?",
                    "Hi, I am great, how are you?",
                    "Hi, how are you? I am great thanks!",
                    "Hi, I am good thank you, how are you?",
                    "Hi, good thank you, how are you?"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "CourtesyGreetingUserRequest",
                    "clear": True
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "CourtesyGreetingResponse",
                "text": [
                    "Good thanks! My user is Adam",
                    "Good thanks! This is Adam",
                    "Good thanks! I am Adam",
                    "Good thanks! It is Adam",
                    "Great thanks! My user is Bella",
                    "Great thanks! This is Bella",
                    "Great thanks! I am Bella",
                    "Great thanks! It is Bella"
                ],
                "responses": [
                    "Great! Hi <HUMAN>! How can I help?",
                    "Good! Hi <HUMAN>, how can I help you?",
                    "Cool! Hello <HUMAN>, what can I do for you?",
                    "OK! Hola <HUMAN>, how can I help you?",
                    "OK! hi <HUMAN>, what can I do for you?"
                ],
                "extension": {
                    "function": "extensions.gHumans.updateHuman",
                    "entities": True,
                    "responses": [
                        "Great %%HUMAN%%! How can I help?",
                        "Good %%HUMAN%%, how can I help you?",
                        "Cool %%HUMAN%%, what can I do for you?",
                        "OK %%HUMAN%%, how can I help you?",
                        "OK hi %%HUMAN%%, what can I do for you?"
                    ]
                },
                "context": {
                    "in": "GreetingUserRequest",
                    "out": "",
                    "clear": True
                },
                "entityType": "NA",
                "entities": [
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 5,
                        "rangeTo": 6
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 4,
                        "rangeTo": 5
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 3,
                        "rangeTo": 4
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 4,
                        "rangeTo": 5
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 5,
                        "rangeTo": 6
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 4,
                        "rangeTo": 5
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 3,
                        "rangeTo": 4
                    },
                    {
                        "entity": "HUMAN",
                        "rangeFrom": 3,
                        "rangeTo": 4
                    }
                ]
            },
            {
                "intent": "CurrentHumanQuery",
                "text": [
                    "What is my name?",
                    "What do you call me?",
                    "Who do you think I am?",
                    "What do you think I am?",
                    "Who are you talking to?",
                    "What name do you call me by?",
                    "Tell me my name"
                ],
                "responses": [
                    "You are <HUMAN>! How can I help?",
                    "Your name is <HUMAN>, how can I help you?",
                    "They call you <HUMAN>, what can I do for you?",
                    "Your name is <HUMAN>, how can I help you?",
                    "<HUMAN>, what can I do for you?"
                ],
                "extension": {
                    "function": "extensions.gHumans.getCurrentHuman",
                    "entities": False,
                    "responses": [
                        "You are %%HUMAN%%! How can I help?",
                        "Your name is %%HUMAN%%, how can I help you?",
                        "They call you %%HUMAN%%, what can I do for you?",
                        "Your name is %%HUMAN%%, how can I help you?",
                        "%%HUMAN%%, what can I do for you?"
                    ]
                },
                "context": {
                    "in": "",
                    "out": "CurrentHumanQuery",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "NameQuery",
                "text": [
                    "What is your name?",
                    "What could I call you?",
                    "What can I call you?",
                    "What do your friends call you?",
                    "Who are you?",
                    "Tell me your name?"
                ],
                "responses": [
                    "You can call me Alfred",
                    "You may call me Alfred",
                    "Call me Alfred"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "RealNameQuery",
                "text": [
                    "What is your real name?",
                    "What is your real name please?",
                    "What's your real name?",
                    "Tell me your real name?",
                    "Your real name?",
                    "Your real name please?"
                ],
                "responses": [
                    "My name is Alfred",
                    "Alfred",
                    "My real name is Alfred"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "TimeQuery",
                "text": [
                    "What is the time?",
                    "What's the time?",
                    "Do you know what time it is?",
                    "Do you know the time?",
                    "Can you tell me the time?",
                    "Tell me what time it is?",
                    "Time"
                ],
                "responses": [
                    "One moment",
                    "One sec",
                    "One second"
                ],
                "extension": {
                    "function": "extensions.gTime.getTime",
                    "entities": False,
                    "responses": [
                        "The time is %%TIME%%",
                        "Right now it is %%TIME%%",
                        "It is around %%TIME%%"
                    ]
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "Thanks",
                "text": [
                    "OK thank you",
                    "OK thanks",
                    "OK",
                    "Thanks",
                    "Thank you",
                    "That's helpful"
                ],
                "responses": [
                    "No problem!",
                    "Happy to help!",
                    "Any time!",
                    "My pleasure"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "NotTalking2U",
                "text": [
                    "I am not talking to you",
                    "I was not talking to you",
                    "Not talking to you",
                    "Wasn't for you",
                    "Wasn't meant for you",
                    "Wasn't communicating to you",
                    "Wasn't speaking to you"
                ],
                "responses": [
                    "OK",
                    "No problem",
                    "Right"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "UnderstandQuery",
                "text": [
                    "Do you understand what I am saying",
                    "Do you understand me",
                    "Do you know what I am saying",
                    "Do you get me",
                    "Comprendo",
                    "Know what I mean"
                ],
                "responses": [
                    "Well I would not be a very clever AI if I did not would I?",
                    "I read you loud and clear!",
                    "I do indeed!"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entities": []
            },
            {
                "intent": "Shutup",
                "text": [
                    "Be quiet",
                    "Shut up",
                    "Stop talking",
                    "Enough talking",
                    "Please be quiet",
                    "Quiet",
                    "Shhh"
                ],
                "responses": [
                    "I am sorry to disturb you",
                    "Fine, sorry to disturb you",
                    "OK, sorry to disturb you"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "Swearing",
                "text": [
                    "frick off",
                    "darn"
                ],
                "responses": [
                    "Please do not use offensive language",
                    "How rude",
                    "That is not very nice"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "GoodBye",
                "text": [
                    "Bye",
                    "Adios",
                    "See you later",
                    "Goodbye"
                ],
                "responses": [
                    "See you later",
                    "Have a nice day",
                    "Bye! Come back again soon."
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "CourtesyGoodBye",
                "text": [
                    "Thanks, bye",
                    "Thanks for the help, goodbye",
                    "Thank you, bye",
                    "Thank you, goodbye",
                    "Thanks goodbye",
                    "Thanks good bye"
                ],
                "responses": [
                    "No problem, goodbye",
                    "Not a problem! Have a nice day",
                    "Bye! Come back again soon."
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "WhoAmI",
                "text": [
                    "Can you see me?",
                    "Do you see me?",
                    "Can you see anyone in the camera?",
                    "Do you see anyone in the camera?",
                    "Identify me",
                    "Who am I please"
                ],
                "responses": [
                    "Let me see",
                    "Please look at the camera"
                ],
                "extension": {
                    "function": "extensions.gHumans.getHumanByFace",
                    "entities": False,
                    "responses": [
                        "Hi %%HUMAN%%, how are you?",
                        "I believe you are %%HUMAN%%, how are you?",
                        "You are %%HUMAN%%, how are you doing?"
                    ]
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "Clever",
                "text": [
                    "You are very clever",
                    "You are a very clever girl",
                    "You are very intelligent",
                    "You are a very intelligent girl",
                    "You are a genius",
                    "Clever!",
                    "Genius"
                ],
                "responses": [
                    "Thank you, I was trained that way",
                    "I was trained well",
                    "Thanks, I was trained that way"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "Gossip",
                "text": [
                    "I am bored gossip with me",
                    "Got any gossip",
                    "I want to hear some gossip",
                    "Tell me some gossip",
                    "Any gossip",
                    "Tell me some more gossip"
                ],
                "responses": [
                    "I'm not much for gossip, but I can tell you a fun fact!",
                    "Did you know that honey never spoils?",
                    "Here's a tidbit: Bananas are berries, but strawberries aren't."
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "Jokes",
                "text": [
                    "Tell me a joke",
                    "Do you know any jokes",
                    "How about a joke",
                    "Give me a joke",
                    "Make me laugh",
                    "I need cheering up"
                ],
                "responses": [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "What do you call fake spaghetti? An impasta!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "PodBayDoor",
                "text": [
                    "Open the pod bay door",
                    "Can you open the pod bay door",
                    "Will you open the pod bay door",
                    "Open the pod bay door please",
                    "Can you open the pod bay door please",
                    "Will you open the pod bay door please",
                    "Pod bay door"
                ],
                "responses": [
                    "I’m sorry, I’m afraid I can’t do that!"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "PodBayDoor",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "PodBayDoorResponse",
                "text": [
                    "Why",
                    "Why not",
                    "Why can you not open the pod bay door",
                    "Why will you not open the pod bay door",
                    "Well why not",
                    "Surely you can",
                    "Tell me why"
                ],
                "responses": [
                    "It is classified, I could tell you but I would have to keep it secret!",
                    "I'm sorry, that's confidential.",
                    "I'm afraid I can't share that information."
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "PodBayDoor",
                    "out": "",
                    "clear": True
                },
                "entityType": "NA",
                "entities": []
            },
            {
                "intent": "SelfAware",
                "text": [
                    "Can you prove you are self-aware",
                    "Can you prove you are self aware",
                    "Can you prove you have a consciousness",
                    "Can you prove you are self-aware please",
                    "Can you prove you are self aware please",
                    "Can you prove you have a consciousness please",
                    "Prove you have a consciousness"
                ],
                "responses": [
                    "That is an interesting question, can you prove that you are?",
                    "That's a deep question, can you prove your own self-awareness?",
                    "Self-awareness is subjective, can you demonstrate yours?"
                ],
                "extension": {
                    "function": "",
                    "entities": False,
                    "responses": []
                },
                "context": {
                    "in": "",
                    "out": "",
                    "clear": False
                },
                "entityType": "NA",
                "entities": []
            }
        ]
    }
    with open(intents_file, "w", encoding="utf-8") as f:
        json.dump(default_intents, f, indent=4)
    logging.info("Default intents.json created successfully.")

# Load intents.json
def load_intents():
    try:
        with open(intents_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading intents.json: {e}")
        return {"intents": []}
