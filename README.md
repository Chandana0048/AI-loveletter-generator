# AI-loveletter-generator
Ever wanted to send a love letter but didn’t know what to write? I built an AI Love Letter Generator that lets you enter your crush’s name, pick your relationship status (like lover, crush, or situationship 👀) and choose the vibe — whether you want it romantic, flirty, poetic, or dramatic.  
The AI crafts a personalized letter based on your inputs, and you can copy it or download it as a text file. Built using TinyLlama, llama-cpp-python, and a cute Streamlit GUI.
This was such a fun side project where I learned about deploying LLMs locally, prompt tuning, and how tiny UX touches can completely change the feel of a product.

🌸 Features

💕 Enter your crush's name  
📖 Choose your relationship type (Crush, Lover, Situationship 😏)  
🎭 Pick a tone (Romantic, Flirty, Poetic, Dramatic)  
📜 AI generates a personalized love letter based on your mood and details  
📋 Option to copy the letter or download as a `.txt` file

🛠️ Tech Stack

- [TinyLlama 1.1B Chat GGUF model](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [Streamlit](https://streamlit.io/)  
- Python 3.10+

🚀 How To Run

1) Clone this repo:
    git clone https://github.com/yourusername/ai-love-letter-generator.git
    cd ai-love-letter-generator

2) Install dependencies:
   pip install -r requirements.txt

3)  Download the model (.gguf file) and place it inside the ./model directory.
    I used:
    tinyllama-1.1b-chat-v1.0.Q4_0.gguf
    Get it from Hugging Face

4) Run the Streamlit app:
   streamlit run app.py

5) Flirt responsibly. Or don’t. I won’t judge. 😌

😅 What I Learnt
    Loading LLMs locally is tricky at first, but worth it
    Prompt engineering makes or breaks your results
    Tiny UX details (like spinners and fun options) make apps feel alive
    It’s okay to build silly side projects for no reason other than joy ✨

💡 Future Upgrades
  Mood-based backgrounds (starry nights? roses? heartbreak mode?)
  Save love letters to a personal gallery
  Random love quote generator
  Add more tone options like 'Sappy Bollywood Drama' 😂






