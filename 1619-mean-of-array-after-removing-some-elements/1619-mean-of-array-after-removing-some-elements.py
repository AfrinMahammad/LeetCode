class Solution:
    def trimMean(self, arr: List[int]) -> float:
        import statistics as s
        n=len(arr)
        arr.sort()
        return s.mean(arr[((5*n)//100):n-((5*n)//100)])