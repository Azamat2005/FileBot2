import wget
import os
import shutil
def bar_progress(current, total, width=80):
      progress_message = "Downloading: %d%% [%d / %d] megabytes" % (current / total * 100, current / 1024 / 1024, total / 1024 /1024)


      os.sys.stdout.write("\r" + progress_message)
      os.sys.stdout.flush()


def Download(url, path_downlaod,):

        try:
            wget.download(url, path_downlaod, bar=bar_progress,)
        except:
            pass

def DeleteFolder(path):
    try:
        shutil.rmtree(path)
    except:
        pass