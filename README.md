# Varonis Secure Repository

Welcome to GitHub Secure repository Guide.
This documnet provides a overview of implementing and maintaining security configuration for you Varonis secure repository.
By automating these configurations we aim safeguard repositories against common security threats, ensuring best practices by NIST.
These all security configurations recommendations are from Github official doc:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository

## Security Configurations

This code focused on 5 repository setting keys:

1. **Private/Public** Repository Status.
2. **Secret Scanning**.
3. **Keeping your dependencies updated automatically with Dependabot version updates**.
4. **Enable and enforce 2FA for GitHub**.
5. **Code scanning**

These configurations are evaluated against the following NIST keys:

1. Access Control
2. System and Information Integrity
3. System and Services Acquisition
4. Identification and Authentication
5. System and Communications Protection

## The security configurations with their impact

### Private/Public Repository Status
* **Security impact**: with public repositories your code is expose to the world with your sensetive information.
* **Detection**: if your project should to be with a privte repository, go to the repository setting and change it or do it with GitHub's REST API endpoints for repositories: https://docs.github.com/en/rest/repos?apiVersion=2022-11-28

If your repository is not private, my script will change it to private:

![image](https://github.com/ChenDgani/Varonis_Repo/assets/112262763/1dbf2759-579f-4fb1-ace4-c5d1947f36fe)


### Keeping your dependencies updated automatically with Dependabot version updates
* **Security impact**: Outdated dependencies can introduce vulnerabilities into your applications.
* **Detection**: Enable Dependabot version updates by checking a dependabot.yml configuration file into your repository. You can use this GitHub's guid: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates

If you don't have a dependabot.yml configuration file my scirpt will alert you and guide you on how to create one:

![image](https://github.com/ChenDgani/Varonis_Repo/assets/112262763/132f6786-19b3-4b2f-a463-ce7281bce831)


### Enable and enforce 2FA for GitHub
* **Security impact**: Two-factor authentication adds an additional layer of security to the authentication process by making it harder for attackers to gain access to a person's devices or online accounts.
* **Detection**: Configure it with your GitHub's settings and use this GitHub's guide: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication

### Code scanning
* **Security impact**: Code scanning is a feature that you use to analyze the code in a GitHub repository to find **security vulnerabilities** and coding errors.
* **Detection**: Managing your code scanning configuration with this GitHub's guide: https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration

If you didn't configure a code scanning mode, my scirpt will alert you and guide you on how to create one:

![image](https://github.com/ChenDgani/Varonis_Repo/assets/112262763/203633ab-d12d-4d76-bdc4-49f24ac0437c)


## In-Depth Analysis: Secret Scanning

Most GitHub projects use tokens or private keys to authenticate communication between project code and external services. Service providers often issue secrets such as private keys or tokens to control access to a project. 

When you add secrets to a Git repository, this creates a serious security risk, because anyone with read access to your repository can use these secrets to access privileged external services. Secrets must be stored in a dedicated secure location outside your project’s repository.

GitHub secret scanning is a set of security features that helps secure code and keep secrets safe across organizations and repositories. 

### Best Practice

Make sure all repositories are scanned secretly. 
Whenever sensitive information is inadvertently exposed, it alerts us quickly, so we can mitigate risks quickly.

### Risks

Exposed secrets can lead to data breaches, harming both the integrity of the project and the privacy of the user. The disclosure of secrets can result in unauthorized access to third-party applications and unwanted communication.

### Manual Configuration Steps

To enable secret scanning manually:

1. **Navigate** to your repository's **Settings**.
2. Select **Security & analysis**.
3. Toggle **Secret scanning** to **Enabled**.

### The impact of enable secret scanning

Once enabled, secret scanning scans for any secrets in your entire Git history on all branches present in your GitHub repository. Secret scanning does not scan issues. You can also enable secret scanning for multiple repositories in an organization at the same time.

### MITRE attack techniques

MITRE is a curated knowledge base and model for cyber adversary behavior, reflecting the various phases of an adversary's attack lifecycle and the platforms they are known to target.

#### Unsecured Credentials: Credentials In Files (ID T1552.001)

explaination of this technique from MITRE site:
It's possible for attackers to search local file systems and remote file shares for credentials that aren't encrypted. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

When users store their secrets in an insecure manner (due to lack of knowledge, human errors, etc.) attackers may use this attack and discover sensitive variables whose disclosure could pose a danger to the system and the organization in particular. By running this secret scan, we can overcome these mistakes more quickly and prevent many risks in the organization.

## Monitoring Security Framework

for expand our scripts into a framework for monitoring and fixing a large number of misconfigurations across multiple services, we should:

- The system will contain a **services DB** about all the resources across services in use (GCP resources, Zoom setting, etc)
- **Detection Engine** that will scans configurations across services to find deviations from the DB's desired states.
- **Alerting Mechanism**: Immediate notifications for detected misconfigurations or security risks.
- **Automated Fixing Mechanism**: Uses APIs to automatically fix misconfigurations. Detailed instructions are provided for fixing configurations that can't be fixed automatically.
- **Logging and Reporting**: Logs all detected problems and actions, generating compliance and audit reports.
- **Scheduled Scans**: Keep security standards up to date with regular checks.
- This system should be managed by an engineer who will always be aware of new security risks in services that interface with the repo.

### Code Structure & Usage

- **`security_config.py`**: Manages the overall operation of security checks and fixes.
- **`.github/workflows.py`**: A workflow is a configurable automated process that will run one or more jobs.

## Getting Started

1. **Clone the repository**: Obtain the latest version of the security main script.
2. **Install dependencies**: Ensure all required libraries are installed.
3. **Configure API keys**: Securely store your service API keys for authentication.
5. **Monitor alerts**: Keep an eye on generated alerts and review automated fixes.

#### Every time a push is made to main, the script will run to ensure the settings have not changed over time and your environment is secure.

# ENJOY !


