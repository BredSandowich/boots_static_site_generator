# boots_static_site_generator
Takes raw content files and turns them into a static website (a mix of HTML and CSS files)

The flow of data through the full system is:

Markdown files are in the /content directory. A template.html file is in the root of the project.
The static site generator (the Python code in src/) reads the Markdown files and the template file.
The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.
We start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on http://localhost:8888 (our local machine).
We open a browser and navigate to http://localhost:8888 to view the rendered site.
