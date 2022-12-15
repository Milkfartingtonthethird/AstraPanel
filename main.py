# define a list of options for the user to choose from
options = ['Option 1', 'Option 2', 'Option 3']

# print the options for the user
print('''    :::      :::::::: ::::::::::: :::::::::      :::     
  :+: :+:   :+:    :+:    :+:     :+:    :+:   :+: :+:   
 +:+   +:+  +:+           +:+     +:+    +:+  +:+   +:+  
+#++:++#++: +#++:++#++    +#+     +#++:++#:  +#++:++#++: 
+#+     +#+        +#+    +#+     +#+    +#+ +#+     +#+ 
#+#     #+# #+#    #+#    #+#     #+#    #+# #+#     #+# 
###     ###  ########     ###     ###    ### ###     ### ''')
print('---------------')
for i in range(len(options)):
    print(f'{i + 1}: {options[i]}')

# create a variable to track whether the user wants to continue using the menu
continue_using = True

# create a while loop to allow the user to select options and perform actions
while continue_using:
    # prompt the user to enter the number of the option they want to select
    user_input = input('Enter the number of the option you want to select: ')

    # use a try/except block to handle any invalid input from the user
    try:
        # convert the user's input to an integer
        option_number = int(user_input)

        # use an if/elif/else block to perform the appropriate action based on the user's choice
        if option_number == 1:
            # do something for Option 1
            print('You selected Option 1')
        elif option_number == 2:
            # do something for Option 2
            print('You selected Option 2')
        elif option_number == 3:
            # do something for Option 3
            print('You selected Option 3')
        else:
            # handle any invalid option numbers
            print('Invalid option')
    except ValueError:
        # handle any invalid input that cannot be converted to an integer
        print('Invalid input')
