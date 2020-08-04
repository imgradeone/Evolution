# Entry point
label start:

    $ anticheat = persistent.anticheat

    $ chapter = 0

    $ _dismiss_pause = config.developer

    # 可以修改女主的名字
    $ s_name = "Sayori" # 可选译名：纱世里（推荐）、莎世里、纱悠里
    $ m_name = "Monika" # 推荐译名：莫妮卡
    $ n_name = "Natsuki" # 可选译名：夏树（推荐）、娜苏琪
    $ y_name = "Yuri" # 推荐译名：优里

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    
    if persistent.intro_seen:
        call script_ch0_mod
    else:
        call intro
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
