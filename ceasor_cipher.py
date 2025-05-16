"""This is a ceasors cipher, it is capable of encrypting and decrypting capable of alphabets and numbers only no symbols"""

print("Welcome to ceasors cipher".title())

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


while True:
    option1 = input("Do you want to encrypt/decrypt: ").lower()
    # print(option1 == "encrypt")

    if option1 == "encrypt" or option1 == "decrypt":
        option2 = int(input("offset: "))

        if option2 <= 0:
            print("Invalid option, should be greater that 0")
        else:
            message = input("Enter your message here: ").lower()

            if option1 == "encrypt":
                # print("**")
                encrypted_message = ""

                for i in message:
                    index = 0
                    if i in alphabets:
                        for j in range(0, len(alphabets)):
                            if alphabets[j] == i:
                                index = j
                        # print(type(index))
                        index += option2


                        # reducing the number to be within limit of the alphabet list
                        while True:
                            if index > len(alphabets)-1:
                                index -= len(alphabets)
                            else:
                                break
                        encrypted_message += alphabets[index]
                    elif i in numbers:
                        for j in range(0, len(numbers)):
                            if numbers[j] == i:
                                index = j
                                # print(index, "---")
                            # adding the offset
                        index += option2
                        # print(index, "*")

                        # reducing the number to be within limit of the alphabet list
                        while True:
                            if index > len(numbers)-1:
                                index -= len(numbers)
                                # print("*", index)

                            else:
                                break
                        encrypted_message += numbers[index]
                    else:
                        encrypted_message += i
                print(encrypted_message)

            else:
                decrypted_message = ""

                for i in message:
                    index = 0

                    if i in alphabets:
                        for j in range(0, len(alphabets)):
                            if alphabets[j] == i:
                                index = j
                                break
                        
                        index -= option2

                        while True:
                            if index < 0:
                                index += len(alphabets)
                            
                            else:
                                break
                        
                        decrypted_message += alphabets[index]
                    
                    elif i in numbers:
                        index = 0

                        for j in range(0, len(numbers)):
                            if i == numbers[j]:
                                index = j
                                break

                        index -= option2

                        while True:
                            if index < 0:
                                index += len(numbers)

                            else:
                                break
                        
                        decrypted_message += numbers[index]

                    else:
                        decrypted_message += i 
                print(decrypted_message)

                

            # print("*****--***")
        break

                
    else:
        print("Invalid option selected, please select 'encrypt' or 'decrypt'")