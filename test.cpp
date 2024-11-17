#include <bits/stdc++.h>
#include <chrono>
using namespace std;

int main(void) {
    cin.tie(0)->sync_with_stdio(0);

    auto start = chrono::high_resolution_clock::now();

    cout << "Blade Runner\n";

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cerr << "Execution time: " << duration.count() << " seconds." << '\n';

    return 0;
}
