class Piece:
    def __init__(self, color, x_coord, y_coord, name):
        self.color = color
        self.y_coord = y_coord
        self.x_coord = x_coord
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def get_cords(self):
        return (self.x_coord, self.y_coord)


class Pawn(Piece):
    def __init__(self, color, x_coord, y_coord, name='p'):
        super().__init__(color, x_coord, y_coord, name)
        self.first_move = False

    def get_possible_moves(self):
        moves = []

        direction = 1 if self.color == 'w' else -1

        forward_move = (self.x_coord, self.y_coord + direction)
        if 1 <= forward_move[1] <= 8:
            moves.append(forward_move)

            if (self.color == 'w' and self.y_coord == 2) or (
                self.color == 'b' and self.y_coord == 7
            ):
                double_forward_move = (self.x_coord, self.y_coord + 2 * direction)
                if 1 <= double_forward_move[1] <= 8:
                    moves.append(double_forward_move)

        return moves


class Rook(Piece):
    def __init__(self, color, x_coord, y_coord, name='r'):
        super().__init__(color, x_coord, y_coord, name)

    def get_possible_moves(self):
        horizontal_moves = [(x, self.y_coord) for x in range(1, 9) if x != self.x_coord]

        vertical_moves = [(self.x_coord, y) for y in range(1, 9) if y != self.y_coord]

        all_moves = horizontal_moves + vertical_moves

        return all_moves


class Bishop(Piece):
    def __init__(self, color, x_coord, y_coord, name='b'):
        super().__init__(color, x_coord, y_coord, name)

    def get_possible_moves(self):
        moves = []

        for i in range(1, min(8 - self.x_coord, 8 - self.y_coord) + 1):
            moves.append((self.x_coord + i, self.y_coord + i))

        for i in range(1, min(self.x_coord - 1, self.y_coord - 1) + 1):
            moves.append((self.x_coord - i, self.y_coord - i))

        for i in range(1, min(self.x_coord - 1, 8 - self.y_coord) + 1):
            moves.append((self.x_coord - i, self.y_coord + i))

        for i in range(1, min(8 - self.x_coord, self.y_coord - 1) + 1):
            moves.append((self.x_coord + i, self.y_coord - i))

        moves = [(x, y) for x, y in moves if 1 <= x <= 8 and 1 <= y <= 8]

        return moves


class Queen(Piece):
    def __init__(self, color, x_coord, y_coord, name='q'):
        super().__init__(color, x_coord, y_coord, name)

    def get_possible_moves(self):
        moves = []

        for x in range(1, 9):
            if x != self.x_coord:
                moves.append((x, self.y_coord))

        for y in range(1, 9):
            if y != self.y_coord:
                moves.append((self.x_coord, y))

        for i in range(1, min(8 - self.x_coord, 8 - self.y_coord) + 1):
            moves.append((self.x_coord + i, self.y_coord + i))

        for i in range(1, min(self.x_coord - 1, self.y_coord - 1) + 1):
            moves.append((self.x_coord - i, self.y_coord - i))

        for i in range(1, min(self.x_coord - 1, 8 - self.y_coord) + 1):
            moves.append((self.x_coord - i, self.y_coord + i))

        for i in range(1, min(8 - self.x_coord, self.y_coord - 1) + 1):
            moves.append((self.x_coord + i, self.y_coord - i))

        moves = [(x, y) for x, y in moves if 1 <= x <= 8 and 1 <= y <= 8]
        return moves


class Knight(Piece):
    def __init__(self, color, x_coord, y_coord, name='kn'):
        super().__init__(color, x_coord, y_coord, name)

    def get_possible_moves(self):
        possible_moves = [
            (self.x_coord + 2, self.y_coord + 1),
            (self.x_coord + 2, self.y_coord - 1),
            (self.x_coord - 2, self.y_coord + 1),
            (self.x_coord - 2, self.y_coord - 1),
            (self.x_coord + 1, self.y_coord + 2),
            (self.x_coord + 1, self.y_coord - 2),
            (self.x_coord - 1, self.y_coord + 2),
            (self.x_coord - 1, self.y_coord - 2),
        ]
        possible_moves = [
            (x, y) for x, y in possible_moves if 1 <= x <= 8 and 1 <= y <= 8
        ]
        return possible_moves


class King(Piece):
    def __init__(self, color, x_coord, y_coord, name='k'):
        super().__init__(color, x_coord, y_coord, name)

    def get_possible_moves(self):
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        possible_moves = [(self.x_coord + dx, self.y_coord + dy) for dx, dy in deltas]
        possible_moves = [
            (x, y) for x, y in possible_moves if 1 <= x <= 8 and 1 <= y <= 8
        ]
        return possible_moves


