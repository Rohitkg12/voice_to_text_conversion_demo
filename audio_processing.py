import speech_recognition as sr

def audio_to_text(audio_filename="recording.wav"):
    """
    Converts an audio file to text using Google's Speech Recognition API.

    Args:
        audio_filename (str): The path to the wav file to be converted.

    Returns:
        str: The converted text from the audio.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_filename) as source:
        audio_data = recognizer.record(source)

    # Use Google's Speech Recognition API to convert audio to text
    try:
        text = recognizer.recognize_google(audio_data)
        print("Google Speech Recognition thinks you said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

if __name__ == "__main__":
    print(audio_to_text())
