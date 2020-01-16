import re
import sys

def err(msg):
    sys.exit(f"ERROR: {msg}")

def check_py():
    if sys.version_info[0] < 3:
        err("Must be using Python 3")

def check_pname():
    name = '{{ cookiecutter.project_slug }}'
    if not re.match(r'^[a-zA-Z]\w+$', name):
        err(f"The project slug ({name}) is not a valid Python module name")

def main():
    check_py()
    check_pname()

if __name__ == "__main__":
    main()
