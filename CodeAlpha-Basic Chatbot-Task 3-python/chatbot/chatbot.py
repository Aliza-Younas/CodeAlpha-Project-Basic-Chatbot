import streamlit as st

# Title and Header
st.title("AI Chatbot")
st.header("Your Virtual Assistant")

# Introduction text
st.write("Welcome to the AI Chatbot! Use the widgets below to interact with me. Let's explore what I can do for you today.")

# User's Mood Slider
mood = st.slider("How are you feeling today?", 0, 100)
if mood < 30:
    st.write("It seems like you're having a tough day. I'm here to chat if you need it.")
elif mood < 70:
    st.write("You're feeling okay! Let's see how I can assist you.")
else:
    st.write("You're in great spirits! Let's have a productive conversation!")

# Camera Input
st.subheader("Capture a Moment")
camera_input = st.camera_input("Take a photo")

# File Upload
st.subheader("Share a File")
uploaded_file = st.file_uploader("Choose a file to upload")
if uploaded_file:
    st.write(f"File '{uploaded_file.name}' has been uploaded successfully!")

# Favorite Fruit Selection
st.subheader("Tell me about your preferences")
favorite_fruit = st.radio("What's your favorite fruit?", ["Orange", "Mango", "Banana", "Peach"])
st.write(f"Your favorite fruit is {favorite_fruit}.")

# Favorite Drink Selection
favorite_drink = st.selectbox("What's your favorite drink?", ["7up", "Pepsi", "Coca Cola", "Sprite"])
st.write(f"Your favorite drink is {favorite_drink}.")

# Multi-select for Hobbies
st.subheader("What are your hobbies?")
hobbies = st.multiselect("Select your hobbies", ["Reading", "Traveling", "Gaming", "Cooking", "Sports", "Music"])
st.write(f"Your selected hobbies are: {', '.join(hobbies) if hobbies else 'None'}")

# Checkbox for Notifications
st.subheader("Stay Updated")
notifications = st.checkbox("Subscribe to notifications")
if notifications:
    st.write("You are subscribed to notifications.")
else:
    st.write("You are not subscribed to notifications.")

# User Query Text Area
st.subheader("Ask the Chatbot")
user_query = st.text_area("Type your question or message here...")

# Chatbot Response Handling
if st.button("Send"):
    if user_query.strip() == "":
        st.write("Please enter a question or comment.")
    else:
        # Simulate a chatbot response
        st.write(f"You asked: {user_query}")
        st.write("Chatbot's Response: Thank you for your question! I'm here to help.")

# Sidebar for Additional Information
st.sidebar.header("About the AI Chatbot")
st.sidebar.write("""
This chatbot is powered by AI and can assist you with various tasks, from answering your questions to providing recommendations. 
Explore the different options and interact with the chatbot to see what it can do!
""")

st.sidebar.subheader("Quick Links")
st.sidebar.markdown("[Visit Streamlit Documentation](https://docs.streamlit.io)")
st.sidebar.markdown("[GitHub Repository](https://github.com)")

# Footer
st.write("Thank you for using the AI Chatbot. Have a wonderful day!")


