from tkinter import *
from tkinter import ttk, scrolledtext


class Main:
    def __init__(self, master):
        class IORedirector(object):
            def __init__(self, text_area):
                self.text_area = text_area

        class StdoutRedirectior(IORedirector):
            def write(self, message):
                self.text_area.config(state='normal')
                self.text_area.insert('insert', message)
                self.text_area.config(state='disabled')

            def flush(self):
                pass

        self.tab = ttk.Notebook(master)
        self.tab_main = Frame(self.tab)
        self.tab_slave = Frame(self.tab)
        self.tab.add(self.tab_main, text='Основа')
        self.tab.add(self.tab_slave, text='Настройки')
        self.tab.grid(row=0, sticky='w')
        # элементы первой вкладки
        self.btn_start = Button(self.tab_main, text='Старт', command=self.start).grid(column=0, row=2, sticky='w',
                                                                                      ipadx=5, ipady=5, padx=2,
                                                                                      pady=10)
        self.btn_exit = Button(self.tab_main, text='Выход', command=self.destroy).grid(column=0, row=2, sticky='e',
                                                                                       ipadx=5, ipady=5, padx=0,
                                                                                       pady=10)
        self.console = scrolledtext.ScrolledText(self.tab_main, width=48, height=9)
        self.console.grid(column=0, row=1, sticky='nw')

        self.info_label = Button(self.tab_main, text='Инструкция тут', bg='yellow').grid(column=0, row=2)
        # элементы второй вкладки
        Label(self.tab_slave, text='Настройки арены:').grid(column=0, row=0, sticky='w')
        Label(self.tab_slave, text='Настройки игрока:').grid(column=0, row=4, sticky='w')
        Label(self.tab_slave, text='Сила отряда').grid(column=0, row=6, sticky='w')
        Label(self.tab_slave, text='Множитель силы (0.0 - 1.0)').grid(column=0, row=7, sticky='w')
        self.radio_tac_state = IntVar()
        self.radio_tac_state.set(1)
        self.radio_arena_type_state = IntVar()
        self.radio_arena_type_state.set(1)
        self.radio_arena_resource_state = IntVar()
        self.radio_arena_resource_state.set(1)
        Radiobutton(self.tab_slave, text='Тактика авторская', variable=self.radio_tac_state,
                    value=1).grid(column=0, row=1, sticky='w')
        Radiobutton(self.tab_slave, text='Тактика альтернативная', variable=self.radio_tac_state,
                    value=2).grid(column=1, row=1, sticky='w')
        Radiobutton(self.tab_slave, text='Арена 10', variable=self.radio_arena_type_state, value=1).grid(column=0,
                                                                                                         row=2,
                                                                                                         sticky='w')
        Radiobutton(self.tab_slave, text='Арена 15', variable=self.radio_arena_type_state, value=2).grid(column=1,
                                                                                                         row=2,
                                                                                                         sticky='w')
        Radiobutton(self.tab_slave, text='Билеты', variable=self.radio_arena_resource_state, value=1).grid(column=0,
                                                                                                           row=3,
                                                                                                           sticky='w')
        Radiobutton(self.tab_slave, text='Яблоки', variable=self.radio_arena_resource_state, value=2).grid(column=1,
                                                                                                           row=3,
                                                                                                           sticky='w')
        # Checkbutton(self.tab_slave, text='Запись результатов арены', variable=self.chc_box_log_state,
        #             offvalue=0, onvalue=1).grid(column=0, row=5, sticky='w')
        self.entry_power_player = Entry(self.tab_slave)
        self.entry_power_player.grid(column=1, row=6, sticky='w')
        self.entry_power_player_factor = Entry(self.tab_slave)
        self.entry_power_player_factor.grid(column=1, row=7, sticky='w')
        self.btn_save = Button(self.tab_slave, text='Сохранить', command=self.write_data_of_player).grid(column=2,
                                                                                                         row=8,
                                                                                                         sticky='e')
        sys.stdout = StdoutRedirectior(self.console)
        self.console.update()
        self.update_text()
        """С помощью методов select() и deselect() флажков можно их программно включать и выключать. То же самое 
        относится к радиокнопкам. """

    def update_text(self):
        self.console.config()

    def destroy(self):
        with open('logs.txt', 'w', encoding='utf-8') as file:
            pass
        root.destroy()

    def read_data_of_player(self):
        try:
            with open('power_of_player.txt', 'r', encoding='utf-8') as file:
                line = file.read().splitlines()
                self.entry_power_player.insert(END, line[0])
                self.entry_power_player_factor.insert(END, line[1])
        except IndexError:
            pass

    def write_data_of_player(self):
        with open('power_of_player.txt', 'w', encoding='utf-8') as file:
            file.writelines(self.entry_power_player.get() + '\n' + self.entry_power_player_factor.get())

    def start(self):
        pass


root = Tk()
root.iconbitmap(r'icon.ico')
ab_hc = Main(root)
ab_hc.read_data_of_player()
root.title('ArenaBot_HC')
root.geometry('408x220+0+714')
root.resizable(False, False)
root.mainloop()
