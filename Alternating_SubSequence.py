t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    def det_positivity(num):
        if num >0:
            return True
        else:
            return False
    left, right = 0, 0
    if arr[left] > 0:
        pos = True
    else:
        pos = False
    ans = []

    while right < len(arr):
        sign = det_positivity(arr[right])
        max_val = -(10**9)
        while right < len(arr) and sign == pos:
            max_val = max(max_val, arr[right])
            right += 1
            if right < len(arr):
                sign = det_positivity(arr[right])
        #print(left, right)
        if pos == True:
            pos = False
        else:
            pos = True
        left = right
        #print(max_val)
        ans.append(max_val)
    print(sum(ans))

