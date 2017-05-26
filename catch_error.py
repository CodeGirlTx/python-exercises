
def catch_error ():
  while 1:
    try:
      x = int(input("Please enter a number: "))
    except ValueError:
        raiseValueError("This is not a number.")
      print("Enter a integer, duh!")

if __name__ == "--main--":
    catch_error()


# if you take away ValueError then you can catch more errors
#but it will silently keep on running.
