def main():
    number = int(raw_input("Enter a number: "))
    if (number <= 10):
        print(unit(number))
    else:
        num_tens = number/10
        num_unit = number % 10
        print(tens(num_tens)+unit(num_unit))

        
def unit(number):

    if number < 10:
        if number ==1:
            return  'I'
        elif number == 2:
            return  'II' 
        elif number == 3:
            return  'III'
        elif number == 4:
            return  'IV'
        elif number == 5:
            return  'V'
        elif number == 6:
            return  'VI'
        elif number == 7:
            return  'VII'
        elif number == 8:
            return  'VIII'
        elif number == 9:
            return  'IX'
        elif number == 10:
            return  'X'
def tens(number):
     if number ==1:
         return  'X'
     elif number == 2:
         return 'XX'
     elif number == 3:
         return 'XXX'
     elif number == 4:
         return 'XL'
     elif number == 5:
         return 'L'
     elif number == 6:
         return 'LX'
     elif number == 7:
         return 'LXX'
     elif number == 8:
         return 'LXXX'
     elif number == 9:
         return 'XC'

main()
         
                       
            
     


    


