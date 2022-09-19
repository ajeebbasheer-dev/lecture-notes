# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.append(os.path.abspath("./_ext"))

project = 'Notebook'
copyright = '2022, Ajeeb Basheer'
author = 'Ajeeb Basheer'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton', 
    'mcq', 
    'sphinx_tabs.tabs', 
    'sphinx_togglebutton', 
    'sphinx_panels']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# sphinx_togglebutton configs
# sphinx_togglebutton_selector = ".toggle-this-element, #my-special-id"
togglebutton_hint = ""
togglebutton_hint_hide = ""

def setup(app):
    app.add_css_file('custom.css')