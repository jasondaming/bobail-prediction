import pytest
from bobail.game import Game

@pytest.fixture
def game():
	return Game()