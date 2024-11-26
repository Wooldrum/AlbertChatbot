import random
import re
from collections import defaultdict
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet as wn

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

question_words = ['how', 'what', 'when', 'where', 'why', 'who', 'which', 'whom', 'whose']

intents = {
    "greeting": [
        ("hello", 1.0), ("hi", 1.0), ("hey", 1.0),
        ("greetings", 0.95), ("good morning", 0.9),
        ("good afternoon", 0.9), ("good evening", 0.9),
        ("howdy", 0.85), ("what's up", 0.8), ("sup", 0.8), ("yo", 0.8)
    ],
    "farewell": [
        ("bye", 1.0), ("goodbye", 1.0), ("see you", 1.0),
        ("farewell", 0.95), ("later", 0.9), ("take care", 0.9),
        ("see ya", 0.85), ("catch you later", 0.85),
        ("peace out", 0.8), ("adios", 0.8), ("ciao", 0.8)
    ],
    "weather": [
        ("weather", 1.0), ("rain", 1.0), ("sunny", 1.0),
        ("forecast", 0.95), ("temperature", 0.9), ("climate", 0.9),
        ("storm", 0.85), ("wind", 0.85), ("snow", 0.85),
        ("rainy", 0.85), ("cloudy", 0.85), ("sunshine", 0.85),
        ("humidity", 0.8), ("conditions", 0.8)
    ],
    "time": [
        ("time", 1.0), ("clock", 1.0), ("hour", 1.0),
        ("minute", 0.95), ("second", 0.9), ("what time", 0.9),
        ("current time", 0.9), ("now", 0.85), ("today", 0.85),
        ("date", 0.85), ("day", 0.85), ("schedule", 0.8), ("calendar", 0.8)
    ],
    "joke": [
        ("joke", 1.0), ("funny", 1.0), ("laugh", 1.0),
        ("humor", 0.95), ("pun", 0.9), ("hilarious", 0.9),
        ("make me laugh", 0.85), ("tell me something funny", 0.85),
        ("comedy", 0.85), ("amuse me", 0.8), ("giggle", 0.8)
    ],
    "technology_news": [
        ("tech", 1.0), ("technology", 1.0), ("innovation", 1.0),
        ("gadgets", 1.0), ("devices", 1.0), ("latest", 1.0),
        ("new tech", 0.95), ("tech news", 0.95), ("technological", 0.9),
        ("breakthrough", 0.9), ("invention", 0.9), ("cutting edge", 0.85),
        ("high tech", 0.85), ("tech trends", 0.85), ("future tech", 0.85)
    ],
    "programming_help": [
        ("code", 1.0), ("programming", 1.0), ("bug", 1.0),
        ("error", 1.0), ("debug", 1.0), ("python", 1.0),
        ("javascript", 1.0), ("java", 1.0), ("develop", 0.95),
        ("script", 0.95), ("compile", 0.9), ("function", 0.9),
        ("variable", 0.9), ("syntax", 0.85), ("algorithm", 0.85)
    ],
    "ai_discussion": [
        ("ai", 1.0), ("artificial intelligence", 1.0),
        ("machine learning", 1.0), ("deep learning", 1.0),
        ("neural network", 1.0), ("robotics", 0.95),
        ("automation", 0.95), ("data science", 0.9),
        ("algorithm", 0.9), ("intelligence", 0.85), ("models", 0.85)
    ],
    "cybersecurity": [
        ("security", 1.0), ("hacking", 1.0), ("breach", 1.0),
        ("malware", 1.0), ("virus", 1.0), ("phishing", 1.0),
        ("cyber attack", 0.95), ("ransomware", 0.95),
        ("encryption", 0.9), ("firewall", 0.9),
        ("antivirus", 0.85), ("cybercrime", 0.85)
    ],
    "stock_market": [
        ("stock", 1.0), ("market", 1.0), ("invest", 1.0),
        ("investment", 1.0), ("portfolio", 1.0), ("trading", 1.0),
        ("shares", 1.0), ("financial", 0.95), ("broker", 0.95),
        ("equity", 0.9), ("buy", 0.9), ("sell", 0.9),
        ("bull market", 0.85), ("bear market", 0.85)
    ],
    "stock_prices": [
        ("price", 1.0), ("value", 1.0), ("increase", 1.0),
        ("decrease", 1.0), ("nasdaq", 1.0), ("nyse", 1.0),
        ("dow jones", 1.0), ("s&p 500", 1.0),
        ("stock price", 0.95), ("valuation", 0.95),
        ("trend", 0.9), ("market cap", 0.9),
        ("volatility", 0.85), ("dividend", 0.85)
    ],
    "gaming_news": [
        ("game", 1.0), ("gaming", 1.0), ("video game", 1.0),
        ("console", 1.0), ("playstation", 1.0), ("xbox", 1.0),
        ("nintendo", 1.0), ("pc gaming", 1.0),
        ("esports", 0.95), ("multiplayer", 0.95),
        ("release", 0.9), ("update", 0.9),
        ("dlc", 0.85), ("gameplay", 0.85), ("tournament", 0.85)
    ],
    "game_recommendations": [
        ("recommend", 1.0), ("suggest", 1.0), ("good", 1.0),
        ("best", 1.0), ("favorite", 1.0), ("game", 1.0),
        ("genre", 0.95), ("action", 0.95), ("adventure", 0.95),
        ("rpg", 0.9), ("strategy", 0.9), ("simulation", 0.85),
        ("puzzle", 0.85), ("sports", 0.85)
    ],
    "esports": [
        ("esports", 1.0), ("tournament", 1.0), ("league", 1.0),
        ("competition", 1.0), ("pro gamer", 1.0),
        ("championship", 0.95), ("match", 0.95),
        ("team", 0.9), ("event", 0.9),
        ("live stream", 0.85), ("spectate", 0.85)
    ],
    "movies": [
        ("movie", 1.0), ("film", 1.0), ("cinema", 1.0),
        ("actor", 1.0), ("actress", 1.0), ("director", 1.0),
        ("hollywood", 1.0), ("bollywood", 1.0),
        ("blockbuster", 0.95), ("trailer", 0.95),
        ("premiere", 0.9), ("screenplay", 0.9),
        ("genre", 0.85), ("award", 0.85)
    ],
    "music": [
        ("music", 1.0), ("song", 1.0), ("album", 1.0),
        ("band", 1.0), ("singer", 1.0), ("concert", 1.0),
        ("genre", 1.0), ("playlist", 0.95), ("melody", 0.95),
        ("lyrics", 0.9), ("performance", 0.9),
        ("instrument", 0.85), ("record", 0.85)
    ],
    "celebrity_news": [
        ("celebrity", 1.0), ("gossip", 1.0), ("scandal", 1.0),
        ("famous", 1.0), ("star", 1.0), ("paparazzi", 1.0),
        ("headline", 0.95), ("rumor", 0.95),
        ("interview", 0.9), ("relationship", 0.9),
        ("breakup", 0.85), ("affair", 0.85)
    ],
    "tv_shows": [
        ("tv", 1.0), ("show", 1.0), ("series", 1.0),
        ("episode", 1.0), ("season", 1.0), ("netflix", 1.0),
        ("hulu", 1.0), ("amazon prime", 1.0),
        ("streaming", 0.95), ("binge", 0.95),
        ("drama", 0.9), ("comedy", 0.9),
        ("pilot", 0.85), ("finale", 0.85)
    ],
    "fishing": [
        ("fish", 1.0), ("fishing", 1.0), ("trout", 1.0),
        ("angler", 0.95), ("bait", 0.9), ("hook", 0.9),
        ("rod", 0.85), ("reel", 0.85), ("catch", 0.85),
        ("lake", 0.85), ("river", 0.85)
    ],
}

