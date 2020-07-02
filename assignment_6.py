text = "X-DSPAM-Confidence:    0.8475";
result1=text.find(':')
print(result1)
result2=text.find('5')
print(result2)
result3=text[result1+1:result2+1]
print(result3)
print(float(result3.lstrip()))

