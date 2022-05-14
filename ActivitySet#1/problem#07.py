# Strings

def str():
  text = "X-DSPAM-Confidence:    0.8475"
  string = text.find("0.8475")
  ans = text[string::1]
  fans = float(ans)
  print(fans)


str()

