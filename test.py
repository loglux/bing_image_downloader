import unittest
import sys
from bing_image_downloader import downloader

class TestBingImageDownloader(unittest.TestCase):
    def test_download_with_query(self):
        query = "grizzly bear"
        filter = ""
        try:
            downloader.download(
                query,
                limit=10,
                output_dir="test_dataset",
                adult_filter_off=True,
                force_replace=True,
                timeout=60,
                filter=filter,
                verbose=False
            )
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Downloader raised an exception: {e}")

    def test_download_with_query_and_filter(self):
        query = "black bear"
        filter = "photo"
        try:
            downloader.download(
                query,
                limit=10,
                output_dir="test_dataset",
                adult_filter_off=True,
                force_replace=True,
                timeout=60,
                filter=filter,
                verbose=False
            )
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Downloader raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
