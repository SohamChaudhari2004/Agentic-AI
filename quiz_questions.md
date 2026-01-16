# Capgemini Interactive Mock Test - Questions

This document contains all questions from the Capgemini Interactive Mock Test, organized by category.

## Table of Contents

- [Pseudo Code Questions](#pseudo-code-questions)
- [IT Fundamentals Questions](#it-fundamentals-questions)

---

## Pseudo Code Questions

### Question 1

**What is the output of the following pseudocode?**

```
Integer x = 10, y = 2
while (x > y)
  print "In loop"
  x = x - 3
End While
```

**Options:**

- A) In loop In loop In loop
- B) In loop In loop
- C) In loop
- D) Infinite Loop

**Answer:** A) In loop In loop In loop

---

### Question 2

**What will be the value of `sum` after the loop?**

```
Integer n = 5, sum = 0, i = 1
while (i <= n)
  sum = sum + i
  i = i + 2
End While
```

**Options:**

- A) 15
- B) 9
- C) 6
- D) 10

**Answer:** B) 9

---

### Question 3

**What does the following function return for `n = 4`?**

```
Function factorial(Integer n)
  if (n == 0)
    return 1
  else
    return n * factorial(n - 1)
  End If
End Function
```

**Options:**

- A) 24
- B) 12
- C) 4
- D) 0

**Answer:** A) 24

---

### Question 4

**How many times will "Hello" be printed?**

```
Integer i, j
for (i = 1 to 3)
  for (j = 1 to i)
    print "Hello"
  End For
End For
```

**Options:**

- A) 9
- B) 6
- C) 3
- D) 5

**Answer:** B) 6

---

### Question 5

**What is the final value of `x`?**

```
Integer x = 4
x = x << 2
```

**Options:**

- A) 8
- B) 4
- C) 16
- D) 1

**Answer:** C) 16

---

### Question 6

**What is the output for `a = 15, b = 4`?**

```
Integer a = 15, b = 4
a = a mod (a - 10)
print a
```

**Options:**

- A) 0
- B) 3
- C) 5
- D) 15

**Answer:** A) 0

---

### Question 7

**What will be printed?**

```
Integer arr[] = {10, 20, 30, 40}
Integer p = &arr[1]
Integer q = &arr[3]
print q - p
```

**Options:**

- A) 2
- B) 20
- C) 8
- D) Error

**Answer:** A) 2

---

### Question 8

**What is the value of `result`?**

```
Integer a = 5, b = 10
Integer result = (a > b) ? a : b
print result
```

**Options:**

- A) 5
- B) 10
- C) 0
- D) 15

**Answer:** B) 10

---

### Question 9

**What is the output of this code?**

```
Integer n = 123
Integer sum = 0
while (n > 0)
  sum = sum + (n % 10)
  n = n / 10
End While
print sum
```

**Options:**

- A) 123
- B) 6
- C) 321
- D) 0

**Answer:** B) 6

---

### Question 10

**What does the function return for `fun(4, 3)`?**

```
Function fun(Integer a, Integer b)
  if (b == 0)
    return 1
  End If
  return a * fun(a, b - 1)
End Function
```

**Options:**

- A) 64
- B) 12
- C) 81
- D) 7

**Answer:** A) 64

---

### Question 11

**What is the value of `x` after this code executes?**

```
Integer x = 10
if (x > 5 AND x < 15)
  x = x + 2
else
  x = x - 2
End If
```

**Options:**

- A) 10
- B) 12
- C) 8
- D) 15

**Answer:** B) 12

---

### Question 12

**What will be the output?**

```
Integer a = 5, b = 3, c = 2
c = a & b
print c
```

**Options:**

- A) 1
- B) 3
- C) 5
- D) 7

**Answer:** A) 1

---

### Question 13

**What is the output of the following pseudocode?**

```
Integer i = 0
do
  print i
  i = i + 1
while (i < 0)
```

**Options:**

- A) 1
- B) 0
- C) No output
- D) Infinite loop

**Answer:** B) 0

---

### Question 14

**What is the output of the function for `n = 5`?**

