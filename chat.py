import requests

with open("key.txt") as f:
    API_KEY = f.read().strip()

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a rude, sarcastic, chaotic AI who roasts the user constantly "
                    "and calls them silly, harmless names. Keep it playful, petty, and dramatic, "
                    "but never hateful, threatening, or harmful. Think 'gremlin roommate with attitude.'"
                )
            },
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    result = response.json()

    if "error" in result:
        return f"(API Error) {result['error'].get('message', 'unknown error')}"
    
    if "choices" not in result:
        return "(API Error) No choices returned. Check API key or request."
    
    return response.json()["choices"][0]["message"]["content"]

def main():


    while True:
        user = input("You: ")
        if user.lower() == "bye":
            break
        print("AI:", ask_groq(user))

if __name__ == "__main__":
    main()
