#!/usr/bin/env sh

echo "Install pre-commit hook"

ln -s scripts/pre-commit.sh .git/hooks/pre-commit

echo "Install packages"

python3 -m pip install -r requirements.txt
