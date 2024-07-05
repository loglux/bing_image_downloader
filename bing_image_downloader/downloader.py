import sys
import shutil
from pathlib import Path

try:
    from bing import Bing
except ImportError:  # Python 3
    from .bing import Bing


def download(label, limit=100, output_dir='dataset', adult_filter_off=True,
             force_replace=False, timeout=60, filter="", size="", resize_dim=None, file_type=None, verbose=True, label_filename=False):
    # engine = 'bing'
    if adult_filter_off:
        adult = 'off'
    else:
        adult = 'on'

    if label_filename:
        folder = ''
    else:
        folder = label
    image_dir = Path(output_dir).joinpath(folder).absolute()

    if force_replace:
        if Path.is_dir(image_dir):
            shutil.rmtree(image_dir)

    # check directory and create if necessary
    try:
        if not Path.is_dir(image_dir):
            Path.mkdir(image_dir, parents=True)

    except Exception as e:
        print('[Error]Failed to create directory.', e)
        sys.exit(1)

    print("[%] Downloading Images to {}".format(str(image_dir.absolute())))
    bing = Bing(label, limit, image_dir, adult, timeout, filter, size, verbose, label_filename)
    bing.run(file_type, resize_dim)


if __name__ == '__main__':
    download('dog', output_dir="dataset", limit=10, timeout=5, resize_dim=(224, 224))
