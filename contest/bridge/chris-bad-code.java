import java.util.Scanner;
import java.math.*;

public class cf1352CALT2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n;
        int a;
        int k;

        int counter;
        int iter;
        int multiplier;

        for (int i = 0; i < t; i++) {
            // we know that this number is near k, but is more than k.
            // how much more than k?
            // the number of divisible numbers between 0 and the final answer.
            // we know the number of divisble numbers from 0 to k. this is floor(k/n)
            // let us call this a

            n = sc.nextInt();
            k = sc.nextInt();
            a = Math.floorDiv(k, n); // number of divisble numbers from 0 to k

            while (Math.floorDiv(k + a, n) - a != 0) {// number of divisble numbers from k to k+a
                a = Math.floorDiv(k + a, n);
            }

            // but to find out the rest will need more computation.
            // can we pre-find the answer? no
            // but we can get to this new number (k + a) and then find the number of
            // divisible numbers between k and that
            // then repeat recursively until the number is 0.

            System.out.println(k + a);

        }

    }

}