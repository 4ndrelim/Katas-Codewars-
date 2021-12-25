// Description 

// The task is simply stated. Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n. 
// Come up with the best algorithm you can; you'll need it!

// Examples:
// sum_of_squares(17) = 2 
// 17 = 16 + 1 (4 and 1 are perfect squares).
// sum_of_squares(15) = 4 
// 15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
// sum_of_squares(16) = 1 
// 16 itself is a perfect square.

// Time constraints:
// 1. 5 easy (sample) test cases: n < 20
// 2. 5 harder test cases: 1000 < n < 15000
// 3. 5 maximally hard test cases: 5e8 < n < 1e9
// 4. 300 random maximally hard test cases: 1e8 < n < 1e9

  
import java.lang.Math;
public class SumOfSquares {
    //greedy approach. Fails. This kata requires knowledge from Number Theory
    static int helper(int n, int cap, int count){
        if (n==0){return count;}
        Integer minCount = Integer.MAX_VALUE;
        for (int i = cap; i >0; i--){
          int currCount = count;
          int newN = n;
          while (newN >= i*i){
            currCount++;
            newN-=i*i;
          }
          int newCount = helper(newN, (int) Math.sqrt(newN), currCount);
          minCount = Math.min(newCount, minCount);
        }
        return minCount;
    }
    static boolean isSquare(int n){
        if (Math.sqrt(n)%1==0){return true;}
        return false;
    }
    public static int nSquaresFor(int n) {
        //int count = 0;
        //return helper(n, (int) Math.sqrt(n), count);
        //Lagrange's FSQT
        if (isSquare(n)){return 1;}
        for (int i = 1; i < (int) Math.sqrt(n); i++){
            if (isSquare(n-i*i)){return 2;}
        }
        while (n%4==0){
            n/=4;
        }
        if ((n-7)%8==0){return 4;}
        else{return 3;}
    }
}
