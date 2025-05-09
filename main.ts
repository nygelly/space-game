info.onScore(3000, function () {
    astroid.ay = 30000
    astroid.vx = 30000
})
info.onScore(400, function () {
    astroid.ay = 4000
    astroid.ax = 4000
})
info.onScore(info.highScore(), function () {
    game.setGameOverScoringType(game.ScoringType.HighScore)
})
info.onScore(600, function () {
    astroid.ay = 6000
    astroid.ax = 6000
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
})
info.onScore(250, function () {
    astroid.ay = 2500
    astroid.ax = 2500
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . 2 1 2 . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, mySprite, 0, 50)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
})
info.onScore(1000, function () {
    astroid.ay = 10000
    astroid.ax = 10000
})
info.onScore(800, function () {
    astroid.ay = 8000
    astroid.ax = 8000
})
info.onScore(750, function () {
    astroid.ay = 7500
    astroid.ax = 7500
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.sonar), music.PlaybackMode.InBackground)
})
info.onScore(300, function () {
    astroid.ay = 3000
    astroid.ax = 3000
})
info.onScore(1500, function () {
    astroid.ay = 15000
    astroid.ax = 15000
})
info.onScore(950, function () {
    astroid.ay = 9500
    astroid.ax = 9500
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1)
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.cameraShake(4, 500)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    sprites.destroy(status.spriteAttachedTo())
})
info.onScore(100, function () {
    astroid.ay = 1000
    astroid.ax = 1000
})
info.onScore(900, function () {
    astroid.ay = 9000
    astroid.ax = 9000
})
info.onScore(650, function () {
    astroid.ay = 6500
    astroid.ax = 6500
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.sonar), music.PlaybackMode.InBackground)
})
info.onScore(0, function () {
    game.gameOver(false)
    music.play(music.melodyPlayable(music.wawawawaa), music.PlaybackMode.InBackground)
    game.setGameOverMessage(false, "You lost?")
    effects.blizzard.endScreenEffect()
})
info.onScore(2500, function () {
    astroid.ay = 25000
    astroid.ax = 25000
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.sonar), music.PlaybackMode.InBackground)
})
info.onScore(2000, function () {
    astroid.ay = 20000
    astroid.ax = 20000
})
info.onScore(150, function () {
    astroid.ay = 1500
    astroid.ax = 1500
})
info.onScore(3500, function () {
    astroid.ay = 35000
    astroid.ax = 35000
})
info.onScore(850, function () {
    astroid.ay = 8500
    astroid.ax = 8500
})
info.onScore(500, function () {
    astroid.ay = 5000
    astroid.ax = 5000
})
info.onScore(450, function () {
    astroid.ay = 4500
    astroid.ax = 4500
})
info.onScore(200, function () {
    astroid.ay = 2000
    astroid.ax = 2000
})
info.onScore(550, function () {
    astroid.ay = 5500
    astroid.ax = 5500
})
info.onScore(100000000, function () {
    game.gameOver(true)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
    game.setGameOverMessage(true, "You Win!")
    effects.confetti.endScreenEffect()
})
info.onScore(350, function () {
    astroid.ay = 3500
    astroid.ax = 3500
})
info.onScore(700, function () {
    astroid.ay = 7000
    astroid.ax = 7000
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite).value += -50
    info.changeScoreBy(1)
})
let statusbar: StatusBarSprite = null
let projectile: Sprite = null
let astroid: Sprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
music.play(music.createSong(hex`
            0078000408020205001c000f0a006400f4010a0000040000000000000000000000000000000002220000000400021d2a08000c00012710001400021d2a18001c000220272000240002202706001c00010a006400f401640000040000000000000000000000000000000002250000000400031d242a08000c0002202710001400031d242a18001c0002202720002400022027
            `), music.PlaybackMode.UntilDone)
mySprite = sprites.create(img`
    c c c c c c e e 2 2 2 2 4 2 e e 
    c c c c c c e e 2 2 2 4 2 2 e e 
    . c c c c e e 2 2 2 2 4 2 e e . 
    . . c f f f c c e e f f e e . . 
    . . . . e e 2 2 2 4 e e . . . . 
    . . . . . c c c e e e . . . . . 
    . . . . . . e 2 4 e . . . . . . 
    . . . . . . e e 4 e . . . . . . 
    . . . . . . . e 2 . . . . . . . 
    . . . . . . . f f . . . . . . . 
    . . . . . . . c 2 . . . . . . . 
    . . . . . . . f f . . . . . . . 
    . . . . . . . c b . . . . . . . 
    . . . . . . . c d . . . . . . . 
    . . . . . . . c d . . . . . . . 
    . . . . . . . c d . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
mySprite.setStayInScreen(true)
info.setLife(3)
game.onUpdateInterval(1000, function () {
    astroid = sprites.create(img`
        . . . . . . . . . c c 8 . . . . 
        . . . . . . 8 c c c f 8 c c . . 
        . . . c c 8 8 f c a f f f c c . 
        . . c c c f f f c a a f f c c c 
        8 c c c f f f f c c a a c 8 c c 
        c c c b f f f 8 a c c a a a c c 
        c a a b b 8 a b c c c c c c c c 
        a f c a a b b a c c c c c f f c 
        a 8 f c a a c c a c a c f f f c 
        c a 8 a a c c c c a a f f f 8 a 
        . a c a a c f f a a b 8 f f c a 
        . . c c b a f f f a b b c c 6 c 
        . . . c b b a f f 6 6 a b 6 c . 
        . . . c c b b b 6 6 a c c c c . 
        . . . . c c a b b c c c . . . . 
        . . . . . c c c c c c . . . . . 
        `, SpriteKind.Enemy)
    astroid.y = scene.screenHeight()
    astroid.vy = -25
    astroid.x = randint(10, scene.screenWidth() - 20)
    statusbar = statusbars.create(15, 2, StatusBarKind.EnemyHealth)
    statusbar.max = 100
    statusbar.setLabel("HP")
    statusbar.setColor(7, 2)
    statusbar.attachToSprite(astroid)
})
