"""
THIS IS WHERE YOU MAKE NEW QUESTIONS!

A question is a class with a descriptive name, which inherits from Question. 
The class must implement 

Property markdown: the string that becomes the markdown cell associated with 
    the question. 

Property inputs: a list of test-inputs which the users answer is 
    validated against.

method answer: an implementation of the correct answer. 

(optional) method special_check: if a simple useranswer(inputs) == correct_answer 
    test does not evaluate to True/False you can implement a custom check here. 
    This is for example relevant when working with pandas. 
"""

from .question import Test, Question


class DataFrameFromLists(Question):
    @property
    def markdown(self):
        s = """ Write a function that takes the following arguments:
        * An unknown number of lists, each containing floats representing the values of a variable.
        * A list of strings, containing the column names for a table. 

        For example, the function might be given a list of column names `key=['ID','year', 'age', 'income_index']
        and _four_ other lists: [1,1,1,2,2,2], [22,23,24,32,33,34], [2000,2001,2002,2000,2001,2002], [100,110,130,100,98,74]

        From these inputs the function should return a pandas DataFrame like 

        | 'ID' | 'year' | 'age' | 'income_index' |
        |------|--------|-------|----------------|
        |   1  | 2000   | 22    |   100          |
        |   1  | 2001   | 23    |   110          |
        |   1  | 2001   | 24    |   130          |                
        |   2  | 2000   | 32    |   100          |
        |   2  | 2001   | 33    |   98           |
        |   2  | 2001   | 44    |   74           |                

        > *Hint:* you will need to understand the `*input` notation for variable length arguments. 
        """
        return s 
    
    @property
    def inputs(self):
        inp = [
            (['a','b'],[1,2,3],[3,2,1]),
            (['ID','year', 'age', 'income_index'],
            [1,1,1,2,2,2],
            [22,23,24,32,33,34],
            [2000,2001,2002,2000,2001,2002],
            [100,110,130,100,98,74])
        ]
        return inp

    def special_check(self, inp, ans, useranswer):
        return (useranswer(*inp) == ans).all().all()

    def answer(self, keys, *values):
        import pandas as pd

        raw = {k:v for k,v in zip(keys, values)} 
        df = pd.DataFrame(raw)
        return df


class LinearRegressionWithSklearn(Question):

    @property
    def markdown(self):
        s = """ For this question you should write a function which takes two 
    numpy arrays as inputs, uses scikit learn's LinearRegression module to 
    estimate a model of the data, and return the coefficients as a numpy array. For example 
    you should make sure your function runs on input like 
    ```
    X = np.array([1,2,3])
    y = np.array([3,2,1])
    ```
    > *Hint:* we expect the output from the .coef_ attribute of the fitted 
    model object.
    > 
    > *Hint:* Your function will be tested with 1-dimensional X input. You might want to investigate how scikit learn handles this."""
        return s

    @property
    def inputs(self):
        import numpy as np 

        inp = [
            (np.array([1,2,3]), np.array([2,3,4])),
            (np.array([4,6,8]), np.array([1,2,3])),
            (np.array([4,6,7]), np.array([3,2,1]))
        ]
        return inp

    def answer(self, X, y):
        from sklearn.linear_model import LinearRegression 
        
        m = LinearRegression()
        m = m.fit(X.reshape(-1,1), y)

        return m.coef_



class joinStringArgs(Question):
    @property 
    def markdown(self):
        s = """ Write a function that takes some arbitrary number of string inputs as arguments and joins them together, separated by commas.

        Note the string should be passed individually. Not in a list or tuple. The input might for example be 
        `'a','b'` or it could be `'hel', 'ld' 'wor', 'ld'`.  To be clear your output should be a string. I
        If for example your function receives inputs `'a', 'b', 'c'` the output should be `'abc'`.     
        """
        return s 

    @property
    def inputs(self):
        inp = [
            ('a','b','c'),
            ('z','y'),
            ('hej','hej')
        ]
        return inp 
    
    def answer(self, *s):
        return ','.join(s)


class SubTwoNumbers(Question):
    @property    
    def markdown(self):
        s = """Write a function that subtracts two numbers x,y and returns the output x - y.
        Sample input might be `x=-2`, `y=8.2' in which case the output should be `-10.2`. 
        The expected output is either float or int. 
        """
        return s 

    @property
    def inputs(self):
        inp = [(1,1),
                (3,2),
               (-2,3)]
        return inp

    def answer(self, x, y):
        return x - y


class AddTwoNumbers(Question):  
    @property    
    def markdown(self):
        s = """ Write a function that adds two numbers x,y and returns the output x - y. 
        Sample input might be `x=-1`, `y=8' in which case the expected output is `7`. 
        The expected output is either float or int.
        """
        return s 

    @property
    def inputs(self):
        inp = [(1,1),
                (2,2),
               (-2,3)]
        return inp

    def answer(self, x, y):
        return x + y



class MultiplyTwoNumbers(Question):
    @property    
    def markdown(self):
        s = """Write a function that multiplies two numbers x,y and returns 
        the output x - y. Sample input can for example be `x=2` and `y=2` in which case your function should return `4`.
        """
        return s 

    @property
    def inputs(self):
        inp = [(1,1),
                (2,2),
               (-2,3)]
        return inp

    def answer(self, x, y):
        return x * y

