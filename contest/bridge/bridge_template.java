import java.io.*;

class Solution {
    /**
     * Return the height H in which the danger is minimized and satisfies the budget
     * constraints.
     *
     * B: a non-negative integer
     * N: a positive integer
     * S: an array of N integers
     */
    static long solve(long B, int N, long[] S) {
        // we are looking for the case that is the first to not exceed cost B
        long curHeight = 0;
        while (calcCost(S, curHeight) > B) {
            curHeight++;
        }

        // tie-breaker with danger?
        int curDanger = calcDanger(S, curHeight);
        if (calcDanger(S, curHeight + 1) == curDanger) { // means that we can skip to the next highest number
            int max = 10000000;
            for (int i = 0; i < N; i++) {
                if (S[i] < max && S[i] > curHeight) {
                    curHeight = S[i];
                }
            }
        }

        return curHeight;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    static int integral(long[] S) {
        int sum = 0;
        for (int i = 0; i < S.length; i++) {
            sum += S[i];
        }
        return sum;
    }

    static int calcDanger(long[] S, long height) {
        int sum = 0;
        for (int i = 0; i < S.length; i++) {
            if (S[i] > height) {
                sum += S[i] - height;
            } else {
                sum += S[i];
            }
        }
        return sum;
    }

    static int calcCost(long[] S, long height) {
        // return integral(S) - calcDanger(S, height);
        int sum = 0;
        for (int i = 0; i < S.length; i++) {
            if (S[i] > height) {
                sum += S[i] - height;
            }
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            long B = Long.parseLong(temp[0]);
            int N = Integer.parseInt(temp[1]);
            temp = in.readLine().split(" ");
            long[] S = new long[N];
            for (int j = 0; j < N; j++) {
                S[j] = Long.parseLong(temp[j]);
            }
            out.println(solve(B, N, S));
        }
        out.flush();
    }
    // Scanner sc = new Scanner(System.in);
    // int t = sc.nextInt();
    // long b;
    // int n;
    // for (int i = 0; i < t; i++) {
    // b = sc.nextLong();
    // n = sc.nextInt();
    // long[] s = new long[n];
    // for (int j = 0; j < n; j++) {
    // s[j] = sc.nextLong();
    // }
    // System.out.println(solve(b, n, s));
    // }
}
