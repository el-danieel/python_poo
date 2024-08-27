class Carro:
    modelo : str
    marca : str
    cor : str
    __tanque = 0.0
    __motor_on : False
    kms = 0.0

    def __init__(self, modelo : str, marca : str, cor : str, tanque: float, kms : float, motor : bool):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.tanque = tanque
        self.kms = kms
        self.motor_on = motor

    def ligar(self):
        if not self.motor_on and self.tanque > 0:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on and self.tanque > 0:
            km = velocidade * tempo
            litros = km / self.consumo_medio

            if self.tanque >= litros:
                self.odometro += km
                self.tanque -= litros
            else:
                km = self.tanque * self.consumo_medio
                self.odometro += km
                self.tanque = 0
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def get_odometro(self):
        return self.__odometro

    def get_tanque(self):
        return self.__tanque

    def __repr__(self):
        return f"Carro(modelo={self.modelo}, marca={self.marca}, cor={self.cor}, odometro={self.__odometro}, motor_on={self.motor_on}"
    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}, '
                f'tanque {self.tanque}, '
                f'consumo_medio {self.consumo_medio}')

        return info