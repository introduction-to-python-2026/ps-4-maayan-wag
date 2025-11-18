def split_before_each_uppercases(formula):
    digit_location = 1
    for chr in formula[1:]:
      if chr.isdigit():
        break
      digit_location +=1
    if digit_location == len(formula):
      return formula,1
    return formula[:digit_location],int(formula[digit_location:])


def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
