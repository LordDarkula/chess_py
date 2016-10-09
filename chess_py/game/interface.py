from chess_py.core import Board
from multiprocessing import Process


class UCI:
    def __init__(self, player, engine_name, author):
        """

        :type player Player
        """
        self.player = player
        self.engine = engine_name
        self.author = author
        self.position = Board.init_default()

    def play(self):
        self.set_up()

    def set_up(self):
        option = ""

        while option != "uci":
            option = self.read()

        self.write("id name " + self.engine)
        self.write0("id author " + self.author)

        self.write("uciok")

    def read(self):
        return self.player.getUCI()

    def write(self, command):
        self.player.setUCI(command)

    def runInParallel(*fns):
        """

        :param fns:
        :return:
        """
        proc = []
        for fn in fns:
            p = Process(target=fn)
            p.start()
            proc.append(p)
        for p in proc:
            p.join()

