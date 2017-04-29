# Python Tutorial

## What is Python, and why use it?
Python is a multi-purpose, object-oriented programming language.  In a few short lines of code, you can perform various tasks like query a database, read and create an Excel document, or pull information from a website. The Python community has created machine learning and plotting programs that even a novice could use.  Truly, the limits and benefits of using Python to do things for you are left up to your imagination and persistence.

**Hello Kristin!**

## Installation
There are a few things you need to begin programming in Python. All of these things (and more) are included with the download of the application bundle [Anaconda](https://www.continuum.io/downloads). The three key ingredients of [Anaconda](https://www.continuum.io/downloads) that you should be most concerned with is Python the language, Spyder the programming language, and Conda the package manager.

**Python** - The language code, base libraries, and compiler that makes up the Python language and enables you to run Python scripts.  
**Spyder** - Also known as an IDE, Spyder is the program you use to actually type and run Python code.  
**Conda** - Known as a package and environment manager.  It is used to download versions of third-party libraries that can be called by your script.  

1.) Download and install [Anaconda](https://www.continuum.io/downloads)  
2.) In a Windows command line console (cmd), execute the following lines:
```sh
conda install pandas numpy matplotlib python-dateutil SQLAlchemy seaborn pymysql openpyxl numexpr six xlrd quandl

pip install pyorient
pip install simple-salesforce
```

3.) Open Spyder  
4.) Click View -> Panes -> Make sure File Explorer is checked.  
5.) Open the project folder in this pane.


## Beginners
Follow along the beginners path below in the beginner directory.  You will learn the anatomy of programming in Python, and perform a variety of basic tasks.

### Beginner 1 - Variables, Hello World!
Your first program. Congratulations!  In this lesson, you will learn a few basic

**comments** - Lines of code that are ignored by the program.  They are meant to convey information to the programmer what is happening in the code.  
**console** - The console is where you may enter, interact with and visualize data, inside a command interpreter - [more info](https://pythonhosted.org/spyder/console.html).  
**debugging** - The process of fixing problems within your code.  
**for loop** - A statement in Python with the syntax beginning with the word 'for' that loops through a set of data - [more info](https://www.learnpython.org/en/Loops)


### Beginner 2 - Functions, Parameters (Arguments), and Numbers
Now that we have learned a few basics, its time for use to begin creating reusable blocks of code.  These blocks are referred to as functions.  Functions can be called over and over again, and imported into other scripts.  They can be passed parameters, and return a value for you to assign to a variable.

**functions** - A named block of code that can take parameters and return a value.  
**parameters** - A variable that can be passed into a function.  Referred to as arguments.  
**integer** - A number without a decimal point  
**floating point** - A number with a decimal point


### Beginner 3 - Dictionaries and Lists
In this lesson, we will learn how to use lists and dictionaries of information.  These objects will become handy when we're working with graphs of data.

**dictionary** - Also known as a 'dict', it is a series of key and value pairs.  
**None** - 'None' is a special keyword in Python that literally means nothing

### Beginner 4 - Import Statements, Pandas, and Excel
The term "third-party library" refers to a package of code that other people have written.  One of the many benefits of writing code in Python is that it has a very large and active development community. This community has built a variety of code that performs many different functions - including scientific operations, file manipulation, and more! The import statement makes these functions available to your code.

In this lesson, we'll learn to import and use Pandas to export a list of information into Excel.

**module** - A group of code that may be imported into your script.  
**import** - A special command in Python that pulls in a module of code and makes it available to use in your script.  
**pandas** - A high performance data-analysis tool, great for out-of-the-box useful tasks like sorting, finding min/max/avg, and outputting to Excel. - [more info](http://pandas.pydata.org/)

## Additional Information
There are many resources to learn more about python.
* [python.org](http://www.python.org)
* [learnpython.org](http://www.learnpython.org)
* [Conor's Python Page](http://confluence.energyscorecards.com/display/AM/Python)
* [Learn Python the Hard Way (book)](https://www.learnpythonthehardway.org/book/)
