local s = require("utils.settings")

hl.config({
  general = {
    border_size = s.border_size,
    gaps_in = s.gaps_in,
    gaps_out = s.gaps_out,
    col = {
      active_border = s.colors.active_border,
      inactive_border = s.colors.inactive_border,
    }
  },

  decoration = {
    rounding = s.decoration.rounding,
    rounding_power = s.decoration.rounding_power
  }
})
