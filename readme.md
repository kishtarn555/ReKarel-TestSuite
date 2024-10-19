This is a test suite containing multiples cases and codes which a proper compiler and VM must be able to correctly compile and run


# Problems

This directory contain multiple problems and solutions that ReKarel must solve correctly.

* `solution.kj`: A code that solves all the cases in ReKarel Java
* `solution.kp`: A code that solves all the cases in ReKarel Pascal
* `cases`: This directory contains the test cases
  * `[case].in` This is the input world of the test case
  * `[case].out` This is the expected output of the test case

All programs in this folder must end without error.

# rte

All codes compile correctly, but when running they produce different errors that the VM must detect

* `code.kcode`: The code that is run on the cases.
* `cases`: This directory contains the test cases
  * `[case].in` This is the input world of the test case
  * `[case].out` This is the expected output of the test case
  * `[case].stderr` The expected standard error of the VM.
  * `[case].signal` The expected exit signal of the VM.
  