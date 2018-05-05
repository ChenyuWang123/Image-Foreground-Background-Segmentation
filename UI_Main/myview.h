#ifndef MYVIEW_H
#define MYVIEW_H

#include <QGraphicsView>
#include <QFileDialog>
#include <QGraphicsScene>
#include <QGraphicsPixmapItem>
#include <QMouseEvent>
#include <QDebug>
#include <QByteArray>

class MyView : public QGraphicsView
{
    Q_OBJECT
public:
    explicit MyView(QWidget *parent = 0);
    
signals:
    
public slots:
    void OpenImage();
    void runProgramm();
protected:
    void mousePressEvent(QMouseEvent *event);
private:
    QPixmap pixmap;
    QGraphicsPixmapItem *pixmapItem;
    QGraphicsScene *scene;
};
extern QString flag;


#endif // MYVIEW_H
