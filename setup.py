Import pkg_resources
from setuptools import setup, find_packages

setup(
    name='SpeakWriteGo',
    version='0.1',
    description='A library for transcribing audio to text',
    author='Emmaricia Madison',
    author_email='emmaricia@gmail.com',
    url='https://github.com/emmaricia40/SpeakWriteGo',
    packages=['SpeakWriteGo'],
    install_requires=[
        'numpy',
        'pytorch',
        'openai',
        'openai-whisper',
        'streamlit'
    ],
)
