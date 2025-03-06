from Game import Game

game = Game()

game.lvl1()
game.add_card_to_room(game.draw_from_deck(), game.red_room)
print(game.get_card_by_id(14))
game.add_card_to_deck(game.get_card_by_id(14))
print(game.deck)
game.add_card_to_room(game.draw_from_deck(), game.red_room)