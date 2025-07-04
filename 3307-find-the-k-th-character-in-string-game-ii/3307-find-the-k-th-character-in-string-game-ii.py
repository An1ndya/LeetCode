class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        lengths = [1]  # initial word length is 1

        for op in operations:
            if op == 0:
                lengths.append(lengths[-1] * 2)
            else:
                lengths.append(lengths[-1] * 2)
            
            # Cap if length exceeds k to avoid overflow
            if lengths[-1] >= k:
                break

        ops_to_consider = len(lengths) - 1
        shift_count = 0

        while ops_to_consider > 0:
            curr_op = operations[ops_to_consider - 1]
            prev_len = lengths[ops_to_consider - 1]

            if k > prev_len:
                k -= prev_len
                if curr_op == 1:
                    shift_count += 1
            ops_to_consider -= 1

        # Now k=1, word[1] = 'a'
        char_code = (ord('a') - ord('a') + shift_count) % 26
        result_char = chr(ord('a') + char_code)

        return result_char
