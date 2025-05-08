import streamlit as st
from langchain.llms import Together
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Streamlit app title
st.title("Simple AI Chat App")

# Sidebar for settings
st.sidebar.title("Settings")

# Platform selection
platform = st.sidebar.selectbox(
    "Select Platform:",
    options=["Together AI", "OpenAI", "Hugging Face"],
    index=0
)

# Model selection based on platform
if platform == "Together AI":
    model = st.sidebar.selectbox(
        "Select Model:",
        options=["mistralai/Mistral-7B-Instruct-v0.1", "togethercomputer/GPT-JT-6B-v1",
                "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
                "meta-llama/Llama-Vision-Free"],
        index=0
    )
elif platform == "OpenAI":
    model = st.sidebar.selectbox(
        "Select Model:",
        options=["text-davinci-003", "gpt-3.5-turbo", "gpt-4"],
        index=0
    )
elif platform == "Hugging Face":
    model = st.sidebar.selectbox(
        "Select Model:",
        options=["bigscience/bloom", "facebook/opt-6.7b"],
        index=0
    )

# API key input
api_key = st.sidebar.text_input(f"Enter your {platform} API Key:", type="password")

# Slider for max_tokens
max_tokens = st.sidebar.slider(
    "Set Max Tokens for Output:",
    min_value=10,
    max_value=500,
    value=30,
    step=10
)

# Initialize session states
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "past_conversations" not in st.session_state:
    st.session_state.past_conversations = {}

# Button to start a new conversation
if st.sidebar.button("Start New Conversation"):
    if st.session_state.conversation:
        title = f"Conversation {len(st.session_state.past_conversations) + 1}"
        st.session_state.past_conversations[title] = st.session_state.memory.chat_memory.messages
    st.session_state.memory = ConversationBufferMemory()
    st.session_state.conversation = None
    st.sidebar.success("New conversation started!")

# Display past conversations in the sidebar
st.sidebar.subheader("Past Conversations")
if st.session_state.past_conversations:
    selected_title = st.sidebar.selectbox(
        "Select a conversation to load:",
        options=[""] + list(st.session_state.past_conversations.keys()),
        index=0,
    )
    if selected_title:
        st.session_state.memory.chat_memory.messages = st.session_state.past_conversations[selected_title]
        st.sidebar.success(f"Loaded {selected_title}")

# Main chat interface
if api_key:
    # Initialize the LLM based on platform
    if st.session_state.conversation is None:
        if platform == "Together AI":
            llm = Together(
                model=model,
                temperature=0.7,
                max_tokens=max_tokens,
                together_api_key=api_key
            )
            st.session_state.conversation = ConversationChain(
                llm=llm,
                memory=st.session_state.memory,
                verbose=True
            )
        else:
            st.error(f"Platform '{platform}' is not yet supported in this app.")
            st.stop()

    # Chat interface
    st.subheader("Chat")
    
    # Display conversation history
    for i, message in enumerate(st.session_state.memory.chat_memory.messages):
        if i % 2 == 0:
            st.write("You:", message.content)
        else:
            st.write("AI:", message.content)

        # User input
    user_input = st.text_input("Type your message:", key="user_input")
    
    if user_input:
        try:
            response = st.session_state.conversation.run(input=user_input)
            st.write("AI:", response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

else:
    st.warning(f"Please enter your {platform} API Key in the sidebar to start chatting.")


