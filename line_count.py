def line_count():
  count = 0
  #start the count at 0
  file = open('file.txt', 'r')
  #open the file
  lines = file.readlines()
  #get the program to read the lines in the file
  for line in lines:
    #start a for loop
    count = count + 1
    #get the program to add 1 to count, everytime it reads a line
  file.close()
  #close the file to save and not screw up the data
  return(count)
  #get the program to return you the number of lines it counted in the file
