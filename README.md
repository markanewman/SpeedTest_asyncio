# Testing `asyncio`

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2023.04.11-success.svg)

I want to test out `asyncio` and develop patterns around it so I can copy paste.
Copilot is fine and all, but I am the one responsible for the result.
I need to know the value of the suggestion.

# Tests

Open a _regular_ PowerShell and run the code in the test.

* Test 1: Copy a 6.47GB CSV file over USB3.
  All trials conducted serially.
  The USB bus contained only the one device.
  ```{ps1}
  cd c:/repos/markanewman/SpeedTest_asyncio/test1
  New-Item -ItemType Directory d:/xxx
  Measure-Command { robocopy "d:/" "d:/xxx" tmp.csv }  
  Measure-Command { python -OO baseline.py -source "d:/tmp.csv" -dest "d:/xxx/tmp.2.csv" }
  Measure-Command { python -OO async.py -source "d:/tmp.csv" -dest "d:/xxx/tmp.2.csv" }
  remove-item -force -recurse d:/xxx
  ```  

# Results

* Test 1: robocopy = 386.8s, baseline = 745.4, async = ???
  * robocopy maintains a consistent speed when viewed in Task Manager 
  * baseline will run fine for the first little while, then the MB/s in Task Manager will hit 0.
    After it hits 0, it will stay there for a while, then pop back up.
    This cycle repeats
  * async ran foe over 45min before I stopped the process

