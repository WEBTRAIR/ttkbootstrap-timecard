import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import datetime

import locale

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')



class MainWindow(tb.Frame):
    def __init__(self, window:tb.Window, **kwargs) -> None:
        super().__init__(master=window, padding=24, **kwargs)
        menubar = tb.Frame(master=window)
        menubar.pack()



        body = tb.Frame(master=window, padding=24, width=100)
        body.pack()

        container_left = tb.Frame(master=body, width=50)
        container_left.pack(side=tb.LEFT)

        container_right = tb.Frame(master=body)
        container_right.pack(side=tb.LEFT)

        
        # ------------------------ container left ------------------------
        info_container = tb.LabelFrame(master=container_left, padding=24)
        info_container.pack()

        #date_row = tb.Label()

        self.today = tb.Label(master=info_container, text='0000 年 00 月 00 日 ( 木 )' ,font=('"" 18 bold'))
        self.today.pack(pady=(0,20))

        clock_row = tb.Frame(master=info_container)
        clock_row.pack(pady=(0,40))

        self.clock_hm = tb.Label(master=clock_row, text='00 : 00',font=('', 80, 'normal'), width=5, bootstyle=())
        self.clock_hm.grid(row=1, column=1, sticky=tb.S, padx=0, pady=0)
        #self.clock_hm.pack(side=tb.LEFT)

        self.clock_s = tb.Label(master=clock_row, text='00', font=("", 40 ,'normal'), width=2, bootstyle=())
        self.clock_s.grid(row=1, column=2, sticky=tb.S, padx=0, pady=(0,6))

        self.response =tb.Label(master=info_container, text='システムからのレスポンスメッセージが表示されます。', width=40, font=('', 20, 'normal'), anchor='center', bootstyle=())
        self.response.pack(pady=(40, 40))

        self.user_demartment = tb.Label(master=info_container, text='情報システム部', font=('', 20, 'normal'))
        self.user_demartment.pack(pady=2)

        self.user_name = tb.Label(master=info_container, text='山田 健太郎', bootstyle='', font=('', 40, 'normal'))
        self.user_name.pack(pady=2)






        # ------------------------ container right ------------------------
        stamp_button_container = tb.Frame(master=container_right)
        stamp_button_container.pack()

        class StampButton(tb.Button):
            def __init__(self, **kwargs):
                super().__init__(width=0, padding=64, state=tb.DISABLED, **kwargs)
            
            def pac(self):
                self.pack(side=tb.LEFT, padx=8)
            
            def grid(self, **kwargs):
                super().grid(**kwargs)
        #tb.Style().configure("TButton", font="TkFixedFont 12")
        #tb.Style().configure('TButton', font='Roboto 24')

        tb.Style().configure('TButton', font='"" 32 bold')
        clock_in = StampButton(master=stamp_button_container, text='出 勤', style='success')
        clock_out = StampButton(master=stamp_button_container, text='退 勤', style='danger')
        breaktime_in = StampButton(master=stamp_button_container,text='休 憩 開 始', style='warning')
        breaktime_out = StampButton(master=stamp_button_container,text='休 憩 終 了', style='warning')

   


        #clock_out.pac()

        #stamp_button_container.rowconfigure(1,weight=1)
        #stamp_button_container.columnconfigure(1,weight=1)
        clock_in.grid(row=1, column=1, sticky=tb.NSEW, padx=20, pady=20)

        #stamp_button_container.rowconfigure(1,weight=1)
        #stamp_button_container.columnconfigure(2,weight=1)
        clock_out.grid(row=1, column=2, sticky=tb.NSEW, padx=20, pady=20)


        breaktime_in.grid(row=2, column=1, sticky=tb.NSEW, padx=20, pady=20)
        breaktime_out.grid(row=2, column=2, sticky=tb.NSEW, padx=20, pady=20)

        self.update_clock()
        
    def update_clock(self):
        self.today.config(text=datetime.strftime(datetime.now(),'%Y 年 %m 月 %d 日 ( %a )'))
        self.clock_hm.config(text=datetime.strftime(datetime.now(), '%H : %M'))
        self.clock_s.config(text=datetime.strftime(datetime.now(), '%S'))
        self.clock_s.after(1000, self.update_clock)
    
    


        



if __name__ == '__main__':
    root = tb.Window(title='Time Card System',
                     themename='darkly')
    MainWindow(root)
    root.mainloop()
