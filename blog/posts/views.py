import pathlib

import markdown
from blog.settings import BASE_DIR
from django.http import JsonResponse

from posts.markdown_helper import read_markdown_meta_data

# Feel free to move this to a new file if you are carrying out the 'tags' calculation there
STOP_WORDS = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]


def post(request, slug):
    file_path = pathlib.Path(BASE_DIR) \
        .joinpath("../assets/posts") \
        .joinpath(slug + '.md')
    with file_path.open("r") as file:
        meta_data = read_markdown_meta_data(file)
        html = markdown.markdown(file.read())
    meta_data["html"] = html
    return JsonResponse(meta_data)


def posts(request):
    posts = []

    path = pathlib.Path(BASE_DIR).joinpath("../assets/posts")
    for file_path in path.iterdir():
        if file_path.is_file():
            with file_path.open("r") as file:
                meta_data = read_markdown_meta_data(file)
                posts.append(meta_data)

    return JsonResponse({
        "posts": posts
    })
