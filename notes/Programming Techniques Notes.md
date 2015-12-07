
#CS: Programming Techniques Notes

##Overview

Programming techniques is one of the four main sections of the controlled assessment. It is the one that is awarded the most marks (six times more than any other section) and so is the most important.

###What are the marks for?

There are 36 marks available for this sections, split into six six-mark categories:

* Interoperability - How do the program parts _fit_ _together?_
* Working - Does your program _work?_
* Efficient - Have you used _efficient techniques?_
* Data Structures - _What_ and _why?_
* Robust - Does your program _survive_ the user?
* Understood - Do you _understand_ what your doing?

###Marking Levels

There are three levels of marking for each category - you can and should be aiming for the highest one:

* State - Say _what_ you have done.
* Explain - Say _how_ it works.
* **Discuss** - _**Why**_ this way?

In order to achieve level two, you must also achieve level one, and for three, two, etc.

###Structuring This Section

I would suggest splitting your answer into categories and then discussing individual techniques within categories.
There are six points you want to make for _each_ technique:

* What - What is this? Give a brief introduction.
* Why
	* Alternatives - What else could you have done? Arguments both for and against all alternatives.
	* Justify - Why did you choose the method you chose? Why is it _better_, not just _good_?
* Example
	* Where - When have you used this? What did you do?
	* Context - Why is it _justified_ in _this_ case?
* Explain - _How_ does this technique _work?_ Show your _understanding._

Aim for one point, per category, per technique. So ideally, you would have six techniques in each category, although this may not be achievable, it may all balance out - some sections have lots of techniques, others have only two or three.

###What are programming techniques?

It may seem difficult to find programming techniques to discuss, but almost _anything_ can be considered a programming techniques. If you use something in your program even once, _include it!_ Here are a few things that could be considered programming techniques:

* Built in Python functions - ```map```, ```filter```, ```char```, ```random.randint```, etc.
* Classes
* Functions
* Loops - ```for``` and ```while```.
* Variables - also ```global``` and ```nonlocal```.
* Lists - also tuples and dictionaries.
* Strings
* Files
* Any other data types.
* Any patterns you define - if you do something in a particular order or way, use that too.

##Analysis of the Categories

###Working

This is six easy marks, simply have a working program. The evidence for this is in the _testing_ section. Specifically, the evidence is _passed_ tests that use _valid_ input. What I mean is tests in which you _didn't_ try to break the program, and it _worked as expected._ That demonstrates that the program is working.

###Interoperability

For this, I recommend dividing your program up into units. If you have functions or classes, this is a good place to start. For instance, in my last controlled assessment, I had thirty functions. Your program probably won't have that many, but the theory is still the same. A diagram might be good here, with some description. The main point is that you must say _what_ provides _what_ to _what_ for _what_ purpose.

###Efficient

Efficiency takes many forms - speed of your program, the memory requirements, the size of your program's code, the readability and ease of understanding of your code, etc.
The key here is _discussion_. _Why_ are the techniques you have chosen _better_? Here, it is crucial to provide alternatives.

###Robustness

* Robustness is the ability of your program to _survive testing._
* For tests which you tried to break the program and failed, how did it survive?
* For tests which _did_ break the program, why did it break and how are you going to fix it?
* It's not about your program crashing of its own accord; It's about the _user's input_ crashing your program.
* Tests in which you don't try to break your program don't prove it is robust - simply that it works.

###Data Structures

* A _program_ is a set of _algorithms_ which convert between _data structures._
* A data structure is a way of storing and representing data.
* _Where_ do you store data and _why?_
* The key here is also _discussion_ - you must provide alternatives.
* Variables, lists, strings, numbers, _why did you use those?_
* Include any _data types_ you used.

###Understood

* _**How**_ does it work?
* _**Why**_ does it work?
* _**Why**_ like that? Offer alternatives and then justify your _choice._
* _**Where**_ does it do it like that - give examples.
* _**What**_ does it do?
* Show your _understanding._

##An Example

####Programming Techniques Used

####Lists

I use lists throughout my program as a way of storing a variable quantity of data. There are several alternatives I could have used instead of lists. For example, I could have used many variable declarations. However, this isn't usable since I need to hold a varying quantity of data. Also, and extension that would allow we to do this with variable definitions is much less efficient and much more unsafe, and less reliable. Another alternative could have been using a tuple. Instead of the normal list syntax:

```python
list = [1, 2, 3]
```

Tuples use the alternate syntax:

```python
tuple = (1, 2, 3)
```

There are several arguments for using tuples. The first of these is that creating tuples is more memory efficient and faster. To show you why I used lists instead, I will take an example of the word lists in my program:

```python
with open('words.txt', 'r') as f:
	return list(f.read().split('\n'))
```

Here, I used a list because I needed to modify the list later:

```python
words[-1], removed = replaced, words[-1]
random.shuffle(words)
```

If I had used a tuple, since they are immutable, whenever I modify it, I would have to create a new tuple. This is slow and memory inefficient because tuples do not allow in-place modification. However, wherever I am using lists which I do not modify, I have used tuple as they are more efficient to create. Another reason I have used lists is that it is more readable and easy to understand to use the list methods:

```python
list.append(item)
list.remove(item)
list.index(item)
```

Rather than the tuple equivalent:

```python
tuple += (item,)
tuple = tuple[:tuple.index(item)] + tuple[tuple.index(item) + 1:]
tuple.index(item)
```

Another alternative is an iterator. However, this is not very useful, since iterators are not modifiable, and they cannot be indexed (elements cannot be selected at random, only in order):

```python
iterator[index] #this doesn't work
```

Also, you can only go through the elements of an iterator once. This means that I would have to save them to a list, thus negating any possible benefit. Despite this, iterators are used occasionally when all these requirements are met, since they are much more efficient than either lists or tuples, only storing one element in memory at a time.
