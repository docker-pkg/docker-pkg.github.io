import json
import sys

def generate_html(packages):
    if 'message' in packages:  # Check for error message in the response
        print(f"Error: {packages['message']}")
        return "<h1>Error fetching packages</h1>"

    html_content = "<html><body><h1>Packages</h1><ul>"
    for package in packages:
        package_name = package['name']  # Ensure this is a dictionary
        html_content += f"<li>{package_name}</li>"
    html_content += "</ul></body></html>"
    return html_content

def main(package_file):
    with open(package_file) as f:
        packages = json.load(f)
    html_content = generate_html(packages)
    with open("index.html", "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    main(sys.argv[1])
