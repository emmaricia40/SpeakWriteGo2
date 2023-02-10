import streamlit as st
from SpeakWriteGo import transcribe_audio_to_text

def run_app():
    st.title("SpeakWriteGo")
    st.write("Transcribe audio to text using OpenAI Whisper")

    uploaded_file = st.file_uploader("Upload your audio file", type=["wav", "mp3", "m4a"])

    if uploaded_file:
        audio_file = transcribe_audio_to_text(uploaded_file)
        st.markdown(f"## Transcribed Audio:\n\n{audio_file}")

if __name__ == "__main__":
    run_app()
