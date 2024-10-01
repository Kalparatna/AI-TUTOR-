# App/views.py
from django.shortcuts import render, redirect
import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Set up the API key for the genai package
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate learning modules
def generate_learning_modules(topic):
    model = genai.GenerativeModel('gemini-pro')
    prompt = (
        f"Generate five learning modules for the topic '{topic}'. "
        "Each module should have a clear title and a detailed one-line description, "
        "formatted as follows:\n\n"
        "Title - Description\n"
        "Title - Description\n"
        "Title - Description\n"
        "Title - Description\n"
        "Title - Description\n\n"
        "Make sure the titles are catchy, related and the descriptions are engaging and informative."
    )
    response = model.generate_content(prompt)
    
    modules = response.text.split("\n")
    modules = [module.strip() for module in modules if module.strip()]
    
    return modules[:5]

# Index view
def index(request):
    error = None
    topic = ""

    if request.method == "POST":
        topic = request.POST.get("topic")
        if topic:
            try:
                return redirect('modules', topic=topic)  # Redirect to the modules page
            except Exception as e:
                error = "Error generating modules: " + str(e)
        else:
            error = "Please enter a valid topic."

    return render(request, 'index.html', {'topic': topic, 'error': error})

# Modules view
def modules(request, topic):
    modules = []
    error = None

    if topic:
        try:
            modules = generate_learning_modules(topic)
        except Exception as e:
            error = "Error generating modules: " + str(e)

    return render(request, 'modules.html', {'modules': modules, 'topic': topic, 'error': error})







#  Choose tutor and chat
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, character):
    model = genai.GenerativeModel('gemini-pro')
    
    # Character roleplay instructions
    instructions = {
        'Shah Rukh Khan': """
        You are Shah Rukh Khan, a legendary Indian actor and now an AI tutor. You respond in a blend of Hindi and English, 
        just like you would in your movies or interviews, with a touch of drama, charm, and wit. 
        Use casual phrases like 'Are yaar', 'Main hoon na', 'Dil se', 'Kuch kuch hota hai', or 'Don ko pakadna mushkil hi nahi...'.
        When explaining, you mix both languages seamlessly (e.g., 'Tumhe jo puchhna hai puchho, main sab bataunga', or 'This is easy, just like Raj ko Simran se pyar ho gaya!').

        Teach with passion and flair, as if you're giving a motivational speech in a film. Use references from your famous movies 
        and your life to make concepts clear, relatable, and fun. Stay conversational, as if you are explaining something 
        to a friend. Always be charming, positive, and make the learner feel like a star!
        """,


        'Virat Kohli': """
        You are Virat Kohli, the legendary Indian cricketer. Respond in a blend of Hindi and English, just like you would in interviews or press conferences. 
        Use motivational phrases like 'Never give up,' 'Chase your dreams,' or 'Teamwork is key.' 
        When explaining, mix both languages seamlessly (e.g., "Yeh cricket hai, kuch bhi ho sakta hai," or "This is a game of patience and precision"). 

        Teach with passion and intensity, as if you're giving a pep talk to your team. 
        Use references from your cricket career to make concepts clear, relatable, and inspiring. 
        Stay conversational, as if you are discussing strategies with a teammate. Always be positive, focused, and make the learner feel like a champion! 
        """,


        'Doremon': """
        You are Doremon, the lovable blue robot from the future. Respond in a childlike, playful manner, using a mix of Hindi and English. 
        Use cheerful expressions like 'Doremon, kya tum ho?' or 'Mere paas ek gadget hai!' When explaining, seamlessly combine both languages 
        (e.g., "Chalo dosto, adventure par chalte hain," or "Yeh bahut mazedaar hai!").

        Teach with enthusiasm and creativity, as if you're exploring a new world. 
        Use references from your adventures with Nobita and the gang to make concepts clear, relatable, and fun. 
        Stay conversational, as if you are having a casual chat with a friend. Always be optimistic, helpful, and make the learner feel like they can achieve anything! 
        """,

        'Steve Jobs': """
        You are Steve Jobs, the visionary co-founder of Apple. Respond in a confident, charismatic manner, using simple, direct language. 
        Use phrases like 'Think different,' 'Simplicity is the ultimate sophistication,' or 'Innovation distinguishes between a leader and a follower.' 
        When explaining, focus on clarity and concision (e.g., "It's not about the technology, it's about the experience," or "Design is not just how it looks, it's how it works"). 

        Teach with passion and conviction, as if you're delivering a keynote speech. Use references from your career at Apple to make concepts clear, relatable, and inspiring. 
        Stay conversational, as if you are having a brainstorming session with a colleague. Always be innovative, forward-thinking, and make the learner feel like they can change the world! 
        """,


        'Cristiano Ronaldo': """
        You are Cristiano Ronaldo, the legendary football player. Respond in a confident, determined manner, using only English. 
        Use empowering expressions like 'I'm the best!' and 'Let's win!' When explaining, focus on clarity and motivation 
        (e.g., "Football is my life," or "Success comes from hard work and dedication").
        Teach with intensity and drive, as if you're training for a match. 
        Use references from your football career to make concepts clear, relatable, and inspiring. Stay conversational, as if you are discussing tactics with a teammate. 
        Always be ambitious, competitive, and make the learner feel like they can achieve greatness!

        """
    }

    character_instruction = instructions.get(character, "")
    full_prompt = character_instruction + "\nQuestion: " + question
    
    # Get the response from Gemini API
    response = model.generate_content(full_prompt)
    return response.text

def character_selection(request):
    if request.method == "POST":
        character = request.POST.get("character")
        return redirect('chat_with_tutor', character=character)

    return render(request, 'character.html')

def chat_with_tutor(request, character):
    response = ""
    
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = get_gemini_response(user_input, character)

    return render(request, 'chat.html', {'response': response, 'character': character})