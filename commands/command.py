import abc
from typing import Callable


class Command(metaclass=abc.ABCMeta):
    args: dict[str, str] = {}

    def check_args(self, args):
        args_count_expected = self.args_count()
        args_count = len(args)

        if args_count == args_count_expected:
            return True

        if args_count > args_count_expected:
            return print("Too much arguments.")

        return print("Not enough arguments")

    @abc.abstractmethod
    def execute(self, args):
        pass

    def __call__(self, args):
        if self.check_args(args):
            return self.execute(args)

        return 1

    def args_count(self):
        return len(self.args)
