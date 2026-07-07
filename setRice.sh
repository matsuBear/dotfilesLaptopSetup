
#!/usr/bin/env bash
set -euo pipefail

setconf() {
    local name="$1"
    [ -d "$name" ] || { echo "Missing '$name' source dir — aborting."; exit 1; }
    rm -rf ~/.config/"$name"
    mv "$name" ~/.config/
    echo "Set $name!"
}



read -p "This will overwrite your existing .config files and setup some fonts. Continue? (y/n) " answer
if [[ "$answer" == "y" ]]; then
    echo "Proceeding..."
	echo -e "Setting up the fonts to /usr/local/share/fonts/\nYou will be prompted to enter you password!"

	if [ -d "/usr/local/share/fonts/" ]; then
		sudo mv fonts/* /usr/local/share/fonts/
		echo -e "Fonts were succesfully set!"
	else
		echo -e "No /usr/local/share/fonts/ directory was found!\nSkipping font setup."
	fi
	setconf waybar
	setconf wofi
	setconf hypr
	setconf kitty
	setconf bash
	read -p "Automatically add prompt to .bashrc file? (y/n) " prompt
	if [[ "$prompt" == "y" ]]; then
		echo -e "if [ -f ~/.config/bash/prompt.sh ]; then\n    source ~/.config/bash/prompt.sh\nfi" >> ~/.bashrc
		echo "Done!"
	else
		echo "Skipped setting prompt."
	fi
	setconf aesth
	if [ ! -d ~/ShellScripts/ ]; then
		mkdir ~/ShellScripts
		echo "Created ShellScripts dir!"
	fi
	mv reload-colors ~/ShellScripts/
	chmod 700 ~/ShellScripts/reload-colors
	echo "All files were set! Do not forget to run reload-colors to generate truly fresh files! Also do remove this directory!"
else
    echo "Aborted."
    exit 1
fi


