attempt=(0)
while True:
    number=int(input("guess the number:"))
    if number<7:
     print("Too low")
     attempt=attempt+1
    elif number>7:
      print("too high")
      attempt=attempt+1
      
    else:
     print("correct")
     attempt=attempt+1
     break


print("attepmts:",attempt)