```
Function solve(Integer n)
  if (n <= 1)
    return n
  End If
  return solve(n-1) + solve(n-2)
End Function
```

**Options:**

- A) 3
- B) 5
- C) 8
- D) 4

**Answer:** B) 5

---

### Question 15

**What will be the final value of `count`?**

```
Integer count = 0, i
for (i = 0; i < 5; i = i + 1)
  if (i == 3)
    continue
  End If
  count = count + 1
End For
```

**Options:**

- A) 5
- B) 4
- C) 3
- D) 2

**Answer:** B) 4

---

### Question 16

**What is the output?**

```
Integer x = 3
x = x >> 1
print x
```

**Options:**

- A) 1
- B) 2
- C) 6
- D) 0

**Answer:** A) 1

---

### Question 17

**How many times does the inner loop execute in total?**

```
Integer i, j, count = 0
for (i = 1 to 4)
  for (j = 1 to 4)
    count = count + 1
  End For
End For
```

**Options:**

- A) 4
- B) 8
- C) 16
- D) 20

**Answer:** C) 16

---

### Question 18

**What is the value of `c`?**

```
Integer a = 6, b = 4
Integer c = a | b
print c
```

**Options:**

- A) 2
- B) 4
- C) 6
- D) 7

**Answer:** D) 7

---

### Question 19

**What will be printed?**

```
String str = "Hello"
print length(str)
```

**Options:**

- A) 4
- B) 5
- C) 6
- D) Error

**Answer:** B) 5

---

### Question 20

**What is the output of this loop?**

```
Integer i = 1
while (i < 10)
  print i
  i = i * 2
End While
```

**Options:**

- A) 1 2 4 8
- B) 1 2 3 4 5 6 7 8 9
- C) 2 4 8 16
- D) 1 2 4 8 16

**Answer:** A) 1 2 4 8

---

### Question 21

**What will the array `arr` contain after execution?**

```
Integer arr[] = {1, 2, 3, 4, 5}
Integer i
for (i = 0 to 4)
  arr[i] = arr[i] * 2
End For
```

**Options:**

- A) {1, 2, 3, 4, 5}
- B) {2, 4, 6, 8, 10}
- C) {2, 3, 4, 5, 6}
- D) {0, 2, 4, 6, 8}

**Answer:** B) {2, 4, 6, 8, 10}

---

### Question 22

**What is the output for `a = 10, b = 20`?**

```
Procedure swap(Integer ref x, Integer ref y)
  Integer temp = x
  x = y
  y = temp
End Procedure

Integer a = 10, b = 20
swap(a, b)
print a, b
```

**Options:**

- A) 10, 20
- B) 20, 10
- C) 10, 10
- D) 20, 20

**Answer:** B) 20, 10

---

### Question 23

**What will be printed?**

```
Integer x = 5
switch (x)
  case 1: print "One"
  case 5: print "Five"
  case 10: print "Ten"
  default: print "Other"
End Switch
```

**Options:**

- A) One
- B) Five
- C) Ten
- D) Other

**Answer:** B) Five

---

### Question 24

**What is the value of `max`?**

```
Integer arr[] = {10, 50, 20, 80, 30}
Integer max = arr[0], i
for (i = 1 to 4)
  if (arr[i] > max)
    max = arr[i]
  End If
End For
print max
```

**Options:**

- A) 10
- B) 30
- C) 50
- D) 80

**Answer:** D) 80

---

### Question 25

**What does this recursive function do for input `str = "world"`?**

```
Function reverse(String str)
  if (length(str) == 0)
    return ""
  End If
  return reverse(substring(str, 1)) + characterAt(str, 0)
End Function
```

**Options:**

- A) Returns "world"
- B) Returns "dlrow"
- C) Causes an infinite loop
- D) Returns "d"

**Answer:** B) Returns "dlrow"

---

### Question 26

**What is the output for `x = 7`?**

```
Integer x = 7
if (x % 2 == 0)
  print "Even"
else
  print "Odd"
End If
```

**Options:**

- A) Even
- B) Odd
- C) 7
- D) Error

**Answer:** B) Odd

---

### Question 27

**What are the final values of `p` and `q`?**

