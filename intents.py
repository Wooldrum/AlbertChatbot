# ========================================
# Alfred Default Responses - Intents and Responses
# ========================================

# Intents with their associated keywords and weights
intents = {
    "greeting": [
        ("hello", 1.0), ("hi", 1.0), ("hey", 1.0),
        ("greetings", 0.95), ("good morning", 0.95),
        ("good afternoon", 0.95), ("good evening", 0.95),
        ("howdy", 0.9), ("what's up", 0.9), ("sup", 0.85), ("yo", 0.85)
    ],
    "farewell": [
        ("bye", 1.0), ("goodbye", 1.0), ("see you", 1.0),
        ("farewell", 0.95), ("later", 0.95), ("take care", 0.95),
        ("see ya", 0.9), ("catch you later", 0.9),
        ("peace out", 0.85), ("adios", 0.85), ("ciao", 0.85)
    ],
    "weather": [
        ("weather", 1.0), ("rain", 1.0), ("sunny", 1.0),
        ("forecast", 0.95), ("temperature", 0.95), ("climate", 0.95),
        ("storm", 0.9), ("wind", 0.9), ("snow", 0.9),
        ("rainy", 0.85), ("cloudy", 0.85), ("sunshine", 0.85),
        ("humidity", 0.85), ("conditions", 0.85)
    ],
    "time": [
        ("time", 1.0), ("clock", 1.0), ("hour", 1.0),
        ("minute", 0.95), ("second", 0.95), ("what time", 0.95),
        ("current time", 0.95), ("now", 0.9), ("today", 0.9),
        ("date", 0.9), ("day", 0.9), ("schedule", 0.85), ("calendar", 0.85)
    ],
    "joke": [
        ("joke", 1.0), ("funny", 1.0), ("laugh", 1.0),
        ("humor", 0.95), ("pun", 0.95), ("hilarious", 0.95),
        ("make me laugh", 0.9), ("tell me something funny", 0.9),
        ("comedy", 0.85), ("amuse me", 0.85), ("giggle", 0.85)
    ],
    "technology_news": [
        ("tech", 1.0), ("technology", 1.0), ("innovation", 1.0),
        ("gadgets", 1.0), ("devices", 1.0), ("latest", 1.0),
        ("new tech", 0.95), ("tech news", 0.95), ("technological", 0.95),
        ("breakthrough", 0.9), ("invention", 0.9), ("cutting edge", 0.9),
        ("high tech", 0.85), ("tech trends", 0.85), ("future tech", 0.85)
    ],
    "programming_help": [
        ("code", 1.0), ("programming", 1.0), ("bug", 1.0),
        ("error", 1.0), ("debug", 1.0), ("python", 1.0),
        ("javascript", 1.0), ("java", 1.0), ("develop", 0.95),
        ("script", 0.95), ("compile", 0.95), ("function", 0.9),
        ("variable", 0.9), ("syntax", 0.9), ("algorithm", 0.85)
    ],
    "ai_discussion": [
        ("ai", 1.0), ("artificial intelligence", 1.0),
        ("machine learning", 1.0), ("deep learning", 1.0),
        ("neural network", 1.0), ("robotics", 0.95),
        ("automation", 0.95), ("data science", 0.95),
        ("algorithm", 0.9), ("intelligence", 0.9), ("models", 0.85)
    ],
    "cybersecurity": [
        ("security", 1.0), ("hacking", 1.0), ("breach", 1.0),
        ("malware", 1.0), ("virus", 1.0), ("phishing", 1.0),
        ("cyber attack", 0.95), ("ransomware", 0.95),
        ("encryption", 0.95), ("firewall", 0.9),
        ("antivirus", 0.9), ("cybercrime", 0.85)
    ],
    "stock_market": [
        ("stock market", 1.0), ("stocks", 1.0), ("investing", 1.0),
        ("investment", 1.0), ("portfolio", 1.0), ("trading", 1.0),
        ("shares", 1.0), ("financial", 0.95), ("broker", 0.95),
        ("equity", 0.95), ("buy", 0.9), ("sell", 0.9),
        ("bull market", 0.9), ("bear market", 0.9),
        ("stock", 1.0), ("stocks", 1.0)
    ],
    "stock_prices": [
        ("price", 1.0), ("value", 1.0), ("increase", 1.0),
        ("decrease", 1.0), ("nasdaq", 1.0), ("nyse", 1.0),
        ("dow jones", 1.0), ("s&p 500", 1.0),
        ("stock price", 1.0), ("valuation", 0.95),
        ("trend", 0.95), ("market cap", 0.9),
        ("volatility", 0.9), ("dividend", 0.85),
        ("stock prices", 1.0)
    ],
    "gaming_news": [
        ("game", 1.0), ("gaming", 1.0), ("video game", 1.0),
        ("console", 1.0), ("playstation", 1.0), ("xbox", 1.0),
        ("nintendo", 1.0), ("pc gaming", 1.0),
        ("esports", 1.0), ("multiplayer", 0.95),
        ("release", 0.95), ("update", 0.9),
        ("dlc", 0.9), ("gameplay", 0.85), ("tournament", 0.85)
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
        ("live stream", 0.85), ("spectate", 0.85),
        ("organization", 1.0), ("start", 0.95)
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
        ("angler", 1.0), ("bait", 0.95), ("hook", 0.95),
        ("rod", 0.95), ("reel", 0.95), ("catch", 0.95),
        ("lake", 0.9), ("river", 0.9), ("go fishing", 1.0),
        ("fishing tips", 1.0), ("help me fish", 1.0)
    ],
    "health_fitness": [
        ("health", 1.0), ("fitness", 1.0), ("exercise", 1.0),
        ("workout", 1.0), ("diet", 0.95), ("nutrition", 0.95),
        ("yoga", 0.9), ("meditation", 0.9), ("gym", 0.85),
        ("running", 0.85), ("cycling", 0.85), ("weightlifting", 0.85),
        ("wellness", 0.85), ("healthy lifestyle", 0.85)
    ],
    "travel": [
        ("travel", 1.0), ("vacation", 1.0), ("trip", 1.0),
        ("flight", 0.95), ("hotel", 0.95), ("tour", 0.95),
        ("destination", 0.9), ("journey", 0.9), ("backpacking", 0.85),
        ("adventure", 0.85), ("road trip", 0.85), ("itinerary", 0.85),
        ("passport", 0.8), ("visa", 0.8)
    ],
    "food_recipes": [
        ("food", 1.0), ("recipe", 1.0), ("cooking", 1.0),
        ("cook", 1.0), ("baking", 0.95), ("meal", 0.95),
        ("ingredients", 0.95), ("dish", 0.9), ("cuisine", 0.9),
        ("restaurant", 0.85), ("dietary", 0.85), ("vegetarian", 0.85),
        ("vegan", 0.85), ("gluten-free", 0.85)
    ],
    "books": [
        ("book", 1.0), ("reading", 1.0), ("novel", 1.0),
        ("author", 1.0), ("literature", 0.95), ("genre", 0.95),
        ("fiction", 0.95), ("non-fiction", 0.9), ("biography", 0.9),
        ("mystery", 0.85), ("science fiction", 0.85), ("fantasy", 0.85),
        ("classic", 0.85), ("thriller", 0.85)
    ],
    "sports": [
        ("sports", 1.0), ("football", 1.0), ("basketball", 1.0),
        ("soccer", 1.0), ("baseball", 0.95), ("tennis", 0.95),
        ("cricket", 0.95), ("golf", 0.9), ("hockey", 0.9),
        ("olympics", 0.85), ("athletics", 0.85), ("equestrian", 0.85),
        ("rugby", 0.85), ("boxing", 0.85)
    ],
    "finance": [
        ("finance", 1.0), ("budget", 1.0), ("investment", 1.0),
        ("saving", 1.0), ("retirement", 0.95), ("tax", 0.95),
        ("loan", 0.95), ("mortgage", 0.9), ("credit", 0.9),
        ("debt", 0.9), ("financial planning", 0.85), ("wealth management", 0.85),
        ("stocks", 0.85), ("bonds", 0.85)
    ],
    "education": [
        ("education", 1.0), ("learning", 1.0), ("school", 1.0),
        ("college", 1.0), ("university", 1.0), ("courses", 0.95),
        ("degree", 0.95), ("tuition", 0.95), ("scholarship", 0.9),
        ("online courses", 0.9), ("certification", 0.9), ("training", 0.85),
        ("study", 0.85), ("tutorial", 0.85)
    ],
    "entertainment": [
        ("entertainment", 1.0), ("music", 1.0), ("movies", 1.0),
        ("tv", 1.0), ("concert", 1.0), ("festival", 0.95),
        ("theater", 0.95), ("show", 0.95), ("celebrity", 0.9),
        ("comedy", 0.9), ("drama", 0.85), ("documentary", 0.85),
        ("streaming", 0.85), ("gaming", 0.85)
    ],
}

