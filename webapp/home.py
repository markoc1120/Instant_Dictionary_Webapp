import justpy as jp


class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view='hHh lpR fFf')
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model='left', bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/home', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-2')
        jp.Div(a=div, text='This is the Home page!', classes='text-4xl m-2')
        jp.Div(a=div, text="""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent imperdiet a turpis in suscipit. Mauris 
                pulvinar massa nisi, quis malesuada augue molestie nec. Donec consectetur hendrerit mollis. Sed ut magna et 
                lectus sollicitudin pharetra a commodo lectus. Quisque tortor arcu, sodales id urna vitae, rhoncus congue 
                augue. Suspendisse luctus congue purus ac aliquam. Etiam vestibulum, leo nec fringilla ultricies, urna metus 
                luctus ante, nec placerat mauris lectus id lorem. Sed in bibendum ligula, a ornare leo. In hac habitasse platea 
                dictumst. Cras porta, tellus sit amet iaculis vestibulum, orci dui semper turpis, eget consequat metus arcu 
                vitae nisl. In mattis nibh vitae dictum volutpat. In porta tellus nec luctus mattis. Duis eleifend magna ut 
                vulputate elementum. Pellentesque ex orci, pulvinar vel condimentum ut, tincidunt non nulla.
                """, classes='text-lg')
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
