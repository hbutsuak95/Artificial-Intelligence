
                                        Artificial Intelligence (CS60045)
                                      Assignment 2 (Programming assignment)
Read the following problem and implement it using any language of your choice (C, C++ , Java or Python). Submit a Report on this problem along with your codes. Also show the input and intermediate stages for a few instances.
Your Report should contain the heuristic used for the search, the number of nodes expanded and the time taken by the different algorithms.



Q1:
Implement A* and IDA* search to solve the 8-puzzle problem. Implement the following heuristics:

a. ha(n)=0; i.e. leading to breadth-first search
b. hb(n)=the number of misplaced tiles (excluding the blank tile)
c. hc(n)= the sum of the distances of the tiles from their goal positions (excluding the blank tile)

Generate a set of 100 random initial boards and test A* and IDA*, running all the heuristics on each of the 100 problems. 
Compare the number of nodes expanded and the running time of A* and IDA* for each of the problems.
