| [< Previous (Intro)](../README.md)  | [Day1](../README.md)| [Next (Session Objectives) >](SessionObjectives.md) |
|----|----|----|
# Environment Setup

On the first day, the class will setup a python environment on your laptop.

### Prerequisite Software

You will need a python environment, and IDE to participate in this course. Please download and install the following
before the course.

1. Download and install [Anaconda 2019.03](https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86_64.exe)
2. Download and install [PyCharm Community Edition 2019.1.3](https://www.jetbrains.com/pycharm/download/)


### Further Notes

<u>Anaconda</u>

- In our classes, we shall use **Python 3.7**; hence download the Python 3.7 version of Anaconda
- Most of the laptops we use today are 64-bit machines. To confirm, checkout the instructions [here](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64-bit-version-of-the-windows-operating-system)
- Your Anaconda download screen will (most probably) look like this. Download the 64-bit installer (pointed to by the red arrow)
![ana440_64_win](images/anaconda_3.7_win64.png)

### Configure a Python Interpreter for PyCharm

You can refer to this [link](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) 
to configure the Python interpreter. Or you can follow the instructions below.
- Once you install both PyCharm and Anaconda, open PyCharm and create a new project. Open `Settings...` 
under the menu `File`.
![settings](images/settings.png)
- Once in settings, click on `Project Interpreter` under `Project: [YOUR PROJECT NAME]` from the left.
Click the gear icon and select `Add`.
![project_interpreter](images/project_interpreter.png)
- Select `System Interpreter` from the left menu, choose the Anaconda3 from the dropdown list, and the click `OK`.
![conda_interpreter](images/add_project_interpreter.png)
- The Anaconda interpreter should be automatically populated under `Project Interpreter`. If not, select the 
Anaconda3 interpreter from the dropdown list. Click on `OK` to close the Settings menu, and now you should be all set.
![select_interpreter](images/select_project_interpreter.png)


| [< Previous (Intro)](../README.md) | [Day1](../README.md) | [Next (Session Objectives) >](SessionObjectives.md) |
| ---- | ---- | ---- |
