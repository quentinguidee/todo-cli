#!/usr/bin/env sh

printf "Running tests before commiting...\n\n"

python3 tests.py
exit_code=$?

if [ $exit_code -ne 0 ]; then
    echo "Tests failed. Cannot commit."
    echo "If you want to force commit, you can add the --no-verify flag."
    exit 1
fi
