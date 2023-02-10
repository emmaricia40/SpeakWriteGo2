import openai
import streamlit as st
import numpy as np

openai.api_key = "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"

def transcribe_audio_to_text(audio_file):
    with open(audio_file, "rb") as f:
        data = f.read()
    response = openai.Whisper.create(
        engine="text-davinci-002",
        prompt=f"Transcribe this audio: {audio_file}",
        n=1,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response["choices"][0]["text"]
    return message
