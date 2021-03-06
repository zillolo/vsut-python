# Very Simple Unit Test [![Build Status](https://travis-ci.org/zillolo/vsut-python.svg?branch=master)](https://travis-ci.org/zillolo/vsut-python)
**VSUT** is a simple unit test framework for Python 3.

## Installation
**VSUT** can be installed using `pip`:
```
pip install vsut
```

## Usage
A unit can be described ,as follows:
```python
...
class UnitTest(vsut.unit.Unit):

    def testComponentOne(self):
        ...
    def testComponentTwo(self):
        ...
```
Any methods that start with 'test' will be executed automatically, once the case is run.

## Asserts & Fail Conditions
The following methods can be used in a test-case to check for success or failure:
* ```assertEqual(expected, actual)``` - Checks for equality of the two arguments.
* ```assertNotEqual(expected, actual)``` - Checks for inequality of the two arguments.
* ```assertTrue(expected)``` - Checks whether the argument is the boolean value True.
* ```assertFalse(expected)``` - Checks whether the argument is the boolean value False.
* ```assertIn(expected, collection)``` - Checks whether the argument is in the collection.
* ```assertNotIn(expected, collection)``` - Checks whether the argument is not in the collection.
* ```assertIs(expected, actual)``` - Checks whether the value is the expected.
* ```assertIsNot(expected, actual)``` - Checks whether the value is not the expected.
* ```assertIsNone(expected)``` - Checks whether the argument is None.
* ```assertIsNotNone(expected)``` - Checks whether the argument is not None.
* ```assertRaises(exception, func, *args)``` - Checks whether the function 'func' raises an exception of the type 'exception'.

For any of these methods an optional **message** parameter can be specified, that will be printed instead of the default message. This is visibile in the following example:
```python
...
assertEqual(True, False, message="True is not False")
...
```

## Full Example
```python
from vsut.unit import Unit
from vsut.assertion import assertEqual

class TestCase(Unit):

    def testExample(self):
        a = True
        b = True
        c = False
        assertEqual(a, b)
        assertEqual(b, c)
```

## Running units
Units can be run with the test runner, as follows:
```
vrun [--format=table] test/test.py test/test1.py
```
Alternatively a whole directory can be specified:
```
vrun [--format=table] test/
```
Every Unit defined in a file in the `test` directory will be run by this command.

The `--format` argument is optional and specifies the method of formatting the output. Available methods are `table` and `csv`, with `table` being the default.
The separator for the csv-data can be specified with the parameter `--separator`.

**NOTE**: Some characters require escaping with `\`, as they are special characters.
#### Output as Table
Output as a table can look like this for example:
```
[TestCase]
Id  |           Name            | Status |   Time   |     Assert     | Message
0   | testAssertEqual           |   OK   | 0.000003 |                |
1   | testAssertEqualFail       |   OK   | 0.000008 |                |
2   | testAssertFalse           |   OK   | 0.000001 |                |
3   | testAssertIn              |   OK   | 0.000002 |                |
4   | testAssertIs              |   OK   | 0.000001 |                |
5   | testAssertIsNone          |   OK   | 0.000002 |                |
6   | testAssertIsNot           |   OK   | 0.000001 |                |
7   | testAssertIsNotNone       |   OK   | 0.000001 |                |
8   | testAssertNotEqual        |   OK   | 0.000001 |                |
9   | testAssertNotIn           |   OK   | 0.000002 |                |
10  | testAssertRaises          |   OK   | 0.000005 |                |
11  | testAssertTrue            |   OK   | 0.000002 |                |
12  | testFailWithCustomMessage |  FAIL  | 0.000003 | assertEqual    | A custom message.
13  | testWillFail              |  FAIL  | 0.000003 | assertEqual    | 1 != 2
14  | testWillFailToo           |  FAIL  | 0.000003 | assertNotEqual | 1 == 1
```

#### Output as CSV
Output as CSV can look like this for example:
```
TestCase
0,testAssertEqual,OK,0.000004
1,testAssertEqualFail,OK,0.000011
2,testAssertFalse,OK,0.000002
3,testAssertIn,OK,0.000004
4,testAssertIs,OK,0.000004
5,testAssertIsNone,OK,0.000002
6,testAssertIsNot,OK,0.000004
7,testAssertIsNotNone,OK,0.000002
8,testAssertNotEqual,OK,0.000003
9,testAssertNotIn,OK,0.000002
10,testAssertRaises,OK,0.000007
11,testAssertTrue,OK,0.000003
12,testFailWithCustomMessage,FAIL,0.000006,assertEqual,A custom message.
13,testWillFail,FAIL,0.000007,assertEqual,1 != 2
14,testWillFailToo,FAIL,0.000006,assertNotEqual,1 == 1
```
