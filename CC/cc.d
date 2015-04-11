import std.stdio;
import std.string;

int main()
{
    auto file = new File("inp.dat", "r");
    int n, m;
    file.readf("%d %d", &n, &m);

    auto G = new int[10^3][10^3];
    for (int i = 0; i < m; i++) {
        int u, v;
        file.readf("%d %d", &u, &v);
        G[u-1][v-1] = 1;
    }
    writeln(G);

    file.close();
    return 0;
}
