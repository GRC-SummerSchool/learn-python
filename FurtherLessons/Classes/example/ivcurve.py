"""
Uses Object-Oriented Programming to run an analysis of IV-curves
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import misc_functions as misc


class IVCurve:

    def __init__(self,filename):

        # Get temperature
        self.T = misc.get_temperature_from_filename(filename)

        # Get other data as a dictionary
        self.meta = misc.parse_firstline(filename)

        #Load the file using numpy loadtxt to put into array
        file_data = np.loadtxt(filename,skiprows=3).transpose()

        #First column is voltage...
        self.V = file_data[0,:]

        #And the other 10 are all current
        self.I = np.mean(file_data[1:,:],0)


    @staticmethod
    def can_load(filename):
        if misc.get_temperature_from_filename(filename) is None:
            return False
        else:
            return True


    def slope_inst(self,V=0,V_window=1.0):
        # Get the parts of the curve that fall into the window
        index=np.logical_and(self.V>=V-V_window,self.V<=V+V_window)

        # Check to make sure there was at least 2 points
        if np.sum(index)<2: return False

        # Fit a linear line to the points
        c_fit=np.polyfit(self.V[index],self.I[index],1)

        # Return slope of line
        return c_fit[0]


    def R_inst(self,V=0,V_window=0.05):
        return 1/self.slope_inst(V=V,V_window=V_window)


if __name__ == "__main__":
    ivc = IVCurve("examples/iv-curves/data/2K.txt")

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