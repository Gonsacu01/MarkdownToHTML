import os
import markdown

# Directories
html_dir = './html'
md_dir = './md'

# Function to convert .md to .html
def md_to_html(md_file_path):
    try:
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            text = md_file.read()
            html = markdown.markdown(text)
            return html
    except Exception as e:
        print(f"Error reading or converting {md_file_path}: {e}")
        return None

# Function to save the HTML content to a file
def save_html(html_content, html_file_path):
    try:
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
    except Exception as e:
        print(f"Error saving HTML to {html_file_path}: {e}")

# Check if all .html files in /html have corresponding .md files in /md and convert them
def check_and_convert():
    try:
        # List all .html files in the html directory
        html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

        # Iterate over each .html file
        for html_file in html_files:
            # Generate the corresponding .md file name
            md_file_name = html_file.replace('.html', '.md')
            md_file_path = os.path.join(md_dir, md_file_name)

            # Check if the .md file exists
            if os.path.exists(md_file_path):
                print(f"Converting {md_file_name} to {html_file}")
                # Convert .md to .html
                html_content = md_to_html(md_file_path)
                if html_content is not None:
                    html_file_path = os.path.join(html_dir, html_file)
                    save_html(html_content, html_file_path)
            else:
                print(f"MD file {md_file_name} does not exist in the /md directory, skipping...")

    except Exception as e:
        print(f"Error during conversion process: {e}")

if __name__ == '__main__':
    check_and_convert()
