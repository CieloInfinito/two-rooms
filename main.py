from Game import Game

game = Game()

game.lvl1()
print(game.deck)
game.bubble_sort_cards_by_id(game.deck)
print(game.deck)