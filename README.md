# Guide

This repository is an archive of Python solutions to problems from [leetcode.com][1]. It includes a local runner to test solutions on your machine. The `problem-set` folder contains subfolders for each problem, named by its ID. Each subfolder has two files, namely `main.py` and `input.txt`. The former file contains the solution, while the latter includes the inputs over which you would like to run your solution. In `main.py`, you should define a `Solution` class and the runner considers the *first* method of this class as the provided solution. To run a solution, navigate to the root `Leet-Code` directory and execute

```bash
./solve <problem-ID>
```

While test verification could be automated, this setup encourages you to manually verify the output against expected results. This is a valuable part of the problem solving process and is considered a good practice.

[1]: https://leetcode.com