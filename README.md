# ECE2112-PA-3
- Robie Galang
- September 15, 2024
- PA #3 Submission

# Libraries Used:
- pandas

# Problem 1
## Task:
- Load the corresponding .csv file
- display the first and last 5 rows of the spreadsheet
## Approach
- loading the .csv file was fairly simple, just used the built in function that panda provided which is the .read code
- for displaying, thanks to the function .head() and .tail(), I was able to attack the code easily as the two codes mentioned does exactly what the problem asks

#Problem 2
## Task:
- Display the first five rows with odd-numbered columns
- Display the row that constains the 'Model' of 'Mazda RX4'
- How many cylinders does the car model 'Camaro Z28' have?
- Determine how many cylinders and what gear type tha car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have

## Approach
- For the first task, I used .iloc function to slice the first five rows and every second column by setting the increment to 2
- To display the row that specifically contains the model 'Mazda RX4' I used .loc() to filter the DataFrame by the value in the 'Model' column
- I used .loc() and just input the row index and column name to filter the value that I wanted to get
- To output the specific rows and columns that I needed, i used .loc() and used proper enclosing of brackets on the index of the rows I wanted to filter out and the name of the columns I wanted to print out or in technical terms, it is known as label-based indexing

# Learnings
- I learned that the pandas library contained a lot very useful functions that helps you traverse on multidimensional array like data. Just like how I used the .loc() function to pick out the data values of specific rows and columns that I wanted to output.

# Versions
- 1.0
- 1.1
  -- Just changed the current working path into a new path for orderliness.
