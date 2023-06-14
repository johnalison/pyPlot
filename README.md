Interactive script for plotting in python.
Reads in json file of histograms (stored as py arrays) and makes interactive plots using matplotlib.

# Usage: 

Plotting from one file

```
  > pyPlot test/testInputs.json
```

or when plotting from two files

```
  > pyPlot test/testInputs.json    test/testInputs2.json  
```

# Examples Commands 

List the directories and plots in the file

```
> ls()
```

Make plots with various option

Plot one variable

```python
>>> plot( "var1","dataSetA/dummy",xMin=1,ylabel="Entries",xlabel="var1",xlim=[-0.5,2],yscale="linear",labels=["var"])
```

> plot(["var1","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=False,xlim=[0,2])

> plot(["var1","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0.,2.],xlim=[0,2])

> plot(["var1","var2"],["dataSetB/dummy","dataSetA/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0,2],xlim=[-0.5,2],yscale="linear",labels=["var 1","var 2"],rebin=2)


# Initial Setup (only need once)

>  python3 -m venv myPyPlotEnv
>  cd myPyPlotEnv
>  source bin/activate
>  python3 -m pip install -r ../requirements.txt
>  cd ../

# Then each time

> source setup.sh


# Initial Development

> python3 -m venv pyPlotEnv
> cd pyPlotEnv/
> source bin/activate
> python3 -m pip install numpy
> python3 -m pip install --upgrade pip
> python3 -m pip install matplotlib
