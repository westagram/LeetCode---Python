class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Create counter data structure
        # DFS through the tile and add to output if the word hasn't appeared
        tiles_counter = collections.Counter(tiles)
        tracking = set()
        self.dfs("", tracking, tiles_counter)
        return len(tracking) - 1

    def dfs(self, current_tile, tracking, tiles_counter):
        tracking.add(current_tile)
        for tile in tiles_counter:
            if tiles_counter[tile] <= 0:
                continue
            tiles_counter[tile] -= 1
            self.dfs(current_tile+tile, tracking, tiles_counter)
            tiles_counter[tile] += 1
