import os
import frontmatter

for file in os.listdir('projects'):
    if file.endswith('.md'):
        with open(os.path.join('projects', file), 'r') as f:
            post = frontmatter.load(f)
            title = post.get('title', 'Untitled Issue')
            priority = post.get('priority', 'No priority set')
            estimate = post.get('estimate', 'No estimate set')
            
            if 'linear-id' in post:
                print(f"Updating existing issue {post['linear-id']}...")
            else:
                print(f"Creating new issue for {title}...")

            

