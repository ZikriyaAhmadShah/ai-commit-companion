import sys
import requests

def generate_commit_message(prompt):
    print("Thinking... Generating your commit message...")
    
    # Using a free, no-auth duckduckgo AI proxy for speed
    url = "https://duckduckgo.com/duckduckgo-html-search" # Example placeholder
    # For a real, instant script, we will use the free community translation/text API
    # Let's use a reliable, free text generation endpoint
    api_url = f"https://api.popcat.xyz/chatbot?msg=Write a short, professional git commit message for: {prompt}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # Clean up the response
            msg = data.get("response", "Update files")
            print("\n Generated Commit Message:")
            print(f'git commit -m "{msg}"')
        else:
            print(" Failed to connect to the AI model. Try again!")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py 'your description of changes'")
    else:
        user_prompt = " ".join(sys.argv[1:])
        generate_commit_message(user_prompt)
