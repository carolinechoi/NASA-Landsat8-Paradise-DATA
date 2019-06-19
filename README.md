# NASA SEES Algorithm

Reading real data files with temperature data - the problem was the temperature data was in Kelvin. And for our purposes it needs to be in both Celsius and Fahrenheit!

Requirements:
1. To read in the temperature values without destroying the position of each data value.
2. Write the data out into a new temperature data files (one for Celsius and one for Fahrenheit).
3. There are well known conversion formulas for converting Kelvin into both of our target temperature scales. Find the formula and convert them into code.
4. **Final Goal** Process the 3 larger ASCII text files.

The data is set into columns and rows positionally (because it is a text file). The data has spatial information about the location of the data (useful but not germane) as well as information about these columns and rows at the top of each file - a potentially useful bit of information? 

## About The Data

More info about the data you will work with. These ASCII files are derived from satellite images taken before, during and after the California Paradise Fire in October of last year (2018). Specifically, the data are from the Landsat 8 Thermal Infrared Sensor (TIRS). 

These images below help visualize the thermal TIRS data that I processed. 

![true colour image](https://drive.google.com/uc?export=view&id=1fK3k6fiHRDTgQOylvsFoTcmW2pdSIy2M)

![false colour image](https://drive.google.com/uc?export=view&id=1z_x89GBdqJ1e8oLIXmdiP9ppOaWLMhKz)
