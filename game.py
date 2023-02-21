from PyQt6.QtWidgets import QPushButton
class Gamecheck:
    def __init__(self,btn_ls:list ,first="X", second ="O") -> None:
        self.first_pl = first
        self.second_pl = second
        self.btn_lst = btn_ls
    def __check_win(self, btn_1:QPushButton,btn_2:QPushButton,btn_3:QPushButton):
        if (btn_1.text()+btn_2.text()+btn_3.text()).upper() == "XXX":
            return self.first_pl
        elif (btn_1.text()+btn_2.text()+btn_3.text()).upper() == "OOO":
            return self.second_pl
        else:
            return None
    def check_winner(self):
        ans = self.__check_win(self.btn_lst[0],self.btn_lst[1],self.btn_lst[2])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[3],self.btn_lst[4],self.btn_lst[5])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[6],self.btn_lst[7],self.btn_lst[8])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[0],self.btn_lst[3],self.btn_lst[6])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[1],self.btn_lst[4],self.btn_lst[7])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[2],self.btn_lst[5],self.btn_lst[8])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[0],self.btn_lst[4],self.btn_lst[8])
        if ans != None:
            return ans
        ans = self.__check_win(self.btn_lst[2],self.btn_lst[4],self.btn_lst[6])
        if ans != None:
            return ans
        


