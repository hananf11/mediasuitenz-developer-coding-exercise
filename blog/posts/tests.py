from django.test import TestCase, Client
from blog.settings import BASE_DIR
from posts.markdown_helper import read_markdown_meta_data, read_markdown_tags
import pathlib


BASE_DIR_POSTS = pathlib.Path(BASE_DIR).joinpath("../assets/posts")


class MarkdownTestCase(TestCase):
    def test_read_meta_data(self):
        """Test that the meta data is read correctly. """
        # I could check more
        # There is probably a better way to do this... I haven't used unittest before
        try_files = {
            "Im-betting-on-SPAs.md": {
                "title": "I’m betting on SPAs",
                "author": "Jon Hollingsworth",
                "slug": "Im-betting-on-SPAs"
            },
            "kiasuism-vs-no8-wire.md": {
                "title": "Kiasuism vs No.8 Wire",
                "author": "Steve Liew",
                "slug": "kiasuism-vs-no8-wire"
            }
        }
        for try_file, try_file_meta_data in try_files.items():
            file_path = BASE_DIR_POSTS / try_file
            with file_path.open("r") as file:
                meta_data = read_markdown_meta_data(file)
            self.assertEqual(meta_data, try_file_meta_data)

    def test_read_tags(self):
        """Test that the tags are being generated from the file correctly, and predictably."""
        try_files = {
            "Im-betting-on-SPAs.md": ["javascript", "page", "server", "content", "saw"],
            "kiasuism-vs-no8-wire.md": ["like", "since", "singapore", "can", "ethnic"],
            "mediasuite-tech-stack.md": ["use", "large", "projects", "technologies", "also"]
        }
        for try_file, try_file_tags in try_files.items():
            file_path = BASE_DIR_POSTS / try_file
            with file_path.open("r") as file:
                tags = read_markdown_tags(file)
            self.assertEqual(tags, try_file_tags, try_file)

    def test_tags_in_file(self):
        """Test that the tags generated from a file are actually within that file.
        If the tag is not in the file that means something probably went wrong as a new word was created eg we'd becoming wed."""
        c = Client()

        for file_path in BASE_DIR_POSTS.iterdir():
            response = c.get(f"/posts/{file_path.stem}/")
            html_string = response.json()["html"].lower()
            with file_path.open("r") as file:
                tags = read_markdown_tags(file)
            for tag in tags:
                self.assertIn(tag, html_string,
                              f"{tag} in html made from {file_path.name}")
