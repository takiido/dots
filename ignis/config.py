import os
from ignis.app import IgnisApp

from bar.bar import Bar


app = IgnisApp.get_default()

app.apply_css(os.path.expanduser("~/.config/ignis/styles/styles.scss"))

Bar(0)
