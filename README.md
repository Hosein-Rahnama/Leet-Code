# Guide
This repository is an archive of Python solutions to problems from [leetcode.com][1]. It's main advantage is a local runner to test solutions on your machine. The `problem-set` directory contains subdirectories for each problem, named by its ID. Each subdirectory has two files, namely `main.py` and `data.json`. The former file contains the solution, while the latter includes the tests over which you would like to run your solution along with some settings for the runner. There may also exist a `note.md` file, which summarizes the key points learned from that problem.

In `main.py`, you should put your solution in exactly the same way the website instructs. Usually, you should define a `Solution` class and the runner considers the first method of this class as the provided solution. There are cases like problem 933, where the name of the class is different. In `data.json`, you should sepcifiy the tests in `json` format. Some problems require more setting for the runner, which should be put in the `runner` field. For example, see the data file for problems 104, 206, 283, 374, 933. To run a solution, navigate to the root `Leet-Code` directory and execute

```bash
./solve <problem-ID>
```
The modules in the `lib` directory provide data structures and APIs for solving problems. Data structures handle conversion between input data files and Python objects. APIs are used in problems such as 374, where the solution relies on calling a provided function.


# Advice
Although test verification has been automated, you should compare the output against expected results manually. Try adding your own tests. This is a valuable part of the problem solving process and is considered a good practice. Is is also beneficial to check other's solutions.

[1]: https://leetcode.com
