import requests

def chat_with_gpt(messages, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Specify the model here
        "messages": messages,
        "temperature": 0.7  # Adjust as needed
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return "Error communicating with the API."
    return response.json()['choices'][0]['message']['content']

def main():
    api_key = "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"  # Replace with your actual API key
    print("Welcome to the ChatGPT interface!")
    messages = []  # Initialize an empty list to keep track of the conversation
    while True:
        user_input = input("Enter your prompt (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        messages.append({"role": "user", "content": user_input})
        response = chat_with_gpt(messages, api_key)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()
