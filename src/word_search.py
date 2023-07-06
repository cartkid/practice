"""
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w']
]
word1_1 = "access"      # [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
word1_2 = "balloon"     # [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]

word1_3 = "wow"         # [(4, 3), (5, 3), (5, 4)] OR 
                        # [(5, 2), (5, 3), (5, 4)] OR 
                        # [(5, 5), (5, 6), (5, 7)]
                          
word1_4 = "sec"         # [(3, 4), (3, 5), (3, 6)] OR 
                        # [(3, 4), (3, 5), (4, 5)]    

word1_5 = "bbaal"       # [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]


grid2 = [
  ['a'],
]
word2_1 = "a"

grid3 = [
    ['c', 'a'],
    ['t', 't'],
    ['h', 'a'],
    ['a', 'c'],
    ['t', 'g']
]
word3_1 = "cat"
word3_2 = "hat"

grid4 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'a', 't', 'n', 'i', 'i'],
    ['a', 'x', 'n', 'x', 'p', 't'],
    ['t', 'x', 'i', 'x', 't', 't']
]
word4_1 = "catnip"      # [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)] OR
                        # [(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)]


All test cases:

search(grid1, word1_1) => [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
search(grid1, word1_2) => [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]
search(grid1, word1_3) => [(4, 3), (5, 3), (5, 4)] OR 
                          [(5, 2), (5, 3), (5, 4)] OR 
                          [(5, 5), (5, 6), (5, 7)]
search(grid1, word1_4) => [(3, 4), (3, 5), (3, 6)] OR
                          [(3, 4), (3, 5), (4, 5)]                           
search(grid1, word1_5) => [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]

search(grid2, word2_1) => [(0, 0)]

search(grid3, word3_1) => [(0, 0), (0, 1), (1, 1)]
search(grid3, word3_2) => [(2, 0), (3, 0), (4, 0)]

search(grid4, word4_1) => [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)] OR
                          [(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word

"""

words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
note1 = "ctay"
note2 = "bcanihjsrrrferet"
note3 = "tbaykkjlga"
note4 = "bbbblkkjbaby"
note5 = "dad"
note6 = "breadmaking"
note7 = "dadaa"


def find(words: list, note: str) -> str:
    temp: str = note
    for word in words:
        temp = note
        for letter in word:
            if letter in temp:
                temp = temp.replace(letter, "", 1)
                # print(f"letter {letter}: temp {temp}")
            else:
                # print(temp)
                temp = False
                break
        if temp != False:
            return word
    return "-"


# result = find(words, note1)
# print(result)
# assert result == "cat"

# result = find(words, note2)
# print(result)
# result = find(words, note3)
# print(result)
# result = find(words, note4)
# print(result)
# result = find(words, note5)
# print(result)
# result = find(words, note6)
# print(result)
# result = find(words, note7)
# print(result)

grid1 = [
    ["b", "b", "b", "a", "l", "l", "o", "o"],
    ["b", "a", "c", "c", "e", "s", "c", "n"],
    ["a", "l", "t", "e", "w", "c", "e", "w"],
    ["a", "l", "o", "s", "s", "e", "c", "c"],
    ["w", "o", "o", "w", "a", "c", "a", "w"],
    ["i", "b", "w", "o", "w", "w", "o", "w"],
]
word1_1 = "access"
word1_2 = "balloon"
word1_3 = "wow"
word1_4 = "sec"
word1_5 = "bbaal"

grid2 = [
    ["a"],
]
word2_1 = "a"

grid3 = [
    ["c", "a"],
    ["t", "t"],
    ["h", "a"],
    ["a", "c"],
    ["t", "g"],
]
word3_1 = "cat"
word3_2 = "hat"

grid4 = [
    ["c", "c", "x", "t", "i", "b"],
    ["c", "a", "t", "n", "i", "i"],
    ["a", "x", "n", "x", "p", "t"],
    ["t", "x", "i", "x", "t", "t"],
]
word4_1 = "catnip"


def search(grid, word, curr_list=[], idx=0) -> list:
    result: list = curr_list
    if len(result) == len(word):
        return result

    for idx in range(idx, len(word)):
        letter = word[idx]
        if idx == 0:
            next_coords = find_letter_coords(grid, letter)
        else:
            curr_coord = result[len(result) - 1]
            next_coords = find_neighbor_letter(grid, letter, curr_coord)
        for next_coord in next_coords:
            temp_coords = result.copy()
            temp_coords.append(next_coord)
            temp_result = search(grid, word, temp_coords, idx + 1)
            if len(temp_result) == len(word):
                return temp_result

    return []


def find_letter_coords(grid, letter_to_find):
    possible = []
    for id_row, row in enumerate(grid):
        for id_col, col in enumerate(row):
            if col == letter_to_find:
                possible.append((id_row, id_col))
    return possible


def find_neighbor_letter(grid, letter_to_find, curr_loc):
    possible = []
    directions = [(1, 0), (0, 1)]
    for direction in directions:
        # grid has space to check that direction
        try:
            row = curr_loc[0] + direction[0]
            col = curr_loc[1] + direction[1]
            if grid[row][col] == letter_to_find:
                possible.append((row, col))
        except:
            # nothing happened, but the grid area to search was invalid, just move on
            pass
    return possible
