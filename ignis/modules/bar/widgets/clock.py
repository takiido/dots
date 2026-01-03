"""Clock widget with calendar tooltip."""

import calendar
import datetime

from ignis import utils, widgets


class Clock(widgets.Box):
    """Displays current time with calendar tooltip.

    Shows time in HH:MM format and a text-based calendar
    as tooltip with current day highlighted.
    """

    UPDATE_INTERVAL_MS = 60000

    def __init__(self) -> None:
        """Initialize the clock widget."""
        self._label = widgets.Label(label="--:--")

        super().__init__(child=[self._label], css_classes=["bar__clock"])

        self._update()
        utils.Poll(self.UPDATE_INTERVAL_MS, lambda _: self._update())

    def _update(self) -> None:
        """Update time display and calendar tooltip."""
        now = datetime.datetime.now()
        self._label.set_label(now.strftime("%H:%M %p"))
        self.set_tooltip_text(self._get_calendar())

    def _get_calendar(self) -> str:
        """Generate text calendar with today highlighted."""
        now = datetime.datetime.now()
        cal = calendar.TextCalendar(firstweekday=6)
        lines = cal.formatmonth(now.year, now.month).splitlines()

        today = str(now.day)
        result = []

        for line in lines:
            words = line.split()
            formatted = []
            for word in words:
                if word == today:
                    formatted.append(f"[{word}]")
                else:
                    formatted.append(f" {word} " if len(word) == 1 else word)
            result.append("  ".join(formatted) if formatted else line)

        return "\n".join(result)
