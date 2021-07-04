#This script require twint and nest_asyncio library
#Please make sure to install this by using the installation procedure from its origin https://github.com/twintproject/twint

import twint
import nest_asyncio
nest_asyncio.apply()

#Twint script starts from here
c.Search = "ImageJ"           #name of software is defined here
c.since = "2010-01-01"        #first starting date for the twit search
c.Until = "2020-12-31"        #last date for the twit search
c.Hide_output = True          #stop printing in the terminal, if it's changed into False, you will print every search
c.lang = "English"            #This limit the twit into only English twit. This doesn't work 100%, however, this filter the only filter could work best atm.
c.Output = "file.csv"          #This to define the output filename and filetype. The .csv is recommended to ease the data processing later

#Running the twint script
twint.run.Search(c) #by executing this, you will start to run your search and you will find your results within the same folder of this script
