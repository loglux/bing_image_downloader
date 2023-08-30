# Forked Bing Image Downloader
## Overview
This is a forked version of Bing Image Downloader with additional features. This Python library allows you to download a bulk of images from Bing.com.

### New Features
- `size`: (optional, default is "") Size of image, choose from [small, medium, large, wallpaper].
- `resize_dim`: (optional, default is `None`) Resize the image to given dimensions, e.g., (256, 256).
- `file_types`: (optional, default is `None` which means all types) Choose from 'jpg', 'png', 'gif', 'bmp'.

### Disclaimer
This program lets you download tons of images from Bing.
Please do not download or use any image that violates its copyright terms. 

### Installation <br />
```sh
pip install git+https://github.com/loglux/bing_image_downloader.git
```

or 
```bash
git clone https://github.com/loglux/bing_image_downloader
cd bing_image_downloader
pip install .
```

### Usage <br />
```python
from bing_image_downloader import downloader

search_queries = ["grizzly bear", "black bear", "teddy bear"]

for query in search_queries:
    downloader.download(query, 
                        limit=100,  
                        output_dir='dataset', 
                        adult_filter_off=True, 
                        force_replace=False, 
                        timeout=5, 
                        verbose=True,
                        size="medium",
                        resize_dim=(224, 224),
                        file_types='jpg,png')
```

`query_string` : String to be searched.<br />
`limit` : (optional, default is 100) Number of images to download.<br />
`output_dir` : (optional, default is 'dataset') Name of output dir.<br />
`adult_filter_off` : (optional, default is True) Enable of disable adult filteration.<br />
`force_replace` : (optional, default is False) Delete folder if present and start a fresh download.<br />
`timeout` : (optional, default is 60) timeout for connection in seconds.<br />
`filter` : (optional, default is "") filter, choose from [line, photo, clipart, gif, transparent]<br />
`verbose` : (optional, default is True) Enable downloaded message.<br />
- `size`: (optional, default is "") Size of image, choose from [small, medium, large, wallpaper].
- `resize_dim`: (optional, default is `None`) Resize the image to given dimensions, e.g., (256, 256).
- `file_types`: (optional, default is `None` which means all types) Choose from 'jpg', 'png', 'gif', 'bmp'.

## Original Bing Image Downloader
https://github.com/gurugaurav/bing_image_downloader




