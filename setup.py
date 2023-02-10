from setuptools import setup, find_packages

setup(
    name='SpeakWriteGo',
    version='0.1',
    description='A Library for transcribing audio to text',
    author='Emmaricia',
    url='https://github.com/emmaricia40/SpeakWriteGo',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'streamlit',
        'openai',
        'openai-whisper'
    ],
)
