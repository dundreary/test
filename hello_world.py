import os
from github import Github

# Указываем токен доступа и имя пользователя/организации
access_token = 'your_access_token'
username = 'your_username'

# Создаем экземпляр объекта Github
g = Github(access_token)

# Получаем пользователя или организацию
user = g.get_user(username)

# Создаем новый репозиторий
repo_name = 'my-new-repo'
repo_description = 'This is a new repository created with Python'
repo = user.create_repo(repo_name, description=repo_description)

# Печатаем URL для клонирования репозитория
print("Repository URL:", repo.clone_url)

# Создаем файл в репозитории
file_name = 'hello_world.py'
file_content = """
print("Hello, World!")
"""
repo.create_file(file_name, "Initial commit", file_content)

# Делаем коммит
repo_commit = repo.get_commits()[0]
print("Commit Message:", repo_commit.commit.message)
