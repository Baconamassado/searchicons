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

    if icon_name in icons:
        return {"name": icon_name, "id": icons[icon_name]}

    closest_match = difflib.get_close_matches(icon_name, icons.keys(), n=1)
    
    if closest_match:
        closest_name = closest_match[0]
        return {
            "requested_name": icon_name,
            "suggested_name": closest_name,
            "suggested_id": icons[closest_name]
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