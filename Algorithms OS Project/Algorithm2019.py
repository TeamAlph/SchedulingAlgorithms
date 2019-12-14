# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:56:39 2019

@author: usman
"""

import winsound
import wx
import platform
import matplotlib.pyplot as plt
import socket
import os
import time
import threading
pol=""
class ChildFrame(wx.Frame):

    def PIKO3(self,event):
            pass
class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i
             
class MainPanel(wx.Panel):
    
    def __init__(self, parent, bg_img='images\\u15.jpg'):
        
        wx.Panel.__init__(self, parent=parent)
        
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.bg = wx.Bitmap(bg_img)
        self._width, self._height = self.bg.GetSize()
        
        
        usman21 = wx.Button(self, -1, "", pos=(330,450),size=(41,40))
        usman21.Bind(wx.EVT_BUTTON,self.mynettest)
        usman21.SetBitmap(wx.Bitmap('images\\wifi4.png'))
       
        
        
        usman22 = wx.Button(self, -1, "", pos=(390,450),size=(41,40))
        usman22.Bind(wx.EVT_BUTTON,self.myspeaker)
        usman22.SetBitmap(wx.Bitmap('images\\sp.png'))
       
        
        usman23 = wx.Button(self, -1, "", pos=(450,450),size=(41,40))
        usman23.Bind(wx.EVT_BUTTON,self.myexit)
        usman23.SetBitmap(wx.Bitmap('images\\pow.png'))
        
        usman24 = wx.Button(self, -1, "", pos=(510,450),size=(41,40))
        usman24.Bind(wx.EVT_BUTTON,self.my144)
        usman24.SetBitmap(wx.Bitmap('images\\me.png'))
        
        usman25 = wx.Button(self, -1, "", pos=(570,450),size=(41,40))
        usman25.Bind(wx.EVT_BUTTON,self.myblue)
        usman25.SetBitmap(wx.Bitmap('images\\bl1.png'))
        
        usman26 = wx.Button(self, -1, "", pos=(630,450),size=(41,40))
        usman26.Bind(wx.EVT_BUTTON,self.mynet)
        usman26.SetBitmap(wx.Bitmap('images\\netcheck.png'))
        
        usman = wx.Button(self, -1, "BESTFIT", pos=(55,170),size=(155,65))
        usman.Bind(wx.EVT_BUTTON,self.my)
        usman.SetBackgroundColour('STEEL BLUE')
        usman.SetForegroundColour(wx.WHITE)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        usman.SetFont(font)
        
        usman1 = wx.Button(self, -1,"ROUNDROBIN", pos=(55, 255),size=(155,65))
        usman1.Bind(wx.EVT_BUTTON,self.my1)
        usman1.SetBackgroundColour('STEEL BLUE')
        usman1.SetForegroundColour(wx.WHITE)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        usman1.SetFont(font)
        
        usman2 = wx.Button(self, -1, "FIRSTFIT", pos=(55, 340),size=(155,65))
        usman2.Bind(wx.EVT_BUTTON,self.my2)
        usman2.SetBackgroundColour('STEEL BLUE')
        usman2.SetForegroundColour(wx.WHITE)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        usman2.SetFont(font)
        
        usman3 = wx.Button(self, -1, "FCFS", pos=(790, 170),size=(155,65))
        usman3.Bind(wx.EVT_BUTTON,self.my3)
        usman3.SetBackgroundColour('STEEL BLUE')
        usman3.SetForegroundColour(wx.WHITE)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        usman3.SetFont(font)
        
        usman4 = wx.Button(self, -1, "SJF", pos=(790, 255),size=(155,65))
        usman4.Bind(wx.EVT_BUTTON,self.my4)
        usman4.SetBackgroundColour('STEEL BLUE')
        usman4.SetForegroundColour(wx.WHITE)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        usman4.SetFont(font)
        
        usman5 = wx.Button(self, -1, "PRIORITY", pos=(790, 340),size=(155,65))
        usman5.Bind(wx.EVT_BUTTON,self.my5) 
        usman5.SetBackgroundColour('STEEL BLUE')
        usman5.SetForegroundColour(wx.WHITE)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL)
        usman5.SetFont(font)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(usman, 23, wx.ALL, 500)
        self.SetSizer(hSizer)
        self.write("----------SYSTEM IS STARTING-----------")
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        g=time.strftime("%H:%M ")
        text = wx.StaticText(self, 0, g, (5000, 10))
        text.SetBackgroundColour('STEEL BLUE')
        text.SetForegroundColour(wx.WHITE)
        font = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        text.Show()
        
        '''
        text1 = wx.StaticText(self, 0, "MANAGEMENT ALGORITHM", (115,10))
        text1.SetBackgroundColour('STEEL BLUE')
        text1.SetForegroundColour(wx.WHITE)
        font = wx.Font(25, wx.MODERN, wx.NORMAL, wx.NORMAL)
        text1.SetFont(font)
        text1.Show()
        '''
        '''
        usman14 = wx.Button(self, -1, "", pos=(6, 6),size=(75,75))
        usman14.Bind(wx.EVT_BUTTON,self.my14)
        usman14.SetBackgroundColour('STEEL BLUE')
        usman14.SetForegroundColour(wx.WHITE)
        usman14.SetBitmap(wx.Bitmap('images\\pro.png'))
        fname = "C:\\Users\\usman\\Downloads\\mb.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
        '''
    def mynettest(self,event):
        self.main()
    def myspeaker(self,event):
        fname = "images\\mb.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
    def myexit(self,event):
        pass
    def myblue(self,event):
        mess="Not Connected"
        fig = plt.figure(figsize=(6,5))
        fig.text(0.5, 1, mess, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
        fname = "images\\click.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
    def mynet(self,event):
        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii") # needed in python 3
        results = results.replace("\r","")
        ls = results.split("\n")
        ls = ls[4:]
        ssids = []
        x = 0
        while x < len(ls):
            if x % 5 == 0:
                ssids.append(ls[x])
            x += 1
        print(ssids)
        fig = plt.figure(figsize=(6,5))
        fig.text(0.5, 1, ssids, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    def my144(self,event):
        p=os.getenv('username')
        l=socket.gethostname()
        l1=platform.system()
        l2=platform.release()
        fig = plt.figure(figsize=(3,2))
        fig.text(0.5, 1, "--User-- "+p+" --DeviceModel-- "+l+" --OperatingSystem-- "+l1+" --Version-- "+l2, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    def my14(self,event):
        p=os.getenv('username')
        l=socket.gethostname()
        l1=platform.system()
        l2=platform.release()
        fig = plt.figure(figsize=(3,2))
        fig.text(0.5, 1, "--User-- "+p+" --DeviceModel-- "+l+" --OperatingSystem-- "+l1+" --Version-- "+l2, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
  
    def heron(self,a):
        new=1
        num_threads=0
        num_threads += 1
    
    # code has been left out, see above
        num_threads -= 1
        return new
  
   
    def left1(self,event):
        pass
           
    def uhm(self, event):
        pass
    def OnSize(self, size):
        
        self.Layout()
        self.Refresh()
    def my(self,event):
        blockSize = [100, 500, 200, 300, 600]  
        processSize = [212, 417, 112, 426]  
        m = len(blockSize)  
        n = len(processSize)  
  
        self.bestFit(blockSize, m, processSize, n) 
    def bestFit(self,blockSize, m, processSize, n): 
      
    # Stores block id of the block  
    # allocated to a process  
        allocation = [-1] * n  
      
    # pick each process and find suitable  
    # blocks according to its size ad  
    # assign to it 
        for i in range(n): 
          
        # Find the best fit block for 
        # current process  
            bestIdx = -1
            for j in range(m): 
                if blockSize[j] >= processSize[i]: 
                    if bestIdx == -1:  
                        bestIdx = j  
                    elif blockSize[bestIdx] > blockSize[j]:  
                        bestIdx = j 
  
        # If we could find a block for  
        # current process  
            if bestIdx != -1: 
              
            # allocate block j to p[i] process  
                allocation[i] = bestIdx  
  
            # Reduce available memory in this block.  
                blockSize[bestIdx] -= processSize[i] 
        print("----THIS IS THE BESTFIT ALGORITHM------")
        print("Process No. Process Size     Block no.") 
        for i in range(n): 
            print(i + 1, "       ", processSize[i],  
                                end = "      ")  
            if allocation[i] != -1:  
                print(allocation[i] + 1)  
            else: 
                print("Not Allocated") 
        print("---------------------------------------")
        print("")
         
    def my1(self,event): 
        proc = [1, 2, 3] 
        n = 3 
        burst_time = [10, 5, 8]  
        quantum = 2;  
        self.findavgTime(proc, n, burst_time, quantum)
        
    def findWaitingTime(self,processes, n, bt,  
                         wt, quantum):  
        rem_bt = [0] * n 
        for i in range(n):  
            rem_bt[i] = bt[i] 
        t = 0 # Current time  
        while(1): 
            done = True
            for i in range(n): 
                    if (rem_bt[i] > 0) : 
                        done = False 
                        
                        if (rem_bt[i] > quantum) : 
                            t += quantum  
                            rem_bt[i] -= quantum  
                        else: 
                                t = t + rem_bt[i]  
                                wt[i] = t - bt[i]  
                                rem_bt[i] = 0
                                
            if (done == True): 
                break
    def findTurnAroundTime(self,processes, n, bt, wt, tat): 
        for i in range(n): 
            tat[i] = bt[i] + wt[i]  
    def findavgTime(self,processes, n, bt, quantum):  
                wt = [0] * n 
                tat = [0] * n   
                self.findWaitingTime(processes, n, bt,wt, quantum)  
                self.findTurnAroundTime(processes, n, bt, wt, tat) 
                print("----THIS IS THE ROUNDROBIN ALGORITHM------")
                print("Processes    Burst Time     Waiting","Time    Turn-Around Time") 
                total_wt = 0
                total_tat = 0
                for i in range(n): 
                    
                    total_wt = total_wt + wt[i]  
                    total_tat = total_tat + tat[i]  
                    print(" ", i + 1, "\t\t", bt[i],  
                          "\t\t", wt[i], "\t\t", tat[i]) 
                    
                print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
                print("Average turn around time = %.5f "% (total_tat / n))  
                print("-----------------------------------------")
                print("")
                    
                    
    def my2(self,event):
         blockSize = [100, 500, 200, 300, 600]  
         processSize = [212, 417, 112, 426] 
         m = len(blockSize) 
         n = len(processSize) 
         self.firstFit(blockSize, m, processSize, n) 
   
    def firstFit(self,blockSize, m, processSize, n): 
        allocation = [-1] * n
        for i in range(n): 
            for j in range(m): 
                if blockSize[j] >= processSize[i]: 
                    
                    # allocate block j to p[i] process  
                    allocation[i] = j  
                    
                    # Reduce available memory in this block.  
                    blockSize[j] -= processSize[i]  
                    
                    break
        print("------THIS IS THE FIRSTFIT ALGORITHM------")        
        print(" Process No. Process Size      Block no.") 
        for i in range(n): 
            print(" ", i + 1, "      ", processSize[i],  
                              "      ", end = " ")  
            if allocation[i] != -1:  
                        print(allocation[i] + 1)  
            else: 
                            print("Not Allocated") 
        print("------------------------------------------")
        print("")
                            
    def my3(self,event):
          # process id's 
          processes = [ 1, 2, 3] 
          n = len(processes) 
          
          # Burst time of all processes 
          burst_time = [10, 5, 8] 
          
          self.findavg(processes, n, burst_time) 
    def findWaiting(self,processes, n, bt, wt): 
  
  
        wt[0] = 0
        for i in range(1, n ): 
            wt[i] = bt[i - 1] + wt[i - 1]  
  
    def findTurnAround(self,processes, n,bt, wt, tat): 
        
        for i in range(n): 
            tat[i] = bt[i] + wt[i] 

    def findavg(self,processes, n, bt): 
        
        wt = [0] * n 
        tat = [0] * n  
        total_wt = 0
        total_tat = 0
        self.findWaiting(processes, n, bt, wt) 
        self.findTurnAround(processes, n,bt, wt, tat) 
        print("------THIS IS THE FCFS ALGORITHM------")
        print( "Processes Burst time " +" Waiting time " +" Turn around time") 
        
        for i in range(n): 
            
            total_wt = total_wt + wt[i] 
            total_tat = total_tat + tat[i] 
            print(" " + str(i + 1) + "\t\t" + 
                        str(bt[i]) + "\t " + 
                        str(wt[i]) + "\t\t " + 
                        str(tat[i]))  
            
        print( "Average waiting time = "+str(total_wt / n)) 
        print("Average turn around time = "+str(total_tat / n)) 
        print("------------------------------------------")
        print("")
    proc = [[1, 6, 1], [2, 8, 1], 
            [3, 7, 2], [4, 3, 3]]    
    def my4(self,event):
        
         n = 4
         self.findavgsjf(self.proc, n) 
    
    def findWaitsjf(self,processes, n, wt):  
        rt = [0] * n 
        for i in range(n):  
            rt[i] = processes[i][1] 
        complete = 0
        t = 0
        minm = 999999999
        short = 0
        check = False
        while (complete != n): 
              for j in range(n): 
                    if ((processes[j][2] <= t) and 
                        (rt[j] < minm) and rt[j] > 0): 
                        minm = rt[j] 
                        short = j 
                        check = True
              if (check == False): 
                            t += 1
                            continue
                        
              rt[short] -= 1
                        
              minm = rt[short]  
              if (minm == 0):  
                 minm = 999999999
                            
              if (rt[short] == 0):  
                                
                  complete += 1
                  check = False
                                
                  fint = t + 1
                                
                  wt[short] = (fint - self.proc[short][1] - self.proc[short][2]) 
                                
                  if (wt[short] < 0): 
                      wt[short] = 0
                                    
              t += 1
              
    def findTurnsjf(self,processes, n, wt, tat):  
      
        for i in range(n): 
            tat[i] = processes[i][1] + wt[i] 
    def findavgsjf(self,processes, n):  
        wt = [0] * n 
        tat = [0] * n   
        self.findWaitsjf(processes, n, wt)  
        self.findTurnsjf(processes, n, wt, tat)  
        print("------THIS IS THE SJF ALGORITHM------")
        print("Processes    Burst Time     Waiting",  "Time     Turn-Around Time") 
        total_wt = 0
        total_tat = 0
        for i in range(n): 
            total_wt = total_wt + wt[i]  
            total_tat = total_tat + tat[i]  
            print(" ", processes[i][0], "\t\t",  
                   processes[i][1], "\t\t",  
                   wt[i], "\t\t", tat[i]) 
        
        print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
        print("Average turn around time = ", total_tat / n)  
        print("------------------------------------------")
        print("")
                                    
    proc1 = [[1, 10, 1],  
            [2, 5, 0],  
            [3, 8, 1]] 
    def my5(self,event):
        
            n = 3
            self.priorityScheduling(self.proc1, n) 
    def findWaitpr(self,processes, n, wt):  
        wt[0] = 0
        for i in range(1, n):  
            wt[i] = processes[i - 1][1] + wt[i - 1]  
    def findTurnpr(self,processes, n, wt, tat):  
      
        for i in range(n): 
            tat[i] = processes[i][1] + wt[i] 
            
    def findavgpr(self,processes, n):  
        wt = [0] * n 
        tat = [0] * n  
        self.findWaitpr(processes, n, wt)   
        self.findTurnpr(processes, n, wt, tat) 
        print("------THIS IS THE PIRORITY ALGORITHM------")
        print("\nProcesses    Burst Time    Waiting","Time    Turn-Around Time") 
        total_wt = 0
        total_tat = 0
        for i in range(n): 
            total_wt = total_wt + wt[i]  
            total_tat = total_tat + tat[i]  
            print(" ", processes[i][0], "\t\t",  
                   processes[i][1], "\t\t",  
                   wt[i], "\t\t", tat[i])
        print("\nAverage waiting time = %.5f "%(total_wt /n)) 
        print("Average turn around time = ", total_tat / n) 
        print("------------------------------------------")
        print("")
    def priorityScheduling(self,proc1, n): 
        proc1 = sorted(proc1, key = lambda proc1:proc1[2],  
                                  reverse = True);  
  
        print("Order in which processes gets executed") 
        for i in proc1: 
            print(i[0], end = " ") 
        self.findavgpr(proc1, n)  
    

    def write(self, text):
        print(text)
        
    def OnEraseBackground(self, evt):
        pass

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)

    def Draw(self, dc):
        cliWidth, cliHeight = self.GetClientSize()
        if not cliWidth or not cliHeight:
            return
        dc.Clear()
        xPos = (cliWidth - self._width)/2
        yPos = (cliHeight - self._height)/2
        dc.DrawBitmap(self.bg, xPos, yPos)
    
        
app = wx.App()

frame = wx.Frame(None, size=(1024,620))
frame.SetIcon(wx.Icon("C:\\Users\\usman\\Pictures\\ThreadmanagementSystem-master\\Project Images Os\\hvt.ico"))
panel = MainPanel(frame)

frame.Show()
app.MainLoop()
del app