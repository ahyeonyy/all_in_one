import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

answer = 0

heapq.heapify(scoville)

for h in scoville:
    if h <= K :
        min_scovile = heapq.heappop(scoville)
        heapq.heappush(scoville,min_scovile +(heapq.heappop(scoville) *2)) 
        answer += 1
    else:
        break
            
    if scoville[-1] <= K:
        print(-1)
print(answer)