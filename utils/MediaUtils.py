import requests
import os


def downloadFromUrl(url: str, path: str, filename: str) -> bool:
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, filename), 'wb') as f:
            resp = requests.get(url)
            f.write(resp.content)
        return True
    except Exception as e:
        print('==========[Error]==========')
        print(e)
        print('===========================')
        return False
