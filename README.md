# Data Splitter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Purpose

This script was created to split a .dat file into separate sample files to cut
down on data processing time. The result is individual sample files that are space-delimited.

![Demo data.](/assets/input-output.png)

## How to use

1) Put the .dat file that you want split into the /data/ folder. 
2) Go into the script (line 11) and change "YOUR_FILE.dat" to your data file name.
3) Run the script.
4) Check the /results/ folder for your new data files. 

## Inputs

This script requires a .dat file placed into the /data/ directory. 

## Outputs

This script will create files for each sample measured in a .dat file.
The output will write to the /results/ folder. 

## Notes

This script was made specifically for files produced by the CryoPC3 magnetometer control software,
but it may work with other softwares as well. 

## License

This script is published under the [MIT license](LICENSE.txt).