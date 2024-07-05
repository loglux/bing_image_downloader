import unittest
import sys
from bing_image_downloader import downloader


class TestBingImageDownloader(unittest.TestCase):
    def test_download_with_query_and_new_features(self):
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
                verbose=False,
                size="medium",
                resize_dim=(256, 256),
                file_type='jpg,png',
                label_filename=True
            )
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Downloader raised an exception: {e}")

    def test_download_with_query_and_filter_and_new_features(self):
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
                verbose=False,
                size="medium",
                resize_dim=(256, 256),
                file_type='jpg,png',
                label_filename=True
            )
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Downloader raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
