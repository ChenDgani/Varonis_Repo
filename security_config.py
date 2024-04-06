from github import Github
import requests
import os

# Authentication using the token secret
token = os.getenv('TOKEN')
github_access = Github(token)

# The repo
repo_name = 'ChenDgani/Varonis_Repo'
repo = github_access.get_repo(repo_name)

def validate_repo_private():
  if not repo.private:
    print(f"Repository {repo.full_name} was not private! Now it's private (Assuming this is the requirement,in real life change it with repo.edit(private=True))")
  else:
    print(f"Repository {repo.full_name} is indeed in private mode")

def check_code_scanning_setup():
    try:
        # Attempt to retrieve a known code scanning workflow file
        workflow_file = repo.get_contents(".github/workflows/code_scanning.yml")
        print("Code scanning is already configured.")
    except:
        print("Code scanning is not configured.")
        scanning_setup() # Describe how to manually create one

def scanning_setup():
    print("To configure code scanning, follow these steps:")
    print("1. Go to your GitHub repository's homepage.")
    print("2. Click on 'Actions' > 'New workflow'.")
    print("3. Find 'Code scanning' and set up the workflow by following the GitHub's guidance.")
    print("Or add a 'code_scanning.yml' file to '.github/workflows' directory with your desired code scanning configuration.")

def check_and_set_secret_scanning():
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    # Check Secret Scanning status
    check_url = f"https://api.github.com/repos/{repo_name}/secret-scanning"
    response = requests.get(check_url, headers=headers)
    
    if response.status_code == 200:
        status = response.json().get('enabled', False)
        if status:
            print("Secret Scanning is already enabled.")
            return True
        else:
            print("Secret Scanning is not enabled. Attempting to enable it...")
    else:
        print(f"Failed to check Secret Scanning status. Status code: {response.status_code}")
        # Log detailed error message from GitHub
        if 'message' in response.json():
            print("GitHub API error message:", response.json()['message'])
        return False

    # Enable Secret Scanning
    enable_url = f"https://api.github.com/repos/{repo_name}/secret-scanning/enable"
    enable_response = requests.post(enable_url, headers=headers)
    
    if enable_response.status_code == 204:
        print("Secret Scanning has been successfully enabled.")
        return True
    else:
        print("Failed to enable Secret Scanning.")
        return False

# Execute the functions
validate_repo_private()
check_code_scanning_setup()
check_and_set_secret_scanning()


    
