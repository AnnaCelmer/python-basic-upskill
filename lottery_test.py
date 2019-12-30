import pytest

from lottery import Lottery

test_data_no_weights = [(2, 2, [{'id': '1', 'first_name': 'Tanny', 'last_name': 'Bransgrove'},
                                {'id': '2', 'first_name': 'Delila', 'last_name': 'Spriggs'},
                                {'id': '3', 'first_name': 'Sigmund', 'last_name': 'Saw'},
                                {'id': '4', 'first_name': 'Wilt', 'last_name': 'Maycey'}]),
                        (3, 2, [{'id': '1', 'first_name': 'Tanny', 'last_name': 'Bransgrove'},
                                {'id': '2', 'first_name': 'Delila', 'last_name': 'Spriggs'}]),
                        (2, 2, [{"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"},
                                {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"},
                                {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0.2"}])
                        ]

test_data_weights = [
    (2, 2, [{"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"},
            {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"},
            {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0.2"}])
]


@pytest.fixture
def lottery():
    lottery = Lottery()
    return lottery


@pytest.mark.parametrize("given_number_of_winners,expected_number_of_winners, participants", test_data_no_weights)
def test_select_winners_no_weights(lottery, given_number_of_winners, expected_number_of_winners, participants):
    winners = lottery.select_winners(participants, given_number_of_winners)
    print(winners)
    assert len(winners) == expected_number_of_winners
    assert winners[0] != winners[1]


@pytest.mark.parametrize("given_number_of_winners,expected_number_of_winners, participants", test_data_weights)
def test_select_winners_weights(lottery, given_number_of_winners, expected_number_of_winners, participants):
    winners = lottery.select_winners(participants, given_number_of_winners)
    print(winners)
    assert len(winners) == expected_number_of_winners
    assert {"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"} in winners
    assert {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"} in winners
    assert {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0.2"} not in winners