response_map = {
    "greeting": [
        "Hi there! How can I assist you today?",
        "Hello! What's on your mind?",
        "Hey! How can I help?",
        "Greetings! Need any assistance?",
        "Howdy! What can I do for you?"
    ],
    "greeting_question": [
        "Hello! How can I help you today?",
        "Hi! What would you like to know?",
        "Greetings! Do you have a question for me?",
        "Hey there! How can I assist you?",
        "Hi! What can I do for you today?"
    ],
    "farewell": [
        "Goodbye! Take care!",
        "See you soon! Stay safe!",
        "Farewell! Hope to chat again!",
        "Later! Have a great day!",
        "Bye! Feel free to come back anytime!"
    ],
    "farewell_question": [
        "Are you saying goodbye or do you have a question?",
        "Do you need anything before you go?",
        "Is there anything else I can help you with?",
        "Leaving so soon? Let me know if you have any questions!",
        "Before you go, is there anything else you need?"
    ],
    "weather": [
        "It's sunny in my code!",
        "Weather is a mystery to me!",
        "I hope it's nice where you are!",
        "Weather updates are beyond my reach!",
        "Every day is a good day to chat!"
    ],
    "weather_question": [
        "I don't have real-time weather data, but I'm here to chat!",
        "Sorry, I can't provide weather updates.",
        "I wish I could tell you the weather, but I don't have that info.",
        "Weather forecasting isn't my forte, but I can help with other things!",
        "I'm not equipped with weather data, but let's talk about something else!"
    ],
    "time": [
        "I can't tell the time, but it's a good time to chat!",
        "Time is a construct, but I'm here now!",
        "It's always chatbot o'clock!",
        "I don't have a watch, but I'm here for you!",
        "Time flies when we're chatting!"
    ],
    "time_question": [
        "I don't have access to the current time, but I'm happy to chat!",
        "I'm not able to tell the time, but let's talk!",
        "Timekeeping isn't my specialty, but I'm here to help!",
        "I can't provide the current time, but is there anything else you need?",
        "Sorry, I can't tell the time, but feel free to ask me something else!"
    ],
    "joke": [
        "Why did the computer show up late? It had a hard drive!",
        "Why was the math book sad? It had too many problems!",
        "What do you call a belt made of watches? A waist of time!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "How many programmers does it take to change a light bulb? None, it's a hardware problem!"
    ],
    "joke_question": [
        "Would you like to hear a joke?",
        "I've got some jokes! Want to hear one?",
        "In the mood for a joke?",
        "I can tell you a joke if you'd like!",
        "Looking for something to laugh at?"
    ],
    "technology_news": [
        "The latest in technology is always fascinating!",
        "Did you hear about the new gadget that just came out?",
        "Technology is advancing so rapidly these days!",
        "AI and robotics are making headlines!",
        "Virtual reality is becoming more immersive!"
    ],
    "technology_news_question": [
        "Are you interested in the latest technology news?",
        "Would you like to discuss recent tech innovations?",
        "Curious about new gadgets or devices?",
        "Do you have questions about recent tech trends?",
        "Looking to talk about technology breakthroughs?"
    ],
    "programming_help": [
        "I'm here to help with your programming questions!",
        "What programming issue are you facing?",
        "Let's debug that code together!",
        "Programming can be challenging, how can I assist?",
        "Tell me more about the error you're encountering."
    ],
    "programming_help_question": [
        "What programming language are you working with?",
        "Describe the problem you're having in your code.",
        "Need help understanding a programming concept?",
        "I'm happy to help with programming questions!",
        "What coding issue can I assist you with?"
    ],
    "ai_discussion": [
        "Artificial Intelligence is transforming the world!",
        "AI and machine learning are exciting fields!",
        "Do you have questions about AI?",
        "Neural networks are fascinating, aren't they?",
        "Automation is changing many industries!"
    ],
    "ai_discussion_question": [
        "What would you like to know about AI?",
        "Interested in discussing machine learning?",
        "Do you have questions about artificial intelligence?",
        "Let's talk about AI advancements!",
        "Curious about how AI works?"
    ],
    "cybersecurity": [
        "Cybersecurity is crucial in today's digital age.",
        "Always be cautious of phishing scams!",
        "Protecting data is more important than ever.",
        "Keeping software updated helps prevent breaches.",
        "Use strong passwords to enhance security!"
    ],
    "cybersecurity_question": [
        "Do you have questions about cybersecurity?",
        "Need advice on staying safe online?",
        "Want to discuss ways to protect your data?",
        "Curious about recent cybersecurity threats?",
        "How can I assist with your cybersecurity concerns?"
    ],
    "stock_market": [
        "The stock market can be quite volatile.",
        "Are you interested in investing?",
        "Diversifying your portfolio is key!",
        "Do you follow any particular stocks?",
        "Investing wisely can lead to great returns."
    ],
    "stock_market_question": [
        "Do you have questions about investing?",
        "Interested in learning about the stock market?",
        "Want to discuss financial strategies?",
        "How can I assist with your investment queries?",
        "Looking for information on trading stocks?"
    ],
    "stock_prices": [
        "Stock prices fluctuate based on various factors.",
        "Keeping an eye on market trends is important.",
        "Would you like to discuss stock valuations?",
        "Economic news often impacts stock prices.",
        "Do you have specific stocks in mind?"
    ],
    "stock_prices_question": [
        "Which stock prices are you interested in?",
        "Do you want to talk about market trends?",
        "Looking for information on stock valuations?",
        "How can I assist with your stock price inquiries?",
        "Interested in the latest movements in the stock market?"
    ],
    "gaming_news": [
        "Have you played any new games lately?",
        "The gaming industry is booming!",
        "What are your favorite video games?",
        "Exciting game releases are coming up!",
        "Gaming technology keeps getting better!"
    ],
    "gaming_news_question": [
        "Looking for the latest gaming news?",
        "Do you have questions about new game releases?",
        "Want to discuss upcoming games?",
        "Curious about recent updates in gaming?",
        "How can I assist with your gaming inquiries?"
    ],
    "game_recommendations": [
        "I can suggest some great games!",
        "What genre of games do you enjoy?",
        "Looking for something action-packed or more relaxed?",
        "Have you tried any indie games?",
        "Multiplayer or single-player games?"
    ],
    "game_recommendations_question": [
        "What type of games are you interested in?",
        "Would you like some game recommendations?",
        "I can suggest games based on your preferences!",
        "Tell me what genres you like, and I'll recommend some games.",
        "Looking for new games to play?"
    ],
    "esports": [
        "Esports tournaments are thrilling to watch!",
        "Do you follow any esports leagues?",
        "Competitive gaming has become a major sport!",
        "Who is your favorite esports team?",
        "Esports events draw huge audiences!"
    ],
    "esports_question": [
        "Are you interested in getting into esports?",
        "Do you have questions about esports competitions?",
        "Looking to learn more about professional gaming?",
        "Want to discuss esports teams or players?",
        "How can I help you with esports information?"
    ],
    "esports_follow_up": [
        "Esports are competitive video gaming events held worldwide.",
        "You can get into esports by practicing a game you're passionate about and joining local tournaments.",
        "Following esports teams and watching professional matches can help you learn more.",
        "Building skills and networking with other gamers is a great way to start in esports.",
        "Would you like more information on specific games or tournaments?"
    ],
    "movies": [
        "Seen any good movies lately?",
        "I love discussing films!",
        "Who's your favorite actor or director?",
        "There's a lot of buzz about upcoming movies!",
        "What genre of movies do you enjoy?"
    ],
    "movies_question": [
        "Looking for movie recommendations?",
        "Do you have questions about a specific film?",
        "Want to discuss recent movie releases?",
        "Curious about upcoming movies?",
        "How can I assist with your movie inquiries?"
    ],
    "music": [
        "Music is a universal language!",
        "What kind of music do you enjoy?",
        "Any favorite bands or artists?",
        "Have you been to any concerts recently?",
        "Music streaming makes discovering new songs easy!"
    ],
    "music_question": [
        "Would you like music recommendations?",
        "Do you have questions about a particular artist?",
        "Want to discuss music genres?",
        "Looking for new songs to listen to?",
        "How can I help with your music interests?"
    ],
    "celebrity_news": [
        "Celebrities often make the headlines!",
        "Did you hear about the latest celebrity gossip?",
        "Who's your favorite star?",
        "Celebrity news can be quite intriguing!",
        "There's always something happening in Hollywood!"
    ],
    "celebrity_news_question": [
        "Interested in the latest celebrity news?",
        "Do you have questions about a particular celebrity?",
        "Want to discuss celebrity events?",
        "Curious about recent celebrity gossip?",
        "How can I assist with your celebrity news inquiries?"
    ],
    "tv_shows": [
        "Binge-watching any good shows recently?",
        "Streaming services have so many options!",
        "What's your favorite TV series?",
        "Have you watched any new series?",
        "TV shows are a great way to unwind!"
    ],
    "tv_shows_question": [
        "Looking for TV show recommendations?",
        "Do you have questions about a specific series?",
        "Want to discuss recent episodes?",
        "Curious about upcoming TV shows?",
        "How can I assist with your TV show interests?"
    ],
    "fishing": [
        "Fishing is a relaxing hobby!",
        "Do you enjoy fishing?",
        "Trout are freshwater fish often found in rivers.",
        "Would you like to know more about fishing techniques?",
        "Fishing requires patience and skill."
    ],
    "fishing_question": [
        "What would you like to know about fishing?",
        "Are you interested in learning how to fish?",
        "Do you have questions about catching trout?",
        "I can share information about fishing if you'd like!",
        "How can I assist you with your fishing inquiries?"
    ],
    "unknown": [
        "I'm not sure I understand. Could you clarify?",
        "Sorry, I didn't get that. Can you rephrase?",
        "Hmm, I'm not sure how to respond to that.",
        "Could you please provide more details?",
        "Let's try discussing something else!"
    ],
    "unknown_question": [
        "That's an interesting question, but I'm not sure how to answer.",
        "I'm sorry, I don't have information on that topic.",
        "Could you ask about something else?",
        "I'm not equipped to answer that question.",
        "Perhaps we can talk about something else?"
    ],
    "negation": [
        "Alright, let me know if there's anything else you're interested in!",
        "No problem! What else would you like to talk about?",
        "Okay, feel free to ask me about something else.",
        "Understood. Is there another topic you'd like to discuss?",
        "Sure, I'm here if you need anything."
    ],
}

