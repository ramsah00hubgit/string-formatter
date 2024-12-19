#  string formatters "% operator"
x = 10 ; printer = "hppp"
print("I just printed %s pages to the printer %s" %(x,printer))

# string formatters - " .format() method"
x = 190; printer="hp"
print("I just printed {0} pages to the printer {1}" .format(x,printer))
print("I just printed{x} pages to the printer {printer}" .format(x=2,printer="hp"))
x = 13 ; printer = "gh"
print(f"I just printed {x} pages to the printer {printer}")



