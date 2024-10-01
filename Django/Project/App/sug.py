# Suggestions view (Dynamically Related to Entered Topic)

from django.shortcuts import render, redirect
import google.generativeai as genai
import os
from dotenv import load_dotenv


def get_suggestions(topic):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Provide three related topics to '{topic}' with a one-line description for each."
    
    response = model.generate_content(prompt)
    print("API Response:", response.text)  # Debugging: Check the raw response

    suggestions = response.text.split("\n")
    suggestions = [suggestion.strip() for suggestion in suggestions if suggestion.strip()]
    
    # Example of parsing and formatting suggestions
    formatted_suggestions = []
    for suggestion in suggestions:
        if " - " in suggestion:
            name, description = suggestion.split(" - ", 1)
            formatted_suggestions.append({"name": name, "description": description})
    
    print("Formatted Suggestions:", formatted_suggestions)  # Debugging: Check parsed suggestions
    return formatted_suggestions[:3]

topic= input(" :  ")
print(get_suggestions(topic))