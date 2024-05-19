from game import Game
from mongoDB import init_database_from_mongo

init_database_from_mongo()
game = Game(21,21, "SnakeGameS28250")
game.run()