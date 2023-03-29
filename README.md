# qtile-decay-dotfiles
Dotfiles for void Linux using Qtile and a dark-decay color scheme.

# Installation

## Dependencies
This guide is mainly for Void Linux.
You may need to adapt the dependencies to use this configuration on another distro.

### XBPS
Install the following dependencies for Void Linux via `xbps-install`:
* Shell: `zsh bat exa`
* Terminal: `alacritty bat exa`
* Qtile: `qtile sxhkd xorg picom`
* Polybar: `polybar`
* Dunst: `dunst`
* GTK: `gtk+3-devel papirus-icon-them`


And all together:
`zsh tmux alacritty bat exa qtile sxhkd xord picom polybar dunst gtk+3-devel papirus-icon-them`

### Git
Install the following git repositories:
* [eww](https://github.com/elkowar/eww)


## Dotfiles Cloning
To install these dotfiles follow [this](https://www.atlassian.com/git/tutorials/dotfiles) guide. Basically you install this repo in your home folder with an alias `config` for git.
`alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'`
To hinder unwanted interactions with your current home folder run `echo ".cfg" >> .gitignore`.
Now the repo can be cloned with `git clone --bare <git-repo-url> $HOME/.cfg`.

This can lead to problems with your current dotfiles. The script below does everything from above and places the current home in a backup folder `.config-backup`:
```bash
git clone --bare https://bitbucket.org/durdn/cfg.git $HOME/.cfg

function config {
   /usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME $@
}

mkdir -p .config-backup
config checkout
if [ $? = 0 ]; then
  echo "Checked out config.";
  else
    echo "Backing up pre-existing dot files.";
    config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .config-backup/{}
fi;
config checkout
config config status.showUntrackedFiles no
```

## Dotfiles Manual Steps

### GTK Themes

#### Color Scheme
This rice uses the [dark-decay](https://github.com/decaycs) color scheme. For GTK you need to move the `dark-decay` theme out of its directory.
```bash
cp -r $HOME/.themes/decay-gtk/Themes/Dark-decay $HOME/.themes/Dark-decay
```

#### Font
Here the Bitstream Vera Sans Mono [Nerd Font](https://www.nerdfonts.com/) is used. Download the [font pack](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/BitstreamVeraSansMono.zip) into the `$HOME/.fonts` folder and unzip it.
This can be done with these bash commands:
```bash
wget -O $HOME/.fonts/Bitstream.zip https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/BitstreamVeraSansMono.zip 
unzip $HOME/.fonts/Bitstream.zip -d $HOME/.fonts
rm $HOME/.fonts/Bitstream.zip
fc-cache # Loads the fonts
```


## Void Linux Configurations


# Acknowledgments
Some configs are modified from other users. In this section I just want to acknowledge and reference there work. 

* [durdn](https://www.twitter.com/durdn) for the [guide](https://www.atlassian.com/git/tutorials/dotfiles) to manage your dotfiles
* [iSparsh/gross](https://github.com/iSparsh/gross) for the base of the eww widgets
* [fwsmit](https://gist.github.com/fwSmit/9127d988b07bcec9d869f2c927d0f616) for the base of the dunstrc

