#!/usr/bin/env bash

SOURCE="$HOME/.config/aesth/color.conf"

if [ ! -f "$SOURCE" ]; then
	echo "Please create a color.conf file ;)"
	exit 1
fi

source "$SOURCE"

cat <<EOF > "$HOME/.config/kitty/aesth.conf"

background #${tone2}
foreground #${tone1}
active_border_color #${acct}

EOF





cat <<EOF > "$HOME/.config/waybar/color.css"

@define-color prim #${prim};

@define-color secd #${secd};

@define-color acct #${acct};
@define-color high-tone #${tone1};
@define-color low-tone #${tone2};

EOF

cat <<EOF > "$HOME/.config/wofi/color.css"

@define-color prim #${prim};

@define-color secd #${secd};

@define-color acct #${acct};
@define-color high-tone #${tone1};
@define-color low-tone #${tone2};

EOF

cat <<EOF > "$HOME/.config/hypr/color.lua"

return {
	prim="rgba(${prim}ff)",
	secd="rgba(${secd}ff)",
	acct="rgba(${acct}ff)",
	high_tone="rgba(${tone1}ff)",
	low_tone="rgba(${tone2}ff)"
	
}

EOF


hexToRGB(){
	local COLOR=$1
	local R=$(printf "%d" "0x${COLOR:0:2}")
	local G=$(printf "%d" "0x${COLOR:2:2}")
	local B=$(printf "%d" "0x${COLOR:4:2}")
	echo "$R;$G;$B"
}


vlight=$(hexToRGB ${tone1})
vdark=$(hexToRGB ${prim})

cat<<EOF > "$HOME/.config/bash/color.sh"

light=$'\001\033[38;2;'"${vlight}"$'m\002'
light_bold=$'\001\033[1;38;2;'"${vlight}"$'m\002'
dark=$'\001\033[38;2;'"${vdark}"$'m\002'
dark_bold=$'\001\033[1;38;2;'"${vdark}"$'m\002'

EOF

cat<<'EOF' > "$HOME/.config/bash/prompt.sh" 

source "$HOME/.config/bash/color.sh"

shopt -s promptvars
PS1=$'\n '"${dark_bold}"' \u  '"${light}"'   [\W]'"${light_bold}${reset}"$'\n     > '
EOF


echo -e "Palette compiled!"


