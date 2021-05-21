# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Project Name'
author = 'Author Name'
# -- Sphinx config ---------------------------------------------------
extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
]

# sphinx_panels config
panels_add_bootstrap_css = True

templates_path = ['_templates']
pygments_style = "sphinx"
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    "*import_posts*", 
    "**/pandoc_ipynb/inputs/*",
    "ipynb_checkpoints/*"
    ]
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# I'm using a custom footer in _templates
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False


# -- HTML Config -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
  "github_url": "",
  "search_bar_text": "Search this site...",
  "google_analytics_id": "",
  "search_bar_position": "navbar"
}

html_favicon = "_static/magnifying.ico"
html_static_path = ['_static']
html_sidebars = {
    "index": ['hello.html'],
    "about": ['hello.html'],
    "posts/**": ['recentposts.html', 'archives.html','tags.html'],
    "**": ['recentposts.html', 'archives.html','tags.html'],
    
}
blog_baseurl = ""
blog_title = "Blog Title"
blog_path = "index"
fontawesome_included = True
blog_post_pattern = "posts/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_except = 1
post_date_format = "%d %B %Y"

# -- Myst config ---------------------------------------------------
myst_admonition_enable = True
myst_deflist_enable = True
myst_update_mathjax = False
extensions += [
    "ablog",
]

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off" #TODO test

def setup(app):
    app.add_css_file("custom.css")
