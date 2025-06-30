import streamlit as st
from llama_cpp import Llama

# Load your TinyLlama model
model_path = "./model/tinyllama-1.1b-chat-v1.0.Q4_0.gguf"
llm = Llama(model_path=model_path, n_ctx=2048)

# Streamlit page config
st.set_page_config(page_title="💌 AI Love Letter Generator", page_icon="💖")

st.title("💖 AI Love Letter Generator")

# User inputs
recipient_name = st.text_input("Enter recipient's name")

relationship = st.selectbox("Choose your relationship:",
                            ["crush", "lover", "situationship 👀", "partner"])

tone = st.selectbox("Choose a tone for the letter:",
                    ["romantic", "flirty", "poetic", "dramatic", "adorable"])

# Generate button
if st.button("✨ Generate Love Letter"):
    if not recipient_name:
        st.warning("Please enter a name first!")
    else:
        with st.spinner("Crafting your love letter..."):

            # Build prompt
            prompt = f"""
You are a skilled modern love letter writer.

Write a {tone} love letter to my {relationship} named {recipient_name}.
Use vivid imagery, sensory details, and clever metaphors.
Make it personal, charming, and sincere.
End with a heartwarming promise to them.

Start with 'Dear {recipient_name},' and end with 'Yours, Always.'
"""

            # Generate letter
            response = llm.create_chat_completion(
                messages=[{"role": "user", "content": prompt}],
                max_tokens=700,
                temperature=0.7,
                top_p=0.95
            )

            love_letter = response["choices"][0]["message"]["content"].strip()

            # Show love letter
            st.subheader("💌 Your AI-Crafted Love Letter:")
            st.write(love_letter)

            # Download as text file
            st.download_button(
                label="📄 Download as .txt",
                data=love_letter,
                file_name=f"{recipient_name}_love_letter.txt",
                mime="text/plain"
            )

            # Show code-like copyable text box
            st.code(love_letter)

# Footer
st.markdown("---")
st.caption("Made with 💖 by Sunshine (and your AI boyfriend 😉)")