```
Integer p = 10, q = 5
p = p + q
q = p - q
p = p - q
print p, q
```

**Options:**

- A) 10, 5
- B) 5, 10
- C) 15, 10
- D) 15, 5

**Answer:** B) 5, 10

---

### Question 28

**What will the code print for `n = 13`?**

```
Function isPrime(Integer n)
  Integer i
  for (i = 2 to n/2)
    if (n % i == 0)
      return false
    End If
  End For
  return true
End Function

print isPrime(13)
```

**Options:**

- A) true
- B) false
- C) 13
- D) 1

**Answer:** A) true

---

### Question 29

**What is the output?**

```
Integer x = 1, y = 1
if ( !(x == 1 AND y == 0) )
  print "True"
else
  print "False"
End If
```

**Options:**

- A) True
- B) False
- C) No output
- D) Error

**Answer:** A) True

---

### Question 30

**What does the function return for `gcd(48, 18)`?**

```
Function gcd(Integer a, Integer b)
  if (b == 0)
    return a
  End If
  return gcd(b, a % b)
End Function
```

**Options:**

- A) 2
- B) 3
- C) 6
- D) 9

**Answer:** C) 6

---

### Question 31

**What is the value of `sum`?**

```
Integer arr[] = {1, 2, 3, 4}
Integer sum = 0, i
for (i = 0 to 3)
  sum = sum + arr[i]
End For
print sum
```

**Options:**

- A) 4
- B) 6
- C) 10
- D) 24

**Answer:** C) 10

---

### Question 32

**What will be the final value of `count`?**

```
Integer i = 5, count = 0
while (i > 0)
  count = count + 1
  if (i == 3)
    break
  End If
  i = i - 1
End While
```

**Options:**

- A) 3
- B) 5
- C) 2
- D) 1

**Answer:** A) 3

---

### Question 33

**What is the output of the following code?**

```
Integer x = 2
Integer y = 5
Integer z = x ^ y
print z
```

**Options:**

- A) 7
- B) 3
- C) 10
- D) 32

**Answer:** A) 7

---

### Question 34

**What is the output?**

```
String s1 = "Cap"
String s2 = "gemini"
String result = s1 + s2
print result
```

**Options:**

- A) Cap gemini
- B) Capgemini
- C) geminiCap
- D) Error

**Answer:** B) Capgemini

---

### Question 35

**What is printed for `grade = 85`?**

```
Integer grade = 85
if (grade >= 90)
  print "A"
else if (grade >= 80)
  print "B"
else if (grade >= 70)
  print "C"
else
  print "F"
End If
```

**Options:**

- A) A
- B) B
- C) C
- D) F

**Answer:** B) B

---

### Question 36

**What is the value of `result`?**

```
Integer a = 10, b = 4
Real result = a / b
print result
```

**Options:**

- A) 2
- B) 2.5
- C) 3
- D) Error

**Answer:** B) 2.5

---

### Question 37

**What is the value of `min`?**

```
Integer arr[] = {30, 15, 40, 5, 25}
Integer min = arr[0], i
for (i = 1 to 4)
  if (arr[i] < min)
    min = arr[i]
  End If
End For
print min
```

**Options:**

- A) 30
- B) 15
- C) 5
- D) 25

**Answer:** C) 5

---

### Question 38

**What is the output of `fun(3)`?**

```
Function fun(Integer n)
  if (n <= 0)
    return
  End If
  print n
  fun(n - 1)
  print n
End Function
```

**Options:**

- A) 3 2 1 1 2 3
- B) 3 2 1
- C) 1 2 3 3 2 1
- D) 3 3 2 2 1 1

**Answer:** A) 3 2 1 1 2 3

---

### Question 39

**What does this code print?**

```
Integer x = 5
while (x > 5)
  print "Looping"
End While
print "Done"
```

**Options:**

- A) Looping
- B) Done
- C) Looping Done
- D) Infinite Loop

**Answer:** B) Done

---

### Question 40

**What is the ASCII value of 'A' printed as an integer?**

```
Character ch = 'A'
print (Integer)ch
```

**Options:**

- A) 1
- B) 97
- C) 65
- D) 0

