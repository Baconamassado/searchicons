# Icon Finder

## About

This script allows you to look up the name of an icon from a list of **Feather Icons** and provides the corresponding ID. If the exact match for the icon name is not found, it will search for the closest match and suggest the nearest icon name along with its ID.

### Example:

- **Standard Icon Name**: `Umbrella`
- **Given Icon Name**: `Umbrel`

If the given icon name (`Umbrel`) does not match exactly, the script will respond with:

Did you mean: Umbrella with the ID (ID of the icon Umbrella)?

---

## Features

- **Exact Match Search**: Looks up the icon directly by name.
- **Fuzzy Search**: Finds the nearest match if the exact name is not found.
- **User-Friendly Output**: Provides suggestions if no exact match is found.
- **Case-Insensitive**: The search is not case-sensitive, so it works regardless of letter casing.

---

## How It Works

1. **Fetches Icon List**: The script fetches the list of Feather Icons from an online source.
2. **Searches for Icon Name**: If the exact icon name is found, it returns the corresponding ID.
3. **Fuzzy Search**: If no exact match is found, the script uses fuzzy matching to suggest the closest icon name and its ID.

---

## Requirements

- **Python 3.x** (Your version)
- **requests** library (`pip install requests`)
- **difflib** (Standard Python library)

---

## Usage

1. Clone the repository or download the script.
2. Run the script and input the icon name when prompted.
3. The script will return the icon name and ID or suggest the closest match.
