from Game import Game

game = Game()

game.lvl1()
print(game.deck)

game.add_card_to_room(game.draw_from_deck(), game.red_room)
print(game.deck)
game.add_card_to_room(game.get_card_by_id(14), game.red_room)

print(game.red_room)