import app from "ags/gtk4/app"
import { Astal } from "ags/gtk4"
import { createPoll } from "ags/time"

function Bar({monitor}){
    const { TOP, LEFT, RIGHT } = Astal.WindowAnchor
    const clock = createPoll("", 1000, "date")
    return (
      <window monitor={monitor} visible anchor={TOP | LEFT | RIGHT}>
        <label label={clock} />
      </window>
    )
}

app.start({
  main() {
      Bar(0)
      Bar(1)
  },
})