**Answer:** C) 65

---

### Question 41

**What will be printed?**

```
Integer i
for (i = 0; i < 10; i = i + 3)
  print i
End For
```

**Options:**

- A) 0 3 6 9
- B) 0 1 2 3 4 5 6 7 8 9
- C) 3 6 9 12
- D) 0 3 6

**Answer:** A) 0 3 6 9

---

### Question 42

**What is the output for `x = 10` after the procedure call?**

```
Procedure modify(Integer val)
  val = val + 5
End Procedure

Integer x = 10
modify(x)
print x
```

**Options:**

- A) 10
- B) 15
- C) 5
- D) Error

**Answer:** A) 10

---

### Question 43

**What is the state of a queue after these operations: `enqueue(5)`, `enqueue(10)`, `dequeue()`, `enqueue(15)`?**

**Options:**

- A) 5, 15
- B) 10, 15
- C) 5, 10
- D) 15, 10

**Answer:** B) 10, 15

---

### Question 44

**What is the state of a stack after these operations: `push(5)`, `push(10)`, `pop()`, `push(15)`?**

**Options:**

- A) 5, 15
- B) 15, 5
- C) 10, 15
- D) 15, 10

**Answer:** A) 5, 15

---

### Question 45

**What is the value of `x`?**

```
Integer x = 5
x = ~x
```

**Options:**

- A) -5
- B) 5
- C) -6
- D) 4

**Answer:** C) -6

---

### Question 46

**What is the output?**

```
Integer x = 5, y = 10, z = 15
if (x > y OR z > y AND x < z)
  print "True"
else
  print "False"
End If
```

**Options:**

- A) True
- B) False
- C) Error
- D) No Output

**Answer:** A) True

---

### Question 47

**What is the sum of the diagonal elements of this 2D array?**

```
Integer matrix[2][2] = {{1, 2}, {3, 4}}
Integer sum = 0, i
for (i = 0 to 1)
  sum = sum + matrix[i][i]
End For
print sum
```

**Options:**

- A) 3
- B) 5
- C) 7
- D) 10

**Answer:** B) 5

---

### Question 48

**What does the function return for `power(2, 4)`?**

```
Function power(Integer base, Integer exp)
  if (exp == 0)
    return 1
  End If
  return base * power(base, exp - 1)
End Function
```

**Options:**

- A) 8
- B) 16
- C) 6
- D) 2

**Answer:** B) 16

---

### Question 49

**What will be printed?**

```
Integer a = 2, b = 3
print "a + b"
```

**Options:**

- A) 5
- B) a + b
- C) 2 + 3
- D) Error

**Answer:** B) a + b

---

### Question 50

**How many times is the condition `x < 10` checked?**

```
Integer x = 0
while (x < 10)
  x = x + 1
End While
```

**Options:**

- A) 9
- B) 10
- C) 11
- D) 0

**Answer:** C) 11

---

## IT Fundamentals Questions

### Question 1

**Which of the following is not an OOP concept?**

**Options:**

- A) Encapsulation
- B) Polymorphism
- C) Inheritance
- D) Compilation

**Answer:** D) Compilation

---

### Question 2

**What is the time complexity of a binary search algorithm?**

**Options:**

- A) O(n)
- B) O(log n)
- C) O(n^2)
- D) O(1)

**Answer:** B) O(log n)

---

### Question 3

**Which data structure uses LIFO (Last-In, First-Out)?**

**Options:**

- A) Queue
- B) Stack
- C) Linked List
- D) Tree

**Answer:** B) Stack

---

### Question 4

**In SQL, which command is used to select data from a database?**

**Options:**

- A) GET
- B) SELECT
- C) OPEN
- D) EXTRACT

**Answer:** B) SELECT

---

### Question 5

**Which layer of the OSI model is responsible for routing?**

**Options:**

- A) Physical Layer
- B) Data Link Layer
- C) Network Layer
- D) Transport Layer

**Answer:** C) Network Layer

---

### Question 6

**What does ACID stand for in database transactions?**

**Options:**

