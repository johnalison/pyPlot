Interactive script for plotting in python.
Reads in json file of histograms (stored as py arrays) and makes interactive plots using matplotlib.

# Usage: 

Plotting from one file

```bash
> pyPlot test/testInputs.json
```

or when plotting from two files

```bash
> pyPlot test/testInputs.json    test/testInputs2.json  
```

# Examples Commands 

List the directories and plots in the file

```bash
> ls()
```

Make plots with various options.

Plot one variable

```python
>>> plot( "var1","dataSetA/dummy")
```

Rebin the varible before plotting

```python
>>> plot( "var1","dataSetA/dummy", rebin=2)
```

Plot one variable with style

```python
>>> plot( "var1","dataSetA/dummy",xMin=1,ylabel="Entries",xlabel="var1",xlim=[-0.5,2],yscale="linear",labels=["var"])
```


Plot two variables from one directory

```python
>>> plot( ["var1","var2"],"dataSetB/dummy",xMin=1,ylabel="Entries",xlabel="var1",xlim=[-0.5,2],yscale="linear",labels=["var 1","var 2"])
```

Plot two variables from one directory with ratio

```python
>>> plot( ["var1","var2"],"dataSetB/dummy",xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0,2],xlim=[-0.5,2],yscale="linear",labels=["var 1","var 2"],rebin=1)
```

Plot one variables from two directories

```python
>>> plot( "var1",["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0,2],xlim=[-0.5,2],yscale="linear",labels=["Dataset A","Dataset B"],rebin=1)
```

Plot two different variables from two different directories

```python
>>> plot( ["var1","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0,2],xlim=[-0.5,2],yscale="linear",labels=["var 1 (Dataset A)","var 2 (Dataset B)"],rebin=1)
```

# Initial Setup (only need once)

```bash
>  python3 -m venv myPyPlotEnv
>  cd myPyPlotEnv
>  source bin/activate
>  python3 -m pip install -r ../requirements.txt
>  cd ../
> source setup.sh
```

# Subsequent setups

After initial setup, only have to do the following on subsequent sessions

```bash
> source setup.sh
```

# Initial Development

```bash
> python3 -m venv pyPlotEnv
> cd pyPlotEnv/
> source bin/activate
> python3 -m pip install numpy
> python3 -m pip install --upgrade pip
> python3 -m pip install matplotlib
```