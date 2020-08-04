label script_ch0_mod:

    stop music fadeout 2.0
    scene bg class_day
    with dissolve_scene_full
    play music t2
    "今天的校园生活还是很枯燥..."
    "气氛还是一如既往的沉闷。"
    "不过，待会的文学部活动肯定会非常有意思的..."
    s "...[player]？"
    show sayori 1 at t11 zorder 2
    mc "Sayori？"
    mc "你怎么在这里？"
    show sayori 5 at d11 zorder 2
    s "呃..."
    s "最近咱们文学部有一些变化，待会你要不要来参观？"
    mc "好哇！"
    "其实我在想，会不会有新的女孩纸加入..."
    call screen dialog("emm，骚年，你想多了，主界面也就 4 个女孩啊...",Return())
    "不过，看在系统提示的份上..."
    s "嘿，[player]..."
    s 1l "要不然我们现在就去看看？"
    mc "可以。"
    s 4r "好耶～！"
    scene bg corridor
    with wipeleft_scene
    stop music fadeout 2.0
    "走出教室，穿过熟悉的大楼 - 之前我不常来学校这边，这里是三年级学生和社团活动使用的地方。"
    "但是，我可是一名文学部部员啊！"
    "一路上，我也想象着文学部的小变化到底会带来什么..."
    "走到部室门口，元气满满的 Sayori 一口气拉开了教室的门。"
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41

    s "哟吼~！"
    s "欢迎回到文学部！"
    return