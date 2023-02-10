from setuptools import setup, find_packages

setup(
    name="SpeakWriteGo",
    py_modules=["whisper"],
    version=read_version(),
    description="A library for transcribing audio to text",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.7",
    author="Emmaricia",
    url="https://github.com/emmaricia40/SpeakWriteGo.git",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": ["whisper=whisper.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
