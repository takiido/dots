from ignis import utils
from modules import Bar, ControlCentre


control_centres = {}

for m in range(utils.get_n_monitors()):
    control_centres[m] = ControlCentre(m)
    Bar(m, control_centres[m])
