id = "020718-4123456"

print("성별: " + id[7])
print("연도: " + id[0:2]) # 0부터 2 직전까지
print("월: " + id[2:4])
print("일: " + id[4:6])

print("\n생년월일: " + id[:6]) # 처음부터 6 직전까지
print("뒤 7자리: " + id[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에서부터): " + id[-7:])
# 맨 뒤에서 7까지
# 맨 뒤에서부터 출력을 하는 게 아니라 맨 뒤에서부터 정보를 읽어옴
# 맨 뒷자리는 index가 -1 임
# 그래서 6은 -1, 5는 -2.. 순으로 감