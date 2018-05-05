#include "myview.h"
#include <QDebug>
#include <QProcess>
#include "123.cpp"
#include "145233.cpp"
#include "show.cpp"
using namespace std;

QString flag ="null";
QString flag1 ="null";

MyView::MyView(QWidget *parent) :
    QGraphicsView(parent)
{
    pixmapItem = new QGraphicsPixmapItem;
    scene = new QGraphicsScene(this);
    setScene(scene);
}

void MyView::OpenImage()
{
    foreach (QGraphicsItem *item, scene->items()) {
        scene->removeItem(item);
    }
    QString fileName = QFileDialog::getOpenFileName(
                this, "open image file",
                ".",
                "Image files (*.bmp *.jpg *.pbm *.pgm *.png *.ppm *.xbm *.xpm);;All files (*.*)");
    if (!fileName.isEmpty()) {
        flag = fileName;
        pixmap = QPixmap(fileName);
        pixmapItem->setPixmap(pixmap);
        scene->addItem(pixmapItem);
        flag1 =fileName;
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
        char* addr1;
        QByteArray ba1 =flag1.toLatin1();
        addr1 = ba1.data();
        _chdir(addr);
        ofstream outfile("./location.txt");
        outfile << addr1;
    } else
        return;
}


void MyView::runProgramm()
{


    if (!flag.isEmpty()) {
        qDebug()<<flag;
    }
Py_Initialize();
    main12345();
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
    fstream _file;
    _file.open("./456.txt",ios::in);
    while(!_file){
        _file.open("./456.txt",ios::in);
    }
    cout<<"1"<<endl;


    maina();
    cout<<"2"<<endl;

    showa();
    cout<<"done"<<endl;
   Py_Finalize();

       foreach (QGraphicsItem *item, scene->items()) {
           scene->removeItem(item);
       }
   pixmap = QPixmap("./one");
   pixmapItem->setPixmap(pixmap);
   scene->addItem(pixmapItem);


}

void MyView::mousePressEvent(QMouseEvent *event)
{
    qDebug()<<"Image Pos:"<<pixmapItem->mapFromScene(mapToScene(event->pos()));
    QPointF s = pixmapItem->mapFromScene(mapToScene(event->pos()));
    qDebug()<< s.x()<<endl;
    ofstream outfile("./coordinate.txt");
    outfile << s.x()<<endl;
    outfile << s.y()<<endl;

}
