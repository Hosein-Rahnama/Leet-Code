import sys
import importlib
import inspect
import json
import copy


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
        output = data["output"]
        tests = data["tests"]

    # Run and print the result.
    print()
    cnt = 1
    for input in tests:
        old_input = copy.deepcopy(input)
        old_input = ", ".join(map(str, old_input))

        result = method(*input)

        print(f"  test: {cnt}")
        print(f" input: {old_input}")
        if output == "return":
            print(f"output: {result}")
        else:
            args = list(inspect.signature(method).parameters.keys())
            arg_index = args.index(output)
            print(f"output: {input[arg_index]}")
        print()
        
        cnt += 1


if __name__ == "__main__":
    run()
