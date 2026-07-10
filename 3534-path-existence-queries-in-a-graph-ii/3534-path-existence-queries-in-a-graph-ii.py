class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        pairs = sorted((x, i) for i, x in enumerate(nums))
        LOG = 20
        up = [[0] * LOG for _ in range(n)]

        r = n - 1
        for l in range(n - 1, -1, -1):
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1
            i = pairs[l][1]
            j = pairs[r][1]
            up[i][0] = j
            for k in range(1, LOG):
                up[i][k] = up[up[i][k - 1]][k - 1]

        ans = []

        for u, v in queries:
            if nums[u] > nums[v]:
                u, v = v, u

            if u == v:
                ans.append(0)
                continue

            if nums[u] == nums[v]:
                ans.append(1)
                continue

            dist = 0
            for k in range(LOG - 1, -1, -1):
                if nums[up[u][k]] < nums[v]:
                    dist += 1 << k
                    u = up[u][k]

            if nums[up[u][0]] < nums[v]:
                ans.append(-1)
            else:
                ans.append(dist + 1)

        return ans