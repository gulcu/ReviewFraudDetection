# ReviewFraudDetection

The code implements a scenario where review spammers are distinguished from honest reviewers with the help of the model proposed by Wang, Sihong, Liu & Yu's paper "Identify Online Store Review Spammers via Social Review Graph" which appeared in ACM Transactions on Intelligent Systems and Technology. The article can be found here:
http://www.cs.ucsb.edu/~gangw/yelp/graph-2011.pdf

To study the computation framework described by the paper, we wanted to see how the iterative process converges after assigning initial values of Trustiness T(r) = 1 for all reviewers r, and Reliability E(s) = 1 for all stores s. Initial Honesty H(v) values for each review v do not matter since they are immediately calculated from the other initial values at the start.  
The example we studied is a very intutitive one. Store s0 is a good store, and s1 is a bad one. Reviewers r0 to r2 are trustable, whereas r3 is not. They rate each store on a 1 to 5(excellent) scale in the following way: 
 ________________________________________________________
| r:Reviewer ID | v:Review ID | s:Store Id  | a:Rating  |
|---------------|-------------|-------------|-----------|
|       0       |      0      |       0     | 5 Stars   |
|       0       |      1      |       1     | 1 Star    |
|       1       |      2      |       0     | 5 Stars   |
|       1       |      3      |       1     | 1 Star    |
|       2       |      4      |       0     | 4 Stars   |
|       2       |      5      |       1     | 2 Stars   |
|       3       |      6      |       0     | 1 Star    |
|       3       |      7      |       1     | 5 Stars   |
_________________________________________________________

The Pyhon program ReviewFraudDetection.py generates graphs of the values calculated for the Trustiness, Honesty and Reliability measures after each iteration of the algorithm proposed by Wang et al. Currently the only purpose is to generate those graphs so I am not planning to refactor or clean up the cryptic code. However, I intend to devise my own solutions which will have cleaner and documented code.
