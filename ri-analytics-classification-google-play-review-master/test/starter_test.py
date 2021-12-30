import json
import os
import sys
import unittest
import warnings
 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import app
 
PAYLOAD_APP_REVIEWS= """
    [
        {
            "review_id": "gp:AOqpTOEVr-VrgKe-k156d7xCsVLjBZyNfidIdoR-VClNWGpFSYloCAWWb2Q9oLOiWAFYyg__qWd0GHmEb1KM2KE",
            "package_name": "com.whatsapp",
            "rating": 5,
            "title": "",
            "body": " Super "
        },
        {
            "review_id": "gp:AOqpTOFIKs6aDonHtvb45XmCX4edZIurJl_yuytj-zq3emhqQxXibx69Tz_C3uqn4Tep4zvfh0ALoGZJTCY1OX4",
            "package_name": "com.whatsapp",
            "rating": 5,
            "title": "",
            "body": " very good nice "
        },
        {
            "review_id": "gp:AOqpTOGZvYM-YqGnUX8QFMhKPpBpxMdmrwqFo_n2gJCHpjt1y8cBP7A2jr7EFvRrKFSFJErgJdBG7rug5vKTnFo",
            "package_name": "com.whatsapp",
            "rating": 5,
            "title": "",
            "body": " It's very very good "
        },
        {
            "review_id": "gp:AOqpTOEXUftZLAdy6GS-nQHakqwK1Ef2FHt_NdMAnGzYfIaWDJYkIWCLvL1rWaQ8NzyOetQ029bELpK6hbrO3QM",
            "package_name": "com.whatsapp",
            "rating": 5,
            "title": "",
            "body": " Superb "
        },
        {
            "review_id": "gp:AOqpTOHWblt5OvlhLK0jWca7FaT_5b0JeEJIHOaABVOsTArDO6dwFSDYHunRBGGX4USOW_rfdHCleXgsZ7ffyX8",
            "package_name": "com.whatsapp",
            "rating": 1,
            "title": "",
            "body": " The app is very buggy. It crashes all the time when I call someone. "
        }
    ]
"""
 
 
class TestBasic(unittest.TestCase):
    def setUp(self):
        # Ignore third-party warnings from setup phase..
        warnings.simplefilter('ignore')
        # Initialize Flask server hosting api
        self.app = app.test_client()
 
    def test_post_classification_result(self):
        #############################################
        # Test English Google App Review classifier #
        #############################################
        resp = self.app.post(
            '/hitec/classify/domain/google-play-reviews/',
            data=PAYLOAD_APP_REVIEWS
        )
        
        status_code = resp._status_code
        body = resp.get_data()
        self.assertEqual(status_code, 200, msg='API should be responsive with 200 status code')
        
        for review in json.loads(body):
            self.assertEqual("cluster_is_bug_report" in review, True, msg='classified reviews should contain the defined key')

        for review in json.loads(body):
            self.assertEqual("cluster_is_feature_request" in review, True, msg='classified reviews should contain the defined key')

if __name__ == '__main__':
    # Run the TestBasic unit tests
    unittest.main(verbosity=2)
 