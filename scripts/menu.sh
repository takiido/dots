#!/bin/bash

WINDOW_WIDTH=22
TITLE=""
VALUE=""

# Arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --title=*)
      TITLE="${1#*=}"
      shift
      ;;
    --title)
      TITLE="$2"
      shift 2
      ;;
    --value=*)
      VALUE="${1#*=}"
      shift
      ;;
    --value)
      VALUE="$2"
      shift 2
      ;;
    *)
      echo "Error: Unknown option $1"
      exit 1
      ;;
  esac
done

center_text() {
  local str="$1"
  local len=${#str}
  local padding=$(( (WINDOW_WIDTH - len) / 2 ))
  
  if [ $padding -gt 0 ]; then
    printf "%${padding}s%s" "" "$str"
  else
    echo -n "$str"
  fi
}

# ASCII progress bar
PROGRESS_BAR=""

if [ "$VALUE" -eq 0 ]; then
  PROGRESS=0
else
  PROGRESS=$(( (VALUE % 10) > 4 ? (VALUE / 10) + 1 : VALUE / 10 ))
fi

BAR_FILLED=""
if [ $PROGRESS -gt 0 ]; then
  BAR_FILLED=$(printf '%0.s██' $(seq 1 "$PROGRESS"))
fi

BAR_EMPTY=""
REMAINING=$(( 10 - PROGRESS ))
if [ $REMAINING -gt 0 ]; then
  BAR_EMPTY=$(printf '%0.s░░' $(seq 1 "$REMAINING"))
fi

PROGRESS_BAR="[${BAR_FILLED}${BAR_EMPTY}]"

# Final text to show
CENTERED_TITLE=$(center_text "$TITLE")
CENTERED_VALUE=$(center_text "${VALUE}%")
TEXT_TO_SHOW="${CENTERED_TITLE}\n\n${PROGRESS_BAR}\n\n${CENTERED_VALUE}"

foot --title="popup" \
     --window-size-chars=${WINDOW_WIDTH}x6 \
     --override=cursor.blink=false \
     --override=colors.cursor="070707 080808" \
     sh -c "stty -echo; echo -e '$TEXT_TO_SHOW'; sleep 3 < /dev/null"

