import streamlit as st
from PIL import Image
from agent import agent 

# Streamlit Page Configuration
st.set_page_config(page_title="Titanic Chat", layout="centered")

# Title
st.title("Titanic Chat AI")
st.text("Please clear cache from 3-dots before using")

# User input field
prompt = st.chat_input("Ask Titanic Chat")

if prompt:

    with st.chat_message("human"):
        st.write(prompt)

    try:

        response_data = agent(prompt)


        if isinstance(response_data, tuple) and len(response_data) == 2:
            response, graph = response_data
        else:
            response, graph = response_data, None

        if response:
            with st.chat_message("assistant"):
                st.write(response)


            if graph:
                graph_path = f"static/graph.png"  
                try:
                    graph_img = Image.open(graph_path)
                    st.image(graph_img, caption="Generated Graph", use_container_width=True)
                except FileNotFoundError:
                    st.error("Graph image not found in the static folder.")
        else:
            st.error("Failed to get a valid response from the server.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
