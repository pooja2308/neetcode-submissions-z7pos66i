class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        from collections import Counter
        count = Counter(blocks[:k])
        white_count = count['W']
        answer = white_count

        left = 0
        for right in range(k, len(blocks)):
            if blocks[left] == 'W':
                white_count -= 1
            if blocks[right]  == 'W':
                white_count += 1
            answer = min(answer, white_count)
            left += 1
        return answer

        