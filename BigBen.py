def on_chat():
    blocks.fill(BRICKS, pos(2, 0, 2), pos(4, 20, 4), FillOperation.REPLACE)
    blocks.fill(BRICKS, pos(1, 20, 1), pos(5, 23, 5), FillOperation.REPLACE)
    blocks.fill(YELLOW_STAINED_GLASS_PANE,
        pos(1, 20, 1),
        pos(1, 23, 5),
        FillOperation.REPLACE)
    blocks.fill(OBSIDIAN,
        pos(2, 24, 2),
        pos(4, 25, 4),
        FillOperation.REPLACE)
    for index in range(5):
        pass
player.on_chat("run", on_chat)
