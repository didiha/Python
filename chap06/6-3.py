# while
customer = "a"
index = 5
while index >= 1:
    print("{0}, 음료가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("음료는 폐기처분되었습니다.")

customer = "b"
index = 1
while True:
    print("{0}, 음료가 준비되었습니다. 호출 {1}회".format(customer, index))
    index += 1
    if index == 6:
        print("음료는 폐기처분되었습니다.")
        break

customer = "c"
someone = "Unknown"

while someone != customer:
    print("{0}, 음료가 준비되었습니다.".format(someone))
    someone = input("이름이 어떻게 되세요? ")