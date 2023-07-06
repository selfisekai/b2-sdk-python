######################################################################
#
# File: doc/source/conf.py
#
# Copyright 2019, Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################
from __future__ import annotations

# -*- coding: utf-8 -*-
#
# B2 Python SDK documentation build configuration file, created by
# sphinx-quickstart on Fri Oct 20 18:2doc/source/conf.py
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import datetime
import os
import sys
sys.path.append(os.path.abspath('../..'))

from b2sdk.version import VERSION  # noqa: E402

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    #'sphinxcontrib.fulltoc',  # 2019-03-29: unfortunately this doesn't work with sphinx_rtd_theme
    'sphinxcontrib.plantuml',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'b2-sdk-python'

year = datetime.date.today().strftime("%Y")
author = u'Backblaze'
copyright = f'{year}, {author}'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = VERSION.rsplit('.', 1)[0]
# The full version, including alpha/beta/rc tags.
release = VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = os.environ.get('B2_SPHINX_TODO', False) and True

# -- Options for HTML output ----------------------------------------------

html_context = {
    "display_github": True,  # Add 'Edit on Github' link instead of 'View page source'
    "github_user": "Backblaze",
    "github_repo": project,
    "github_version": "master",
    "conf_py_path": "/doc/source/",
    "source_suffix": source_suffix,
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'collapse_navigation': True,
}

autodoc_default_options = {
    'member-order': 'bysource',
    'exclude-members': '__weakref__, _abc_cache, _abc_negative_cache, _abc_negative_cache_version, _abc_registry, _abc_impl',
    'members': True,
    'undoc-members': True,
}  # yapf: disable

always_document_param_types = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**':
        [
            'about.html',
            'navigation.html',
            'relations.html',  # needs 'show_related': True theme option to display
            'searchbox.html',
            'donate.html',
        ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'B2_Python_SDKdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'B2_Python_SDK.tex', u'B2\\_Python\\_SDK', u'Backblaze', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'b2_python_sdk', u'B2 Python SDK Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc, 'B2_Python_SDK', u'B2 Python SDK Documentation', author, 'B2_Python_SDK',
        'Backblaze Python SDK', 'Miscellaneous'
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
