
# Activity 8: Testing Function Output

In this activity, we will walk through how to create a series of tests to verify whether or not our functions work properly!

When you've completed the guided part of this activity, be sure to also complete the [Extension Activity](#extension-activity-test-your-own-functions)!

## 1. Installing PyTest

This is the first time we are using the `pip` installer! `pip` is a package manager for Python that allows you to install libraries to your device with a single line of code. Throughout this course, we will install many packages together, and there might even be some packages you install on your own for projects!

To use `pip` you just run a simple command in your terminal to install the specific package you want. Most packages have a copy-paste line on their main website or GitHub repo. For PyTest, the following line can be run in your terminal.

```powershell
pip install -U pytest
```

To verify your installation, run the following. It should display the current version number. 

```powershell
pytest --version
```

*At the time of writing this document, the current version number is `9.0.3` but if your version number is higher, that's okay.*

## 2. Create a Root Folder

Whenever you are creating a new Python project, it is best to stay organized by placing all the files related to the project in the same folder. Create a `root` folder.

Inside the folder, create a new `extension.py` file.

## 3. Creating Input - Output Functions For Testing

In `extension.py` we will create some simple functions that accept parameters and return some kind of output. PyTest works by allowing you to run a function, and compare expected results with actual results. A simple starting example might be a function that doubles a number:

```python
def double_integer(a: int) -> int:
    """Double an integer.
    
    :param a: The value to double.
    :return: The doubled value.
    """
    double = a * 2
    return double
```

*Note that this function is using a docstring to explain what it does!*

This function makes it really easy to create tests because we will know exactly what the output should be!

We will create one more function as well to help us see some other PyTest functionality. Our next function will just add two numbers together:

```python
def add(a: float, b: float) -> float:
    """Adds two numbers together
    
    :param a: First number to add.
    :param b: Second number to add.
    :return: Sum of two numbers.
    """
    total = a + b
    return total
```

*Note that this function is using a docstring to explain what it does!*

## 4. Creating Tests

With some functions to test, it's time to actually create our tests! There are some important things that you will **always** need to ensure to make sure your tests run as expected.

1. Import PyTest
2. Name tests properly
3. Include **assertions**

### Importing PyTest

At the top of your program, import PyTest:

```python
import pytest
```

### Naming Tests Properly

For PyTest to be able to successfully detect tests, your test functions all need to be named starting with `test_`. If you do not name your tests properly, PyTest will assume they are just regular functions and not run them. Later on, we will talk about effective tests to create, but for now we will run a basic test on each.

For our `double_integer()` function, the following test can be added. Right now, we are just using `pass` as a placeholder and will add the contents afterward.

```python
def test_double_integer():
    pass
```

For our `add()` function, the following test can be added.

```python
def test_add():
    pass
```

### Including Assertions

| Assertion                                                                                                  |
|:-----------------------------------------------------------------------------------------------------------|
| *A statement that checks whether a condition is true and causes a test to fail if the condition is false.* |

Assertions are the secret sauce that make PyTest work. With PyTest, assertions are a special type of conditional statement that not only evaluates to `True` or `False`, but is able to translate that into a `Pass` or `Fail` for a test. If the assertion is `True`, the test passes. If the assertion is `False`, the test fails.

To include an assertion, we use the `assert` keyword, followed by the condition to check. 

Before even running tests on our functions, we can assert if two values are equal on a single test like this, where we are *asserting* that `1` is in fact equal to `1`:

```python
def test_pass():
    assert 1 == 1
```

Likewise, we can make a `False` assertion and see what happens:

```python
def test_fail():
    assert False
```

We won't run those tests yet, but we will add them to our file so that we now have 4 tests to run! We will also update our other two test functions with assertions:

This test *should* pass because `4` *should* equal double `2`.

```python
def test_double_integer():
    assert 4 == double_integer(2)
```

This test *should* pass because `0.1` added to `0.2` *should* equal `0.3`.

```python
def test_add():
    assert 0.3 == add(0.1, 0.2)
```

## 5. Running Tests

You might notice in your IDE that some play buttons pop up next to your test functions! These buttons are a *lie*! Your IDE is trying to run its own unit tests, which work different from PyTest. To run PyTest we need to do so from the terminal with the command `pytest filepath`. 

