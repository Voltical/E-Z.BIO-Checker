import requests

def check_links(base_url, paths):
    """
    Check the availability of links on the given base URL.

    Parameters:
        base_url (str): The base domain to check links for.
        paths (list): A list of paths or subdomains to test.

    Returns:
        dict: A dictionary with paths as keys and availability status as values.
    """
    available_links = {}
    
    for path in paths:
        url = f"{base_url}/{path.strip()}"  # Fetch full path
        try:
            response = requests.get(url, timeout=5)  # Send GET requests with a delay
            if response.status_code == 404:
                available_links[path] = "Available"
            else:
                available_links[path] = f"Taken (Status Code: {response.status_code})"
        except requests.RequestException as e:
            available_links[path] = f"Error: {e}"
    
    return available_links

def load_paths_from_file(file_path):
    """
    Load paths from a file.

    Parameters:
        file_path (str): Path to the file containing paths.

    Returns:
        list: A list of paths loaded from the file.
    """
    try:
        with open(file_path, "r") as file:
            paths = file.readlines()
            return [path.strip() for path in paths if path.strip()]  # Remove empty lines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

if __name__ == "__main__":
    # Define the base URL and input file
    base_url = "https://e-z.bio"
    input_file = "paths.txt"  # File containing paths to check (one per line)

    # Load paths from the file
    paths_to_check = load_paths_from_file(input_file)

    # If paths are loaded, proceed to check
    if paths_to_check:
        print(f"Loaded {len(paths_to_check)} paths from {input_file}")
        results = check_links(base_url, paths_to_check)
        
        # Print the results
        for path, status in results.items():
            print(f"{base_url}/{path}: {status}")
    else:
        print("No paths to check. Exiting.")
