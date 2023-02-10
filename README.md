# SpeakWriteGo
SpeakWriteGo
SpeakWriteGo is a python library that allows you to transcribe audio files into text using OpenAI's whisper API. This library supports audio files in the format of WAV, MP3 and M4A.

Features
Transcribe audio files in English and Spanish
Microphone recording and transcribing
Play original audio file while transcribing
User-friendly interface built with Streamlit
Supports WAV, MP3, and M4A audio file formats
Requirements
OpenAI API key
Numpy
Pytorch
Openai-whisper
Streamlit
Installation
You can install SpeakWriteGo using pip:

Copy code
pip install SpeakWriteGo
Usage
python
Copy code
import SpeakWriteGo

# Load the whisper model
model = SpeakWriteGo.load_model(*base)

# Upload audio file
uploaded_file = SpeakWriteGo.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])

# Transcribe audio file in English
if SpeakWriteGo.button("Transcribe In English"):
    audio_file = open(uploaded_file, "rb").read()
    response = openai.Function("whisper-transcribe")(
        audio=audio_file,
        model="text-davinci-002",
        voice="english",
    )
    transcript = response["data"][0]["text"]
    SpeakWriteGo.write("Transcription:", transcript)

# Transcribe audio file in Spanish
if SpeakWriteGo.button("Transcribe In Spanish"):
    audio_file = open(uploaded_file, "rb").read()
    response = openai.Function("whisper-transcribe")(
        audio=audio_file,
        model="text-davinci-002",
        voice="spanish",
    )
    transcript = response["data"][0]["text"]
    SpeakWriteGo.write("Transcription:", transcript)

# Record audio and transcribe
if SpeakWriteGo.button("Microphone"):
    SpeakWriteGo.write("Recording audio... Please speak into your microphone")
    # Record audio and transcribe
Contributions
Contributions are always welcome. If you have any ideas or suggestions, feel free to open an issue or make a pull request.

License
SpeakWriteGo is licensed under the MIT License.
