# end of chapter problem
def collatz(number):
   if number % 2 == 0:
        return number // 2
   elif number % 2 == 1:
        return 3* number + 1


print('Please enter a number!')
entry = input()
while entry !=1:
    try:
        entry=collatz(int(entry))
    except ValueError:
        print('Please enter an integer value. Thank you!')
        break
    print(entry)

