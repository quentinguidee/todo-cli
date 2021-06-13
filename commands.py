from typing import Callable
from courses import courses


class Command:
    def __init__(self, to_execute: Callable, args: dict = {}) -> None:
        self.function_to_execute = to_execute
        self.args = args

    def execute(self, args):
        if self.args_count() == len(args):
            return self.function_to_execute(*args)

        return print("Args error.")

    def args_count(self):
        return len(self.args)


commands = {
    "course": {
        "add": Command(courses.add, args={"name": "The course to add."}),
        "remove": Command(courses.remove, args={"name": "The course to remove."}),
        "list": Command(courses.list)
    }
}


def execute(*args: str):
    commands_copy = commands
    while True:
        if type(commands_copy) is not dict:
            break

        commands_copy = commands_copy.get(args[0])
        args = args[1:]

        if commands_copy == None:
            print("Command not found.")
            return

    if type(commands_copy) is Command:
        commands_copy.execute(args)
        return
