import abc


class IDesconto:
    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


class DescontoVIP(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2


class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3


class Pedido:
    def __init__(self, desconto: IDesconto) -> None:
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)


if __name__ == "__main__":
    pedido_normal = Pedido(DescontoNormal())
    print(pedido_normal.total(100))
    pedido_vip = Pedido(DescontoVIP())
    print(pedido_vip.total(100))
    pedido_premium = Pedido(DescontoPremium())
    print(pedido_premium.total(100))
