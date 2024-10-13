import json
import sys

def generate_html(packages):
    """Generates HTML content for the index page based on the package data."""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>docker-pack Container Registry</title>
</head>
<body>
    <h1>docker-pack Container Registry</h1>
    <p>Explore our Docker images and packages hosted on GitHub Container Registry:</p>
    <ul>
"""

    for package in packages:
        package_name = package['name']
        package_url = package['html_url']
        html_content += f'        <li><a href="{package_url}">{package_name}</a></li>\n'

    html_content += """    </ul>
</body>
</html>
"""

    return html_content

def main(packages_file):
    """Main function to read the package data and update the HTML file."""
    # Load the package data from the JSON file
    with open(packages_file, 'r') as f:
        data = f.read()
        print(f"Raw JSON data: {data}")  # Print the raw data for debugging
        packages = json.loads(data)  # Parse the JSON data

    # Check the loaded packages
    print(f"Loaded packages: {packages}")  # Print the loaded packages for debugging

    # Generate the HTML content
    html_content = generate_html(packages)

    # Write the HTML content to index.html
    with open('index.html', 'w') as f:
        f.write(html_content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python update_html.py <path_to_packages_json>")
        sys.exit(1)

    main(sys.argv[1])
