import sys
import importlib
import inspect
import json
import copy

from colorama import Fore, Style
from lib.LinkedList import LinkedList
from lib.BinaryTree import BinaryTree


def run():
    # Get problem ID and input file path from command line.
    problem_id = sys.argv[1]
    data_file = sys.argv[2]

    # Load the Solution class.
    sys.path.append(f"./problem-set/{problem_id}")
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
    
    runner = data.get("runner", {})
    report = runner.get("report")
    convert_input = runner.get("convert", {}).get("input")
    convert_output = runner.get("convert", {}).get("output")

    tests = data["tests"]

    # Run the tests, check the results and print them.
    print()
    cnt = 0
    for test in tests:
        # Get test data.
        input = test["input"]
        expected_output = test["output"]

        old_input = copy.deepcopy(input)
        old_input = ", ".join(map(str, old_input))

        # Convert specific inputs into python objects.
        if (convert_input is not None):
            flag, args = convert_input
            if (flag == "LinkedList"):
                for i in args:
                    input[i] = LinkedList(input[i]).head
            elif (flag == "BinaryTree"):
                for i in args:
                    input[i] = BinaryTree(input[i]).root

        # Run a test.
        output = method(*input)

        # Check for reporting a modified input.
        if (report is not None):
            args = list(inspect.signature(method).parameters.keys())
            j = args.index(report)
            output = input[j]

        # Convert specific outputs.
        if (convert_output is not None):
            if (flag == "LinkedList"):
                output = LinkedList.from_head(output).values()
            elif (flag == "BinaryTree"):
                output = BinaryTree.from_root(output).values()

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
