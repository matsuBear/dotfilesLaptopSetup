
source "$HOME/.config/bash/color.sh"

shopt -s promptvars
PS1=$'\n '"${dark_bold}"' \u  '"${light}"'   [\W]'"${light_bold}${reset}"$'\n     > '
