# PROJECT NAME: Project 1 . Explore the Beauty of Automata
# TEAM MEMBERS: Bibek Dhungana, Santona Subedi, Dhan Limbu
# DATE: Nov 4, 2022
# PURPOSE: Construct a NFA (Non Deterministic Automata) and input from the text file and
#          check if the string is acccepted by the Automata.


# This variable gives information if the given input is rejected by the given NFA.
isRejected = True

#NAME: main
#INPUT: N/A
#RETURN TYPE: N/A
#DESCRIPTION: main function of the program

def main():
    print("----------------------------------------INSTRUCTION---------------------------------------------")
    print("There are two different files located in currently working directory.")
    print("Either modify proj-1-machine.txt text file or type proj-1-machine-1.txt to input your own string.")
    print("proj-1-machine.txt has beta as a given tuple and proj-1-machine-1.txt has beta as an empty tuple.")
    print("String Accepted ----- if string is Accepted")
    print("String Rejected ----- if string is rejected")
    print("-------------------------------------------------------------------------------------------------")

    # getting the input from the users( which file to choose)
    user_input = input(
        f"Enter the name of the file you want to use: \n option A: Enter proj-1-machine.txt or A \n option B: Enter proj-1-machine-1.txt or B\n")


    print("-------------------------------------------------------------------------------------------------")

    # if user_input is proj-1-machine.txt or A, it will run NFA with the tuple present in the file
    if (user_input == "proj-1-machine.txt" or user_input.lower() == 'a'):
    

        print("------------------------------------NFA---------------------------------------------------------")

        # opening the file proj-1-machine.txt as file1 -- contains beta as (1101,0001,1110)
        file1 = open("proj-1-machine.txt")

        # reading the contents of the file
        content1 = file1.read()
        
        #getting tuple from the file.
        leftParenthesis = content1.rfind('(');
        rightParenthesis = content1.rfind(')');
        tupleString = (content1[leftParenthesis+1:rightParenthesis-2]).split(',')
      
      
        #getting value of string from the file.
        firstString = tupleString[0].strip();
        secondString = tupleString[1].strip();
        thirdString = tupleString[2].strip();
        
        

        # printing the content of file in the console.
        print(content1)

        print("-----------------------------------OUTPUT---------------------------------------------------------")

        # First State of NFA.runs the first string through the NFA.
        state_q0(firstString)

        if (isRejected == True):
            print("String Rejected")

        # runs the second string through the NFA
        state_q0(secondString)

        if (isRejected == True):
            print("String Rejected")

        # Final State of NFA.runs the third string through the NFA.
        state_q0(thirdString)

        if (isRejected == True):
            print("String Rejected")

    # if user_input is proj-1-machine-1.txt or B, it will run NFA with the tuple present in the file and ask for string input.
    if (user_input == "proj-1-machine-1.txt" or user_input.lower() == "b"):

        print("-----------------------------------NFA---------------------------------------------------------")

        # opening file proj-1-machine-1.txt as open_file variable
        file2 = open("proj-1-machine-1.txt")

        # reading all the content of the file.
        contents = file2.read()

        # printing the content of the in the console.
        print(contents)

        print("-----------------------------------OUTPUT---------------------------------------------------------")


        # getting the input string to test with given NFA.
        user_input = input("Input a string to test if it is accepted by given NFA.")

        # running while loop until the users enter empty string.
        while (user_input != ""):

            # run the users string through the NFA
            state_q0(user_input)

            if (isRejected == True):
                print("String Rejected")
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
            # do nothing.
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
        print("String Accepted!!")

    # if remaining string length is not zero, then the string is rejected.
    else:
        # do nothing.
        pass


# running the main function
main()

print("-------------------------------------End of the Program---------------------------------------------")