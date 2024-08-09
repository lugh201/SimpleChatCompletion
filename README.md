# SimpleChatCompletion


```markdown
# GPT-4 Chat Completion with Azure OpenAI

This project allows users to chat with the GPT-4 model using Azure OpenAI. The script records the conversation and saves statistics about the session in a log file.

## Features
- Chat between GPT and user using the Chat Completions API.
- Allows the user to end the conversation.
- Saves conversation statistics (total prompt tokens, total completion tokens, number of successful and unsuccessful responses) in a unique text file within a `logs` directory.

## Requirements

- Python 3.6 or higher
- `openai` package

## Installation

1. **Clone the repository** or download the script.

2. **Install the `openai` package**:

    ```bash
    pip install openai
    ```

3. **Set up your Azure OpenAI credentials**:
    - Replace the placeholder values in the script with your actual Azure OpenAI credentials:
        ```python
        api_key = "your_api_key"
        endpoint = "https://your_resource_name.openai.azure.com/"
        deployment_name = "gpt-4"
        api_version = "2024-02-01"
        ```

## Usage

1. **Run the script**:

    ```bash
    python your_script_name.py
    ```

2. **Start chatting with GPT**:
    - The system will prompt you to type your questions.
    - Type 'end' to finish the conversation.

3. **View the log file**:
    - After the conversation ends, the script saves the conversation statistics in a unique text file within the `logs` directory.
    - The log file will be named `conversation_stats_<session_id>.txt`.

## Example

```bash
$ python your_script_name.py
Start chatting with GPT. Type 'end' to finish the conversation.
Q: What is the weather today?
GPT: To provide the current weather, I would need to know your location.
Q: New York
GPT: The weather in New York today is sunny with a chance of rain in the evening.
Q: end
Conversation stats saved to logs/conversation_stats_<session_id>.txt
```

## Customization

- **Temperature**: Adjust the `temperature` value in the `main` function to control the randomness of responses.
    ```python
    temperature = 0.7  # Choose a temperature between 0.0 and 1.0
    ```

- **Max Tokens**: Adjust the `max_tokens` value in the `get_response` function to control the length of responses.
    ```python
    response = client.chat.completions.create(
        model=deployment_name,
        messages=conversation,
        max_tokens=50  # Set lower max tokens for brief responses
    )
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Instructions:

1. **Save this content** in a file named `README.md` in the same directory as your script.
2. **Ensure the placeholders** (e.g., `your_api_key`, `your_resource_name`, `your_script_name.py`) are replaced with the actual values relevant to your project.

This `README.md` file provides a comprehensive overview of how to set up and use the script, including installation, usage, and customization options.
