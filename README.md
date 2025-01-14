# API Automation Testing with Python & BDD Framework

### Install Python
pip install requests

pip show requests
    Name: requests
    Version: 2.32.3
    Summary: Python HTTP for Humans.
    Home-page: https://requests.readthedocs.io
    ...
    Location: C:\Program Files\Python313\Lib\site-packages
    Requires: certifi, charset-normalizer, idna, urllib3
    Required-by:

### Install PyCharm
https://www.jetbrains.com/pycharm/download/?section=windows
PyCharm 的适用场景：
1. Python SDET 开发：
    - 构建自动化测试框架，例如 pytest、Selenium WebDriver。
    - 支持 API 自动化测试和数据库验证测试。

2. 机器学习与数据分析：
    - 支持 Jupyter Notebook 和 数据科学库 (NumPy、Pandas、Matplotlib)。

3. Web 应用开发和测试：
    - 使用 Django 或 Flask 框架开发和测试 Web 应用程序。

4. DevOps 测试自动化：
    - 支持 Docker、Kubernetes 等工具配置，方便环境搭建和集成测试。

5. BDD 测试开发：
    - 支持基于 Gherkin 语法的 Behave 测试框架，便于业务团队和开发团队协作。

### Create a New Project (BackendAutomation) in PyCharm
pip install requests
pip show requests

### Create a New Python Package (utilities) in PyCharm
- utilities => New file: 
  - properties.ini 
  - configurations.py
  - payloads.py

### Github API Authentication
https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    curl --request GET \
    --url "https://api.github.com/octocat" \
    --header "Authorization: Bearer {{token}}" \
    --header "X-GitHub-Api-Version: 2022-11-28"

### Github API Get Repos
https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-the-authenticated-user
"current_user_repositories_url": "https://api.github.com/user/repos"
    curl -L \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer {{token}}" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      https://api.github.com/user/repos

### HTTPBIN
https://httpbin.org/#/Cookies

### MySQL
mysql -u root -p 
    show databases;
    use apidevelop;
    select * from books;
    select * from customerinfo;

https://pypi.org/project/mysql-connector-python/
pip install mysql-connector-python

### BDD
https://cucumber.io/
https://cucumber.io/docs/installation/
https://cucumber.io/docs/installation/python

https://behave.readthedocs.io/en/latest/
https://behave.readthedocs.io/en/latest/gherkin/#feature-testing-setup
https://behave.readthedocs.io/en/latest/gherkin/#features

@tags @tag
Feature: feature name
  description
  further description

  Background: some requirement of this test
    Given some setup condition
      And some other setup action

  Scenario: some scenario
      Given some condition
       When some action is taken
       Then some result is expected.

  Scenario: some other scenario
      Given some other condition
       When some action is taken
       Then some other result is expected.

  Scenario: ...

### Install Behave
https://behave.readthedocs.io/en/latest/install/
pip install behave

### Install Gherkins
https://www.jetbrains.com/pycharm/download/?section=windows
Ctrl+ALT+S > Search for Gherkins

New => Directory (features) => New (create a new file with .feature extension) => New Folder (steps) => New File (step_impl.py)

// Terminal
behave
behave features/BookApi.feature

### Environment File Functions
https://behave.readthedocs.io/en/stable/api.html#environment-file-functions

environment.py
