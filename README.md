# qtile-decay-dotfiles
Dotfiles for void Linux using Qtile and a dark-decay color scheme.

# Installation

## Dependencies
This guide is mainly for Void Linux.
You may need to adapt the dependencies to use this configuration on another distro.

Install the following dependencies for void Linux:
* Shell: `zsh bat exa`
* Terminal: `alacritty bat exa`
* Qtile: `qtile sxhkd xorg picom`


And all together:
`zsh tmux alacritty bat exa qtile sxhkd xord picom`


## Dotfiles
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

## Void Linux Configurations
