import os
import frontmatter

for file in os.listdir('projects'):
    name, extension = os.path.splitext(file)
    if extension == '.md':
        print(f"Found Markdown file: {file}")
        count += 1
print(f"Total Markdown files found: {count}")