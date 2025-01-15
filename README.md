# VPN Backend Tests

## Technology Stack
This section lists all the core frameworks/libraries used to this project:
- <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"/>
- <img src="https://img.shields.io/badge/Pytest-FFFFFF?style=for-the-badge&logo=pytest&logoColor=yellow"/>


## Environmental preparation 
1. Download Python 3.12.3 from https://www.python.org/downloads/ and install on your PC
2. Check your success installation
```sh
  python3 --version
  ```

## Steps to launch of tests:
1. Clone the repository with backend tests 
```sh
  git clone {repo link}
  ```
2. Go to the project root folder
```sh
  cd /vpn-backend-autotests
  ```
3. Create virtual environment by command
```sh
  python3 -m venv venv
  ```
4. Activate virtual environment
```sh
  source venv/bin/activate
  ```

5. Install requirements
```sh
  pip install -r requirements.txt
  ```
6. To change domain or protocol for send requests you need open `.env` file and to 
specify a new domain in the variable  `DOMAIN` or protocol type in the variable `PROTOCOL`.


7. To run all tests or one specific test file use the following commands
```sh
  pytest -s -v tests
  ```
```sh
  pytest -s -v tests/test_{name}.py
  ```
Running tests with report generation 
```sh
  pytest -s -v tests --html=report.html
  ```

## Contact
If you still have some questions, please ask them in my Slack profile - [Darina Bannik](https://planetvpn.slack.com/team/U03LV5XPYCX) 🙌














