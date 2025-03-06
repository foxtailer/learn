# Blog  2

A simple blog platform where users can create folders with Markdown files to generate HTML pages based on 
templates dynamically. In order to understand Django more clearly, the goal of this project is to write 
some functionality that Django provides as a framework, without using Django itself.

## Features

- **Markdown-Based Content:**
  - Users organize blog posts as text files with Markdown syntax.
- **Automatic HTML Generation:**
  - Converts Markdown files into styled HTML pages using predefined templates.
- **Folder Organization:**
  - Each folder corresponds to a post of the blog.
- **Deployment:**
  - Powered by a WSGI Python application as backend part.
  - Uses Nginx as a reverse proxy and Gunicorn as the application server.

```
/blog/
    /app/ - WSGI Aplication
        ...
    /src/ - User data
        /post_name_1/
            post.md
            img_1.jpg
        /post_name_2/
            post.md
            img_1.jpg
    /nginx/
        nginx.conf
    compose.yml
```

# Run

1. Navigate to the project root folder.
2. Execute: `docker compose up --build`
3. Open `127.0.0.1/:8001` in browser.