# This script automates creating customer folders.
# V 1.1
# 01/04/2021
# By Dinesha Dayananda

# Pesudocode:
# IF  exists (NewCustomers.txt ) THEN  
#           SET customerNamesArray = readLines(NewCustomers.txt)        
#           SET finalValue = size(customerNamesArray)         
#           SET counter  = 0    
#           FOR index = counter to finalValue
#                       TRY createFolder                            
#                        IF throwException(folderExists) 
#                                   PRINT("<FirstnameLastname> folder already exists")
#                        ELSE
#                                    PRINT("<FirstnameLastname> folder created.)
    
#                        ENDIF
#                        counter = counter + 1
# ELSE
#           PRINT("NewCustomers.txt  does not exist. Please save NewCustomers.txt in the Administration folder and retry. ")
# ENDIF 
# 
# **The folders are created at the file server and  script is run from DC1 server.
#   So, the script should include the Absolute Path to the location where folders created
#   (\Administration\New_Customers\ ) on the file server. Relative path wouldn't work.
  
import os 

# If the current working directory is not the parent directory of this script,
# change the cwd to the parent directory of this script.
if os.getcwd() != os.path.dirname(os.path.realpath(__file__)) :
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    # Parent directory where the customer folders are created.
    parent_dir = "/home/dd/MyDocuments/Administration/New_Customers/"
    # Open the NewCustomers.txt and read each line into fl.
    f = open("NewCustomers.txt", "r")
    fl = f.readlines()
    # Loop through the lines and try to create a folder for each line.
    for x in fl:
        directory = x.title().replace(" ", "")    
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path)
            print("A new directory is created for % s " % x)
        except FileExistsError:
            print("A directory already exists for % s" % x)
        except:
            print("Something unusual has happened. Please contact the Development team.")
except FileNotFoundError: # if NewCustomers.txt doesn't exist at the right location.
    print("NewCustomers.txt is not in the same folder where this script is. \n Please save the file and try again.")
