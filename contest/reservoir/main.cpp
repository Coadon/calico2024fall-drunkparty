#include <functional>
#include <iostream>
#include <vector>

using namespace std;

// SEGFAULT


int comps(int N, int M, vector<vector<bool>> &nodes) {
    bool visited[N][M];
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (nodes[i][j]) {
                visited[i][j] = true; // censor it
            }
        }
    }
    std::function<void(int,int)> dfs = [&] (int i, int j) {
        if (visited[i][j]) return;
        visited[i][j] = true;
        // process
        if ( i+1 <= N && nodes[i+1][j]) {
            dfs(i+1, j);
        }
        if (nodes[i-1][j]) {
            dfs(i-1, j);
        }
        if ( j+1 <= M && nodes[i][j+1]) {
            dfs(i, j+1);
        }
        if (nodes[i][j-1]) {
            dfs(i, j-1);
        }
    };
    auto find_false = [&] () -> pair<int,int> {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                if (!visited[i][j]) {
                    return {i, j};
                }
            }
        }
        return {-1, -1};
    };
    for (int islands = 0; true; islands++) {
        pair<int,int> f = find_false();
        if (f.first == -1) return islands;
        dfs(f.first, f.second);
    }
}

/**
 * Return the maximum number of islands.
 *
 * N: number of rows
 * M: number of columns
 * G: grid of heights
 */
int solve(int N, int M, vector<vector<int>> &G, int peak) {
    pair<int,int> max_islands = {0,0};
    for (int h = 1; h <= peak; h++) {
        vector<vector<bool>> nodes;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++) {
                nodes[i][j] = G[i][j] >= h;
        }
        int islands = comps(N, M, nodes);
        if (max_islands.second <= islands) {
            max_islands = {h, islands};
        }
    }
    return max_islands.first;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int peak = 0;
        int N, M;
        cin >> N >> M;
        vector<vector<int>> G(N, vector<int>(M));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++) {
                cin >> G[i][j];
                peak = max(peak, G[i][j]);
        }
        cout << solve(N, M, G, peak) << '\n';
    }
}
