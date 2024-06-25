Easy Level Tasks:

1.Web Scraping Tool with BeautifulSoup:
Develop a web scraping application using Python's BeautifulSoup library. Extract data from a website and present it in a structured format (e.g., CSV, JSON).


2.Basic Chatbot with NLTK:
Build a simple chatbot using Natural Language Toolkit (NLTK) for text processing and response generation. The chatbot should be able to engage in basic conversation and answer frequently asked questions.


3.Task Management Web App with Flask:
Create a web-based task management application using Flask framework. Users can register, log in, add tasks, mark them as complete, and delete tasks.


4. Voice Recorder with PyAudio:
Develop a voice recording application using PyAudio library. Users can record, playback, and save audio recordings in different formats.

 Voice Recorder Application

Overview
The Voice Recorder Application is a Python-based tool that allows users to record audio, play recorded audio files, and convert audio files to different formats. It is designed to be simple and user-friendly.

Features
Record Audio: Capture high-quality audio and save it as a WAV file.
Play Audio: Play back recorded audio files.
Convert Audio: Convert audio files to different formats such as MP3, FLAC, etc.

Requirements
Python 3.x
pyaudio
wave
pydub

pip install pyaudio wave pydub

Usage
Run the application and follow the menu prompts to record, play, or convert audio files.


python voice_recorder.py

Code Overview
The application consists of the following functions:

record_audio(filename, duration, channels=1, rate=44100, chunk=1024): Records audio and saves it to a file.
play_audio(filename): Plays an audio file.
convert_audio(input_filename, output_filename, format="mp3"): Converts an audio file to a different format.
main(): The main function providing a menu interface for the user.

Example

Select option 1 in the menu to record audio.
Enter test.wav as the filename.
Enter 10 as the duration.
To play the recorded audio:

Select option 2 in the menu.
Enter test.wav as the filename.
To convert the recorded audio to MP3 format:

Select option 3 in the menu.
Enter test.wav as the input filename.
Enter test.mp3 as the output filename.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.
