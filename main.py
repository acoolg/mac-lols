@namespace
class SpriteKind:
    lol_mail = SpriteKind.create()
    app = SpriteKind.create()
    mouse = SpriteKind.create()
    index = SpriteKind.create()
    key = SpriteKind.create()
"""

page (1) = start screen

page (0) = app screen

"""

def on_a_pressed():
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            932,
            1,
            255,
            68,
            75,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_combos_attach_combo():
    global keyboard, key_1
    music.play(music.create_sound_effect(WaveShape.SINE,
            200,
            600,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
    keyboard = sprites.create(assets.image("""
        key board
    """), SpriteKind.index)
    key_1 = sprites.create(assets.image("""
        key 1
    """), SpriteKind.key)
controller.combos.attach_combo("up, up, down, down, left, right, left, right, B, A, B, A",
    on_combos_attach_combo)

def on_b_pressed():
    music.play(music.create_sound_effect(WaveShape.NOISE,
            3900,
            4601,
            255,
            68,
            10,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

key_1: Sprite = None
keyboard: Sprite = None
scene.set_background_image(assets.image("""
    準則
"""))
mail = sprites.create(assets.image("""
    mail
"""), SpriteKind.app)
app_store = sprites.create(assets.image("""
    appstore
"""), SpriteKind.text)
mouse2 = sprites.create(assets.image("""
    mouse
"""), SpriteKind.mouse)
controller.move_sprite(mouse2)
mail.set_position(19, 106)
app_store.set_position(36, 106)