from setuptools import setup, find_packages

setup(
    name="SpeakWriteGo",
    version='0.1',
    description="A Library for transcribing audio to text",
    author="Emmaricia",
    url="https://github.com/openai/whisper",
    license="MIT",
    packages=["SpeakWriteGo"],
    install_requires=[
        'numpy',
        'torch',
        'openai',
        'openai-whisper',
        'streamlit'
    ],
)
