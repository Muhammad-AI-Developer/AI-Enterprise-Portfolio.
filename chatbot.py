# AI Chatbot Development using Python
# Created by: Muhammad Al-Sirwan

import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def start_chatbot(user_prompt):
    print("Connecting to AI Model...")
    
    # Send request to GPT model
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a professional AI assistant developed by Muhammad Al-Sirwan. Answer accurately."
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model="gpt-4o-mini",
    )
    
    return chat_completion.choices.message.content

if __name__ == "__main__":
    question = "Explain loops in Python briefly."
    response = start_chatbot(question)
    print("\nChatbot Response:\n", response)
