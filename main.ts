namespace SpriteKind {
    export const lol_mail = SpriteKind.create()
    export const app = SpriteKind.create()
    export const mouse = SpriteKind.create()
    export const index = SpriteKind.create()
    export const key = SpriteKind.create()
}
/**
 * page (1) = start screen
 * 
 * page (0) = app screen
 */
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.createSoundEffect(WaveShape.Square, 932, 1, 255, 68, 75, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
controller.combos.attachCombo("up, up, down, down, left, right, left, right, B, A, B, A", function () {
    music.play(music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
    keyboard = sprites.create(assets.image`key board`, SpriteKind.index)
    key_1 = sprites.create(assets.image`key 1`, SpriteKind.key)
    key_1.setPosition(8, 66)
    key_2 = sprites.create(assets.image`key 2`, SpriteKind.key)
    key_2.setPosition(8, 66)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.createSoundEffect(WaveShape.Noise, 3900, 4601, 255, 68, 10, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
let key_2: Sprite = null
let key_1: Sprite = null
let keyboard: Sprite = null
scene.setBackgroundImage(assets.image`準則`)
let mail = sprites.create(assets.image`mail`, SpriteKind.app)
let app_store = sprites.create(assets.image`appstore`, SpriteKind.Text)
let mouse = sprites.create(assets.image`mouse`, SpriteKind.mouse)
controller.moveSprite(mouse)
mail.setPosition(19, 106)
app_store.setPosition(36, 106)
