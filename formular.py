class Formular (object):
    
    def __init__(self, P, S, N , I):

        self.P = P
        self.S = S
        self.N = N
        self.I = I
  
    def straightLine(self):

        print self.tableHeader('STRAIGHT LINE')

        dc = ((self.P - self.S) / self.N)

        accumulated = 0

        for n in range(0, self.N + 1):

            accumulated += dc

            if (n<1):

                accumulated = 0

            bv = self.P - (n * dc)

            print self.table(n, round(dc,1), round(accumulated,1), round(bv,1))

    
    def diminishing(self):

        print self.tableHeader('DIMINISHING')

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

            print self.table(n, round(dc,1), round(accumulated,1), round(bv,1))

            P = bv

    def sinking(self):

        print self.tableHeader('SINKING')

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

            print self.table(n, round(dc,1), round(accumulated,1), round(bv,1))

    def tableHeader(self, title):

        header = """\t \t \t \t +------+---------------+-------------------+--------------+
                                 | Time | Depriciation  |  Accumulated Dep  |  Book Value  |
                                 +------+---------------+-------------------+--------------+"""

        return "\n  \n \t \t \t \t \t \t \t "+ title + "\n " + header

    def table(self, time, dc, accumulated, bv):

        return """\t \t \t \t |  """  + str(time).zfill(2).center(2)+  """  |  """ + str(dc).center(11) + """  |  """ + str(accumulated).center(15) + """  |  """ + str(bv).center(10) + """  |
                                 ----------------------------------------------------------- """