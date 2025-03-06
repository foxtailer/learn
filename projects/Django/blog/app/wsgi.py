import os
from markdown import markdown
from jinja2 import Template


# Local
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SRC_DIR = os.path.join(BASE_DIR, "src")
# TEMPLATE_DIR = os.path.join(SRC_DIR, "templates")

# Docker
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = '/app/src'
TEMPLATE_DIR = '/app/src/templates'


def application(environ, start_response):
    
    # What data app get from gunicorn
    # for k, v in environ.items():
    #     print(k, '>>', v)

    path_info = environ.get("PATH_INFO", "/").strip("/")

    # Define the index and 404 template paths
    index_template_path = os.path.join(TEMPLATE_DIR, "index.html")
    post_template_path = os.path.join(TEMPLATE_DIR, "post.html")
    not_found_template_path = os.path.join(TEMPLATE_DIR, "404.html")

    # Handle the root path ('/')
    if path_info == "":
        try:
            # List all directories in the src folder
            posts = []
            for post_dir in os.listdir(SRC_DIR):
                post_path = os.path.join(SRC_DIR, post_dir)
                # Ensure it's a directory (post folder) and not the 'templates' directory
                if os.path.isdir(post_path) and post_dir != 'templates':
                    # Check if post.md exists in the folder
                    post_md_path = os.path.join(post_path, 'post.md')
                    if os.path.exists(post_md_path):
                        post_title = post_dir  # Use the directory name as the post title
                        post_url = f"/{post_dir}"  # URL path for the post
                        posts.append({'title': post_title, 'url': post_url})

            # Read the index template and render it with the list of posts
            with open(index_template_path, "r") as file:
                index_template = Template(file.read())
            
            # Render the template with posts list
            index_content = index_template.render(posts=posts)

            # Return the response
            start_response("200 OK", [("Content-Type", "text/html")])
            return [index_content.encode()]

        except FileNotFoundError:
            start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
            return [b"Index page template not found."]

    # Handle post pages
    post_folder_path = os.path.join(SRC_DIR, path_info)
    post_md_path = os.path.join(post_folder_path, "post.md")

    if os.path.exists(post_folder_path) and os.path.isfile(post_md_path):
        try:
            # Read and convert the Markdown content
            with open(post_md_path, "r") as file:
                markdown_content = file.read()
            html_content = markdown(markdown_content)

            # Render the post template
            with open(post_template_path, "r") as template_file:
                template = Template(template_file.read())

            rendered_content = template.render(post_title=path_info, post_content=html_content)

            start_response("200 OK", [("Content-Type", "text/html")])
            return [rendered_content.encode()]
        except Exception as e:
            start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
            return [f"Error rendering post: {str(e)}".encode()]

    # Handle 404 (not found)
    try:
        with open(not_found_template_path, "r") as file:
            not_found_content = file.read()

        start_response("404 Not Found", [("Content-Type", "text/html")])
        return [not_found_content.encode()]
    except FileNotFoundError:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"404 Page not found."]
