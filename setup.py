import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bing_image_downloader_ext",
    version="1.1.3",  # Incremented from the forked 1.1.2
    author="Loglux",
    author_email="",
    description="Forked version of bing_image_downloader with support for resizing, file types, and size filters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loglux/bing_image_downloader",
    keywords=['bing', 'images', 'scraping', 'image download', 'bulk image downloader', 'resize', 'file type', 'size filter'],
    packages=['bing_image_downloader'],
    install_requires=[
        'Pillow',  # PIL is used for resizing
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
