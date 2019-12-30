import numpy as np
import pytest

from lottery import Lottery

tests_participants = [{'id': '1', 'first_name': 'Tanny', 'last_name': 'Bransgrove'},
                      {'id': '2', 'first_name': 'Delila', 'last_name': 'Spriggs'},
                      {'id': '3', 'first_name': 'Sigmund', 'last_name': 'Saw'},
                      {'id': '4', 'first_name': 'Wilt', 'last_name': 'Maycey'},
                      {'id': '5', 'first_name': 'Carilyn', 'last_name': 'Semper'}
                      ]

test_data_no_weights = [(2, 2, tests_participants),
                        (3, 2, [{'id': '1', 'first_name': 'Tanny', 'last_name': 'Bransgrove'},
                                {'id': '2', 'first_name': 'Delila', 'last_name': 'Spriggs'}]),
                        (2, 2, [{"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"},
                                {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"},
                                {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0.2"}])
                        ]

test_data_weights = [
    (2, 2, [{"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"},
            {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"},
            {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0"}])
]

test_data_award_prizes = [
    ("results_test.json", 5, [{'id': 1, 'name': 'Annual Vim subscription', 'amount': 5}], tests_participants),
    ("results_medals_test.json", 3, [{"id": 1, "name": "Gold medal", "amount": 1},
                                     {"id": 2, "name": "Silver medal", "amount": 1},
                                     {"id": 3, "name": "Bronze medal", "amount": 1}], tests_participants)]


@pytest.fixture(scope="function")
def lottery():
    return Lottery()


@pytest.mark.parametrize("given_number_of_winners,expected_number_of_winners, participants", test_data_no_weights)
def test_select_winners_no_weights(lottery, given_number_of_winners, expected_number_of_winners, participants):
    winners = lottery.select_winners(participants, given_number_of_winners)
    assert len(winners) == expected_number_of_winners
    assert winners[0] != winners[1]


@pytest.mark.parametrize("given_number_of_winners,expected_number_of_winners, participants", test_data_weights)
def test_select_winners_weights(lottery, given_number_of_winners, expected_number_of_winners, participants):
    winners = lottery.select_winners(participants, given_number_of_winners)
    assert len(winners) == expected_number_of_winners
    assert {"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"} in winners
    assert {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"} in winners
    assert {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0"} not in winners


@pytest.mark.parametrize("output_file, expected_number_of_winners, prizes, participants", test_data_award_prizes)
def test_award_prizes(output_file, expected_number_of_winners, prizes, participants):
    lottery = Lottery()
    print(f'participants: {participants}')
    awarded_prizes = lottery.award_prizes(prizes, participants, output_file)
    given_number_of_winners = np.array([i["winners"] for i in awarded_prizes])
    assert given_number_of_winners.size == expected_number_of_winners
