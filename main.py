# PROJECT NAME: Project 1 . Explore the Beauty of Automata
# TEAM MEMBERS: Bibek Dhungana, Santona Subedi, Dhan Limbu
# DATE: Nov 4, 2022
# PURPOSE: Construct a NFA (Non Deterministic Automata) and input from the text file and check if the string
#          is acccepted by the Automata.


# This Flag gives information if the given input is rejected by the given NFA.
isRejected = True


# main function of the program
def main():
    print("----------------------------------------INSTRUCTION---------------------------------------------")
    print("There are two different files located in currently working directory.")
    print("Either modify proj-1-machine.txt text file or type proj-1-machine-1.txt to input your own string.")
    print("proj-1-machine.txt has beta as a given tuple and proj-1-machine-1.txt has beta as an empty tuple.")
    print("-------------------------------------------------------------------------------------------------")

    # getting the input from the users( which file to choose)
    user_input = input(
        f"Enter the name of the file you want to use: \n option A:proj-1-machine.txt (A) \n option B:proj-1-machine-1.txt (B)\n")

    print("-------------------------------------------------------------------------------------------------")

    # if user_input is proj-1-machine.txt or A, it will run NFA with the tuple present in the file
    if (user_input == "proj-1-machine.txt" or user_input.lower() == 'a'):
        a = "1101"
        b = "0001"
        c = "1110"
        print("***********NFA************")
        # opening the file proj-1-machine.txt as file1 -- contains beta as (1101,0001,1110)
        with open("proj-1-machine.txt") as file1:

            # reading the contents of the file
            content1 = file1.read()

            # printing the content of file in the console.
            print(content1)

        # First State of NFA.runs the first string through the NFA.
        state_q0(a)  

        if (isRejected == True):
            print("rejected")
            
        # runs the second string through the NFA
        state_q0(b) 
        
        if (isRejected == True):
            print("rejected")
            
        #Final State of NFA.runs the third string through the NFA. 
        state_q0(c)  
        
        if (isRejected == True):
            print("rejected")

    # if user_input is proj-1-machine-1.txt or B, it will run NFA with the tuple present in the file and ask for string input.
    if (user_input == "proj-1-machine-1.txt" or user_input.lower() == "b"):
        print("*******NFA*******")
        # opening file proj-1-machine-1.txt as open_file variable
        with open("proj-1-machine-1.txt") as file2:

            # reading all the content of the file.
            contents = file2.read()

            # printing the content of the in the console.
            print(contents)

            # getting the input string to test with given NFA.
        user_input = input("Input a string to test if it is accepted by NFA.")

        # running while loop until the users enter empty string.
        while (user_input != ""):

            # run the users string through the NFA
            state_q0(user_input)

            if (isRejected == True):
                print("rejected")
            user_input = input("Input a string or type an empty string to exit the program:")


# NAME: state_q0
# INPUT : string
# RETURN TYPE: void
# DESCRIPTION: function to define state q0 of the NFA
def state_q0(n):
    # accessing the global variable rejectedFlag
    global isRejected

    # if length of string is empty when you are in this state , the string is rejected.
    if (len(n) == 0):
        isRejected = True

        # if the length if string is not zero
    else:
        # if the current character is zero, then move to state q1 or q0 -- uses recursion here. (stack is used implicitly by recursion)
        if (n[0] == "0"):
            state_q0(n[1:])  # removing the first character of the string and calling state_q0 function
            state_q1(n[1:])  # removing the first character of the string and calling state_q1 function

        # if the current character is 1, then go to q0.
        elif (n[0] == "1"):
            state_q0(n[1:])  # removing the first character of the string and calling state_q0 function


# NAME: state_q1
# INPUT : string
# RETURN TYPE: void
# DESCRIPTION: function to define state q1 of the NFA
def state_q1(n):
    # accessing the global variable inside the function.
    global isRejected

    # If you are in this state and length of string is zero, then rejected.
    if (len(n) == 0):
        isRejected = True
    else:
        # if the first index in the string is 0, then there is nothing to go.
        if (n[0] == "0"):
            pass
        # if the first index in the string is 1, then move to state q2.
        elif (n[0] == "1"):
            state_q2(n[1:])


# NAME: state_q2
# INPUT : string
# RETURN TYPE: void
# DESCRIPTION: function to define state q1 of the NFA. Final state of NFA.
def state_q2(n):
    # accessing the global value inside the function.
    global isRejected

    # this is final state and if the remaining string is empty, the entire string is accepted.
    if (len(n) == 0):
        isRejected = False
        print("accepted")

    # if remaining string length is not zero, then the string is rejected.
    else:
        pass


# running the main function
main()
print("-------------------------------------End of the Program--------------------------------------------------")