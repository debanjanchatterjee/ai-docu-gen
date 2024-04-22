from flask import Flask, render_template, request
from src.utils.github_api import get_repo_details

import sys
print(sys.path)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/repo', methods=['POST'])
def repo_details():
    # repo_url = request.form['repo_url']
    # # Use GitHub API or other methods to get repository details
    # # For simplicity, this example uses a placeholder
    # repo_details = {
    #     'name': 'My GitHub Repo',
    #     'files': ['file1.py', 'file2.py', 'folder1/file3.py'],
    #     'metadata': {'owner': 'username', 'description': 'A sample repository'}
    # }
    # return render_template('repo_details.html', repo=repo_details)
    get_repo_details(request.form['repo_url'])