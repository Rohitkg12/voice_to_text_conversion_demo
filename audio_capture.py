import pyaudio
import wave

def capture_audio(filename="recording.wav", seconds=5):
    """
    Captures audio from the microphone and saves it to a file.

    Args:
        filename (str): The name of the file where the recording will be saved.
        seconds (int): Duration of the recording in seconds.
    """
    # Audio recording parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = seconds

    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Finished recording.")

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recording to a file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    capture_audio()
