from unittest import mock

import pytest

from lottery import Lottery
from participants import Participants
from prizes import Prizes

test_list_of_participants_no_weights = [{'id': '1', 'first_name': 'Tanny', 'last_name': 'Bransgrove'},
                                        {'id': '2', 'first_name': 'Delila', 'last_name': 'Spriggs'},
                                        {'id': '3', 'first_name': 'Sigmund', 'last_name': 'Saw'},
                                        {'id': '4', 'first_name': 'Wilt', 'last_name': 'Maycey'},
                                        {'id': '5', 'first_name': 'Carilyn', 'last_name': 'Semper'}]

test_list_of_participants_weights = [{"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"},
                                     {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"},
                                     {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0"}]

test_item_giveaway_template_prizes = [{"id": 1, "name": "Annual Vim subscription", "amount": 5}]

test_separate_prizes_template_prizes = [
    {"id": 1, "name": "Gold medal", "amount": 1},
    {"id": 2, "name": "Silver medal", "amount": 1},
    {"id": 3, "name": "Bronze medal", "amount": 1}]


def mock_participant(test_list_of_participant):
    participants = mock.Mock(spec=Participants)
    participants.list_of_participants = test_list_of_participant
    return participants


@pytest.fixture
def mock_separate_prizes():
    prizes = mock.Mock(spec=Prizes("separate_prizes"))
    prizes.list_of_prizes = test_separate_prizes_template_prizes
    return prizes


@pytest.mark.parametrize(
    "given_number_of_winners, expected_number_of_winners",
    [(5, 5), (7, 5)])
def test_select_winners_without_weights(mock_separate_prizes, given_number_of_winners, expected_number_of_winners):
    participants = mock_participant(test_list_of_participants_no_weights)
    lottery = Lottery(mock_separate_prizes, participants)
    winners = lottery.select_winners(given_number_of_winners)
    assert len(winners) == expected_number_of_winners


def test_select_winners_with_weights(mock_separate_prizes):
    participants = mock_participant(test_list_of_participants_weights)
    lottery = Lottery(mock_separate_prizes, participants)
    winners = lottery.select_winners(2)
    assert len(winners) == 2
    assert {"id": "1", "first_name": "Tanny", "last_name": "Bransgrove", "weight": "1"} in winners
    assert {"id": "2", "first_name": "Delila", "last_name": "Spriggs", "weight": "1"} in winners
    assert {"id": "3", "first_name": "Sigmund", "last_name": "Saw", "weight": "0"} not in winners
