#Please use the pyglet library to create a Hello world application

import pyglet
# window = pyglet.window.Window()
# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')
#
# @window.event
# def on_draw():
#     window.clear()
#     label.draw()
#
# pyglet.app.run()

new_window = pyglet.window.Window()

label = pyglet.text.Label('Hello, World !',
                          font_name ='Cooper',
                          font_size = 16,
                          x = new_window.width//2,
                          y = new_window.height//2,
                          anchor_x ='center',
                          anchor_y ='center')
@new_window.event
def on_draw():
    new_window.clear()
    label.draw()

pyglet.app.run()