keyword_intent_map = defaultdict(lambda: ("unknown", 0))

for intent, keywords in intents.items():
    for keyword, weight in keywords:
        keyword_intent_map[keyword] = (intent, weight)
        for syn in wn.synsets(keyword):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ').lower()
                if synonym != keyword:
                    synonym_weight = weight * random.uniform(0.8, 0.95)
                    synonym_weight = min(synonym_weight, 1.0)
                    if synonym not in keyword_intent_map or keyword_intent_map[synonym][1] < synonym_weight:
                        keyword_intent_map[synonym] = (intent, synonym_weight)
        if keyword in question_words:
            keyword_intent_map[keyword] = ("question", weight * 0.5)

def preprocess_input(user_input):
    user_input_cleaned = re.sub(r'[^\w\s]', '', user_input.lower())
    tokens = nltk.word_tokenize(user_input_cleaned)
    return [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

def analyze_input(user_input, context):
    words = preprocess_input(user_input)
    scores = defaultdict(float)
    is_question = False

    for word in words:
        if word in question_words:
            is_question = True
            break

    if user_input.strip().endswith('?'):
        is_question = True

    if not words:
        return context.get('last_intent', 'unknown'), is_question

    if words[0] in ['yes', 'yeah', 'yep', 'sure', 'absolutely']:
        return context.get('last_intent', 'unknown'), is_question
    elif words[0] in ['no', 'nope', 'nah', 'not really']:
        return 'negation', is_question

    for word in words:
        if word in keyword_intent_map:
            intent, weight = keyword_intent_map[word]
            if word in question_words:
                weight *= 1.5
            scores[intent] += weight

    if is_question:
        for intent in scores:
            scores[intent] *= 1.2

    if scores:
        best_intent = max(scores, key=scores.get)
        return best_intent, is_question

    return "unknown", is_question

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    context = {}
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                print(random.choice(response_map["farewell"]))
                break

            intent, is_question = analyze_input(user_input, context)
            context['last_intent'] = intent

            if intent == 'negation':
                possible_responses = response_map["negation"]
            else:
                if is_question:
                    possible_responses = response_map.get(f"{intent}_question", response_map.get(intent, response_map["unknown"]))
                else:
                    possible_responses = response_map.get(intent, response_map["unknown"])

                if user_input.lower() in ['yes', 'yeah', 'yep', 'sure', 'absolutely']:
                    last_intent = context.get('last_intent')
                    follow_up_responses = response_map.get(f"{last_intent}_follow_up", [])
                    if follow_up_responses:
                        possible_responses = follow_up_responses

            response = random.choice(possible_responses)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: Oops! Something went wrong: {e}")

if __name__ == "__main__":
    chatbot()
