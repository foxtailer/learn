import sys

folder_path = "/home/zoy/vscode/learn/courses/Python Tutorial"
if folder_path not in sys.path:
    sys.path.append(folder_path)

from decorators_pycon import timer



