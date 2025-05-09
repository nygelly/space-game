def on_on_score():
    astroid.ay = 30000
    astroid.vx = 30000
info.on_score(3000, on_on_score)

def on_on_score2():
    astroid.ay = 4000
    astroid.ax = 4000
info.on_score(400, on_on_score2)

def on_on_score3():
    game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
info.on_score(info.high_score(), on_on_score3)

def on_on_score4():
    astroid.ay = 6000
    astroid.ax = 6000
info.on_score(600, on_on_score4)

def on_up_pressed():
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_score5():
    astroid.ay = 2500
    astroid.ax = 2500
info.on_score(250, on_on_score5)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
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
            """),
        mySprite,
        0,
        50)
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_score6():
    astroid.ay = 10000
    astroid.ax = 10000
info.on_score(1000, on_on_score6)

def on_on_score7():
    astroid.ay = 8000
    astroid.ax = 8000
info.on_score(800, on_on_score7)

def on_on_score8():
    astroid.ay = 7500
    astroid.ax = 7500
info.on_score(750, on_on_score8)

def on_left_pressed():
    music.play(music.melody_playable(music.sonar),
        music.PlaybackMode.IN_BACKGROUND)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_score9():
    astroid.ay = 3000
    astroid.ax = 3000
info.on_score(300, on_on_score9)

def on_on_score10():
    astroid.ay = 15000
    astroid.ax = 15000
info.on_score(1500, on_on_score10)

def on_on_score11():
    astroid.ay = 9500
    astroid.ax = 9500
info.on_score(950, on_on_score11)

def on_on_overlap(sprite2, otherSprite2):
    info.change_life_by(-1)
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_zero(status):
    sprites.destroy(status.sprite_attached_to())
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_score12():
    astroid.ay = 1000
    astroid.ax = 1000
info.on_score(100, on_on_score12)

def on_on_score13():
    astroid.ay = 9000
    astroid.ax = 9000
info.on_score(900, on_on_score13)

def on_on_score14():
    astroid.ay = 6500
    astroid.ax = 6500
info.on_score(650, on_on_score14)

def on_right_pressed():
    music.play(music.melody_playable(music.sonar),
        music.PlaybackMode.IN_BACKGROUND)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_score15():
    game.game_over(False)
    music.play(music.melody_playable(music.wawawawaa),
        music.PlaybackMode.IN_BACKGROUND)
    game.set_game_over_message(False, "You lost?")
    effects.blizzard.end_screen_effect()
info.on_score(0, on_on_score15)

def on_on_score16():
    astroid.ay = 25000
    astroid.ax = 25000
info.on_score(2500, on_on_score16)

def on_down_pressed():
    music.play(music.melody_playable(music.sonar),
        music.PlaybackMode.IN_BACKGROUND)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_score17():
    astroid.ay = 20000
    astroid.ax = 20000
info.on_score(2000, on_on_score17)

def on_on_score18():
    astroid.ay = 1500
    astroid.ax = 1500
info.on_score(150, on_on_score18)

def on_on_score19():
    astroid.ay = 35000
    astroid.ax = 35000
info.on_score(3500, on_on_score19)

def on_on_score20():
    astroid.ay = 8500
    astroid.ax = 8500
info.on_score(850, on_on_score20)

def on_on_score21():
    astroid.ay = 5000
    astroid.ax = 5000
info.on_score(500, on_on_score21)

def on_on_score22():
    astroid.ay = 4500
    astroid.ax = 4500
info.on_score(450, on_on_score22)

def on_on_score23():
    astroid.ay = 2000
    astroid.ax = 2000
info.on_score(200, on_on_score23)

def on_on_score24():
    astroid.ay = 5500
    astroid.ax = 5500
info.on_score(550, on_on_score24)

def on_on_score25():
    game.game_over(True)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.UNTIL_DONE)
    game.set_game_over_message(True, "You Win!")
    effects.confetti.end_screen_effect()
info.on_score(100000000, on_on_score25)

def on_on_score26():
    astroid.ay = 3500
    astroid.ax = 3500
info.on_score(350, on_on_score26)

def on_on_score27():
    astroid.ay = 7000
    astroid.ax = 7000
info.on_score(700, on_on_score27)

def on_on_overlap2(sprite, otherSprite):
    sprites.destroy(sprite)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite).value += -50
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

statusbar: StatusBarSprite = None
projectile: Sprite = None
astroid: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
music.play(music.create_song(hex("""
        0078000408020205001c000f0a006400f4010a0000040000000000000000000000000000000002220000000400021d2a08000c00012710001400021d2a18001c000220272000240002202706001c00010a006400f401640000040000000000000000000000000000000002250000000400031d242a08000c0002202710001400031d242a18001c0002202720002400022027
        """)),
    music.PlaybackMode.UNTIL_DONE)
mySprite = sprites.create(img("""
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
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global astroid, statusbar
    astroid = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    astroid.y = scene.screen_height()
    astroid.vy = -25
    astroid.x = randint(10, scene.screen_width() - 20)
    statusbar = statusbars.create(15, 2, StatusBarKind.enemy_health)
    statusbar.max = 100
    statusbar.set_label("HP")
    statusbar.set_color(7, 2)
    statusbar.attach_to_sprite(astroid)
game.on_update_interval(1000, on_update_interval)
