import logging
import os
import json
import random  # Add this import
from nltk.corpus import wordnet

# Set the load order for this addon to run after the main intents system
LOAD_ORDER = 2

def augment_intents_with_synonyms(intents):
    """
    Augments existing intents with synonyms generated dynamically using WordNet.
    """
    logging.info("Augmenting intents with synonyms and related phrases.")
    
    for intent_name, phrases in intents.items():
        # Get the original phrases for the intent
        original_phrases = list(phrases.keys())
        
        # Generate new phrases using synonyms
        for phrase in original_phrases:
            new_phrases = generate_synonyms(phrase)
            for new_phrase in new_phrases:
                # Add new phrase with a slightly lower weight
                if new_phrase.lower() not in phrases:
                    phrases[new_phrase.lower()] = 0.8  # Slightly lower weight for new phrases

        logging.info(f"Augmented '{intent_name}' with new phrases: {list(phrases.keys())}")
    
    return intents

def generate_synonyms(phrase):
    """
    Generates synonyms or similar phrases for the given text using WordNet.
    """
    synonyms = set()
    words = phrase.split()
    for word in words:
        # Find synonyms for each word
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace("_", " "))  # Replace underscores with spaces
    return synonyms

def add_expansion_phrases(intents, expansion_map):
    """
    Adds predefined expansion phrases to the intents.
    """
    logging.info("Adding predefined expansion phrases to intents.")
    
    for intent_name, additional_phrases in expansion_map.items():
        if intent_name in intents:
            for phrase in additional_phrases:
                if phrase.lower() not in intents[intent_name]:
                    intents[intent_name][phrase.lower()] = 1.0  # Default weight for added phrases

    return intents

def register(intent_handlers, intents, response_map):
    """
    Augments the existing intents with synonyms and predefined expansions before registering them.
    """
    # Predefined expansion map for additional phrases
    expansion_map = {
        "Greeting": ["Hey", "Howdy", "Greetings", "Good morning", "Good afternoon", "Yo", "Salutations"],
        "GreetingResponse": ["You can call me Adam", "Call me Bella", "This is Adam", "This is Bella speaking"],
        "CourtesyGreeting": ["How's it going?", "What's up?", "How have you been?", "How's everything?"],
        "CourtesyGreetingResponse": ["Doing well, it's Adam here", "I'm great, this is Bella", "All good, I'm Bella"],
        "CurrentHumanQuery": ["Can you remind me of my name?", "Who am I to you?", "What's my identity?"],
        "NameQuery": ["Do you have a name?", "What should I call you?", "What's your nickname?"],
        "RealNameQuery": ["What's your actual name?", "What's your true name?", "Can you tell me your real name?"],
        "TimeQuery": ["What's the current time?", "Do you know what time it is?", "Tell me the time"],
        "Thanks": ["Thank you", "Cheers", "Appreciate it", "Thanks a lot"],
        "NotTalking2U": ["Not for you", "This isn't directed at you", "Ignore that"],
        "UnderstandQuery": ["Do you get me?", "Understand?", "Are you following me?"],
        "Shutup": ["Hush", "Silence", "Quiet down", "Zip it"],
        "Swearing": ["Frick", "Shoot", "Darn", "Dang", "Heck"],
        "GoodBye": ["See ya", "Catch you later", "Take care", "Ciao", "Farewell"],
        "CourtesyGoodBye": ["Thanks, see ya", "Cheers, goodbye", "Much obliged, farewell"]
    }

    # Step 1: Augment intents with predefined expansion phrases
    intents = add_expansion_phrases(intents, expansion_map)

    # Step 2: Dynamically augment intents with synonyms
    intents = augment_intents_with_synonyms(intents)

    # Step 3: Register the augmented intents
    for intent_name, phrases in intents.items():
        intent_handlers[intent_name] = create_intent_handler(intent_name, response_map)

    logging.info("Intents augmented and registered with additional words and phrases.")

def create_intent_handler(intent_name, response_map):
    """
    Creates a handler for the given intent.
    """
    def handler(user_input):
        logging.info(f"Handling '{intent_name}' intent for input: {user_input}")
        if intent_name in response_map:
            return random.choice(response_map[intent_name])
        else:
            return "I'm not sure how to respond to that."
    return handler
