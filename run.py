import sys
import importlib
import inspect
import json


def run():
    # Get problem ID and input file from terminal.
    problem_id = sys.argv[1]
    input_file = sys.argv[2]

    # Add the problem folder to system path.
    sys.path.append(f"./problem-set/{problem_id}")

    # Load the Solution class.
    module = importlib.import_module("main")
    Solution = module.Solution
    object = Solution()

    # Get the names of methods in the Solution class.
    methods = []
    for name, func in Solution.__dict__.items():
        if not name.startswith("__") and inspect.isfunction(func):
            methods.append(name)
    method_name = methods[0]
    method = getattr(object, method_name)

    # Load and parse input.
    with open(input_file, "r") as f:
        input_list = json.load(f)

    # Run and print the result.
    for input in input_list:
        result = method(*input)
        print(result)


if __name__ == "__main__":
    run()
