# ========================================
# Core Chatbot - Alfred, by Wooldrum
# ========================================

import os
import importlib.util
import logging
import string
import json

# Global variable for custom intent analyzer
custom_analyze_user_input = None

# Logging Setup
def setup_logging():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, 'debug.log')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Global Variables for Intents and Responses
intents = {}
response_map = {}
intent_handlers = {}
common_phrases = {}

# Utility Functions
def preprocess_input(user_input):
    translator = str.maketrans('', '', string.punctuation)
    return user_input.lower().translate(translator).strip()

def analyze_input(user_input):
    preprocessed_input = preprocess_input(user_input)
    words = preprocessed_input.split()

    ngrams = []
    for n in range(1, 4):
        ngrams.extend([' '.join(words[i:i+n]) for i in range(len(words)-n+1)])

    scores = {}
    for intent, keywords in intents.items():
        intent_score = 0
        keyword_dict = dict(keywords)
        for ngram in ngrams:
            if ngram in keyword_dict:
                intent_score += keyword_dict[ngram]
        scores[intent] = intent_score
        logging.debug(f"Intent '{intent}' score: {intent_score}")

    for phrase, intent in common_phrases.items():
        if phrase in preprocessed_input:
            scores[intent] = scores.get(intent, 0) + 1.0
            logging.debug(f"Common phrase '{phrase}' found for intent '{intent}'")

    if scores:
        best_intent = max(scores, key=scores.get)
        logging.debug(f"Best intent: {best_intent} with score {scores[best_intent]}")
        if scores[best_intent] > 0:
            return best_intent
    return "unknown"

def load_addons():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    addon_dir = os.path.join(base_dir, 'addons')

    if not os.path.exists(addon_dir):
        os.makedirs(addon_dir)
        logging.info(f"Addon directory created at {addon_dir}")
        print(f"Place addon files in {addon_dir} and restart the chatbot.")
        return

    addon_files = [f for f in os.listdir(addon_dir) if f.endswith(".py")]
    addons = []

    for filename in addon_files:
        addon_path = os.path.join(addon_dir, filename)
        try:
            spec = importlib.util.spec_from_file_location(filename, addon_path)
            addon_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(addon_module)

            load_order = getattr(addon_module, 'LOAD_ORDER', 100)
            addons.append((load_order, addon_module))
        except Exception as e:
            logging.error(f"Failed to load addon '{filename}': {e}")

    addons.sort(key=lambda x: x[0])
    for _, addon in addons:
        try:
            if hasattr(addon, 'register'):
                addon.register(intent_handlers, intents, response_map)
                logging.info(f"Addon '{addon.__name__}' loaded successfully.")
            if hasattr(addon, 'custom_analyze_user_input'):
                global custom_analyze_user_input
                custom_analyze_user_input = addon.custom_analyze_user_input
                logging.info(f"Custom intent analyzer from '{addon.__name__}' loaded.")
        except Exception as e:
            logging.error(f"Error initializing addon '{addon.__name__}': {e}")

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Take care!")
            break

        if custom_analyze_user_input:
            intent = custom_analyze_user_input(user_input)
            if intent == 'unknown':
                intent = analyze_input(user_input)
        else:
            intent = analyze_input(user_input)

        handler = intent_handlers.get(intent)
        if handler:
            try:
                response = handler(user_input)
                if response is None:
                    response = random.choice(response_map.get(intent, ["I'm not sure how to respond."]))
            except Exception as e:
                logging.error(f"Error in handler for intent '{intent}': {e}")
                response = "Sorry, I encountered an error."
        else:
            response = random.choice(response_map.get(intent, ["I'm not sure how to respond."]))

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    import random
    setup_logging()
    load_addons()
    chatbot()
