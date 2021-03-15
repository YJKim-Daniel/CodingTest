# 내 답안이 코드로 보면 더 깔끔해 보이기는 하는데,
# 속도 측면에서는 for문 하나로 한번에 분류하는게 나을 수 있음

str_input = input()

# chr와 digit 분류
list_chr_inputs = [x for x in str_input if x.isalpha()]
list_digit_inputs = [x for x in str_input if x.isdigit()]

# 문자 종류에 따른 요구사항 처리
list_chr_inputs.sort()
int_digit_summed = sum(map(int, list_digit_inputs))

# 결과 출력
result = ''.join(list_chr_inputs) + str(int_digit_summed)
print(result)

# K1KA5CB7
# AJKDLSI412K4JSJ9D