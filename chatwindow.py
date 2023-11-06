import requests
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.message_history = []

    def add_message(self, message):
        self.message_history.append({"role": self.role, "content": message})
        return message

    def save_conversation(self, filename):
        with open(filename, 'w') as f:
            for message in self.message_history:
                role = message['role']
                text = message['content']
                f.write(f'{role}: {text}\n')

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
    api_key = os.getenv("OPENAI_API_KEY")  # Get the API key from the environment variable
    if not api_key:
        print("API key not found. Please set it in the .env file.")
        return

    # Create agents
    gm = Agent('GM', 'assistant')
    npc1 = Agent('NPC1', 'assistant')  # Male Warrior
    npc2 = Agent('NPC2', 'assistant')  # Female Lovable Rogue
    npc3 = Agent('NPC3', 'assistant')  # Male Dimwitted Sorcerer
    player = Agent('Player', 'user')

    # Start the story with a more focused prompt
    gm_message = gm.add_message("You enter a dungeon. Ahead, you see a dimly lit room. The air is stale, having been undisturbed for centuries. The room is empty, save for some magically glowing torches on the walls. Now that you are in this room, what would you like to do?")
    print(f"{gm.name}: {gm_message}")

    for i in range(5):  # Limiting to 5 rounds for simplicity
        # Combine all previous messages for context
        full_history = gm.message_history + npc1.message_history + npc2.message_history + npc3.message_history + player.message_history

        # NPC interactions with personality-based prompts
        npc1_response = chat_with_gpt(full_history + [{'role': 'system', 'content': "Keep in mind what the GM states. Every other aspect of your response needs to revolve around the latest thing the GM states. You are a brave male Warrior. Just act your part, there is no need to state what you are. How do you lead your group through this scenario? How do you respond to the Rogue, Sorcerer, and player, if they have said anything?"}], api_key)
        print(f"{npc1.name} (Warrior): {npc1_response}")
        npc1.add_message(npc1_response)

        npc2_response = chat_with_gpt(full_history + npc1.message_history + [{'role': 'system', 'content': "Keep in mind what the GM states. Every other aspect of your response needs to revolve around the latest thing the GM states. You are a cunning female Rogue. Just act your part, there is no need to state what you are. Following the Warrior's lead, what clever actions do you take? How do you respond to the Warrior, Sorcerer, and player, if they have said anything?"}], api_key)
        print(f"{npc2.name} (Rogue): {npc2_response}")
        npc2.add_message(npc2_response)

        npc3_response = chat_with_gpt(full_history + npc1.message_history + npc2.message_history + [{'role': 'system', 'content': "Keep in mind what the GM states. Every other aspect of your response needs to revolve around the latest thing the GM states. You are a whimsical male Sorcerer. Just act your part, there is no need to state what you are. Reacting to both the Warrior and Rogue, how do you add your magic to the mix? How do you respond to the Warrior, Rogue, and Player, if they have said anything?"}], api_key)
        print(f"{npc3.name} (Sorcerer): {npc3_response}")
        npc3.add_message(npc3_response)

        # Player interaction
        player_input = input(f"{player.name}: ")
        player.add_message(player_input)

        # Update full history for the GM's response
        full_history = gm.message_history + npc1.message_history + npc2.message_history + npc3.message_history + player.message_history
        gm_prompt = "As the Game Master, narrate the unfolding story, weaving together the actions of the Warrior, Rogue, Sorcerer, and Player. You do not physically exist, you merely serve to set the stage and keep the story going forward. You are responsible to maintain some sense of direction for the group. Make sure that your responses are appropriate for what everyone has said thus far."
        gm_response = chat_with_gpt(full_history + [{'role': 'system', 'content': gm_prompt}], api_key)
        print(f"{gm.name}: {gm_response}")
        gm.add_message(gm_response)

    # Save the conversation
    gm.save_conversation('gm_conv.txt')
    npc1.save_conversation('npc1_conv.txt')
    npc2.save_conversation('npc2_conv.txt')
    npc3.save_conversation('npc3_conv.txt')
    player.save_conversation('player_conv.txt')

if __name__ == "__main__":
    main()
