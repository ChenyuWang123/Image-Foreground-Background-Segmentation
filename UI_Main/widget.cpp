#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    QVBoxLayout *layout = new QVBoxLayout;
    QPushButton *openBtn1 = new QPushButton("open Image",this);
    QPushButton *openBtn2 = new QPushButton("run your code",this);
    view = new MyView(this);

    connect(openBtn1,SIGNAL(clicked()),view,SLOT(OpenImage()));
    connect(openBtn2,SIGNAL(clicked()),view,SLOT(runProgramm()));

    layout->addWidget(openBtn1);
    layout->addWidget(openBtn2);
    layout->addWidget(view);

    setLayout(layout);
}

Widget::~Widget()
{
    
}
