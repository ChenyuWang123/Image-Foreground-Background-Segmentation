#include <vector>
#include<iostream>
#include <fstream>
#include <string>
#include "Python.h"
#include <QDebug>
#include <stdio.h>
#include <direct.h>
#include <QByteArray>
using namespace std;


class Edge{
    public:
    int f, c, u, v;
    Edge(int flow, int capacity, int u, int v);
};

class G{
    int push(int u);
    void relabel(int u);
    void preflow();
    void setreverse(int i, int flow);
    vector<int> e;
public:
    int V;
    vector<Edge> edge;
    vector<int> h;
    G(int V);
    void add(int u, int v, int w);
    void mincut();
};

G::G(int V){
    this->V = V;
    for (int i = 0; i < V; i++){
        h.push_back(0);
        e.push_back(0);
    }
}

void G::add(int u, int v, int c){
    edge.push_back(Edge(0, c, u, v));
}

int overflow(vector<int>& v){
    for (int i = 1; i < v.size() - 1; i++)
        if (v[i] > 0)
            return i;
    return -1;
}

void G::setreverse(int i, int flow){
    for (int j = 0; j < edge.size(); j++){
        if (edge[j].v == edge[i].u && edge[j].u == edge[i].v){
            edge[j].f -= flow;
            return;
        }
    }
    Edge reverse = Edge(0, flow, edge[i].v, edge[i].u);
    edge.push_back(reverse);
}
int G::push(int u){
    for (int i = 0; i < edge.size(); i++){
        if (edge[i].u == u){
            if (edge[i].f == edge[i].c)
                continue;
            if (h[u] > h[edge[i].v]){
                int flow = min(edge[i].c - edge[i].f,e[u]);
                e[u]-= flow;
                e[edge[i].v] += flow;
                edge[i].f += flow;
                setreverse(i, flow);
                return 1;
            }
        }
    }
    return 0;
}

void G::relabel(int u){
    int mh = INT_MAX;
    for (int i = 0; i < edge.size(); i++){
        if (edge[i].u == u){
            if (edge[i].f == edge[i].c)
                continue;
            if (h[edge[i].v] < mh){
                mh = h[edge[i].v];
                h[u] = mh + 1;
            }
        }
    }
}

void G::mincut(){
    h[0] = V;
    for (int i = 0; i < edge.size(); i++){
        if (edge[i].u == 0){
            edge[i].f = edge[i].c;
            e[edge[i].v] += edge[i].f;
            edge.push_back(Edge(-edge[i].f, 0, edge[i].v, 0));
        }
    }
    while (overflow(e) != -1){
        int u = overflow(e);
        if (!push(u))
            relabel(u);
    }
}

Edge::Edge(int flow, int capacity, int u, int v){
    this->f = flow;
    this->c = capacity;
    this->u = u;
    this->v = v;
}





int maina()
{
    int L = flag.length();
    int k =0;
    for(int i=0;i<=L;i++){
        if (flag[L-i] == '/'){
            k = L-i;
            break;
        }
    }
    flag.chop(L-k-1);
    qDebug()<<flag;
    char* addr;
    QByteArray ba =flag.toLatin1();
    addr = ba.data();
    _chdir(addr);
    ifstream fin;
    fin.open("./456.txt");
    string s;
    std::vector<float> Gmmpre ={};
    while( fin >> s )
    {
        float k = stof(s);
        Gmmpre.push_back(k);
    }
    int p = 0;
    int t = 1+Gmmpre.size()/2;
    G g(t+1);

    for(int i = 0;i<Gmmpre.size()/2;i++){
        g.add(p, i+1, (int)(10000*Gmmpre[2*i]));
        g.add(i+1, t, 10000-(int)(10000*Gmmpre[2*i]));
    }
    g.mincut();
    vector<int> result = {};
    for(int i=1;i<g.V;i++){
        if (g.h[i]<g.V)
            result.push_back(1);
        else
            result.push_back(0);
    }
    fin.close();

    ofstream outFile("./re.txt");
    // the important part
    for (const auto &e : result) outFile << e << ",";

    return 0;

}
