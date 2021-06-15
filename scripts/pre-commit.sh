#!/usr/bin/env sh

printf "Running tests before commiting...\n\n"

python3 tests.py
exit_code=$?

if [ $exit_code -ne 0 ]; then
    echo "Tests failed"
    exit 1
fi
