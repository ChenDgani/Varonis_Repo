from github import Github
import requests
import os

# Authentication using the token from GitHub Secrets
token = os.getenv('TOKEN')
github_access = Github(token)

# The repository to manage
repo_name = 'ChenDgani/Varonis_Repo'
repo = github_access.get_repo(repo_name)

def validate_repo_private():
  if not repo.private:
    print("Repository {repo.full_name} was not private! Now it's private")
  else:
    print("Repository {repo.full_name} is indeed in private mode")

def check_code_scanning_setup():
    try:
        # Attempt to retrieve a known code scanning workflow file
        workflow_file = repo.get_contents(".github/workflows/code_scanning.yml")
        print("Code scanning is already configured.")
    except:
        print("Code scanning is not configured.")
        # Provide instructions or automate workflow file creation
        advise_on_code_scanning_setup()

def advise_on_code_scanning_setup():
    print("To configure code scanning, follow these steps:")
    print("1. Go to your GitHub repository's homepage.")
    print("2. Click on 'Actions' > 'New workflow'.")
    print("3. Find 'Code scanning' and set up the workflow by following the GitHub's guidance.")
    print("Or add a 'code_scanning.yml' file to '.github/workflows' directory with your desired code scanning configuration.")


# Execute the functions
validate_repo_private()
check_code_scanning_setup()


    
