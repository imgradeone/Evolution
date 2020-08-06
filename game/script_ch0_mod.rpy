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
    #call screen dialog("emm，骚年，你想多了，主界面也就 4 个女孩啊...",Return())
    "不过，看在 Sayori 的份上..."
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
    mc "..."
    mc "不是，这什么也没变啊..."
    show sayori 5b at s41
    s "emm..."
    s "变的不是外观..."
    s "而是..."
    show yuri 1c at l42
    y "茶水？"
    y "今天我刚买了几包昏睡红茶{nw}"
    $ _history_list.pop()
    y "今天我刚买了几包{fast}新的红茶，你们可以尝尝。"
    y 4a "赏诗的时候可以多点新气氛哦~"
    show natsuki 4g at l43
    n "什么啊？这就叫新变化？"
    n 5d "咱这 Mod 可是叫 Evolution 啊！"
    n 5c "不可能才因为你这茶水就成什么 evolution 嘛。"
    y "那你还想说纸杯蛋糕—{nw}"
    show monika 1m at l11
    show sayori 1m
    show natsuki 5c
    show yuri 4d
    m "emm..."
    m "先别吵..."
    show yuri 1f
    show sayori 1
    show natsuki 1
    show monika 1p at t44
    m "我...好像又是最后一个到的..."
    show natsuki at f43
    n "你是不是去练钢琴了？"
    m 1q "..."
    show natsuki at t43
    show monika at f44
    m "没有...这回真的没有..."
    m 1 "不过..."
    m 1b "现在大家都到了！"
    m "我们也可以正式开始了！"
    show monika at t44
    show natsuki at f43
    stop music fadeout 3.0
    n 5m "不是..."
    n "我听 Sayori 说，文学部有什么新变化..."
    n "但是，我看了一圈，完全看不出来变化啊。"
    play music t6
    show natsuki at t43
    show monika 1q at f44
    m "..."
    m 1o "Well..."
    m 2b "待会你们就知道了！"
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show monika at t11    
    m 5 "那么欢迎来到进化的文学部！"
    m "首先，按照常例—"
    n "诶？"
    show natsuki 1e at l31
    n "Monika！"
    n "咱们不是进化了吗？怎么还要按以前的常例？"
    m 1q "..."
    m 1n "emm...口误而已..."
    n 5g "哼唧。"
    m 2 "今天，我们来即兴创作！"
    m 5 "每个人在这里临时创作一首诗歌，不要求长，时间不超过 30 分钟。"
    
    return