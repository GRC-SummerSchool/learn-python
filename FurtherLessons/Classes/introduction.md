|[< Previous (Generators)](../Functions/generators.md) | [Intermediate Python](../README.md)| [Next (Classes) >](classes.md) |
|----|----|----|

# Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP for short) is a style of programming that groups variables and functions into _classes_,
which helps give them context, and ensures that you always have the right variables on-hand to run a chunk of code.

Compare the following two fragments of code:

```python
indRef = 7
imgRef = imgs[imgRef,:,:]
imgIdRef = imgsID[i]
imgSrcRef = imgsSrc[:,Ref]
results = []
for i in range(len(imgs)):	
	result = predict(imgs[i,:,:],imgsID[i], imgsSrc[i,:], imgRef, imgIdRef, imgSrcRef)
	results.append(result)
``` 

```python
imgRef = datamanger.getRef()

results = []
for img in datamanger.getImgs():
	result = predict(img,imgRef)
	results.append(result)
```
In the second example, all the variables are bundled up into different user-defined objects: `datamanger`, `imgRef`, `img`.
This keeps the code cleaner and more readable- which means, easier to debug. If you look closely, the first code fragment has a mistake; 
the code would likely still "execute", but give very strange unintended results.

Writing object-oriented programming typically takes more planning at the beginning of a project, but pays off massively as the code
starts to become more complex.

## 4 Pillars

There are 4 main ideas behind OOP:
1. **Encapsulation** The fact that variables are bundled up into different classes allows objects to use the same variable 
and function names, but in different contexts. `checkbox.check()` clearly means something different from `hockeyplayer.check()`, even
though they both use a function called "check()".

2. **Data Abstraction** Objects allow for programmers to understand at a glance what is the intended use a collection of variables, without needing
the details of the inner workings of the functions, or trying to trace where a stray variable came from. Again, OOP gives the code context.

3. **Polymorphism** By adding "behavior" (functions) to an object, you can present the same set of behaviors from multiple different (yet related) objects.
This set of behaviors is known as an *interface*. But take, for example, a `Dog` object vs a `Cat` object. They might both have a `call()` method, but
`dog.call()` results in the dog approaching the person, while `cat.call()` results in the cat ignoring the person. Regardless of the end result, a programmer
can have a variable `pet` that is either a dog or a cat, and `pet.call()` will work in both cases.

4. **Inheritance** Inheritance allows for a programmer to define sub-categories of a base class, which allows for code reuse and reinforces the idea
of interfaces. `Dog` and `Cat` could both be a sub-category of `Animals`, for example, which means the `pet.birthday()` behavior would only need to be
written once. This topic will be explored in much more depth in a later lesson.

## When to use

If you're just starting a project, take the time before beginning to ask yourself, "What is the code trying to represent?" Using OOP is especially useful in cases where:
- You have one or more 'nouns' represented by multiple variables.

  *Examples:*
    - *The example above had an image represented by an img, an id, and a source*
    - *A dog might have a name, an age, a breed, an owner, a microchip number, and vaccination status*
    
- You're passing data around as a dictionary.

  *If you've got multiple dictionaries that all have the same keys, consider writing a class for the data instead.* 
  *The same thing applies to data you're storing in multiple arrays that you have to make sure you coordinate the indices for.*

- Making complicated functions user-friendly.

  *Hiding the details of the implementation allows the programmer using the class to focus on the big picture*
  ```python
  #Without OOP:
  session.run(["AdamOptimizer:0","loss:0"],feed_dict={input_pl:input,lr_pl:learning_rate,dropout:0.5})	

  #With OOP:
  model.train(input,lr=learning_rate)
  ```
  The above example is actual code from a generic [Tensorflow neural network](https://www.tensorflow.org/) for machine learning.
  Representing the model as an object means the user doesn't need to know how sessions get used, or what the optimizer is called.

### Excerise
Think about a project you've worked on or are planning, and see if you can find 2 or 3 classes that the project could use.
If you've got a partner or a neighbor, discuss with them the potential benefits.

|[< Previous (Generators)](../Functions/generators.md) | [Intermediate Python](../README.md)| [Next (Classes) >](classes.md) |
|----|----|----|