# URL Parser

## Objective
This program accepts a URL from the user, validates it, and extracts its different components using Python's `urllib.parse` module. It also checks whether HTTPS is enabled and displays the query parameters along with their total count.

## Features
- Validates the entered URL.
- Displays:
  - Protocol (Scheme)
  - Hostname
  - Path
  - Port Number
  - Query String
  - Fragment
- Checks whether HTTPS is enabled.
- Extracts query parameters.
- Displays the total number of query parameters.
- Handles invalid URLs gracefully.

## Files
- `url_parser.py` – Main Python program.

## Modules Used
- `urllib.parse`
  - `urlparse()`
  - `parse_qs()`

## How to Run
1. Open a terminal in the project folder.
2. Run the program:

```bash
python url_parser.py
```

3. Enter a URL when prompted.

## Sample Output

### Example 1 (HTTPS URL)

```
Enter URL: https://www.google.com/search?q=python&source=hp

Protocol: https
Hostname: www.google.com
Path: /search
Port: None
Query Parameters: q=python&source=hp
Fragment:
HTTPS: Enabled

Query Parameters:
    q: ['python']
    source: ['hp']

Number of Query Parameters: 2
```

---

### Example 2 (HTTP URL)

```
Enter URL: http://example.com:8080/docs/index.html?id=10&user=aamina#section2

Protocol: http
Hostname: example.com
Path: /docs/index.html
Port: 8080
Query Parameters: id=10&user=aamina
Fragment: section2
HTTPS: Not enabled

Query Parameters:
    id: ['10']
    user: ['aamina']

Number of Query Parameters: 2
```

---

### Example 3 (Invalid URL)

```
Enter URL: www.google.com

Invalid URL: Missing protocol or hostname.
```

## Concepts Practiced
- Functions
- URL parsing
- Input validation
- Conditional statements
- Dictionaries
- Query parameter extraction
- Python standard library (`urllib.parse`)
