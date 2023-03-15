import os

def FileFInder(dir_path):
    try:
        res = []
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)

        return res
    except:
        pass
