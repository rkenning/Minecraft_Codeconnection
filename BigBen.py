def on_chat():
    blocks.fill(BRICKS, pos(1, 0, 1), pos(5, 20, 5), FillOperation.REPLACE)
    blocks.fill(BRICKS, pos(0, 20, 0), pos(6, 25, 6), FillOperation.REPLACE)
    blocks.fill(YELLOW_STAINED_GLASS_PANE,
        pos(0, 20, 0),
        pos(0, 25, 6),
        FillOperation.REPLACE)
    blocks.fill(BLACK_STAINED_GLASS_PANE,
        pos(0, 22, 3),
        pos(0, 24, 3),
        FillOperation.REPLACE)
    blocks.fill(BLACK_STAINED_GLASS_PANE,
        pos(0, 22, 3),
        pos(0, 22, 5),
        FillOperation.REPLACE)
    blocks.fill(OBSIDIAN,
        pos(2, 26, 2),
        pos(4, 29, 4),
        FillOperation.REPLACE)
    for index in range(5):
        pass
player.on_chat("ben", on_chat)
