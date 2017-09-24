Creating Alias

I performed following steps to set up environment variable

1. Created a folder named PUI2017 on my CUSP Compute

![Creating Folder on Compute](https://github.com/ssb10/PUI2017_ssb602/blob/master/HW2_ssb602/Creating_folder.png)


2. Edited the bash_profile
  Added the following lines
  export PUI2017="/home/cusp/ssb602/PUI2017"
  alias pui2017 = "cd $PUI2017"
  
  ![Editing bash_profile](https://github.com/ssb10/PUI2017_ssb602/blob/master/HW2_ssb602/bashrc_scrrenshot.png)
  

3. Used the command source .bash_profile save and run the changes
In order to check if the alias was created I ran following commands:
i)echo $PUI2017 --> This returned the path to PUI2017
ii)pui2017 --> this took me to the directory PUI2017

![Checking if alias works](https://github.com/ssb10/PUI2017_ssb602/blob/master/HW2_ssb602/Terminal_Screenshot.png)

