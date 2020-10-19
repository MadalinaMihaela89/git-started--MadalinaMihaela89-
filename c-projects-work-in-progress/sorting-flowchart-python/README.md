# Sorting flowchart

## Story

In computer science, there is a recurring problem, which is how to sort a list of
numbers. Your friend Maria has found a flowchart about one of the sorting
algorithms, and she asks you to help her to write the equivalent python script.
This is a simple sorting algorithm that repeatedly steps through the list,
compares each pair of adjacent items and swaps them if they are in the wrong order.

## What are you going to learn?

You will learn and practice how to do the following things:

- write code from flowchart,
- how to sort numbers without built-in functions,
- clean code refactoring (making code more easy to read and maintain
  without changing any feature).

## Tasks

1. Implement the algorithm described by [this flowchart](https://learn.code.cool/media/progbasics/sorting-assignment.png) in Python.
    - Running the program outputs the following numbers in a list: [1, 2, 56, 32, 51, 2, 8, 92, 15]
    - Running the program outputs the above numbers in a list in ascending order without hard coding the order (using the steps seen in the flowchart): [1, 2, 2, 8, 15, 32, 51, 56, 92]

2. Refactor your solution: use functions, make it more easy to read and maintain.
    - Running the program results in the exact same behavior before and after refactoring.
    - Variable names in the program are meaningful nouns and not abbreviated
    - Function names in the program are meaningful verbs and not abbreviated
    - There are no unnecessary (dead) code or comments in the program
    - There are no duplicating code parts or code parts doing the same thing differently in the program
    - There are no function that doing more than one thing in the program
    - After each modification the changes are committed, the program is runnable and results in the exact same behavior than at the beginning
    - Commit messages are meaningful

## General requirements

None

## Hints

- There are two loops and both of them can be implemented with `while` or `for`
  (but think about which is better when).
- One loop is an outer loop and one is an inner loop. Do you know which one is which?

- While refactoring make sure you protect the main part of the program
  (outside of the functions) with an `if __name__ == "__main__":`
  [code snippet](https://docs.python.org/3/library/__main__.html).

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/solo/blueprint/sorting-flowchart/python).

## Background materials

- <i class="far fa-exclamation"></i> [About Flowcharts](https://learn.code.cool/full-stack/#/../pages/general/flowcharts)
- <i class="far fa-exclamation"></i> [Basics of clean code](https://learn.code.cool/full-stack/#/../pages/general/clean-code)
- <i class="far fa-exclamation"></i> [Refactoring in action](https://learn.code.cool/full-stack/#/../pages/general/refactoring-in-action)
- <i class="far fa-exclamation"></i> About [nice commit messages](https://chris.beams.io/posts/git-commit/)
- <i class="far fa-video"></i> [Bubble-sort with Hungarian ("Csángó") folk dance](https://www.youtube.com/watch?v=lyZQPjUT5B4)

- <i class="far fa-exclamation"></i> [What is `if __name__ == "__main__"`??](https://thepythonguru.com/what-is-if-__name__-__main__/)
