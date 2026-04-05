import numpy as np
from copy import deepcopy
from marqlo_players_final_ver import alphaBetaAI

# Create a mock environment
class MockEnv:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype='int32')
        self.topPosition = (np.ones(7) * 5).astype('int32')
        self.shape = (6, 7)
    
    def getEnv(self):
        env = MockEnv()
        env.board = deepcopy(self.board)
        env.topPosition = deepcopy(self.topPosition)
        return env

# Set up the board according to the example
env = MockEnv()
# Row 0 (bottom): Y R R Y Y _ _
env.board[0][0] = 2  # Y
env.board[0][1] = 1  # R
env.board[0][2] = 1  # R
env.board[0][3] = 2  # Y
env.board[0][4] = 2  # Y

# Row 1: _ R Y R _ _ _
env.board[1][1] = 1  # R
env.board[1][2] = 2  # Y
env.board[1][3] = 1  # R

# Row 2: _ Y _ R _ _ _
env.board[2][1] = 2  # Y
env.board[2][3] = 1  # R

# Row 3: _ _ _ Y _ _ _
env.board[3][3] = 2  # Y

print("Board:")
for row in range(5, -1, -1):
    print(f"Row {row}: ", end="")
    for col in range(7):
        if env.board[row][col] == 0:
            print(" _ ", end="")
        elif env.board[row][col] == 1:
            print(" R ", end="")
        else:
            print(" Y ", end="")
    print()

# Create AI player and evaluate
ai = alphaBetaAI(1)  # Player 1 evaluating
score = ai.evaluate(env, -1, 1)  # last_move=-1 means no terminal check

print(f"\nEvaluation score: {score}")

# Let's also manually check the windows to verify
print("\n--- Debug window scoring ---")

# Horizontal windows
print("\nHorizontal windows:")
h_score = 0
for row in range(6):
    for col in range(4):
        window = [env.board[row][col+i] for i in range(4)]
        w_score = ai.evaluate_window(window, 1, 2)
        if w_score != 0:
            print(f"Row {row}, cols {col}-{col+3}: {window} = {w_score}")
            h_score += w_score
print(f"Total horizontal: {h_score}")

# Vertical windows
print("\nVertical windows:")
v_score = 0
for row in range(3):
    for col in range(7):
        window = [env.board[row+i][col] for i in range(4)]
        w_score = ai.evaluate_window(window, 1, 2)
        if w_score != 0:
            print(f"Col {col}, rows {row}-{row+3}: {window} = {w_score}")
            v_score += w_score
print(f"Total vertical: {v_score}")

# Diagonal BL-TR
print("\nDiagonal BL-TR:")
d_score_bltr = 0
for row in range(3):
    for col in range(4):
        window = [env.board[row+i][col+i] for i in range(4)]
        w_score = ai.evaluate_window(window, 1, 2)
        if w_score != 0:
            print(f"Start ({row},{col}): {window} = {w_score}")
            d_score_bltr += w_score
print(f"Total BL-TR: {d_score_bltr}")

# Diagonal TL-BR
print("\nDiagonal TL-BR:")
d_score_tlbr = 0
for row in range(3, 6):
    for col in range(4):
        window = [env.board[row-i][col+i] for i in range(4)]
        w_score = ai.evaluate_window(window, 1, 2)
        if w_score != 0:
            print(f"Start ({row},{col}): {window} = {w_score}")
            d_score_tlbr += w_score
print(f"Total TL-BR: {d_score_tlbr}")

# Center control
print("\nCenter control:")
center_col = 3
center_count = sum(1 for row in range(6) if env.board[row][center_col] == 1)
center_score = center_count * 3
print(f"Pieces in column 3: {center_count} = {center_score}")

print(f"\n--- Summary ---")
print(f"Horizontal: {h_score}")
print(f"Vertical: {v_score}")
print(f"Diagonal BL-TR: {d_score_bltr}")
print(f"Diagonal TL-BR: {d_score_tlbr}")
print(f"Center: {center_score}")
print(f"TOTAL: {h_score + v_score + d_score_bltr + d_score_tlbr + center_score}")
