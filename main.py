
from audio_capture import capture_audio
from audio_processing import audio_to_text
from openai_integration import query_openai

def main():
    # Step 1: Capture audio
    print("Please speak into the microphone.")
    capture_audio("user_input.wav", 5)  # Captures audio for 5 seconds
    print("Audio captured. Processing...")

    # Step 2: Convert audio to text
    text = audio_to_text("user_input.wav")
    if not text:
        print("Failed to convert audio to text.")
        return

    print(f"Transcribed text: {text}")

    # Step 3 (Optional): Use the transcribed text with OpenAI's API
    # Uncomment the following lines to enable OpenAI integration
    # print("Sending text to OpenAI for further processing...")
    # response = query_openai(text)
    # print(f"OpenAI's response: {response}")

if __name__ == "__main__":
    main()
