import tkinter as tk
import OsInfoDefs as osdef
import tkinter.ttk as ttk
import NetworkSet
from tkinter import messagebox


class Mainui(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        MainFrame=tk.Frame(self)
        MainFrame.pack(fill='both',expand=True)
        Systeminfo=tk.LabelFrame(MainFrame,text='System Info', relief="ridge",font=('Malgun Gothic',18, 'bold'), bd=2)
        Systeminfo.pack(side='left',fill='both',expand=True)
        Networkinfo=tk.LabelFrame(MainFrame,text='Network Info', relief="ridge",font=('Malgun Gothic',18, 'bold'), bd=2)
        Networkinfo.pack(side='left',fill='both',expand=True)
        Netinfofull=tk.Frame(Networkinfo, relief="solid",bg='white')
        Netinfofull.pack(side='top',fill='both',expand=True)
        Infofull=tk.Frame(Systeminfo, relief="solid",bg='white')
        Infofull.pack(side='top',fill='both',expand=True)
        btframe=tk.Frame(Systeminfo, relief="solid",bg='white')
        btframe.pack(side='top',fill='both',expand=True)
        netbtframe=tk.Frame(Networkinfo, relief="solid",bg='white')
        netbtframe.pack(side='bottom',fill='both',expand=True)
        label1=tk.Label(Infofull,text='Last Boottime:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=12)
        label1.grid(row=0,column=0)
        label2=tk.Label(Infofull,text='SW Interrupts:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=12)
        label2.grid(row=1,column=0)
        label3=tk.Label(Infofull,text='CPU overload:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12)
        label3.grid(row=2,column=0)
        label3=tk.Label(Infofull,text='Memory',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12)
        label3.grid(row=3,column=0,sticky='E',pady=(15,0))
        label4=tk.Label(Infofull,text='Total:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label4.grid(row=4,column=0,sticky='E')
        label5=tk.Label(Infofull,text='Availabel:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label5.grid(row=5,column=0,sticky='E')
        label6=tk.Label(Infofull,text='Used(percent):',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=12,anchor='e')
        label6.grid(row=6,column=0,sticky='E')
        label7=tk.Label(Infofull,text='Disk(Selected)',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label7.grid(row=7,column=0,sticky='E',pady=(15,0))
        label8=tk.Label(Infofull,text='Read Count:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label8.grid(row=8,column=0,sticky='E')
        label9=tk.Label(Infofull,text='└──Time:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label9.grid(row=9,column=0,sticky='E')
        label10=tk.Label(Infofull,text='Write Count' ,font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label10.grid(row=10,column=0,sticky='E')
        label11=tk.Label(Infofull,text='└──Time:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=12,anchor='e')
        label11.grid(row=11,column=0,sticky='E')
        label12=tk.Label(Infofull,text='Used(percent):',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=12,anchor='e')
        label12.grid(row=12,column=0,sticky='E')
        #----------------------inputdatalabel------------------------------------------------------
        
        i_label1=tk.Label(Infofull,text='',font=('Malgun Gothic', 11, 'bold'),bg='#ffffb3',width=18)
        i_label1.grid(row=0,column=1,sticky='W,S,N,E')
        i_label2=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_label2.grid(row=1,column=1)
        i_label3=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_label3.grid(row=2,column=1)
        i_label4=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_label4.grid(row=4,column=1)
        i_label5=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_label5.grid(row=5,column=1)
        i_label6=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_label6.grid(row=6,column=1)
        i_combo=ttk.Combobox(Infofull,state='readonly',font=('Malgun Gothic', 10, 'bold'),width=3)
        i_combo.grid(row=7,column=1,pady=(15,0))
        i_label8=tk.Label(Infofull,text='',font=('Malgun Gothic', 11, 'bold'),bg='white',width=18)
        i_label8.grid(row=8,column=1)
        i_label9=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_label9.grid(row=9,column=1)
        i_label10=tk.Label(Infofull,text='',font=('Malgun Gothic', 11, 'bold'),bg='white',width=18)
        i_label10.grid(row=10,column=1)
        i_label11=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_label11.grid(row=11,column=1)
        i_label12=tk.Label(Infofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_label12.grid(row=12,column=1)
        #------------------------------------Network label----------------------------------------------
        nlabel1=tk.Label(Netinfofull,text='Selected NetWork:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15,anchor='e')
        nlabel1.grid(row=0,column=0,sticky='E')
        nlabel2=tk.Label(Netinfofull,text='Address:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15,anchor='e')
        nlabel2.grid(row=1,column=0,sticky='E')
        nlabel3=tk.Label(Netinfofull,text='Gateway:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15,anchor='e')
        nlabel3.grid(row=2,column=0,sticky='E')
        nlabel4=tk.Label(Netinfofull,text='Subnet Mask:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15,anchor='e')
        nlabel4.grid(row=3,column=0,sticky='E')
        nlabel5=tk.Label(Netinfofull,text='DNS Type:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15,anchor='e')
        nlabel5.grid(row=4,column=0,sticky='E',pady=(15,0))
        nlabel6=tk.Label(Netinfofull,text='            └─Basic:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15,anchor='e')
        nlabel6.grid(row=5,column=0,sticky='W')
        nlabel7=tk.Label(Netinfofull,text='            └─ Sub:',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=15)
        nlabel7.grid(row=6,column=0,sticky='W')
        nlabel8=tk.Label(Netinfofull,text='Sent Gbyte:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=15,anchor='e')
        nlabel8.grid(row=7,column=0,sticky='E',pady=(15,0))
        nlabel9=tk.Label(Netinfofull,text='(Error) └Count:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=15,anchor='e')
        nlabel9.grid(row=8,column=0,sticky='E')
        nlabel10=tk.Label(Netinfofull,text='Recv Gbyte:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=15,anchor='e')
        nlabel10.grid(row=9,column=0,sticky='E')
        nlabel11=tk.Label(Netinfofull,text='(Error) └Count:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=15,anchor='e')
        nlabel11.grid(row=10,column=0,sticky='E')
        nlabel12=tk.Label(Netinfofull,text='Speed:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=15,anchor='e')
        nlabel12.grid(row=11,column=0,sticky='E')
        nlabel13=tk.Label(Netinfofull,text='Mtu:',font=('Malgun Gothic', 13, 'bold'),bg='white',width=15,anchor='e')
        nlabel13.grid(row=12,column=0,sticky='E')
        #--------------------------------------inputNetwork label-----------------------------
        i_ncombo=ttk.Combobox(Netinfofull,state='readonly',font=('Malgun Gothic', 10, 'bold'),width=19)
        i_ncombo.grid(row=0,column=1)
        i_nlabel2=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_nlabel2.grid(row=1,column=1)
        i_nlabel3=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_nlabel3.grid(row=2,column=1)
        i_nlabel4=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_nlabel4.grid(row=3,column=1)
        i_nlabel5=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_nlabel5.grid(row=4,column=1,pady=(15,0))
        i_nlabel6=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_nlabel6.grid(row=5,column=1)
        i_nlabel7=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='#ffffb3',width=18)
        i_nlabel7.grid(row=6,column=1)
        i_nlabel8=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_nlabel8.grid(row=7,column=1,pady=(15,0))
        i_nlabel9=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_nlabel9.grid(row=8,column=1)
        i_nlabel10=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_nlabel10.grid(row=9,column=1)
        i_nlabel11=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_nlabel11.grid(row=10,column=1)
        i_nlabel12=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_nlabel12.grid(row=11,column=1)
        i_nlabel13=tk.Label(Netinfofull,text='',font=('Malgun Gothic', 13, 'bold'),bg='white',width=18)
        i_nlabel13.grid(row=12,column=1)
        

        def setCRdata():
            temp=osdef.CRinfo()
            i_label1.config(text=f'{temp[0]}')
            i_label2.config(text=f'{temp[1]} Case')
            i_label3.config(text=f'{temp[2]} % (For 15m)')
            i_label4.config(text=f'{temp[3]} GB')
            i_label5.config(text=f'{temp[4]} GB')
            i_label6.config(text=f'{temp[5]}GB ({temp[6]}%)')
            i_combo.config(values=osdef.Disklist())
            i_combo.current(0)
        def setdisk(event):
            try:
                num=i_combo.current()
                name=i_combo.get()
                temp=osdef.seldisk(num,name)
                i_label8.config(text=f'{temp[0]} Case')
                i_label9.config(text=f'{temp[1]} ms')
                i_label10.config(text=f'{temp[2]} Case')
                i_label11.config(text=f'{temp[3]} ms')
                i_label12.config(text=f'{temp[4]}GB ({temp[5]}%)')
            except PermissionError:
                i_label8.config(text='Not found disk')
                i_label9.config(text='')
                i_label10.config(text='')
                i_label11.config(text='')
                i_label12.config(text='')
        def selnetwork():
            i_ncombo.config(values=osdef.networklist())
            i_ncombo.current(0)
            networkset(None)
            
        def networkset(event):
            try:
                temp=i_ncombo.get()
                temp=temp.replace('"',"")
                ninfo1=osdef.selnetwork(temp)
                i_nlabel2.config(text=ninfo1[0])
                i_nlabel3.config(text=ninfo1[1])
                i_nlabel4.config(text=ninfo1[2])
                i_nlabel5.config(text=ninfo1[3])
                i_nlabel6.config(text=ninfo1[4])
                i_nlabel7.config(text=ninfo1[5])
                networketc(temp)
            except Exception as e:
                messagebox.showerror("Exception",f"Error Content - {e} -")
        def networketc(temp):
            info2=osdef.networkused(temp)
            i_nlabel8.config(text=f'{info2[0]} GB')
            i_nlabel9.config(text=f'{info2[3]} Case')
            i_nlabel10.config(text=f'{info2[1]} GB')
            i_nlabel11.config(text=f'{info2[2]} Case')
            i_nlabel12.config(text=f'{info2[4]} MB')
            i_nlabel13.config(text=f'{info2[5]} Byte')
        
        def ipsetpop():
            templist=[]
            templist.append(i_ncombo.get().replace('"',""))
            templist.append(i_nlabel2.cget('text'))
            templist.append(i_nlabel3.cget('text'))
            templist.append(i_nlabel4.cget('text'))
            templist.append(i_nlabel5.cget('text'))
            templist.append(i_nlabel6.cget('text'))
            templist.append(i_nlabel7.cget('text'))
            NetworkSet.NetworkSet(templist)
            return templist
            
                
        setCRdata()
        selnetwork()
        setdisk(None)
        
        
        updatebt=tk.Button(btframe,command=setCRdata,text='Update',font=('Malgun Gothic', 11, 'bold'))
        updatebt.pack(ipady=0,pady=(15,10))
        netupdatebt=tk.Button(netbtframe,command=lambda:networkset(None),text='Update',font=('Malgun Gothic', 11, 'bold'))
        netupdatebt.pack(side='left',ipady=0,padx=(80,0))
        netusetbt=tk.Button(netbtframe,command=ipsetpop,text='IP Set',font=('Malgun Gothic', 11, 'bold'))
        netusetbt.pack(side='right',ipady=0,padx=(0,80),ipadx=(5))
        
        i_combo.bind("<<ComboboxSelected>>", setdisk)
        i_ncombo.bind("<<ComboboxSelected>>", networkset)
        
        # print(seldisk)
        # bt=tk.Button(Infofull,text='아아')
        # bt.pack()