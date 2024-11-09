import requests
import difflib

url = "https://raw.githubusercontent.com/Baconamassado/lucideblox-icons/refs/heads/main/icons.json"

def fetch_icons(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()        # Parse JSON data
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching icons: {e}")
        return None

def find_icon(data, icon_name):
    if "icons" not in data:
        print("Error: No 'icons' key found in JSON data.")
        return None

    icons = data["icons"]
    icon_keys = list(icons.keys())

    icon_keys_lower = [key.lower() for key in icon_keys]
    
    icon_name_lower = icon_name.strip().lower()

    # First, check if the exact icon exists
    if icon_name_lower in icon_keys_lower:
        icon_index = icon_keys_lower.index(icon_name_lower)
        return {"name": icon_keys[icon_index], "id": icons[icon_keys[icon_index]]}

    # Get closest matches
    closest_matches = difflib.get_close_matches(icon_name_lower, icon_keys_lower, n=5, cutoff=0.6)

    if closest_matches:
        closest_name = closest_matches[0]  # Take the first closest match
        icon_index = icon_keys_lower.index(closest_name)
        return {
            "requested_name": icon_name,
            "suggested_name": icon_keys[icon_index],
            "suggested_id": icons[icon_keys[icon_index]]
        }
    else:
        print("No close matches found.")
        return None

# Main code block
if __name__ == "__main__":
    icon_name = input("Enter the icon name to search: ").strip() 

    data = fetch_icons(url)
    if data:
        result = find_icon(data, icon_name)  # Try to find the icon
        
        if result:
            if "suggested_name" in result:
                print(f"Icon '{icon_name}' not found. Did you mean '{result['suggested_name']}' with ID '{result['suggested_id']}'?")
            else:
                print(f"Icon '{result['name']}' found with ID '{result['id']}'")
        else:
            print("Icon not found and no similar matches.")
