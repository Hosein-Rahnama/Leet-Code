import sys
import importlib
import inspect
import json
import copy
from colorama import Fore, Style


def run():
    # Get problem ID and input file path from command line.
    problem_id = sys.argv[1]
    data_file = sys.argv[2]

    # Add the problem folder to system path.
    sys.path.append(f"./problem-set/{problem_id}")

    # Load the Solution class.
    module = importlib.import_module("main")
    Solution = module.Solution
    object = Solution()

    # Get the names of methods in the Solution class in order of appearance.
    methods = []
    for name, func in Solution.__dict__.items():
        if not name.startswith("__") and inspect.isfunction(func):
            methods.append(name)
    method_name = methods[0]
    method = getattr(object, method_name)

    # Load and parse problem data.
    with open(data_file, "r") as f:
        data = json.load(f)
    
    report = data["report"]
    tests = data["tests"]

    # Run the tests, check the results and print them.
    print()
    cnt = 0
    for test in tests:
        # Run a test.
        input = test["input"]
        expected_output = test["output"]

        old_input = copy.deepcopy(input)
        old_input = ", ".join(map(str, old_input))

        output = method(*input)

        if report != "return":
            args = list(inspect.signature(method).parameters.keys())
            arg_index = args.index(report)
            output = input[arg_index]

        status = output == expected_output
        cnt += 1

        # Display the result of a test.
        if (status == True):
            status_text = Fore.GREEN + "passed" + Style.RESET_ALL
        else:
            status_text = Fore.RED + "failed" + Style.RESET_ALL

        print(f"{Fore.WHITE + "  test" + Style.RESET_ALL}: {cnt}")
        print(f"{Fore.BLUE + " input" + Style.RESET_ALL}: {old_input}")
        print(f"{Fore.BLUE + "output" + Style.RESET_ALL}: {output}")
        print(f"{Fore.YELLOW + "status" + Style.RESET_ALL}: {status_text}")
        if (status == False):
            print(f"{Fore.MAGENTA + "expect" + Style.RESET_ALL}: {expected_output}")
        print()


if __name__ == "__main__":
    run()
