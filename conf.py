# -*- coding: utf-8 -*-
#
# Project ACRN documentation build configuration file, created by
# sphinx-quickstart on Wed Jan 10 20:51:29 2018.
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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['breathe']

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
project = u'Project ACRN™'
copyright = u'2018, Project ACRN'
author = u'Project ARCN developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The following code tries to extract the information by reading the
# Makefile from the acrn-hypervisor repo by finding these lines:
#   MAJOR_VERSION=0
#   MINOR_VERSION=1
#   RC_VERSION=1

try:
    version_major = None
    version_minor = None
    version_rc = None
    for line in open(os.path.normpath("../acrn-hypervisor/Makefile")) :
        # remove comments
        line = line.split('#', 1)[0]
        line = line.rstrip()
        if (line.count("=") == 1) :
           key, val = [x.strip() for x in line.split('=', 2)]
           if key == 'MAJOR_VERSION':
              version_major = val
           if key == 'MINOR_VERSION':
              version_minor = val
           if key == 'RC_VERSION':
              version_rc = val
           if version_major and version_minor and version_rc :
              break
except:
    pass
finally:
    if version_major and version_minor and version_rc :
        version = release = "v " + version_major + '.' + version_minor
        if int(version_rc) > 0 :
           version = release = version + '-rc' + version_rc
    else:
        sys.stderr.write('Warning: Could not extract hypervisor version from Makefile\n')
        version = release = "unknown"



#
# The short X.Y version.
# version = u'0.1'
# The full version, including alpha/beta/rc tags.
# release = u'0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build' ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
try:
    import sphinx_rtd_theme
except ImportError:
    html_theme = 'alabaster'
    # This is required for the alabaster theme
    # refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
    html_sidebars = {
        '**': [
            'relations.html',  # needs 'show_related': True theme option to display
            'searchbox.html',
            ]
        }
    sys.stderr.write('Warning: sphinx_rtd_theme missing. Use pip to install it.\n')
else:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme_options = {
        'canonical_url': '',
        'analytics_id': '',
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'None',
        # Toc options
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4,
    }


# Here's where we (manually) list the document versions maintained on
# the published doc website.  On a daily basis we publish to the
# /latest folder but when releases are made, we publish to a /<relnum>
# folder (specified via RELEASE=name on the make command).

if tags.has('release'):
   current_version = version
else:
   version = current_version = "latest"

html_context = {
   'current_version': current_version,
   'versions': ( ("latest", "/latest/"),
                 ("0.1-rc4", "/0.1-rc4/"),
               )
    }


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

html_logo = 'images/ACRN_Logo_300w.png'
html_favicon = 'images/ACRN-favicon-32x32.png'

numfig = True
#numfig_secnum_depth = (2)
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Code Block %s'}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

def setup(app):
   app.add_stylesheet("acrn-custom.css")

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ACRN Project Help'


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
    (master_doc, 'acrn.tex', u'Project ACRN Documentation',
     u'Project ACRN', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'acrn', u'Project ACRN Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Project ACRN', u'Project ACRN Documentation',
     author, 'Project ACRN', 
     'IoT-Optimized Hypervisor for Intel Architecture',
     'Miscellaneous'),
]

rst_epilog = """
.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN
   :ltrim:
.. |trade|  unicode:: U+02122 .. TRADEMARK SIGN
   :ltrim:
.. |reg|    unicode:: U+000AE .. REGISTERED TRADEMARK SIGN
   :ltrim:
.. |deg|    unicode:: U+000B0 .. DEGREE SIGN
   :ltrim:
.. |plusminus|  unicode:: U+000B1 .. PLUS-MINUS SIGN
   :rtrim:
.. |micro|  unicode:: U+000B5 .. MICRO SIGN
   :rtrim:
"""


breathe_projects = {
	"Project ACRN" : "doxygen/xml",
}
breathe_default_project = "Project ACRN"
breathe_default_members = ('members', 'undoc-members', 'content-only')
