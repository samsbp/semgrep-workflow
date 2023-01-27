## Github Action

Semgrep-integ.yml is the github action workflow that can be used . It need secrets such as 
1. "SEMGREP_APP_TOKEN" incase of using semgrep webapp 
2. "AUTH_TOKEN" for defectdojo api token


use github repository secrets to store and retrieve via actions
https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
