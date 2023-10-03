CREATE TABLE chessboard(
    colour CHAR,
    col_letter CHAR,
    col_number SMALLINT,
    "row_number" SMALLINT
);
 
-- The input data in format:
INSERT INTO chessboard (colour, col_letter, "row_number")
VALUES
    ('w', 'A', 2),
    ('b', 'B', 4);
    
UPDATE chessboard
SET col_number = ABS(64 -  ASCII(col_letter));
 
    
DO $$
DECLARE
    col_number_w SMALLINT := (SELECT col_number FROM chessboard WHERE colour = 'w');
    row_number_w SMALLINT := (SELECT "row_number" FROM chessboard WHERE colour = 'w');
    col_number_b SMALLINT := (SELECT col_number FROM chessboard WHERE colour = 'b');
    row_number_b SMALLINT := (SELECT "row_number" FROM chessboard WHERE colour = 'b');
BEGIN
    WHILE TRUE LOOP
        IF row_number_w = 8 THEN
            RAISE NOTICE 'Game over! White pawn is promoted to a queen at %',
                CHR(col_number_w + 64) || row_number_w;
            EXIT;
        END IF;
        row_number_w := row_number_w + 1;
 
        IF (col_number_w + 1 = col_number_b OR col_number_w - 1 = col_number_b) AND
           row_number_w = row_number_b THEN
            RAISE NOTICE 'Game over! White win, capture on %',
                CHR(col_number_b + 64) || row_number_b;
            EXIT;
        END IF;
 
        IF row_number_b = 1 THEN
            RAISE NOTICE 'Game over! Black pawn is promoted to a queen at %',
                CHR(col_number_b + 64) || row_number_b;
            EXIT;
        END IF;
        row_number_b := row_number_b - 1;
 
        IF (col_number_b + 1 = col_number_w OR col_number_b - 1 = col_number_w) AND
           row_number_b = row_number_w THEN
            RAISE NOTICE 'Game over! Black win, capture on %',
                CHR(col_number_w + 64) || row_number_w;
            EXIT;
        END IF;
    END LOOP;
END $$;
 
DROP TABLE chessboard;
