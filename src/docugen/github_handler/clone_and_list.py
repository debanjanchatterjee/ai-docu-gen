import os
import tempfile
import subprocess

def clone_and_list_files(repo_url):
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            subprocess.run(["git", "clone", repo_url, temp_dir], check=True)

            # Walk the cloned repo and gather relative file paths
            files = []
            for root, dirs, filenames in os.walk(temp_dir):
                for filename in filenames:
                    rel_path = os.path.relpath(os.path.join(root, filename), temp_dir)
                    files.append(rel_path)

            return files, None
        except subprocess.CalledProcessError as e:
            return None, str(e)