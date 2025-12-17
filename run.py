import sys
import inspect
import importlib
import json
import copy

from colorama import Fore, Style

from lib.LinkedList import LinkedList
from lib.BinaryTree import BinaryTree


def run():
    # Get problem ID and input file path from command line.
    problem_id = sys.argv[1]
    data_file = sys.argv[2]

    # Load modules.
    sys.path.append(f"./problem-set/{problem_id}")
    sys.path.append(f"./lib")

    # Load the class which provides the solution.
    solution = load_class()

    # Load and parse problem data.
    with open(data_file, "r") as f:
        data = json.load(f)

    # Get runner settings.    
    runner = data.get("runner", {})
    runner_type = runner.get("type", "function")
    api_options = {"name": runner.get("api.name")}
    report = runner.get("report")
    convert_options = {
        "input": runner.get("convert", {}).get("input"), 
        "output": runner.get("convert", {}).get("output")
    }

    # Get all tests.
    tests = data["tests"]

    # Run the tests, check the results and print them.
    test_num = 1
    for test in tests:
        api_options["parameter"] = test.get("api.parameter")
        input = test["input"]
        input_freeze = copy.deepcopy(input)
        expected_output = test["output"]

        input = convert_input(input, convert_options["input"])
        output = run_test(solution, input, report, api_options, runner_type)
        output = convert_output(output, convert_options["output"])
        status = output == expected_output

        show_test_result(status, test_num, input_freeze, output, expected_output, api_options)
        test_num += 1

def load_class():
    module = importlib.import_module("main")
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == "main":
            return obj

def convert_input(input, options):
    if (options is not None):
        model, args = options
        if (model == "LinkedList"):
            for i in args:
                input[i] = LinkedList(input[i]).head
        elif (model == "BinaryTree"):
            for i in args:
                input[i] = BinaryTree(input[i]).root
    return input

def convert_output(output, options):
    if (options is not None):
        model = options[0]
        if (model == "LinkedList"):
            output = LinkedList.from_head(output).values()
        elif (model == "BinaryTree"):
            output = BinaryTree.from_root(output).values()
    return output

def run_test(solution, input, report, api_options, runner_type):
    if (runner_type in ["function", None]):
        output = run_function(solution, input, report)
    elif runner_type == "model":
        output = run_model(solution, input)
    elif runner_type == "api":
        output = run_api(solution, input, report, api_options)
    else:
        raise ValueError(f"Unsupported runner type: {runner_type}")
    return output

def run_function(solution, input, report):
    # Get the first method of the Solution class.
    methods = []
    for name, func in solution.__dict__.items():
        if not name.startswith("__") and inspect.isfunction(func):
            methods.append(name)
    method_name = methods[0]
    method = getattr(solution(), method_name)

    output = method(*input)

    # Check for reporting a modified input.
    if (report is not None):
        args = list(inspect.signature(method).parameters.keys())
        j = args.index(report)
        output = input[j]

    return output

def run_model(solution, input):
    calls = input[0]
    args = input[1]
    
    # Perform the sequence of calls.
    instance = solution(*args[0])
    output = [None]
    for method_name, input in zip(calls[1:], args[1:]):
        method = getattr(instance, method_name)
        output.append(method(*input))

    return output

def run_api(solution, input, report, api_options):
    # Construct the API with the given parameters.
    module = importlib.import_module("API")
    make_api = getattr(module, f"make_{api_options["name"]}")
    api = make_api(*api_options["parameter"])

    # Inject API into the solution name space.
    module = importlib.import_module("main")
    setattr(module, api_options["name"], api)
    
    output = run_function(solution, input, report)
    
    return output

def show_test_result(status, test_num, input, output, expected_output, api_options):
    if (test_num == 1):
        print()

    input = ", ".join(map(str, input))
    if (status == True):
        status_text = Fore.GREEN + "passed" + Style.RESET_ALL
    else:
        status_text = Fore.RED + "failed" + Style.RESET_ALL

    print(f"{Fore.WHITE + "  test" + Style.RESET_ALL}: {test_num}")
    if (api_options["name"]):
        api_parameter = ", ".join(map(str, api_options["parameter"]))
        print(f"{Fore.LIGHTCYAN_EX + "   api" + Style.RESET_ALL}: {api_parameter}")
    print(f"{Fore.BLUE + " input" + Style.RESET_ALL}: {input}")
    print(f"{Fore.BLUE + "output" + Style.RESET_ALL}: {output}")
    print(f"{Fore.YELLOW + "status" + Style.RESET_ALL}: {status_text}")
    if (status == False):
        print(f"{Fore.MAGENTA + "expect" + Style.RESET_ALL}: {expected_output}")
    print()


if __name__ == "__main__":
    run()
