from modules import Bar
from ignis.css_manager import CssManager, CssInfoString, CssInfoPath
from ignis import utils
import os

css_manager = CssManager.get_default()

# From file
css_manager.apply_css(
    CssInfoPath(
        name="main",
        path=os.path.join(os.path.dirname(__file__), "style.scss"),
        compiler_function=lambda path: utils.sass_compile(path=path),
    )
)

for m in range(utils.get_n_monitors()):
    Bar(m)
