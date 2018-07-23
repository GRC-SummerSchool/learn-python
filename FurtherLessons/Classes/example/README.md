|[< Previous (Magic Methods)](../magicmethod.md) | [Intermediate Python](../../README.md)| [Next (Home) >](../../../README.md) |
|----|----|----|

# OOP Example


_Familiarity with numpy and matplotlib modules recommended._

This section demonstrates how to use classes to represent the data found in [the iv-curve example](../../../examples/iv-curves).

## Step 1: Determine appropriate structure
To understand what an appropriate class structure for the analysis is, you must first understand what you're trying to represent.
In this case, the data comes from a series of experiment designed to measure the zero-point resistance of a sample as a function of temperature.
Each file represents measurements on a sample at a certain temperature, and in the complete dataset, each sample was measured using several different molecules
(the data here contains one sample, with one molecule). The final analysis compared the ratio of resistance of Molecule A/Molecule B
as a function of temperature across several different samples.

Putting that into terms of classes, the program should contain classes to represent:
1. A single IV Curve.
-  Key Attributes: temperature, voltage, current.
-  Key Methods: Resistance at a given voltage
2. A single Experiment.
- Key Attributes: List or dictionary of IVCurves in the experiment, Molecule used in experiment.
- Key Methods: Resistance vs Temperature curves, plotting all IVCurves
3. A single Sample.
- Key Attributes: Sample name & information, List or dictionary of Experiments on the Sample.
- Key Methods: Resistance ratio vs temperature curves
4. A Molecule? Depending on how complicated the molecule representation needs to be for the final analysis,
it could be appropriate to create a Molecule class.

Since the data given represents only one experiment, this example will work through creating the first two classes (and 
leaving out the molecule).

## Step 2: IVCurve
With an approximate idea of the capabilities required of each class, it's easiest to work from the inside out. Since an
Experiment contains multiple IVCurves, it's best to start by creating the nested class. If we can get a IVCurve class that
we're happy with, then we'll know how to initialize them from the Experiment class.

_If you're not familiar with Pycharm's debugging tool, now's a good time to get started._

We start simple. One file appears to have everything we need to create the class- and the filename contains the temperature.
There's also some extra information on the first line of each file which might come in handy later. There's a few functions
pre-written to help with parsing strings.

```python
import numpy as np
import matplotlib.pyplot as plt
import misc_functions as misc

class IVCurve:
	
    def __init__(self, filename):
    
        # Get temperature
        self.T = misc.get_temperature_from_filename(filename)
        
        # Get other data as a dictionary
        self.meta = misc.parse_firstline(filename)
        
        #Load the file using numpy loadtxt to put into array
        file_data = np.loadtxt(filename,skiprows=3).transpose()

        #First column is voltage...
        self.V = file_data[0,:]

        #And the other 10 are all current
        self.I = np.mean(file_data[1:,:],axis=0)
		
	

if __name__=="__main__":
    ivc = IVCurve("examples/iv-curves/data/1.6K.txt")
    0 # Put a debugging stop here to investigate variables in ivc
    
    # Viewing variables
    plt.figure()
    plt.subplot(221)
    plt.plot(ivc.V)
    plt.title("Voltage")
    
    plt.subplot(222)
    plt.plot(ivc.I)
    plt.title("Current")
    
    plt.subplot(212)
    plt.plot(ivc.V,ivc.I)
    plt.title("IV Curve")
    
    plt.show()
```
The `if __name__=="__main__"` statement at the bottom will only run if we run the script directly, and not if we import
it into another script. As such, it makes a good place to debug the class, since we can leave the code there for the next time
we need to make modifications. If a function makes a

With that, we have a basic representation of a single dataset. Now we can add a method to calculate the resistance at the curve at
a given voltage, nominally 0 V. Mathematically, this is calculated with `R = dV/dI`. Computationally, we use a small window 
around the given voltage to determine the slope at that point, then take the inverse. A small window could lead to noisy results,
but a large window loses the curvature seen at smaller temperatures.

```python
class IVCurve:
    # ...

    def slope_inst(self, V = 0, V_window = 1.0):
    	
        # Get the parts of the curve that fall into the window
        index= np.logical_and(self.V >= V-V_window, self.V <= V+V_window)
		
        # Check to make sure there was at least 2 points
        if np.sum(index)< 2: return False
        
        # Fit a linear line to the points
        c_fit=np.polyfit(self.V[index],self.I[index],1)
        
        # Return slope of line
        return c_fit[0]

    def R_inst(self,V = 0, V_window = 0.05):
        return 1/self.slope_inst(V=V,V_window=V_window)

if __name__=="__main__":
    
    # The resistance using the whole curve as the "window" should about equal the
    # second line of the original data file.
    print(ivc.R_inst(V_window=1.0)) # Should equal about 472.3k

    # Plot R_inst as a function of V
    R_inst=[]
    for v in ivc.V:
        R_inst.append(ivc.R_inst(V=v))

    plt.figure()
    plt.plot(ivc.V,R_inst)


    plt.show()    
```

