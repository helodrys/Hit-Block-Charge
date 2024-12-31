from hit_block_charge.project import attack, block, charge
def test_block():
    player = {
    "Health": 3,
    "Defense": 0,
    "Charge": 0
    }
    bot = {
        "Health": 3,
        "Defense": 0,
        "Charge": 0
    }
    block(player)
    assert player["Defense"] == 1
    block(bot)
    assert bot["Defense"] == 1

def test_charge():
    player = {
    "Health": 3,
    "Defense": 0,
    "Charge": 0
    }
    bot = {
        "Health": 3,
        "Defense": 0,
        "Charge": 1
    }
    charge(player)
    assert player["Charge"] == 1
    charge(bot)
    assert bot["Charge"] == 2

def test_attack():
    player = {
    "Health": 3,
    "Defense": 0,
    "Charge": 3
    }
    bot = {
        "Health": 3,
        "Defense": 0,
        "Charge": 0
    }
    defense_bot = {
        "Health": 3,
        "Defense": 1,
        "Charge": 0
    }
    attack(player, bot)
    assert player["Charge"] == 2 and bot["Health"] == 2
    attack(player, defense_bot)
    assert player["Charge"] == 1 and defense_bot["Defense"] == 0