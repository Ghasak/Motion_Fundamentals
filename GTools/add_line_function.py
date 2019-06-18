import numpy as np

def add_line(message):
    """ This Function is used to type fancy printing
        created for the purpose of isolating all the
        commands and functions in python.
    """

    #N_spaces = message.count(' ') # From both sides
    banner = 70
    words = [message]
    word_sum = sum(len(i) for i in words)
    margin1 = int(banner/5)*"-"
    margi1_len = len(margin1)
    margin2 = (banner-(margi1_len+word_sum+2))*"-"
    if len(margin1+message+margin2) < banner:
        """
        Here for simple one line sentence we add
        directly the margins with the message
        """
        print(banner*"-")
        print(f"""{margin1} {message} {margin2}""")
        print(banner*"-")
    else:
        """
        Here we check the number of words and reset the list and
        spaces everytime we go to a new line until the message
        is finished.
        """
        print(banner*"-")
        wordsx = message.split()
        xr = 4 # alignment added later (adjusted manually)
        i = 0
        spacex = 0
        listwords = []
        while i < len(wordsx):

            listwords.append(wordsx[i])
            if sum(len(i) for i in listwords) + spacex < banner-xr:
                print(wordsx[i], end = " ")
                spacex = spacex +1

            else:
                print(wordsx[i])
                listwords = []
                spacex = 0

            i = i +1

        print("\n", end= "")
        print(banner*"-")



def main():
    # Test of your function is here
    add_line("This is short sentence")

    add_line("Apple and Orange with many other furits are so important to the body which we have to say it everyday!!")

    dd_line("Here is another example that I have used so long sentences which I will use from now on to check several ways that you can see I am adding more than two lines here to check if the function is still working and this could cause some problem in the future")

if __name__ == "__main__":
        pass

