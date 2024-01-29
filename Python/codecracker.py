import random
correct_pin = "8485"
while True:
  attempt = ""
  for _ in range(4):
    digit = random.randint(0, 9)
    attempt += str(digit)
  if attempt == correct_pin:
    print(f"PIN code cracked! The code is: {attempt}")
    break