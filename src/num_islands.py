from typing import List


def num_islands(grid: List[List[str]]) -> int:
    count: int = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == "1":
                # land found
                _dfs(grid, y, x)
                count += 1
    print(grid)
    return count


def _dfs(grid: List[List[str]], y: int, x: int):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != "1":
        return

    grid[y][x] = "2"
    _dfs(grid, y - 1, x)
    _dfs(grid, y + 1, x)
    _dfs(grid, y, x - 1)
    _dfs(grid, y, x + 1)