- A) Atomicity, Consistency, Isolation, Durability
- B) Atomicity, Concurrency, Integrity, Durability
- C) Availability, Consistency, Isolation, Durability
- D) Atomicity, Consistency, Integrity, Data

**Answer:** A) Atomicity, Consistency, Isolation, Durability

---

### Question 7

**Which of these is a non-linear data structure?**

**Options:**

- A) Array
- B) Stack
- C) Queue
- D) Tree

**Answer:** D) Tree

---

### Question 8

**What is the purpose of the `finally` block in exception handling?**

**Options:**

- A) It executes only when an exception occurs.
- B) It always executes whether an exception occurs or not.
- C) It is a block where exceptions are declared.
- D) It executes only when an exception does not occur.

**Answer:** B) It always executes whether an exception occurs or not.

---

### Question 9

**Which sorting algorithm has the worst-case time complexity of O(n^2)?**

**Options:**

- A) Merge Sort
- B) Quick Sort
- C) Heap Sort
- D) Bubble Sort

**Answer:** D) Bubble Sort

---

### Question 10

**What is a primary key in a database?**

**Options:**

- A) A key that can have NULL values.
- B) A key that uniquely identifies each record in a table.
- C) A key that is a foreign key in another table.
- D) A key used for sorting data only.

**Answer:** B) A key that uniquely identifies each record in a table.

---

### Question 11

**What is the main function of an Operating System?**

**Options:**

- A) Word Processing
- B) Database Management
- C) Resource Management
- D) Web Browsing

**Answer:** C) Resource Management

---

### Question 12

**Which protocol is used to send email?**

**Options:**

- A) FTP
- B) SMTP
- C) HTTP
- D) POP3

**Answer:** B) SMTP

---

### Question 13

**What does DNS stand for?**

**Options:**

- A) Domain Name System
- B) Dynamic Name System
- C) Domain Network Service
- D) Dynamic Network Service

**Answer:** A) Domain Name System

---

### Question 14

**Which of the following is an interpreted language?**

**Options:**

- A) C++
- B) Java
- C) C
- D) Python

**Answer:** D) Python

---

### Question 15

**The process of converting source code into machine code is called?**

**Options:**

- A) Execution
- B) Compilation
- C) Interpretation
- D) Debugging

**Answer:** B) Compilation

---

### Question 16

**In database normalization, what is 1NF?**

**Options:**

- A) No repeating groups
- B) All non-key attributes are fully functional on the primary key
- C) No transitive dependencies
- D) All attributes must be numeric

**Answer:** A) No repeating groups

---

### Question 17

**What is the difference between a process and a thread?**

**Options:**

- A) Processes share memory, threads do not
- B) Threads are heavyweight, processes are lightweight
- C) A process can have multiple threads
- D) Threads have their own separate memory space

**Answer:** C) A process can have multiple threads

---

### Question 18

**Which of the following is a cloud computing service model?**

**Options:**

- A) HTTP
- B) SaaS
- C) FTP
- D) TCP/IP

**Answer:** B) SaaS

---

### Question 19

**What does SQL stand for?**

**Options:**

- A) Structured Query Language
- B) Simple Query Language
- C) Standardized Query Language
- D) Sequential Query Language

**Answer:** A) Structured Query Language

---

### Question 20

**Which data structure is best for implementing a priority queue?**

**Options:**

- A) Stack
- B) Linked List
- C) Heap
- D) Array

**Answer:** C) Heap

---

### Question 21

**What type of software is Git?**

**Options:**

- A) A database
- B) An operating system
- C) A version control system
- D) A web server

**Answer:** C) A version control system

---

### Question 22

**What is method overriding?**

**Options:**

- A) Two methods with the same name but different parameters in the same class
- B) A subclass providing a specific implementation for a method defined in its superclass
- C) A method that cannot be called
- D) A method that calls itself

**Answer:** B) A subclass providing a specific implementation for a method defined in its superclass

---

### Question 23

**Which of these is NOT a valid IPv4 address?**

**Options:**

- A) 192.168.1.1
- B) 255.255.255.0
- C) 10.0.0.256
- D) 172.16.0.1

**Answer:** C) 10.0.0.256

---

### Question 24

