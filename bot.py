from botcity.core import DesktopBot
import pandas


class Bot(DesktopBot):
    def action(self, execution=None):
        self.headless = True
        self.browse(r'https://empire.goodgamestudios.com/')
        
    def preencher_dados(self):
        if not self.find( "login", matching=0.97, waiting_time=100000):
            self.not_found("login")
        self.click()

        if not self.find( "nome", matching=0.97, waiting_time=100000):
            self.not_found("nome")
        self.click()
        self.paste('<nome>')

        if not self.find( "senha", matching=0.97, waiting_time=100000):
            self.not_found("senha")
        self.click()
        self.paste('<senha>')

        if not self.find( "logar", matching=0.97, waiting_time=10000):
            self.not_found("logar")
        self.click()

    def close_popups(self):
        c = 0
        while True:
            if c == 0:
                if self.find( "x", matching=0.97, waiting_time=10000) or self.find( "tipe3", matching=0.97, waiting_time=10000) or self.find( "close_offer", matching=0.97, waiting_time=10000) or self.find( "mais um x", matching=0.97, waiting_time=10000):
                    self.click()
                if not self.find( "x", matching=0.97, waiting_time=10000) and not self.find( "tipe3", matching=0.97, waiting_time=10000) and not self.find( "close_offer", matching=0.97, waiting_time=10000) and not  self.find( "mais um x", matching=0.97, waiting_time=10000):
                    break
            if c != 0:
                if self.find( "x", matching=0.97, waiting_time=1000) or self.find( "tipe3", matching=0.97, waiting_time=1000) or self.find( "close_offer", matching=0.97, waiting_time=1000) or self.find( "mais um x", matching=0.97, waiting_time=1000):
                    self.click()
                if not self.find( "x", matching=0.97, waiting_time=1000) and not self.find( "tipe3", matching=0.97, waiting_time=1000) and not self.find( "close_offer", matching=0.97, waiting_time=1000) and not  self.find( "mais um x", matching=0.97, waiting_time=1000):
                    break
            c = 1

    def not_found(self, label):
        print(f"Element not found: {label}")

    def world_map(self):
        if not self.find( "wm", matching=0.97, waiting_time=10000):
            self.not_found("wm")
        self.click()
        
    def castle(self):
        if self.find( "castle", matching=0.97, waiting_time=10000):
            self.click()
            self.click()

    def ataca_fortaleza(self, x, y):
        global atk
        if self.find( "olhar", matching=0.97, waiting_time=10000):
            self.click_relative(-88, 3)
            self.control_a()
            self.backspace()
            self.paste(x)
        if self.find( "oliar", matching=0.97, waiting_time=10000):
            self.click_relative(-39, -3)
            self.control_a()
            self.backspace()
            self.paste(y)
            self.enter()

        if not self.find( "bussola", matching=0.97, waiting_time=3000):
            if self.find( "olhador", matching=0.97, waiting_time=10000):
                self.move_relative(23, 491)
                self.click_relative(22, 491)
                self.click_relative(22, 491)

        if self.find( "acha essa porra", matching=0.97, waiting_time=3000):
            self.click()
            if self.find( "v", matching=0.97, waiting_time=13000):
                self.click()
                if self.find( "predef", matching=0.97, waiting_time=10000):
                    self.click()
                    if self.find( "umaonda", matching=0.97, waiting_time=13000):
                        self.click()
                        if self.find( "atacar", matching=0.97, waiting_time=13000):
                            self.click()
                            if self.find( "cavalo", matching=0.97, waiting_time=10000):
                                self.click_relative(35, 148)
                                if self.find( "all", matching=0.97, waiting_time=10000):
                                    self.click_relative(108, 141)
                                    atk += 1
                                    print(atk)


if __name__ == '__main__':
    castle = Bot()
    mapa = pandas.read_excel(r'C:\Users\User\Desktop\coordenadas_gelo - Copia.xlsx')
    atk = 0
    for c in range(0, len(mapa)):
        castle.ataca_fortaleza(int(mapa['X'][c]), int(mapa['Y'][c]))
        castle.ataca_fortaleza(int(mapa['X1'][c]), int(mapa['Y1'][c]))
        if atk >= 30:
            print('Terminado!')
            break
