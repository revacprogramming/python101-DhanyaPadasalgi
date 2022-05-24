# Strings

text = "X-DSPAM-Confidence:    0.8475"
a=text.find('0')
t=text[a: ]
t=float(t)
print(t)
