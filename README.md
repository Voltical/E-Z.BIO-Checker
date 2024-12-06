# EZ-Bio Link Checker

A simple Python script to check the availability of custom links on the `e-z.bio` domain. Perfect for testing the availability of usernames or paths quickly and efficiently.

## Features:
- **Bulk Check Support**: Load multiple links from a file.
- **Status Detection**: Identifies available, taken, or error states for each link.
- **Customizable**: Modify the base URL and input file with ease.
- **Error Handling**: Graceful handling of network timeouts and server errors.

## How to Use:
1. Clone the repository:
   ```bash
   git clone https://github.com/Voltical/E-Z.BIO-Checker.git
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Prepare the file (`paths.txt`) with one path per line.
4. Run the script:
   ```bash
   python run.py
   ```

## Requirements:
- Python 3.6+
- `requests` library

## Future Enhancements:
- Export results to a CSV or JSON file.
- Add support for multithreaded requests for faster checks.
