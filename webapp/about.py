import justpy as jp


class About:
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the About page!', classes='text-4xl m-2')
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
