import urllib.request
import json

def get_joke_no_install():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        # Виконуємо запит за допомогою вбудованої urllib
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                # Читаємо та декодуємо дані
                data = response.read().decode('utf-8')
                # Парсимо JSON
                joke_data = json.loads(data)
                
                print("--- Random Joke (urllib) ---")
                print(f"Setup: {joke_data['setup']}")
                print(f"Punchline: {joke_data['punchline']}")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    get_joke_no_install()
