import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../band_site'))  # Add your project directory

# Change this line to use your actual project name
os.environ['DJANGO_SETTINGS_MODULE'] = 'band_site.settings'

django.setup()
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'band_site'
copyright = '2025, jako gelderblom'
author = 'jako gelderblom'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
