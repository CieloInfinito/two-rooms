from Game import Game

game = Game()

game.lvl1()

game.add_card_to_room(game.get_card_by_id(6), game.red_room)
game.add_card_to_room(game.get_card_by_id(14), game.red_room)
game.add_card_to_room(game.get_card_by_id(15), game.red_room)
game.add_card_to_room(game.get_card_by_id(21), game.red_room)



game.show_room(game.red_room)

print(game.resolve_turn(game.red_room))
game.show_room(game.red_room)
game.show_room(game.basement)

print(game.basement)
print(game.get_card_by_id(15))