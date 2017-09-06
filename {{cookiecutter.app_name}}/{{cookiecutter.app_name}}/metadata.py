# -*- coding: utf-8 -*-
"""Project metadata

Information describing the project.
"""

# The package name, which is also the "UNIX name" for the project.
package = {{cookiecutter.app_name}}
project = {{cookiecutter.project_name}}
project_no_spaces = project.replace(' ', '')
version = '0.1'
description = {{cookiecutter.project_short_description}}
authors = {{cookiecutter.github_username}}
authors_string = ', '.join(authors)
emails = {{cookiecutter.email}}
license = 'MIT'
copyright = '2017 ' + authors_string
url = 'http://example.com/'
