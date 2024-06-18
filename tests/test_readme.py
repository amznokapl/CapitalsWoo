import os
import unittest

class TestReadmeContent(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue(os.path.exists("README.md"), "README.md file does not exist")

    def test_readme_content(self):
        with open("README.md", "r") as f:
            content = f.read()
            self.assertIn("Project Description", content)
            self.assertIn("Branches", content)
            self.assertIn("main", content)
            self.assertIn("develop", content)
