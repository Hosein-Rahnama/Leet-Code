# Guide

This repository is an archive of Python solutions to problems from [leetcode.com][1]. It includes a local runner to test solutions on your machine. The `problem-set` folder contains subfolders for each problem, named by its ID. Each subfolder has two files, namely `main.py` and `data.json`. The former file contains the solution, while the latter includes the tests over which you would like to run your solution. In `main.py`, you should define a `Solution` class and the runner considers the first method of this class as the provided solution. In `data.json`, you should sepcifiy the tests in `json` format. If your solution does not return any result and modifies an input in-place, the name of that input should be mentioned in the `data.json` via the `report` field. On the other hand, if your solution returns a result, the `report` field should be set to `return`. To run a solution, navigate to the root `Leet-Code` directory and execute

```bash
./solve <problem-ID>
```

 Although test verification has been automated, you should compare the output against expected results manually. Try adding your own tests. This is a valuable part of the problem solving process and is considered a good practice.

[1]: https://leetcode.com
