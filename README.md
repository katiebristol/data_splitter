# Data Splitter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Purpose

This script was created to split a .dat file into separate sample files to cut
down on data processing time. The result is individual sample files that are space-delimited.

|Sample|Measurement|
|A|1|
|B|1|
|C|1|
|A|2|
|B|2|
|C|2|
|A|3|
|B|3|
|C|3|

to

|Sample|Measurement|
|A|1|
|A|2|
|A|3|

and so on, for each sample. 


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