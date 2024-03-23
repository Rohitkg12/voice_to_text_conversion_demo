import openai

openai.api_key = 'your_openai_api_key_here'

def query_openai(text):
    """
    Sends a text query to OpenAI's API and returns the response.

    Args:
        text (str): The text to send to OpenAI's API.

    Returns:
        str: The response from OpenAI's API.
    """
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=text,
      temperature=0.7,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    text = "This is a test query to OpenAI's API."
    print(query_openai(text))
