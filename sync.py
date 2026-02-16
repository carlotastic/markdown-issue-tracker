import os
import frontmatter
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LINEAR_API_KEY")
TEAM_ID = os.getenv("LINEAR_TEAM_ID")
TEAM_KEY = os.getenv("LINEAR_TEAM_KEY")


def create_linear_issue(title, description, priority, estimate):
    url = "https://api.linear.app/graphql"

    priority_mapping = {"Urgent" : 1, "High": 2, "Medium": 3, "Low": 4}
    priority_value = priority_mapping.get(priority, 4)
    query = """
    mutation IssueCreate($title: String!, $description: String!, $priority: Int, $estimate: Int, $teamId: String!) {
      issueCreate(input: {title: $title, description: $description, priority: $priority, estimate: $estimate, teamId: $teamId}) {
        success
        issue {
          id
        }
      }
    }"""

    variables = {
        "title": title,
        "description": description,
        "priority": int(priority_value),
        "estimate": int(estimate) if str(estimate).isdigit() else 0.0,
        "teamId": TEAM_ID
    }
    
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    data = response.json()

    if data.get('data') and data['data']['issueCreate']['success']:
        return data['data']['issueCreate']['issue']['id']
    else:
        print(f"Failed to create issue: {data}")
        return None






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
                new_id = create_linear_issue(title, post.content, priority, estimate)
                if new_id:
                    post['linear-id'] = new_id
                    with open(os.path.join('projects', file), 'wb') as f:
                        f.write(frontmatter.dumps(post).encode('utf-8'))
                    print(f"Issue created with ID: {new_id} and saved back to {file}")

            

