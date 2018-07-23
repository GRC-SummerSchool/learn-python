from ivcurve import IVCurve
from os import listdir
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm


class Experiment:
    def __init__(self,directory,molecule=None):
        self.molecule=molecule

        # Cleaning up input to make it more user-friendly:
        # Directory input can end with or without trailing '/'
        directory=directory.rstrip('\\/')+'/'

        # Get all files in the directory
        files=listdir(directory)

        self.ivcs=[] # Abbreviation for IVCurves

        # Load all in directory
        for f in files:
            filename=directory+f
            if IVCurve.can_load(filename):
                self.ivcs.append(IVCurve(filename))

        # Order list by temperature
        self.ivcs.sort(key=lambda ivc:ivc.T)

        # Create a list of temperatures
        # This uses a technique called list comprehension - creating a list from another list
        self.Ts=[ivc.T for ivc in self.ivcs]

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

    def R_of_T(self,**kwargs):

        #Again, using list comprehension
        Rs = [ivc.R_inst(**kwargs) for ivc in self.ivcs]

        return self.Ts, Rs


if __name__=="__main__":
    import os
    os.chdir('/Users/izzy/Codebase/learn-python')

    experiment = Experiment("examples/iv-curves/data/")

    experiment.plot_iv()

    T, R = experiment.R_of_T()
    plt.loglog(T,R) # log-log scale
    plt.title("Zero-Point Resistance v. Temperature")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Zero-Point Resistance (Ohm)")
    plt.show()