**What is the purpose of an index in a database?**

**Options:**

- A) To enforce uniqueness
- B) To speed up data retrieval
- C) To create relationships between tables
- D) To store large binary data

**Answer:** B) To speed up data retrieval

---

### Question 25

**Which software development model is iterative?**

**Options:**

- A) Waterfall
- B) V-Model
- C) Agile
- D) Big Bang

**Answer:** C) Agile

---

### Question 26

**What is a deadlock in an operating system?**

**Options:**

- A) A situation where two or more processes are waiting for each other to release a resource
- B) When a process uses too much memory
- C) When the CPU is idle
- D) When a process terminates unexpectedly

**Answer:** A) A situation where two or more processes are waiting for each other to release a resource

---

### Question 27

**Which layer of the TCP/IP model corresponds to the OSI model's Network layer?**

**Options:**

- A) Application
- B) Transport
- C) Internet
- D) Network Interface

**Answer:** C) Internet

---

### Question 28

**What is a Foreign Key?**

**Options:**

- A) A key that uniquely identifies a record in any table
- B) A key in one table that refers to the Primary Key in another table
- C) A key that is not unique
- D) A key used for encrypting data

**Answer:** B) A key in one table that refers to the Primary Key in another table

---

### Question 29

**The concept of hiding implementation details and showing only functionality is known as:**

**Options:**

- A) Inheritance
- B) Polymorphism
- C) Abstraction
- D) Encapsulation

**Answer:** C) Abstraction

---

### Question 30

**What is a MAC address?**

**Options:**

- A) A logical address for a network
- B) A physical address assigned to a network interface card (NIC)
- C) The address of a web server
- D) An address used for email

**Answer:** B) A physical address assigned to a network interface card (NIC)

---

### Question 31

**What is polymorphism?**

**Options:**

- A) The ability of an object to take on many forms
- B) The process of hiding data
- C) The process of creating a new class from an existing class
- D) A single function with the same name for different types

**Answer:** A) The ability of an object to take on many forms

---

### Question 32

**What is a key difference between TCP and UDP?**

**Options:**

- A) TCP is connectionless, UDP is connection-oriented
- B) TCP guarantees delivery, UDP does not
- C) TCP is faster than UDP
- D) TCP is used for video streaming, UDP for file transfers

**Answer:** B) TCP guarantees delivery, UDP does not

---

### Question 33

**What is an API?**

**Options:**

- A) An application that runs on a server
- B) A set of rules that allow applications to communicate with each other
- C) A type of database
- D) A programming language

**Answer:** B) A set of rules that allow applications to communicate with each other

---

### Question 34

**What is the main function of a compiler?**

**Options:**

- A) To run a program line by line
- B) To translate the entire source code into machine code at once
- C) To find and fix bugs in the code
- D) To manage system memory

**Answer:** B) To translate the entire source code into machine code at once

---

### Question 35

**What is virtual memory?**

**Options:**

- A) A part of the hard disk used as an extension of RAM
- B) Memory that does not physically exist
- C) The memory used by virtual machines
- D) A type of very fast memory

**Answer:** A) A part of the hard disk used as an extension of RAM

---

### Question 36

**In SQL, which statement removes all rows from a table without logging the individual row deletions?**

**Options:**

- A) DELETE
- B) DROP
- C) TRUNCATE
- D) REMOVE

**Answer:** C) TRUNCATE

---

### Question 37

**What is a firewall?**

**Options:**

- A) A software that detects and removes viruses
- B) A network security system that monitors and controls incoming and outgoing network traffic
- C) A device to connect multiple computers in a network
- D) A type of computer virus

**Answer:** B) A network security system that monitors and controls incoming and outgoing network traffic

---

### Question 38

**What is Big O notation used for?**

**Options:**

- A) To describe the performance or complexity of an algorithm
- B) To calculate the exact running time of a program
- C) To measure the size of a program
- D) To notate object-oriented code

**Answer:** A) To describe the performance or complexity of an algorithm

---

### Question 39

**What is an abstract class?**

**Options:**

- A) A class that cannot be instantiated
- B) A class with no methods
- C) A class that has only private members
- D) A class that exists only in theory

