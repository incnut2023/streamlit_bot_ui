import streamlit as st
import requests

# Replace this with the actual endpoint of your chat service
CHAT_SERVICE_ENDPOINT = 'https://sturdy-disco-5gg9gvqprg6wh4jv7-5000.app.github.dev'

def get_chat_response(user_input):
    try:
        response = requests.post(
            f'{CHAT_SERVICE_ENDPOINT}/get_response',  # Replace '/chat' with the actual endpoint
            json={'user_input': user_input}
        )
        response.raise_for_status()
        return response.json().get('response', 'Error: No response from chat service')
    except requests.RequestException as e:
        return f'Error communicating with chat service: {e}'

def main():
    st.title("Chat App")

    user_input = st.text_input("Type your message:")
    if st.button("Send"):
        if user_input.strip() != '':
            st.text(f"You: {user_input}")

            # Send user input to the chat service
            chat_response = get_chat_response(user_input)
            st.write(f"Chat Service: {chat_response}")

if __name__ == "__main__":
    main()
