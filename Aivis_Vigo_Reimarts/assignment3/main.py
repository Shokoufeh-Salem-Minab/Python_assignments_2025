from helpers import api_tools, file_tools
from datetime import datetime  # built-in library

# API endpoint
API_URL = "https://rickandmortyapi.com/api/character"

# Clear previous results
file_tools.clear_file("data/results.txt")

# Fetch characters from API
print("Fetching characters from Rick and Morty API...")
data = api_tools.fetch_characters(API_URL)

if data:
    # Extract character information
    characters = api_tools.extract_character_info(data)
    
    # Write header with timestamp
    header = f"=== Rick and Morty Characters ===="
    timestamp = f"Fetched at: {datetime.now()}"
    separator = "=" * 50
    
    file_tools.save_to_file("data/results.txt", header)
    file_tools.save_to_file("data/results.txt", timestamp)
    file_tools.save_to_file("data/results.txt", separator)
    file_tools.save_to_file("data/results.txt", "")
    
    # Write character information
    print(f"\nFound {len(characters)} characters:\n")
    for i, char in enumerate(characters, 1):
        char_text = f"{i}. {char['name']} - Status: {char['status']}, Species: {char['species']}, Origin: {char['origin']}"
        print(char_text)
        file_tools.save_to_file("data/results.txt", char_text)
    
    # Write summary
    file_tools.save_to_file("data/results.txt", "")
    file_tools.save_to_file("data/results.txt", separator)
    file_tools.save_to_file("data/results.txt", f"Total characters returned: {len(characters)}")
    
    print(f"\n✓ Results saved to data/results.txt")
    
else:
    print("Failed to fetch characters from API")
    file_tools.save_to_file("data/results.txt", "Error: Failed to fetch data from API")
    