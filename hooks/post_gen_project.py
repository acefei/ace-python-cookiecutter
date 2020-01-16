import requests


def fetch_gitignore():
    url = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore' 
    r = requests.get(url)  
    with open('.gitignore', 'w') as f:
        f.write(r.text)

def main():
    fetch_gitignore()

if __name__ == '__main__':
    main()
