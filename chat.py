import requests

BACKEND_URL = "https://rude-backend.onrender.com"

def ask_groq(prompt):
    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": prompt},
            timeout=30
        )
        data = response.json()
        return data.get("reply", "(Error: No reply field in backend response)")
    except Exception as e:
        return f"(Client Error) {e}"
def main():


    while True:
        user = input("You: ")
        if user.lower() == "bye":
            break
        print("AI:", ask_groq(user))

if __name__ == "__main__":
    main()
