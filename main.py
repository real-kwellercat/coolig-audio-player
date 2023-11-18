print("Coolig. The Cool ig.")
import pyglet
import sys
window = pyglet.window.Window()
image = pyglet.resource.image('wat.png')
player = pyglet.media.Player()
window.set_size(386,356)
@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    
def on_eos():
    print("Audio playback ended.")
    sys.exit()

music = pyglet.resource.media('boppin.mp3')
player.queue(music)
player.push_handlers(on_eos)

player.play()

is_playing = player.playing
pyglet.app.run()


