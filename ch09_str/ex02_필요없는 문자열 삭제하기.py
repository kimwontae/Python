#필요없는 문자열 삭제하기
#str.strip([chars])
print("aaaaaaaaPythonaaaaaaaaa".strip('a'))


test_str="apyathonbbbbbaaa"
temp1=test_str.strip('a')
print(temp1)

print(temp1.strip('b'))

print(test_str.strip('ab'))