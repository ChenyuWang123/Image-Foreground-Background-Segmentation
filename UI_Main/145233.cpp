#include "Python.h"
#include "Python.h"
#include <QDebug>
#include <stdio.h>
#include <direct.h>
#include <QByteArray>
void main12345() {
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
    PyRun_SimpleString("exec(open('./GMM.py').read())");

}
