class Formular (object):
    
    def __init__(self, P, S, N , I):

        self.P = float(P)
        self.S = float(S)
        self.N = N
        self.I = float(I)
  
    def straightLine(self):

        dc = ((self.P - self.S) / self.N)

        accumulated = 0

        for n in range(0, self.N + 1):

            accumulated += dc

            if (n<1):

                accumulated = 0

            bv = self.P - (n * dc)

            print n, round(dc,1), round(accumulated,1), round(bv,1)

        print "\n straightline ================== \n"
    
    def diminishing(self):

        ct = (1 - ( self.S / self.P ) ** ( 1 / float(self.N) ) )

        P = self.P

        accumulated = 0

        for n in range( 0, self.N + 1 ):

            dc = P * ct

            # find a way to remove this conditional statement

            if (n<1):

                dc = 0

            bv = P - dc

            accumulated += dc

            print n, round(dc, 1) , round(accumulated,1) , round(bv, 1)

            P = bv

        print "\n Diminishing======================= \n"

    def sinking(self):

        f1 = self.P - self.S
        f2 = self.I /  ((( 1 + self.I) ** self.N ) - 1)

        P = self.P 

        accumulated = 0;

        for n in range(0, self.N + 1 ):


            f3 = ( 1 + self.I ) ** (n - 1)

            dc = f1 * f2 * f3

            if (n<1):

                dc = 0

            bv = P - dc

            P = bv

            accumulated += dc

            print n , round(dc, 1), round(accumulated, 1), round(bv, 1)

        print "\n Sinking======================== \n"

    # def table(self, header1, header2, header3):

    #     def box (content):
    #         return  """
    #           +--------------+
    #           |   content    |
    #           +--------------+
    #           """

    #     for i in numbers:
    #         print box(numbers(i));

if __name__ == '__main__':

    def input():

        print "\n =========================== WELCOME TO SAGAT CALCULATOR :D ========================= \n"

        S = raw_input("Input for S: ")
        P = raw_input("Input for P: ")
        N = raw_input("Input for N: ")
        I = raw_input("Input for I: ")

        return dict(S=S, P=P, N=N, I=I)

    inp = input()

    Sagat = Formular(inp['S'], inp['P'], inp['N'], int(inp['I']))

    Sagat.straightLine()
    Sagat.diminishing()
    Sagat.sinking()