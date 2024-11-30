# ========================================
# Expanded Advanced Conversation Addon
# ========================================

import random
import os

# Context dictionary to store conversation context
conversation_context = {
    'previous_intent': None,
    'previous_response': None,
    'user_name': None,
    'current_topic': None,
    'follow_up_needed': False,
}

# Path to the userinfo.txt file in the main directory
main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
userinfo_path = os.path.join(main_dir, 'userinfo.txt')

# Load user info if available
try:
    with open(userinfo_path, 'r') as f:
        user_name = f.read().strip()
        if user_name:
            conversation_context['user_name'] = user_name
except FileNotFoundError:
    pass
except Exception as e:
    print(f"Error loading user info: {e}")


# General Helper Function
def random_response(responses):
    return random.choice(responses)


# Intent Handlers
def handle_greeting(user_input):
    user_name = conversation_context.get('user_name')
    if not user_name:
        user_name = input("Chatbot: May I have your name?\nYou: ").strip()
        if user_name:
            conversation_context['user_name'] = user_name
            # Save the user's name to userinfo.txt
            try:
                with open(userinfo_path, 'w') as f:
                    f.write(user_name)
            except Exception as e:
                print(f"Error saving user info: {e}")

    user_name = conversation_context.get('user_name', 'there')
    responses = [
        f"Hi {user_name}! How's your day going?",
        f"Hello, {user_name}! How can I assist you today?",
        f"Hey {user_name}! What's on your mind?",
    ]
    return random_response(responses)


def handle_small_talk(user_input):
    positive_words = ['good', 'great', 'fine', 'well', 'awesome', 'fantastic']
    negative_words = ['bad', 'not good', 'terrible', 'sad', 'unhappy', 'tired']

    if any(word in user_input.lower() for word in positive_words):
        responses = [
            "I'm glad to hear that! What else would you like to discuss?",
            "That's wonderful! Is there anything I can help with today?",
            "Great! Do you have a specific topic in mind?",
        ]
    elif any(word in user_input.lower() for word in negative_words):
        responses = [
            "I'm sorry to hear that. If you'd like to share more, I'm here to listen.",
            "That's unfortunate. Let me know if there's something I can do to help.",
            "I hope things get better soon. Is there anything specific you'd like to talk about?",
        ]
    else:
        responses = [
            "I see. How can I assist you today?",
            "Thanks for sharing. Is there anything you'd like to discuss?",
            "Understood. What can I help you with?",
        ]
    return random_response(responses)


def handle_hobbies(user_input):
    conversation_context['current_topic'] = 'hobbies'
    responses = [
        "Hobbies are great! What do you enjoy doing in your free time?",
        "Do you like reading, painting, gaming, or something else?",
        "Hobbies can be so relaxing. What's yours?",
    ]
    return random_response(responses)


def handle_travel(user_input):
    conversation_context['current_topic'] = 'travel'
    responses = [
        "Traveling is such an adventure! Do you have a favorite destination?",
        "Where do you dream of going next?",
        "Do you prefer beaches, mountains, or cities?",
    ]
    return random_response(responses)


def handle_health(user_input):
    conversation_context['current_topic'] = 'health'
    responses = [
        "Health is wealth! Are you looking for fitness tips or healthy recipes?",
        "Staying active is so important. Do you have a workout routine?",
        "Are you interested in mental health tips or general well-being advice?",
    ]
    return random_response(responses)


def handle_emotions(user_input):
    conversation_context['current_topic'] = 'emotions'
    positive_words = ['happy', 'excited', 'content', 'peaceful', 'joyful']
    negative_words = ['angry', 'sad', 'frustrated', 'anxious', 'lonely']

    if any(word in user_input.lower() for word in positive_words):
        responses = [
            "That's wonderful to hear! What made your day special?",
            "I'm glad you're feeling good. Do you want to share more?",
            "That's great! What's the highlight of your day so far?",
        ]
    elif any(word in user_input.lower() for word in negative_words):
        responses = [
            "I'm sorry you're feeling that way. Do you want to talk about it?",
            "I'm here to listen. What's been on your mind?",
            "It's okay to feel that way sometimes. Let me know if I can help.",
        ]
    else:
        responses = [
            "Emotions can be complicated. Do you want to share more about how you're feeling?",
            "I'm here to talk. Let me know what you're going through.",
            "How are you feeling today?",
        ]
    return random_response(responses)


def handle_unknown(user_input):
    responses = [
        "I'm not sure I understand. Could you clarify?",
        "Could you rephrase that for me?",
        "Hmm, I'm not sure how to respond to that.",
    ]
    return random_response(responses)


# Intent Recognition
def analyze_user_input(user_input):
    user_input_lower = user_input.lower()

    # Greeting intent
    if any(greet in user_input_lower for greet in ['hello', 'hi', 'hey', 'howdy']):
        return 'greeting'

    # Small talk intent
    if any(word in user_input_lower for word in ['how are you', 'how is it going', 'what’s up']):
        return 'small_talk'

    # Hobbies intent
    if any(word in user_input_lower for word in ['hobby', 'hobbies', 'free time', 'leisure']):
        return 'hobbies'

    # Travel intent
    if any(word in user_input_lower for word in ['travel', 'vacation', 'trip', 'destination']):
        return 'travel'

    # Health intent
    if any(word in user_input_lower for word in ['health', 'fitness', 'exercise', 'well-being']):
        return 'health'

    # Emotions intent
    if any(word in user_input_lower for word in ['feel', 'feeling', 'emotions', 'mood']):
        return 'emotions'

    return 'unknown'


# Register the Addon
def register(intent_handlers, intents, response_map):
    intent_handlers['greeting'] = handle_greeting
    intent_handlers['small_talk'] = handle_small_talk
    intent_handlers['hobbies'] = handle_hobbies
    intent_handlers['travel'] = handle_travel
    intent_handlers['health'] = handle_health
    intent_handlers['emotions'] = handle_emotions
    intent_handlers['unknown'] = handle_unknown

    # Use a custom intent analyzer
    global custom_analyze_user_input
    custom_analyze_user_input = analyze_user_input


# Indicate custom analyzer
custom_analyze_user_input = analyze_user_input
