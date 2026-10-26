import pygame

from src.game_events import GameEventHandler
from tests.doubles import StubBulletManager, StubShip


def test_eventos_do_jogo_com_stub():
    ship = StubShip()
    bullets = StubBulletManager()
    handler = GameEventHandler(ship, bullets)
    handler._handle_keydown(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
    assert ship.moving_right is True
    handler._handle_keyup(pygame.event.Event(pygame.KEYUP, key=pygame.K_RIGHT))
    assert ship.moving_right is False
    handler._handle_keydown(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
    assert bullets.disparos == 1


def test_disparo_do_jogo_com_mock(mocker):
    bullets = mocker.Mock()
    handler = GameEventHandler(StubShip(), bullets)
    handler._handle_keydown(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
    bullets._fire_bullet.assert_called_once_with()
