
#15 41
# Celem ćwiczenia jest imlementacja metody Minimax z obcinaniem alpha-beta do gry Connect Four (czwórki).
#
# W trakcie ćwiczenia można skorzystać z reposytorium z implementacją gry Connect Four udostępnionym przez Jakuba Łyskawę.
# Ewentualnie, można zaimplementować samemu grę Connect Four (ale, tak aby rozwiązanie miało ten sam interfejs co podany poniżej).
#
# Implementację Minimax należy przetestować używając różną głębokość przeszukiwania.
# Implementacja Solvera musi zapewniać interfejs jak poniżej, ale można dodać dowolne metody prywatne oraz klasy wspomagające (jeżeli będą potrzebne).
#
# Punktacja:
#
# Działająca metoda Minimax - 2 pkt
# Działająca metoda Minimax z obcinaniem alpha-beta - 1.5 pkt
# Analiza jakości solvera w zależności od głębokości przeszukiwania 1.5pkt
# można zaimplementować w tym celu wizualizację rozgrywki dwóch agentów, bądź kilka przykładów 'z ręki'
# Jakość kodu 2pkt
# Aby importowanie elementów z poniższej komórki działało należy umieścić tego notebooka w tym samym folderze co paczkę two_player_games:
#
#
#


from typing import Tuple, List

from two_player_games.player import Player
from two_player_games.games.connect_four import ConnectFour, ConnectFourMove

ROW_COUNT = 6
COLUMN_COUNT = 7

class Tree:
    def __init__(self, root,):
        self.root = root
        # self.leaf_nodes = leaf_nodes
class Node:

    def __init__(self, state,leaf_nodes = []):
        self.game = game
        self.leaf_nodes = leaf_nodes
    def add_leaf(self,state):
        node = Node(state)
        self.leaf_nodes.append(node)
class MinMaxSolver:

    def __init__(self, game: ConnectFour):
        self.game = game

    # evaluate_position fukcja(złożona z 3 funkcji) liczy wszyskie mozliwsci połazczenia w rząd.
    # liczy wszyskie mozliwe łancuchy iteracyjnie biorąc każdy nie null elemęt w tabeli i następnie
    # sprawdza w 5 kierunktów czyli wszyskie kratki któ©e z nią graniczą które nie idą w góre jezeli
    # trafi na kolejne pole zajęte przez tego samego gracza to kontynułuje az nie napotka
    # albo innego gracza albo końca mapy albo pustego pola
    # te same łancuchy moze liczyć wielokrotnie np od lewej do prawej a potem odrwrotnie lub idąc w góre
    # tez wiele razy co daje większy wynik przy większej ilosci dłuższych łancuchów co jest porządane
    #  gdyż pozawala to na większą ilość mozliwosci dostawienia wygrywającego elemętu.
    # listy które tworzy zawierają 0 jezeli nie trafił na nic w tym kierunku | jezeli w ściane i 1,2,3 jezeli tyle
    # było w tym kierunku
    def evaluate_position(self,player):
        rows = self.positon(player)
        evaluation = 0
        for point in rows:
            if type(point) == int:
                evaluation += point
        return evaluation
    def find_rows(self,x,y,player: Player) :
        moving_array = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]
        curr = self.game.state.fields[x][y]

        rows = []
        for i in range(5):
            curr_x = x
            curr_y = y
            curr_length = 0
            while True:

                curr_vector = moving_array[i]
                xadd,yadd = curr_vector
                curr_x += xadd
                curr_y += yadd
                if 0 <= curr_x < COLUMN_COUNT and 0 <= curr_y < ROW_COUNT:
                    curr = self.game.state.fields[curr_x][curr_y]

                else:
                    if curr_length == 0:
                        #trafiło w ściane
                        rows.append('|')
                    else:
                        rows.append(curr_length)
                    break

                if curr is not None and curr == player:

                    curr_length += 1
                else:
                    # if curr_length != 0:
                    rows.append(curr_length)
                    break

        # print(rows)

        return rows
    def positon(self, player: Player) -> float:
        # j-x
        # i-y
        rows = []
        curr_length = 0


        for i in range(ROW_COUNT):
            for j in range(0, COLUMN_COUNT):
                curr = self.game.state.fields[j][i]
                if curr is not None and curr == player:
                    element_rows = self.find_rows(j,i,player)
                    rows.extend(element_rows)

        return rows

    def minimax(self, depth, alpha: float, beta: float, is_maximizing_player: bool) -> Tuple[int, float]:
        """Returns column index and score"""
        # if depth == 0 or

        # imaginary game
        im_game = self.game

        pass

    def get_best_move(self) -> int:
        pass

    # git
    def _get_valid_locations(self) -> List[int]:
        valid_columns = []
        for i in range(COLUMN_COUNT):
            if self._is_valid_move(i):
                valid_columns.append(1)
            else:
                valid_columns.append(0)
        return valid_columns

    # git
    def _is_valid_move(self, col_index: int) -> bool:
        if self.game.state.fields[col_index].count(None) != 0:
            return True
        else:
            return False


p1 = Player("a")
p2 = Player("b")
game = ConnectFour(size=(COLUMN_COUNT, ROW_COUNT), first_player=p1, second_player=p2)
minimaxsolver = MinMaxSolver(game)
lista = [0, 1, 0, 0, 2, 3]
print(minimaxsolver.chains_to_score(lista),"placki")
# game.make_move(ConnectFourMove(3))
# game.make_move(ConnectFourMove(4))
# game.make_move(ConnectFourMove(3))
#
# game.make_move(ConnectFourMove(4))
# game.make_move(ConnectFourMove(3))
# game.make_move(ConnectFourMove(4))
#
game.make_move(ConnectFourMove(3))
game.make_move(ConnectFourMove(4))
game.make_move(ConnectFourMove(3))

game.make_move(ConnectFourMove(4))
game.make_move(ConnectFourMove(2))
game.make_move(ConnectFourMove(4))
game.make_move(ConnectFourMove(3))
game.make_move(ConnectFourMove(0))
game.make_move(ConnectFourMove(6))
game.make_move(ConnectFourMove(0))

# game.make_move(ConnectFourMove(0))
# game.make_move(ConnectFourMove(6))
# game.make_move(ConnectFourMove(6))
# game.make_move(ConnectFourMove(0))
# game.make_move(ConnectFourMove(0))
# game.make_move(ConnectFourMove(6))
# game.make_move(ConnectFourMove(2))
# game.make_move(ConnectFourMove(3))
# game.make_move(ConnectFourMove(3))
# game.make_move(ConnectFourMove(6))
# game.make_move(ConnectFourMove(5))
# game.make_move(ConnectFourMove(6))
# game.make_move(ConnectFourMove(5))
# game.make_move(ConnectFourMove(6))
# game.make_move(ConnectFourMove(0))

print(minimaxsolver._is_valid_move(3))
print(minimaxsolver._get_valid_locations())

print(game)
print(game.state.fields[0][0])
# minimaxsolver.positon(p1)
#
# minimaxsolver.find_rows(5,0,p1)
print(minimaxsolver.evaluate_position(p1))
print("winner to ",game.get_winner().char)





















