# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conf_thyglobal import *

html_title = "Thierry"
project = "Thy's Notes"
project_copyright = '2022, Thierry Humphrey'
author = 'Thierry Humphrey'

myst_substitutions = {
    'wordcount': '{sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read',
}

html_theme_options |= {
    # "announcement"         : "My announcement!",

    # 'repository_url'       : 'https://github.com/thy-x/python',
    # 'repository_branch'    : 'main',
    # 'path_to_docs'         : 'docs',
    # 'use_repository_button': True,
    # 'use_edit_page_button' : True,
}

intersphinx_mapping_enabled = (
    'py3',
    'sphinx',
)
intersphinx_mapping = {k: v for k, v in intersphinx_mapping.items() if k in intersphinx_mapping_enabled}
