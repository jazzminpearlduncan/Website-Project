# Set up pyenv environment
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"  # For login shells, use --path
eval "$(pyenv init -)"  # For interactive shells

# Set up pyenv-virtualenv
eval "$(pyenv virtualenv-init -)"

