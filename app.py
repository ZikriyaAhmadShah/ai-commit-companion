import sys
import random

def generate_local_commit(prompt):
    print(" Analyzing your changes...")
    
    prompt_lower = prompt.lower()
    
    # Conventional Commits rules
    if "fix" in prompt_lower or "bug" in prompt_lower or "crash" in prompt_lower:
        prefix = "fix: "
    elif "add" in prompt_lower or "create" in prompt_lower or "new" in prompt_lower:
        prefix = "feat: "
    elif "docs" in prompt_lower or "readme" in prompt_lower:
        prefix = "docs: "
    elif "clean" in prompt_lower or "refactor" in prompt_lower:
        prefix = "refactor: "
    else:
        prefix = "chore: "

    # Clean up the prompt to make it a sharp commit message
    clean_prompt = prompt.replace("fixed a ", "").replace("added a ", "").replace("fixed ", "").replace("added ", "")
    clean_prompt = clean_prompt.strip().lower()
    
    final_message = f"{prefix}{clean_prompt}"
    
    print("\n Generated Commit Message:")
    print(f'git commit -m "{final_message}"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py 'your description of changes'")
    else:
        user_prompt = " ".join(sys.argv[1:])
        generate_local_commit(user_prompt)
