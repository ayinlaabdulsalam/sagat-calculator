from formular import Formular

def input():

    S = float(raw_input("\nInput for S: ").strip())
    P = float(raw_input("Input for P: ").strip())
    N = int(raw_input("Input for N: ").strip())
    I = float(raw_input("Input for I in decimal: ").strip())

    return dict(S=S, P=P, N=N, I=I)

def askMethod():

    return raw_input("\n Press A to run all methods  |   Press L for straight link  |  Press D for diminishing |  Press S for sinking\n ").strip().upper()

if __name__ == '__main__':

    print "\n \t \t \t =======================     WELCOME TO SAGAT CALCULATOR :D     ======================== \n"

    meth = askMethod()

    validInput = meth in ['A', 'L', 'D', 'S']

    if (not validInput):

        print "\t \t \t ********************** C'mon mahn Mr Sagat how to use this thing ****************************"

        askMethod()

    inp = input()

    Sagat = Formular(inp['S'], inp['P'], inp['N'], inp['I'])

    if (meth == 'A'):

        Sagat.straightLine()
        Sagat.diminishing()
        Sagat.sinking()

    elif (meth == 'L'):

        Sagat.straightLine()

    elif (meth == 'D'):

        Sagat.diminishing()

    elif (meth == 'S'):

        Sagat.sinking()