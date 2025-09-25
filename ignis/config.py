from ignis.widgets import Widget
        

Widget.Window(
    namespace="some-window",  # the name of the window (not title!)
    child=Widget.Scale(
    vertical=False,
    min=0,
    max=100,
    step=1,
    value=20,
    on_change=lambda x: print(x.value),
    draw_value=True,
    value_pos='top'
))
