from setuptools import setup, find_packages

setup(
    name="SpeakWriteGo",
    py_modules=["whisper"],
    version='0.1',
    description="A Library for transcribing audio to text",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.7",
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
