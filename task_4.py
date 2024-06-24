import pyaudio
import wave
from pydub import AudioSegment

def record_audio(filename, duration, channels=1, rate=44100, chunk=1024):
    """
    Record audio and save it to a file.

    :param filename: Name of the file to save the recording
    :param duration: Duration of the recording in seconds
    :param channels: Number of channels (1 for mono, 2 for stereo)
    :param rate: Sampling rate
    :param chunk: Buffer size
    """
    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
    except Exception as e:
        print(f"Error initializing recording: {e}")
        return

    print("Recording...")

    frames = []

    try:
        for _ in range(0, int(rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)
    except Exception as e:
        print(f"Error during recording: {e}")
    finally:
        print("Recording finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

    try:
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
        print(f"Audio saved to {filename}")
    except Exception as e:
        print(f"Error saving audio: {e}")

def play_audio(filename):
    """
    Play an audio file.

    :param filename: Name of the audio file to play
    """
    p = pyaudio.PyAudio()

    try:
        with wave.open(filename, 'rb') as wf:
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            data = wf.readframes(1024)

            while data:
                stream.write(data)
                data = wf.readframes(1024)

            stream.stop_stream()
            stream.close()
    except Exception as e:
        print(f"Error playing audio: {e}")
    finally:
        p.terminate()

    print(f"Playback finished for {filename}")

def convert_audio(input_filename, output_filename, format="mp3"):
    """
    Convert audio file to a different format.

    :param input_filename: Name of the input file
    :param output_filename: Name of the output file
    :param format: Format of the output file (e.g., 'mp3', 'wav', 'flac')
    """
    try:
        audio = AudioSegment.from_file(input_filename)
        audio.export(output_filename, format=format)
        print(f"Audio converted to {output_filename}")
    except Exception as e:
        print(f"Error converting audio: {e}")

def main():
    print("Welcome to the Voice Recorder Application!")
    while True:
        print("\nMenu:")
        print("1. Record Audio")
        print("2. Play Audio")
        print("3. Convert Audio")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            filename = input("Enter filename to save recording (with .wav extension): ")
            duration = int(input("Enter duration of recording in seconds: "))
            record_audio(filename, duration)

        elif choice == '2':
            filename = input("Enter the filename of the audio to play (with .wav extension): ")
            play_audio(filename)

        elif choice == '3':
            input_filename = input("Enter the filename of the audio to convert (with .wav extension): ")
            output_filename = input("Enter the filename to save the converted audio (with appropriate extension, e.g., .mp3, .flac): ")
            format = output_filename.split('.')[-1]
            convert_audio(input_filename, output_filename, format)

        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
