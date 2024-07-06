import openai
import time
openai.api_key = 'sk-proj-GZ09R3ktS7H8vAlpIK34T3BlbkFJ6hGZ1x0do27EJCEv6LGX'

def chat_with_gpt(user_input):
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=150
            )
            return response
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded: {e}")
            print("Waiting for 60 seconds before retrying...")
            time.sleep(60)
        except Exception as e:
            print(f"An error occurred: {e}")
            break

user_input = "Your input here"
response = chat_with_gpt(user_input)
print(response)
