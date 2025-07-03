dict={"Suraj":75,
      "Shyam":85,
      "Suryanshu":95,
      "Dhruv":62}
user_input=input("enter a name to get their marks:")
a=dict.get(user_input)
if user_input in dict:
    print("marks of {} is {}".format(user_input,a))
else:
    print("name not found")
