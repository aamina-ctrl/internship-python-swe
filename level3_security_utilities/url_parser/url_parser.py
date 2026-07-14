from urllib.parse import urlparse, parse_qs
def validate_url(url):
    parsed= urlparse(url)
    if not parsed.scheme or not parsed.hostname:
        print("Invalid URL: Missing protocol or hostname.")
        return None
    else:
        return parsed
    
def display_components(parsed):
    print(f"Protocol: {parsed.scheme}")
    print(f"Hostname: {parsed.hostname}")
    print(f"Path: {parsed.path}")
    print(f"Port: {parsed.port}")
    print(f"Query Parameters: {parsed.query}")
    print(f"Fragment: {parsed.fragment}")

    if parsed.scheme=="https":
        print("HTTPS: Enabled")
    else:
        print("HTTPS: Not enabled")

    parameters=parse_qs(parsed.query)
    if parameters:
        print("Query Parameters:")
        for key, value in parameters.items():
            print(f"  {key}: {value}")
        print(f"Number of Query Parameters: {len(parameters)}")

def main():
    url=input("Enter a VALID URL:")
    parsed=validate_url(url)
    if parsed:
        display_components(parsed)
main()    