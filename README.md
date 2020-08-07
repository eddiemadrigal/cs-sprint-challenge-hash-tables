# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions

Hashing functions take an input (usually a string) and return an integer as an output. To convert a string into an integer, hashing functions operate on the individual characters that make up the string.

2. Collision resolution

Collisions occur when hash functions return the same integer for different inputs.  When this occurs, chain resolution is commonly used to allow each slot to hold a reference to a collection (or chain) of items.

3. Performance of basic hash table operations

Once we take collisions into account with our hash tables, the performance implications are a bit different. There may be times when search, insertion and delete operations take linear time O(n). However, the average casae is still contant time O(1). So, if we handle collisions well and we have a hashing function that does an excellent job of spreading the data evenly across the hash table, hash tables become very performant data structures.

4. Load factor

Hash tables use an array for storage, so the load factor would be the number of occupied slots divided by the length of the array. So, an array of length of 10 with three items in it has a load factor of 0.3

5. Automatic resizing

As the load factor of the hash table increases, so does the likelihood of a collision, which reduces the performance of the hash table.  Therefore, you need to monitor the load factor and resize your hash table when the load factor gets too large.  The general rule of thumb is to resize your hash table when your load factor is greater than 0.7

6. Various use cases for hash tables

a. Digital phone book (person's name to a phone number)
b. DNS resolution (maps web address to IP address)
c. Student records (unique id maps to student information)
d. library system (a book's unique id maps to detailed book informaiton)

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

