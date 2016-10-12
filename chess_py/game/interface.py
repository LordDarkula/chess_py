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
        self.running = True
        self.latest_input = ""

    def play(self):
        self.runInParallel(lambda: self.read(), lambda: self.set_up())
        self.set_up()

    def set_up(self):
        option = self.latest_input

        while option != "uci":
            option = self.latest_input

        self.write("id name " + self.engine)
        self.write("id author " + self.author)

        self.write("uciok")

    def read(self):
        """
        Continuously reads from the console and updates
        ``self.latest_input`` with latest command. Runs
        as a side process at all times so main process
        has the most current information form the console
        accessed through ``self.latest_input``.
        """
        while self.running:
            self.latest_input = self.player.getUCI()

    def write(self, command):
        """
        Writes to the console given the command.
        Called by the main process when it needs to
        send commands to the console.

        :type command: str
        """
        self.player.setUCI(command)

    def runInParallel(*fns):
        """
        Runs multiple processes in parallel.

        :type fns: def
        """
        proc = []
        for fn in fns:
            p = Process(target=fn)
            p.start()
            proc.append(p)
        for p in proc:
            p.join()

