class AN_Calculation:
    def __init__(self, fast, second) :
        self.fast = fast
        self.second = second

    def plus():
        # This function for Additions more and more numbers
        list = []
        data_num = int(input('How many Data you want to add (+) -- '))
        print('\n')

        while True:
            if data_num == 0:
                break
            user_number = int(input(f'Type {data_num} Data = + '))
            list.append(user_number)
            data_num -= 1

        plus_result = 0
        for i in list:
            plus_result += i
        print(f'This is your Data result = {plus_result} \n')

    def minus():
        # This function for Substraction more and more numbers

        list = []
        data_num = int(input('How many Data you want to Minimize (-) -- '))
        print('\n')

        while True:
            if data_num == 0:
                break
            user_number = int(input(f'Type {data_num} Data = - '))
            list.append(user_number)
            data_num -= 1

        fast_result = list[0]
        second_result = 0

        for i in list[1:]:
            second_result += i
        print(f'This is your Data result = {fast_result-second_result}')

    def multiply():
        # This function for Multiplications more and more numbers

        list = []
        data_num = int(input('How many Data you want to Multiply (*) -- '))
        print('\n')

        while True:
            if data_num == 0:
                break
            user_number = int(input(f'Type {data_num} Data * '))
            list.append(user_number)
            data_num -= 1

        plus_result = 1
        for i in list:
            plus_result *= i
        print(f'\nThis is your Data result = {plus_result}')

    def division():
        # This function for Division more and more numbers

        list = []
        data_num = int(input('How many Data you want to Division (/) -- '))
        print('\n')

        while True:
            if data_num == 0:
                break
            user_number = int(input(f'Type {data_num} Data / '))
            list.append(user_number)
            data_num -= 1

        fast_result = list[0]
        second_result = 1

        for i in list[1:]:
            second_result *= i
        result = fast_result * ( 1 / second_result)
        print(f'This is your Data result = {result}')   

    def choice(self):
        return f'\nAddition  = {self.fast + self.second} \nSubstraction  = {self.fast - self.second} \nMultip;ications  = {self.fast * self.second} \nDivision  = {self.fast / self.second}\n'

       
if __name__ == "__main__":
    
    print(f'\n1 - Standeard Calculator  \n2 - Random Calculator')
    fast_choice = input(f"1 or 2  = ")

    if fast_choice == '1':
        while True :
            print('\n')
            choice = input('What do you want for calculator . Type any one(+ - * / ) or shutDown - ')
            func = AN_Calculation(0,0)

            if choice == "+" :
                AN_Calculation.plus()
            elif choice == "-":
                AN_Calculation.minus()
            elif choice == "*" :
                AN_Calculation.multiply()
            elif choice == "/" :
                AN_Calculation.division()
            elif choice ==  'shutDown':
                break
            else:
                print('Error! Please type again...')        

    elif fast_choice == '2':
        print('\n')
        fast = int(input('Type Fast Number'))
        second = int(input('Type Second Number'))
        re = AN_Calculation(fast,second)
        print(re.choice())

        