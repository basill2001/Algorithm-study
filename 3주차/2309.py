# 난쟁이들의 키 받기
heights=[]
for i in range(9):
    heights.append(int(input()))

result=[]
# 2345678

# 차례로 뽑기
for a in range(3):
    for b in range(a+1,4):
        for c in range(b+1,5):
            for d in range(c+1,6):
                for e in range(d+1,7):
                    for f in range(e+1,8):
                        for g in range(f+1,9):
                            ha=heights[a]
                            hb=heights[b]
                            hc=heights[c]
                            hd=heights[d]
                            he=heights[e]
                            hf=heights[f]
                            hg=heights[g]
                            # 합이 100이면 정답
                            if ha+hb+hc+hd+he+hf+hg==100:
                                result.append([ha,hb,hc,hd,he,hf,hg])

# 첫번째 결과
result[0].sort()
# 출력
for dwarf in result[0]:
    print(dwarf)
