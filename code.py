%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

p1 = [-1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1]
p2 = [1, -1, 1, -1, -1, -1]
p3 = [-1, -1, -1, 1, -1, 1, 1]
p4 = [1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1]
p5 = [1, 1, 1, -1, -1, -1]
p6 = [1, 1, -1, -1, -1, 1, -1]
p7 = [1, -1, 1, -1, -1]


class Wave:
    def __init__(self, pattern, name):
        self.p = pattern
        self.N = len(self.p)
        self.r_list = []
        self.name = name
    
    def s_bar(self):
        s = 0
        for i in range(self.N):
            s = s + self.p[i]
        
        return s/self.N
    
    def r(self, rag):
        s = 0
        for i in range(self.N):
            s = s + self.p[i]*self.p[(i-rag)%self.N]
            
        return s/self.N
    
    def r_listup(self):
        for i in range(self.N):
            self.r_list = self.r_list + [self.r(i)]
        
        return self.r_list
    
    def print_data(self):
        self.r_listup()
        plt.plot(self.r_list, label=self.name)
        plt.legend()
        avg = self.s_bar()
        print("average:" + str(avg))
        

w = Wave(p1, "Pattern1")
w.print_data()
w = Wave(p2, "Pattern2")
w.print_data()
w = Wave(p3, "Pattern3")
w.print_data()
w = Wave(p4, "Pattern4")
w.print_data()
w = Wave(p5, "Pattern5")
w.print_data()
w = Wave(p6, "Pattern6")
w.print_data()
w = Wave(p7, "Pattern7")
w.print_data()
