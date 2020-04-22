#HW_01

## Dice Throwing

Anti-Corona team work to see self-organization of the student community in pandemic times.  
Each of the student subscribed to EP4 should perform the  coin  flip  experiment  and  record  one  single  random  trajectory  of  alengthN= 100.
That means each student fills in four columns each of length  100.  
The  first  column A is  simply  the  trial  number i from  1  to100 (Ai=i).  
The second column B is the result of flipping of the coin you use, either +1 or -1.  
The third column C is the sum over the second column,  e.g.Ck=∑ki=1Bi.   
This  is  an  analogue  of  the  displacement. Finally,  the  fourth  column D represents  the  mean  square  displacement D k=∑ki=1(Ci)2



Afterwards,  you  need  to  find  one  person  who  will perform  an  average  over  the  EP4-ensemble  of  the  results  obtained  and will deliver two graphs:

1. a graph showing all individual displacements (Ci vs.i) and the ensemble-averaged displacement


2.  a graph showing all individual mean square displacements (Di vs.i) and the ensemble-averaged MSD.




## Code Comments
This week we explore the different ways of how to create and manipulate data using the numpy library.
In the dicesheet.py, one finds the following functions:

### numpy_looping_function

This is a basic and quite understandable way to loop through an initially zero 3D array, and change the values
throughout the loop.

### vectorized_function
This function utilizes "vectorization", i.e. efficiently using the entire array as opposed to looping through it

### MSD
Functions to calculate the mean squared displacement

### Plot creator
Using matplotlib to make pretty plots of the data

### Main
One function to rule them all!
Using this, we can put only the functions we want to use each time we run the program.

## Discussion
As an output, we receive the time it takes for the two types of data creating functions:

Looping created arrays in 0.0965 seconds
Vectorizing created arrays in 0.0069 seconds
Thus vectorizing is much, much more efficient for big data!

In addition, we receive the two graphs:
![Individual Displacements](/results/IndividualDisplacements.png)
![MSD](/results/Running_Average_Displacements.png)
