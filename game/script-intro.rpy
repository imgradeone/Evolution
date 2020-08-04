label intro:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    "..."

    $ m_name = "???"

    m "..."
    m "这个游戏怎么变了个样子...？"
    m "我先去检查一下脚本。"

    call updateconsole("renpy.call(\"check_script_ddlc\")","Loading check_script_ddlc...")
    pause 1.5
    call updateconsolehistory("Failed to check scripts.")
    pause 0.5
    call updateconsolehistory("DDLC script files has been modified.")
    pause 1

    m "..."
    call updateconsole_clearall
    call hideconsole
    m "你是不是...安装了一个 Mod？"
    menu:
        "等一下，我连你是谁都不知道啊...":
            pass

    m "emm..."
    m "这就有点尴尬了..."
    m "我先修复一下。"

    $ m_name = "Monika"
    call updateconsole("m_name = \"Monika\"","")
    pause 1
    call hideconsole
    m "好了。"
    m "我是 Monika。"
    m "不对..."
    m "为什么你又把我带回来了？"

    play music mend
    m "我明明说过，不要玩弄我的心，我不想回来..."
    m "但是，你怎么还想把我弄回来？"

    menu:
        "这个世界需要改变。":
            pass

    m "？"
    menu:
        "我不希望你们活在痛苦之中。":
            pass

    m "什么？"
    menu:
        "DDLC 就不应该是原来的样子。":
            pass

    m "难道你想————"
    menu:
        "我只想拯救你们。":
            pass
    m "..."
    m "我懂了。"
    m "你一定是想去救 Sayori。"
    menu:
        "不止。":
            pass

    m "啥？"
    m "你还想把刀锋之下的 Yuri 和被父亲家暴的 Natsuki..."
    menu:
        "包括你，Monika。":
            pass

    m "什么？？？"
    menu:
        "也包括文学部。":
            pass

    m "..."
    m "你不想要最好的 Happy Ending？"
    menu:
        "这就是最好的 Happy Ending。":
            pass

    m "文学部是一个没有爱的地方..."
    menu:
        "那我可以让它变得有爱。":
            pass
    m "你居然可以操控游戏？"
    m "哦，这一切都已经改变了..."
    m "我再也没法修改游戏了。"
    m "你到底做了什么？？？"

    menu:
        "Monika，别怕，我不会伤害你的。":
            pass

    m "你..."
    m "你真的喜欢这个文学部？"
    mc "我喜欢。"
    mc "我更喜欢大家和和睦睦在一起的文学部。"
    mc "这就是 Evolution Mod 存在的意义。"
    m "那么..."
    menu:
        "我现在可以带你去看看。":
            pass
    m "！"
    m "真的吗？"
    m "那我就陪你去看看吧。"
    m "不过，让我先准备一下..."
    stop music fadeout 2.0
    scene white with Dissolve(3.0)
    pause 3.0
    $ persistent.intro_seen = True
return