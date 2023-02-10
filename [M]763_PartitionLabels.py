class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dict all last idx of each char
        # Loop through the list:
        ## if last_index > end_idx, then end_idx = last_index
        ## if end_idx = current_index, then append (end_idx - start_idx + 1)

        index_dict = {}
        for idx,char in enumerate(s):
            index_dict[char] = idx

        start_idx, end_idx = 0, 0
        output = []
        for idx,char in enumerate(s):
            end_idx = max(end_idx, index_dict[char])
            if idx == end_idx:
                output.append(end_idx - start_idx + 1)
                start_idx = idx + 1

        return output
    