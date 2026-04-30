import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Initialize client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Send a message
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=150,
    messages=[
        {"role": "user", "content": "Say hello like a thoughtful life coach"}
    ]
)

# Print response
print(response.content[0].text)