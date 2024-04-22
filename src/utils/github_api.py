import requests

def get_repo_details(repo_url):
    # Extract owner and repo name from URL
    owner, repo_name = repo_url.split('/')[-2:]

    # Make a GET request to GitHub API
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo_name}')
    if response.status_code == 200:
        repo_data = response.json()
        print(repo_data)
        return {
            'name': repo_data['name'],
            'files': [file['path'] for file in repo_data['files']],
            'metadata': {'owner': repo_data['owner']['login'], 'description': repo_data['description']}
        }
    else:
        return None