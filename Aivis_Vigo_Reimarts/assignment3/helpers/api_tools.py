import requests

def fetch_characters(url):
    """Fetch characters from Rick and Morty API"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def extract_character_info(data):
    """Extract character names and status from API response"""
    if not data or 'results' not in data:
        return []
    
    characters = []
    for character in data['results']:
        char_info = {
            'name': character.get('name', 'Unknown'),
            'status': character.get('status', 'Unknown'),
            'species': character.get('species', 'Unknown'),
            'origin': character.get('origin', {}).get('name', 'Unknown')
        }
        characters.append(char_info)
    
    return characters
