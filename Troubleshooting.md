# Troubleshooting

## Win/10 import error in Pycharm with DLL load failed: The specific module could not be found.
```
ImportError: Importing the multiarray numpy extension module failed. 
Most likely you are trying to import a failed build of numpy. 
If you're working with a numpy git repo, try 'git clean -xdf' (removes all files not under version control). 
Otherwise reinstall numpy. 
Original error was: DLL load failed: The specified module could not be found.
```

This may occur only on Win/10 and specific versions of Pycharm. The same code may work fine when importing from python console outside of Pycharm.
See this [link](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360001194720-Numpy-import-error-in-PyCharm-Importing-the-multiarray-numpy-extension-module-failed-) for complete description of problem and possible solutions.


### Solution 1:
Add `C:\Users\<USERNAME>\AppData\Local\Continuum\anaconda3\Library\bin` to Windows `PATH` environment variable (and restart pycharm).

The path should be Library\bin folder where anaconda3 is actually installed on your computer. For default install with user directory on C:,
the above path should be correct, substituting the username.

### Alternative solution:
Uninstall offending library and reinstall. 

This can be a bit difficult for files inside anaconda. 

Note if you are behind a corporate firewall, you will need to make sure proxy settings are correct in order to reinstall.