# Define common phrases for better intent detection
common_phrases = {
    "single player": "game_recommendations",
    "multi player": "game_recommendations",
    "stock price": "stock_prices",
    "stock prices": "stock_prices",
    "stock": "stock_market",
    "stocks": "stock_market",
    "how to": "question",
    "can you": "question",
    "could you": "question",
    "help me": "help_request",
    "go fishing": "fishing",
    "fishing tips": "fishing",
    "catch fish": "fishing",
    # Add more as needed
}

# Define responses for each intent
response_map = {
    "greeting": [
        "Hi there! How can I assist you today?",
        "Hello! What's on your mind?",
        "Hey! How can I help?",
        "Greetings! Need any assistance?",
        "Howdy! What can I do for you?"
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
        "Starting an esports organization is exciting!",
        "Esports tournaments are thrilling to watch!",
        "Do you follow any esports leagues?",
        "Competitive gaming has become a major sport!",
        "Who is your favorite esports team?"
    ],
    "esports_question": [
        "Are you interested in getting into esports?",
        "Do you have questions about esports competitions?",
        "Looking to learn more about professional gaming?",
        "Want to discuss esports teams or players?",
        "How can I help you with esports information?"
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
        "How can I assist you with your movie inquiries?"
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
        "I'd be happy to share some fishing tips!",
        "Do you prefer freshwater or saltwater fishing?",
        "Catching trout requires patience and the right bait.",
        "Angling can be very rewarding!"
    ],
    "fishing_question": [
        "What would you like to know about fishing?",
        "Are you interested in learning how to fish?",
        "Need advice on catching trout or angler fish?",
        "I can share information about fishing techniques!",
        "How can I assist you with your fishing inquiries?"
    ],
    "health_fitness": [
        "Maintaining good health is essential! How can I assist you with fitness or nutrition?",
        "Health and fitness are vital for a balanced life. What would you like to discuss?",
        "Staying fit requires dedication. Do you need workout tips or diet advice?",
        "Health is wealth! How can I help you with your fitness goals?",
        "Great choice! Let's talk about maintaining a healthy lifestyle."
    ],
    "health_fitness_question": [
        "Are you looking for workout routines or nutrition tips?",
        "Do you need advice on staying healthy?",
        "Would you like to discuss fitness plans or dietary guidelines?",
        "How can I assist you with your health and fitness?",
        "Are you interested in exercise tips or nutrition information?"
    ],
    "travel": [
        "Traveling opens up new horizons! Where would you like to go?",
        "Adventure awaits! Do you need travel tips or destination ideas?",
        "Exploring the world is exciting. How can I assist your travel plans?",
        "Planning a trip? Let me know how I can help!",
        "Travel is a wonderful experience. What destination are you interested in?"
    ],
    "travel_question": [
        "Are you looking for destination recommendations or travel tips?",
        "Do you need assistance with planning your trip?",
        "Would you like information on flights or accommodations?",
        "How can I help with your travel inquiries?",
        "Are you interested in exploring specific countries or cities?"
    ],
    "food_recipes": [
        "Cooking is fun! What recipe are you looking for?",
        "I can help you find delicious recipes. What would you like to cook?",
        "Food brings people together. Do you need a recipe or cooking tips?",
        "Looking to try something new in the kitchen? Let me know!",
        "I'd love to share some tasty recipes with you!"
    ],
    "food_recipes_question": [
        "Are you searching for a specific recipe or general cooking ideas?",
        "Do you need help with meal planning or ingredient substitutions?",
        "Would you like vegetarian, vegan, or gluten-free recipes?",
        "How can I assist you with your cooking needs?",
        "Are you interested in quick recipes or elaborate dishes?"
    ],
    "books": [
        "Books are gateways to knowledge! What book are you interested in?",
        "I love discussing literature. Do you need book recommendations?",
        "Reading enriches the mind. How can I assist you with books?",
        "Looking for your next read? Let me know your favorite genres!",
        "Books open up new worlds. What are you reading lately?"
    ],
    "books_question": [
        "Are you looking for a specific book or recommendations?",
        "Do you need information about an author or genre?",
        "Would you like suggestions for your next read?",
        "How can I help you with your book-related queries?",
        "Are you interested in fiction, non-fiction, or specific genres?"
    ],
    "sports": [
        "Sports keep us active and entertained! Which sport are you interested in?",
        "I enjoy discussing sports. Do you follow any teams or events?",
        "Sports are thrilling! How can I assist you today?",
        "Looking to talk about a particular sport or recent matches?",
        "Sports bring people together. What would you like to discuss?"
    ],
    "sports_question": [
        "Are you interested in a specific sport or general sports news?",
        "Do you follow any particular teams or athletes?",
        "Would you like updates on recent matches or events?",
        "How can I assist you with your sports inquiries?",
        "Are you looking for sports news, statistics, or history?"
    ],
    "finance": [
        "Finance is crucial for personal growth. How can I assist you?",
        "Managing finances wisely leads to success. What do you need help with?",
        "Financial planning is key. Do you have any specific questions?",
        "Let's talk about budgeting, investing, or saving strategies!",
        "Understanding finance can empower you. How can I help?"
    ],
    "finance_question": [
        "Are you looking for budgeting tips or investment advice?",
        "Do you need information on loans, mortgages, or savings?",
        "Would you like to discuss financial planning or wealth management?",
        "How can I assist you with your financial queries?",
        "Are you interested in personal finance, business finance, or markets?"
    ],
    "education": [
        "Education shapes our future! What topic are you interested in?",
        "I can help with learning resources or educational information. How can I assist?",
        "Learning never stops. Do you need help with a specific subject?",
        "Looking to expand your knowledge? Let me know how I can help!",
        "Education empowers. What would you like to discuss?"
    ],
    "education_question": [
        "Are you seeking resources for a particular subject or course?",
        "Do you need help with study tips or educational planning?",
        "Would you like information on degrees, certifications, or online courses?",
        "How can I assist you with your educational needs?",
        "Are you interested in learning materials, tutoring, or academic advice?"
    ],
    "entertainment": [
        "Entertainment keeps life exciting! What would you like to talk about?",
        "I love discussing movies, music, and more. How can I assist you?",
        "Looking for entertainment recommendations? Let me know!",
        "Entertainment options are endless. What interests you today?",
        "From movies to music, I'm here to chat about all things entertainment!"
    ],
    "entertainment_question": [
        "Are you interested in movies, music, or other forms of entertainment?",
        "Do you need recommendations for films or songs?",
        "Would you like to discuss a specific movie, show, or artist?",
        "How can I assist you with your entertainment inquiries?",
        "Are you looking for entertainment news, reviews, or suggestions?"
    ],
    "stock_specific_response": [
        "The current price of {name} ({symbol}) is {price}. Change: {change}, {percent_change}",
        "{name} ({symbol}) is currently trading at {price}. Daily Change: {change}, {percent_change}",
        "As of now, {name}'s stock price is {price}. Change: {change}, {percent_change}",
        "{name} stock ({symbol}) is valued at {price} at the moment. Change: {change}, {percent_change}",
        "The latest price for {name} ({symbol}) is {price}. Change: {change}, {percent_change}"
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