**Answer:** A) A class that cannot be instantiated

---

### Question 40

**What is the main difference between HTTP and HTTPS?**

**Options:**

- A) HTTPS is faster than HTTP
- B) HTTP is used for video, HTTPS for text
- C) HTTPS encrypts data, while HTTP sends it in plain text
- D) There is no difference

**Answer:** C) HTTPS encrypts data, while HTTP sends it in plain text

---

### Question 41

**What is Garbage Collection in programming?**

**Options:**

- A) Manually deleting unused variables
- B) A form of automatic memory management
- C) A process to clean the computer's hard drive
- D) A tool for removing syntax errors

**Answer:** B) A form of automatic memory management

---

### Question 42

**What is the primary role of a router in a network?**

**Options:**

- A) To connect devices within the same local network
- B) To filter network traffic based on MAC addresses
- C) To forward data packets between different computer networks
- D) To convert digital signals to analog signals

**Answer:** C) To forward data packets between different computer networks

---

### Question 43

**What is a constructor in object-oriented programming?**

**Options:**

- A) A method to destroy an object
- B) A special method for creating and initializing an object
- C) A regular method that can be called on an object
- D) A method to copy an object

**Answer:** B) A special method for creating and initializing an object

---

### Question 44

**What does SDLC stand for?**

**Options:**

- A) Software Development Life Cycle
- B) System Design Life Cycle
- C) Software Design Logic Course
- D) System Development Logic Circuit

**Answer:** A) Software Development Life Cycle

---

### Question 45

**What is the difference between static and dynamic typing?**

**Options:**

- A) Static typing is checked at compile-time, dynamic is at run-time
- B) Dynamic typing is faster than static typing
- C) Static typing is used in Python, dynamic in C++
- D) There is no difference

**Answer:** A) Static typing is checked at compile-time, dynamic is at run-time

---

### Question 46

**What is caching?**

**Options:**

- A) Encrypting data for security
- B) Storing copies of files or data in a temporary storage location so they can be accessed more quickly
- C) Compressing data to save space
- D) Deleting old files from a system

**Answer:** B) Storing copies of files or data in a temporary storage location so they can be accessed more quickly

---

### Question 47

**What is an interface in OOP?**

**Options:**

- A) A user interface for an application
- B) A class that contains only concrete methods
- C) An abstract type that is used to specify a behavior that classes must implement
- D) A way to connect two different computer systems

**Answer:** C) An abstract type that is used to specify a behavior that classes must implement

---

### Question 48

**What is the purpose of the `this` keyword in many programming languages?**

**Options:**

- A) To refer to the superclass of the current object
- B) To refer to the current instance of the class
- C) To create a new object
- D) To destroy the current object

**Answer:** B) To refer to the current instance of the class

---

### Question 49

**What is a subnet mask?**

**Options:**

- A) An address that hides the identity of a computer
- B) A password for a network
- C) A 32-bit number that separates an IP address into network and host portions
- D) A security feature of a firewall

**Answer:** C) A 32-bit number that separates an IP address into network and host portions

---

### Question 50

**What is multithreading?**

**Options:**

- A) Running multiple processes at the same time
- B) A technique that allows a CPU to execute multiple threads of execution concurrently within a single process
- C) Having multiple users on the same computer
- D) Connecting to multiple networks at once

**Answer:** B) A technique that allows a CPU to execute multiple threads of execution concurrently within a single process

---

## Summary

**Total Questions:** 100

- **Pseudo Code Questions:** 50
- **IT Fundamentals Questions:** 50

This comprehensive question bank covers essential topics for the Capgemini assessment, including:

### Pseudo Code Topics:

- Loops and iterations
- Conditional statements
- Functions and recursion
- Arrays and data manipulation
- Bitwise operations
- String operations
- Mathematical calculations
- Algorithm logic

### IT Fundamentals Topics:

- Object-Oriented Programming
- Data Structures and Algorithms
- Database Management
- Computer Networks
- Operating Systems
- Programming Languages
- Software Engineering
- System Design
- Web Technologies
- Security Concepts

---

_Good luck with your preparation!_
