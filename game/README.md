> 几乎完全是谷歌娘机翻

## DDLC Mod 模板

这些 `.rpy` 文件是在 DDLC 的 `script.rpa` 找得到、对基本 mod 工程来说需要修改的重要脚本文件的拷贝。

如上所述，每个文件都与 DDLC 中包含的文件相似，但其中删除了特定于故事的游戏流程，这样您就可以讲出您想讲的故事了。但是，原始代码会包含在注释块中，以便复刻原游戏的某些部分。

## 脚本详解

#### `options.rpy`

该文件包含可以更改以自定义 mod 的选项。该文件还包括导出 mod 供他人下载时使用的构建选项。

#### `overrides.rpy`

该文件用于覆盖 DDLC 中的特定定义。您不仅可以使用它来更改图像和其他变量，还可以避免直接编辑 `/advanced_scripts` 中的文件。

#### `script-example.rpy`、`tutorials.rpy`

这些场景可以教您一些有关制作 mod 的知识，并且也是代码示例！

#### `script.rpy`

这个脚本属于顶级游戏结构，不应包含任何实际事件或脚本；只需要逻辑和标签调用。 **您的 mod 构建从这里开始。**

#### `splash.rpy`

这个脚本包含 Ren'Py 在游戏启动后向玩家显示的第一个屏幕。它还定义了首次加载游戏时的许多行为，例如检查角色文件和场景自动跳转。