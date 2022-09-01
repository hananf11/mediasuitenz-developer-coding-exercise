import pathlib

import markdown
from blog.settings import BASE_DIR
from django.http import JsonResponse

from posts.markdown_helper import read_markdown_meta_data, read_markdown_tags


def post(request, slug):
    file_path = pathlib.Path(BASE_DIR) \
        .joinpath("../assets/posts") \
        .joinpath(slug + '.md')
    with file_path.open("r") as file:
        meta_data = read_markdown_meta_data(file)
        # revert the position for the markdown to html function.
        tags = read_markdown_tags(file, revert_position=True)
        meta_data['tags'] = tags
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
                tags = read_markdown_tags(file)
                meta_data['tags'] = tags
                posts.append(meta_data)

    return JsonResponse({
        "posts": posts
    })
