class ApiResources:
    headers = {
        "Content-Type": "application/json"
    }

    add_book = '/Library/Addbook.php'
    get_book = '/Library/GetBook.php'
    delete_book = '/Library/DeleteBook.php'
    github = 'https://api.github.com'
    github_user_repos = github + '/user/repos'
    github_rate_limits = github + '/rate_limit'
    github_user_followers = github + '/user/followers'