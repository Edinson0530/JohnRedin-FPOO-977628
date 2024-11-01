def verify_winner(table):
    # Verificar filas
    for row in table:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return f"Ganador: {row[0]} (fila)"

    # Verificar columnas
    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] and table[0][col] != "_":
            return f"Ganador: {table[0][col]} (columna)"
    
    # Verificar diagonal principal
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != "_":
        return f"Ganador: {table[0][0]} (diagonal principal)"
    
    # Verificar diagonal secundaria
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != "_":
        return f"Ganador: {table[0][2]} (diagonal secundaria)"
    
    # Verificar si hay espacios vacíos (juego en progreso)
    for row in table:
        if "_" in row:
            return "El juego sigue en progreso"
    
    # Si no hay ganador y no hay espacios vacíos, es un empate
    return "Empate"

# Tableros de prueba
board_no_winner = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
board_winner_rows = [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]]
board_winner_columns = [["O", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]]
board_winner_diagonal = [["X", "O", "_"], ["_", "X", "O"], ["_", "_", "X"]]
board_tie = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
board_in_progress = [["X", "O", "X"], ["_", "O", "_"], ["O", "X", "_"]]

# Pruebas
print(verify_winner(board_no_winner))       # Empate
print(verify_winner(board_winner_rows))     # Ganador: X (fila)
print(verify_winner(board_winner_columns))  # Ganador: O (columna)
print(verify_winner(board_winner_diagonal)) # Ganador: X (diagonal principal)
print(verify_winner(board_tie))             # Empate
print(verify_winner(board_in_progress))     # El juego sigue en progreso
