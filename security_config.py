from github import Github
import requests
import os

# Authentication using the token secret
token = os.getenv('GITHUB_TOKEN')
github_access = Github(token)

# The repo
repo_name = 'ChenDgani/Varonis_Repo'
repo = github_access.get_repo(repo_name)

def validate_repo_private():
  print("Describes a scenario where the repository is supposed to be private, and each push is checked for this purpose")
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
    print("Or add a 'code_scanning.yml' file to '.github/workflows' directory with your desired code scanning configuration. ")

def validate_dependabot_config():
  try:
        # Attempt to get the dependabot.yml file
        config_file = repo.get_contents(".github/dependabot.yml")
        print("Dependabot configuration found.")
  except Exception as e:
        print("Dependabot configuration not found or an error occurred:", e)
        print("For keeping you dependecied updated and secure, please create a dependabot.yml in your repository")
        print("Dependabot uses this information to check for outdated packages and applications.")
        print("When Dependabot identifies an outdated dependency, it raises a pull request to update the manifest to the latest version of the dependency. ")
    
# Execute the functions
validate_repo_private()
check_code_scanning_setup()
validate_dependabot_config()

    
