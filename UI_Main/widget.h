#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include "myview.h"

class Widget : public QWidget
{
    Q_OBJECT
    
public:
    Widget(QWidget *parent = 0);
    ~Widget();
signals:
    void openFile();
private:
    QPushButton *openBtn;
    MyView *view;
};

#endif // WIDGET_H
