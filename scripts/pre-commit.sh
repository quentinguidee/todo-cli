#!/usr/bin/env sh

printf "\nTests: Running..."

python3 tests.py >/dev/null 2>&1
exit_code=$?

if [ $exit_code -ne 0 ]; then
    printf "\rTests: FAILED.\n\n"
    echo "The tests don't pass. Cannot commit."
    echo "Re-run 'python3 tests.py' for more info."
    echo ""
    echo "If you want to force commit, you can add the --no-verify flag."
    exit 1
fi

printf "\rTests: PASSED.\n"

printf "pycodestyle: Running..."

pycodestyle . --max-line-length=120 >/dev/null 2>&1
exit_code=$?

if [ $exit_code -ne 0 ]; then
    printf "\rpycodestyle: FAILED.\n\n"
    echo "Some formatting mistakes found. Cannot commit."
    echo "Re-run 'pycodestyle . --max-line-length=120' for more info."
    echo ""
    echo "If you want to force commit, you can add the --no-verify flag."
    exit 1
fi

printf "\rpycodestyle: PASSED.\n\n"