If you've followed all of the steps so far, you will need to open your projects root folder in the terminal. This can be done by right-clicking the folder in your IDE and selecting `Open in..` > `Terminal`:

![Opening in the terminal](./opening_in_terminal.gif)

**Tip:** This **WILL NOT WORK** if you do not open the correct folder first!

Once you are in the correct root folder, the following terminal command will run your test functions:

```powershell
pytest main.py
```

When the command runs, it might look like you are getting errors, but the error message look very different from the ones we learned about in Lesson 7. Instead, any errors you *should* be seeing are `AssertionError`s, which display when a test fails.

Before running the tests, we expected 3 tests to pass and 1 to fail. But our results show something different so lets take a closer look at what we are seeing! Below is a breakdown of what you should see in your terminal when running the PyTest command.

At the top we have this big banner to signify the start of our tests and verify our version of PyCharm:

![test banner](./test-banner.png)

Below that, we have information about how many tests were run, and which ones failed and succeeded. The order of test results is the same as the order of your tests. 

![Brief test overview](./test-overview.png)

We can see from this information that 4 tests were collected. The `.` symbol represents a passed test, and the `F` represents a failed test. So our test results were: `PASS`, `FAIL`, `FAIL`, `PASS`. Already, this seems unexpected!

Below that we have the report on our failed tests.

![Failed test report 1](./failed-test-report.png)

We can see that the test result gives us some helpful information, including the name of the test and the actual results that were calculated. We also get an `AssertionError` which is a special error raised by PyTest to indicate that a test failed.

**Tip:** Computers have a really hard time storing decimal values accurately, so when we add `0.1` and `0.2` we instead of `0.3` we get `0.30000000000000004`.

We will implement a solution to fix this later, but first let's finish examining our test results.

Unsurprisingly, our test intended to fail also failed because it asserted a `False` value:

![Failed test report 2](./failed-test-report-2.png)

Finally, we have our short test summary, which outlines all of the tests that failed and the actual results they produced causing them to fail:

![Failed test summary](./failed-test-summary.png)

## 6. Fixing Some Failed Tests

We have some failed tests to fix! The easiest one to fix is our `test_fail()` test. We can simply change the assertion to be `True`.

For our `add_test()`, we run into a problem caused by the limitations that computers have in storing data. To account for this, PyTest has a special kind of assertion called approximation to deal with decimals that should be correct, but aren't. It can be used like this:

```python
def test_add():
    assert pytest.approx(0.3) == add(0.1, 0.2)
```

Now instead of looking for the exact value of 0.3, we just need to get close. We can now run our tests again and see if they are fixed!

When all of your tests pass, the result should look like this:

![All tests passed!](./passed-tests.png)

## Thinking Like a Tester

When you are testing functions, you need to be able to identify how to fix tests when a test fails. A test can fail for either of the following reasons:

* The function returns incorrect data
* The test making an incorrect assertion

Whenever you have a test that fails, you are responsible for determining the root cause and coming up with a valid solution. Consider the two following examples with tests that fail:

---

### Example 1: A Simple Division

```python
def divide(a: float, b: float) -> float:
    """Divide a by b.
    
    :param a: The dividend.
    :param b: The divisior.
    :return: The quotient.
    """
    quotient = a / b
    return quotient

def test_divide():
    assert divide(0.3, 0.1) == 3
```

### Example 2: A Simple Multiplication

```python
def multiply(a: float, b: float) -> float:
    """Multiply a and b.
    
    :param a: The first factor.
    :param b: The second factor.
    :return: The product.
    """

    product = a * a
    return product

def test_multiply():
    assert multiply(2, 5) == 10
```

---

These two tests failed for completely different reasons. As a tester, can you identify what went wrong with each one?

When you look at Example 1, did it fail because of the function or because of the test?

When you look at Example 2, did it fail because of the function or because of the test?

How would you fix each one so that the tests pass?

# Extension Activity: Test Your Own Functions

Create your own functions and use PyTest to verify that each function produces the correct output. 

### Requirements

* Create **3 different functions** that accept at least one parameter and return a calculated value.
* Create at least **2 tests for each function**, using different input values for each test.
* Include at least **one test involving decimal values** that uses `pytest.approx()`.
