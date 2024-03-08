#imports
import re
import os
import time


# banner image
banner = """
                                    
#   #   #   ####  #   # ####  ####  
 # #   # #  #   # #  ##  #    #   # 
  #   ##### ####  # # #  #### ####  
 # #  #   # #     ##  #  #  # #   # 
#   # #   # #     #   # ##### ####                                                                                                                                        
"""

print(banner)
        
time.sleep(0.5)
key = input("Enter your key: ")
steamkeyregex=re.match('[a-zA-Z0-9]{4,6}-', key)
if steamkeyregex is None:
	  
        print("Other key detected!")
	  
else:
	  
        print("Steam key detected!")

pause()
