from setuptools import setup, find_packages

setup(
    name="SpeakWriteGo",
    version="0.1",
    description="A Library for transcribing audio to text",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Emmaricia",
    url="https://github.com/emma/SpeakWriteGo",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pytorch',
        'openai',
        'streamlit'
    ],
)
