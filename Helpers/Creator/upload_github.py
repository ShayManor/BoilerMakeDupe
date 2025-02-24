import os
import subprocess
from github import Github

import subprocess
import json


def get_github_credentials():
    """
    Retrieves GitHub username and token using the GitHub CLI (gh).

    Returns:
        tuple: A tuple containing the username and token (username, token)
    """
    token_process = subprocess.run(
        ['gh', 'auth', 'token'],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    token = token_process.stdout.strip()

    user_process = subprocess.run(
        ['gh', 'api', 'user'],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    user_data = json.loads(user_process.stdout)
    username = user_data.get('login')

    return username, token


def upload_to_github(filepath: str) -> str:
    """
    Uploads the folder at `filepath` to GitHub as a new repository and returns the clone URL.

    Args:
        filepath (str): The path to the folder you want to upload.
        github_token (str): Your GitHub personal access token.
        github_username (str): Your GitHub username.

    Returns:
        str: The public clone URL of the newly created repository.
    """
    github_username, github_token = get_github_credentials()
    repo_name = os.path.basename(os.path.normpath(filepath))

    g = Github(github_token)
    user = g.get_user()
    repo = user.create_repo(repo_name)

    if not os.path.exists(os.path.join(filepath, '.git')):
        subprocess.run(['git', 'init'], cwd=filepath, check=True)

    subprocess.run(['git', 'add', '.'], cwd=filepath, check=True)
    try:
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=filepath, check=True)
    except subprocess.CalledProcessError:
        pass

    remotes = subprocess.run(
        ['git', 'remote'], cwd=filepath, check=True, stdout=subprocess.PIPE, text=True
    ).stdout.strip().splitlines()
    if 'origin' in remotes:
        subprocess.run(['git', 'remote', 'remove', 'origin'], cwd=filepath, check=True)

    # Construct the HTTPS URL with token (for push authentication).
    remote_url = f"https://{github_token}:x-oauth-basic@github.com/{github_username}/{repo_name}.git"

    # Add the remote and push the code.
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=filepath, check=True)
    subprocess.run(['git', 'branch', '-M', 'main'], cwd=filepath, check=True)
    subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=filepath, check=True)

    # Return the public clone URL (without the token).
    return repo.clone_url


# Example usage:
if __name__ == "__main__":
    local_agent_path = "../../Agents/ai-sales-agent"

    repo_url = upload_to_github(local_agent_path)
    print("Repository created at:", repo_url)
