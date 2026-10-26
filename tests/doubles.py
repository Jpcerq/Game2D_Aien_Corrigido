from src.desconto import IDesconto


class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0


class StubShip:
    def __init__(self):
        self.moving_right = False
        self.moving_left = False


class StubBulletManager:
    def __init__(self):
        self.disparos = 0

    def _fire_bullet(self):
        self.disparos += 1
