#!/usr/bin/env bash

SESSION="dev"
DIR="${1:-$(pwd)}"

tmux new-session -d -s "$SESSION" -c "$DIR"

# Pane 1 nvim
tmux send-keys -t "$SESSION:0.0" "nvim ." Enter

# Pane 2 opencode
tmux split-window -h -c "$DIR" -t "$SESSION:0.0" "opencode"

# Pane 3 terminal
tmux split-window -v -c "$DIR" -t "$SESSION:0.0"

# Size: left column 50%, terminal takes ~30% of left height
tmux resize-pane -t "$SESSION:0.0" -x 80%
tmux resize-pane -t "$SESSION:0.0" -y 90%

# Focus nvim
tmux select-pane -t "$SESSION:0.0"

tmux attach-session -t "$SESSION"