With that, we're ready to start working on our next class!

## Step 3: Experiment
As we begin writing the Experiment class, we may need to go back-and-forth a bit with the IVCurve class.
 
Ideally, since all the files for a single Experiment are sorted into a single directory, it'd be easiest to have that be the
only input into the initializer. Luckily, python comes with a function to list all the files in a folder:

```python
from ivcurve import IVCurve
from os import listdir

class Experiment:
    def __init__(self, directory, molecule = None):
        
        print(listdir(directory))


if __name__=="__main__":

    experiment = Experiment("examples/iv-curves/data/")
```
When you examine the output of the `listdir` function, you may see that there were some hidden files that get found by python.
Those can't be turned into IVCurves, and will need to be filtered out. Secondly, the files are listed in alphabetical order,
not numerical by temperature. A list will be easier to work with when it comes to graphing the data later, but will need to
be explicitly ordered after all the curves are loaded in. (A dictionary does not retain any order, and could have its keys
swapped around differently every time the code runs).

To filter out the hidden files, we'll create a static method in the IVCurve class that returns True/False if a filename can be
loaded. This allows us to check beforehand if we'll run into trouble:

```python
class IVCurve:
    # ...
    
    @staticmethod
    def can_load(filename):
        
        if misc.get_temperature_from_filename(filename) is None:
            return False
        else:
            return True
```

Initializing the Experiment class involves finding all the files in the directory, and creating an instance of IVCurve
for each file that IVCurve can load. The created instances are stored in a list. We'll also create a field for the molecule,
but in this example, the field won't be used, and defaults to None.

```python
from ivcurve import IVCurve
from os import listdir

class Experiment:
    def __init__(self, directory, molecule = None):
        
        self.molecule = molecule
        
        # Cleaning up input to make it more user-friendly:
        # Directory input can end with or without trailing '/'
        directory = directory.rstrip('\\/') + '/'
        
        # Get all files in the directory
        files = listdir(directory)
        
        self.ivcs = [] # Abbreviation for IVCurves
        
        # Load all in directory
        for f in files:
            filename = directory + f
            if IVCurve.can_load(filename):
                self.ivcs.append( IVCurve(filename) )
        
        # Order list by temperature
        self.ivcs.sort(key=lambda ivc: ivc.T)
        
        # Create a list of temperatures
        # This uses a technique called list comprehension - creating a list from another list
        self.Ts = [ivc.T for ivc in self.ivcs]
        


if __name__=="__main__":

    experiment = Experiment("examples/iv-curves/data/")
    0 # Put a debugging stop here to investigate variables in experiment
```
To visualize the information better, we'll first add a method to plot all the IVCurves. We'll add temperature-based color-coding
on each of the lines instead of the plot's default coloring order. If you're new to matplotlib, don't worry- creating plots
is something easily google-able!
```python
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm


class Experiment:
    #...

    def plot_iv(self):
        #Make a new window
        fig=plt.figure()

        #Color represents the temperature of the measurement

        cmap = plt.get_cmap('rainbow') # Rainbow or Blue->Red Intuitive coloring for temperature
        cNorm = colors.LogNorm(vmin=1,vmax=300) # Setting max/min of scale, adjusted to log scale
        scalarMap = cm.ScalarMappable(norm=cNorm,cmap=cmap) # This will map number -> color
        scalarMap._A = [] #this is needed to add a color bar later

        for ivc in reversed(self.ivcs):
            # ivc is an instance of IVCurve
            
            colorVal = scalarMap.to_rgba(ivc.T) # Determine color to use for line

            #Plot IV curve
            plt.plot(ivc.V,ivc.I,color=colorVal)

        
        if self.molecule is None:
            name = "None"
        else: name = str(self.molecule)
        plt.title("IV Curves for Molecule "+name)
        plt.ylabel("Current (A)")
        plt.xlabel("Voltage")
        plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0)) # Scientific Notation

        plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])

        plt.show()
        plt.close(fig)

if __name__=="__main__":
    experiment = Experiment("examples/iv-curves/data/")
    experiment.plot_iv()

```

The final plot should look something like this:


Once the Experiment object can initialize with the variables we need, we can add a method that goes to each IVCurve and 
creates a list of the zero-point resistance. Since we'd like to plot this information, we'll have it also return the temperature
list.
```python
import matplotlib.pyplot as plt

class Experiment:
    # ...
    
    def R_of_T(self,**kwargs):

        #Again, using list comprehension
        Rs = [ivc.R_inst(**kwargs) for ivc in self.ivcs]

        return self.Ts, Rs


if __name__=="__main__":
    experiment = Experiment("examples/iv-curves/data/")

    T, R = experiment.R_of_T()
    
    plt.loglog(T,R) # log-log scale
    plt.title("Zero-Point Resistance v. Temperature")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Zero-Point Resistance (Ohm)")
    plt.show()
```

With this, we've done everything we set out to do!

# Step 4: Bells and Whistles
With the basic class structure in place, it simple to elaborate the code from there. Each "type" of analysis has a place 
where it can run smoothly without interrupting any other parts of the code. In this particular case, a calculation that
would run with "a single IV curve" would get placed in the IV Curve class, while an analysis dependent on the collection
of curves would run with the Experiment class. As in the example above, that may mean a calculation gets split: the IV curve
calculates the resistance for that curve, and the experiment object collects that & the temperatures into a list.

Here are some more methods that could be implemented:

- **Fitting R of T:** A method in the Experiment class might use the output of `R_of_T()` to fit an exponent to the
results (`R = T^c`). This could be done as a function of voltage.
- **Trace-Retrace:** You may have noticed as we wrote the IVCurve class that the measurements were taken as trace-retrace:
starting at 0V, going to 1V, down to -1V, then back to 0V. It's more convenient to have data representing -1V to 1 V.
Collapsing the I-V data can be done either in the initialization (so it always applies), or in a separate `get_collapsed_iv()`
method.
- **Frequency filtering:** At very low temperatures, the center section of each curve has very low current- on the order
of nanoamps! Because of that, the measurements may be susceptible to 50 Hz noise from the (European) power grid. Filtering
out the noise on one curve should be done in the IVCurve class (and requires knowing the sampling rate- which was saved in
the meta attribute!), but determining if there's an issue with the noise requires looking at all the curves to see if 
there's a 50 Hz spike in the first place, so would be written for the Experiment class.
- **Offset correction:** Again, due to the low currents in the region of interest, there's a small-yet-noticeable offset
current from the measurement instrument. Since the curves themselves are not symmetric, the offset can be subtracted by
once again taking a linear fit around 0V, but taking the constant instead of the slope. Offset correction is especially
relevant for...
- **Linear/Non-linear cross over:** Each IVCurve has a voltage where it switches from linear behavior to exponential behavior.
Calculating the cross-over point is a job for the IVCurve class, but plotting that voltage as a function of temperature is a
job for the Experiment class.

## Step 5: Using the classes

The IVCurve and Experiment classes were designed to be nested inside another class, so that the entire analysis could be done
just by calling a couple methods, but don't let that stop you from writing functions as usual! A good rule of thumb for if
something should be a method, a function, or just an outright script is how reusable/specific code is. In this project,
having a couple of classes to handle the initial data analysis (and frequency filtering, and offset correction) allowed for
highly customized, use-this-once-per-project scripts to be written quickly and efficiently.

In the list above, determining interference from the electric grid is likely a one-time analysis, so it would work better 
as a script that uses an Experiment instance, instead of a method of the class itself. Meanwhile, especially if interference
is likely, taking the Fourier transform and calculating the frequency axis is likely to be something the IVCurve class 
does frequently, so works better as a method. Below is an example of how to use an Experiment object in a script:
```python
from experiment import Experiment
import matplotlib.pyplot as plt
experiment = Experiment("examples/iv-curves/data/")

minT = experiment.Ts[0]
maxT = experiment.Ts[-1]

for ivc in experiment.ivcs:
    fHz, fI = ivc.get_fft()
    plt.plot(fHz,fI)

plt.show()
```
The only difference between a script or function and a method is that the variable name `experiment` gets used instead of
`self` as we'd ben doing before.

## Step 6: So Long, and Thanks for All the Fish
The purpose of these lessons was not to make you an expert programmer, but to give you enough knowledge about python that
you'll at least be able to understand the answers on StackOverflow the next time you need to google a question!

Stay turned for future topics on the [Intermediate Python](../../README.md) home page!

|[< Previous (Magic Methods)](../magicmethod.md) | [Intermediate Python](../../README.md)| [Next (Home) >](../../../README.md) |
|----|----|----|