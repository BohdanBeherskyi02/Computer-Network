import requests

def get_random_joke():
    # URL відкритого API з анекдотами
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        # Виконуємо запит до API
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на помилки запиту
        
        # Парсимо отриманий JSON
        joke_data = response.json()
        
        # Виводимо анекдот у консоль
        print(f"--- Random Joke ---")
        print(f"Setup: {joke_data['setup']}")
        print(f"Punchline: {joke_data['punchline']}")
        
    except Exception as e:
        print(f"Сталася помилка при отриманні анекдоту: {e}")

if __name__ == "__main__":
    get_random_joke()
