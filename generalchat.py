from openai import AzureOpenAI
import json
import uuid
import os
# Replace with your actual Azure OpenAI resource details
api_key = "YOUR_API_KEY"
endpoint = "YOUR_ENDPOINT_URL"
deployment_name = "YOUR_DEPLOYMENT_NAME"
api_version = "YOUR_API_VERSION"

# Initialize the OpenAI API client with proper credentials
client = AzureOpenAI(
    azure_endpoint=endpoint, 
    api_key=api_key,  
    api_version=api_version
)

def get_response(conversation):
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=conversation,
            max_tokens=150,
            temperature=0.3
        )
        return response
    except Exception as e:
        print(f"An exception has occurred: {e}")
        return None

def main():
    """
    Main function that initiates a conversation with GPT and saves conversation stats to a file.

    Returns:
        None
    """
    session_id = str(uuid.uuid4())
    total_prompt_tokens = 0
    total_completion_tokens = 0
    successful_responses = 0
    unsuccessful_responses = 0

    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    print("Start chatting with GPT. Type 'end' to finish the conversation.")

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'end':
            break

        conversation.append({"role": "user", "content": user_input})
        response = get_response(conversation)

        if response:
            completion = response.choices[0].message.content.strip()
            print(f"GPT: {completion}\n")

            conversation.append({"role": "assistant", "content": completion})

            total_prompt_tokens += response.usage.prompt_tokens
            total_completion_tokens += response.usage.completion_tokens
            successful_responses += 1
        else:
            unsuccessful_responses += 1

    stats = {
        "session_id": session_id,
        "total_prompt_tokens": total_prompt_tokens,
        "total_completion_tokens": total_completion_tokens,
        "successful_responses": successful_responses,
        "unsuccessful_responses": unsuccessful_responses,
        "conversation": conversation,
    }
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    stats_filename = os.path.join('logs', f"conversation_stats_{session_id}.txt")
    with open(stats_filename, 'w') as stats_file:
        json.dump(stats, stats_file, indent=4)

    print(f"Conversation stats saved to {stats_filename}")
    print(response)

if __name__ == "__main__":
    main()

