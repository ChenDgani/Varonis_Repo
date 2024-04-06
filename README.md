# Varonis Secure Repository

Welcome to GitHub Secure repository Guide.
This documnet provides a overvew of implementing and maintaining security configuration for you Varonis secure repository.
By automating these configurations we aim safeguard repositories against common security threats, ensuring best practices by NIST.
These all security configurations recommendations are from Github official doc:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository

## Security Configurations

This code focused on 5 repository setting keys:

Private/Public Repository Status
Secret Scanning
Code Scanning
Dependabot Alerts
Branch Protection

These configurations are evaluated against the following NIST keys:

Access Control
System and Information Integrity
Configuration Management
Risk Assessment
System and Communications Protection

## In-Depth Analysis: Secret Scanning

Most GitHub projects use tokens or private keys to authenticate communication between project code and external services. Service providers often issue secrets such as private keys or tokens to control access to a project. 

However, when you add secrets to a Git repository, this creates a serious security risk, because anyone with read access to your repository can use these secrets to access privileged external services. Secrets must be stored in a dedicated secure location outside your project’s repository.

GitHub secret scanning is a set of security features that helps secure code and keep secrets safe across organizations and repositories. Some of these security features are available on all plans, while businesses using GitHub Advanced Security can take advantage of additional features. All public repositories on GitHub also have GitHub Advanced Security enabled.

### Best Practice

Activating secret scanning on all repositories is paramount. 
It ensures timely alerts for any sensitive information inadvertently exposed, allowing for swift remediation actions to mitigate potential security risks.

### Risks

Your repository is vulnerable to unauthorized access if you disable or overlook secret scanning. Exposed secrets can lead to data breaches, compromising both project integrity and user privacy.

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

- **Scheduled Scans**: Keep security standards up to date with regular checks.
- **Alerting Mechanism**: Immediate notifications for detected misconfigurations or security risks.
- **Automated Remediation**: Detects and fixes common issues automatically, with manual overrides when needed.

### Code Structure & Usage

- **`security_config.py`**: Manages the overall operation of security checks and fixes.
- **`.github/workflows.py`**: A workflow is a configurable automated process that will run one or more jobs.

## Getting Started

1. **Clone the repository**: Obtain the latest version of the security main script.
2. **Install dependencies**: Ensure all required libraries are installed.
3. **Configure API keys**: Securely store your service API keys for authentication.
4. **Schedule execution**: Set up a cron job or similar scheduler to run the checks periodically.
5. **Monitor alerts**: Keep an eye on generated alerts and review automated fixes.

# ENJOY !


