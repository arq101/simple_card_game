#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import random

from cards import CardDeck

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s -- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',)
logger = logging.getLogger(__name__)

_matching_options = {
    1: 'face value',
    2: 'suit',
    3: 'face value and suit'
}


def _deal_decks():
    """Gets instances of 2 decks of cards and returns the shuffled decks"""
    comp_1 = CardDeck()
    comp_2 = CardDeck()

    logging.info('Shuffling cards')
    comp_1_card_deck = list(comp_1.deck_of_cards)
    random.shuffle(comp_1_card_deck)
    comp_2_card_deck = list(comp_2.deck_of_cards)
    random.shuffle(comp_2_card_deck)
    logging.info('Done shuffling')

    return comp_1_card_deck, comp_2_card_deck


def _play_match(deck_1, deck_2, condition):
    """Match is played by taking a card from each deck. If a match is found
    depending matching conditions, then a player is chosen randomly as having shouted out 'Match'
    and takes the ownership of cards played in that run."""
    players = ['player_1', 'player_2']
    player_1_total_won = 0
    player_2_total_won = 0

    logging.info('Playing cards ...')
    cards_dealt = 0
    while deck_1:
        player_1_deck = deck_1.pop()
        player_2_deck = deck_2.pop()
        cards_dealt += 2

        if _matching_options[int(condition)] == 'face value':
            if player_1_deck[0] == player_2_deck[0]:
                match_found_by = random.choice(players)
                logging.info('Match found by {}'.format(match_found_by))
                if match_found_by == 'player_1':
                    player_1_total_won += cards_dealt
                else:
                    player_2_total_won += cards_dealt

                # reset cards dealt so far back to zero
                cards_dealt = 0
        elif _matching_options[int(condition)] == 'suit':
            if player_1_deck[1] == player_2_deck[1]:
                match_found_by = random.choice(players)
                logging.info('Match found by {}'.format(match_found_by))
                if match_found_by == 'player_1':
                    player_1_total_won += cards_dealt
                else:
                    player_2_total_won += cards_dealt
                cards_dealt = 0
        elif _matching_options[int(condition)] == 'face value and suit':
            if player_1_deck[0] == player_2_deck[0] and player_1_deck[1] == player_2_deck[1]:
                match_found_by = random.choice(players)
                logging.info('Match found by {}'.format(match_found_by))
                if match_found_by == 'player_1':
                    player_1_total_won += cards_dealt
                else:
                    player_2_total_won += cards_dealt
                cards_dealt = 0

    return player_1_total_won, player_2_total_won


def _declare_winner(player_1, player_2):
    if player_1 > player_2:
        logging.info(
            'Winner is Player 1. Player 1 accumulated {0} cards and Player 2 had {1} cards.'.format(
                player_1, player_2))
    elif player_1 < player_2:
        logging.info(
            'Winner is Player 2. Player 2 accumulated {0} cards and Player 1 had {1} cards.'.format(
                player_2, player_1))
    elif player_1 == player_2:
        logging.info('Drawn game. Both players accumulated {} cards'.format(player_1))


def main():
    logging.info('Starting card "match" game')
    print("Please enter number of packs to use (1 to 4, or e to exit): ", end="")
    num_of_packs = input()

    if num_of_packs in {'1', '2', '3', '4'}:
        print("Please select matching conditions: \n",
              "1 - face value \n",
              "2 - suit \n",
              "3 - face value and suit \n",
              "e - exit game",
              )
        matching_condition = input('> ')
        if matching_condition in {'1', '2', '3'}:
            logging.info('Matching on {}'.format(_matching_options[int(matching_condition)]))
        elif matching_condition == 'e':
            logging.info('Selected to exit game.')
            sys.exit(0)
        else:
            logging.info('Invalid option selected for matching condition, exiting!')
            sys.exit(0)

        player_1_grand_total = 0
        player_2_grand_total = 0
        i = 0
        while i < int(num_of_packs):
            deck_1, deck_2 = _deal_decks()
            player_1_totals, player_2_totals = _play_match(deck_1, deck_2, matching_condition)
            player_1_grand_total += player_1_totals
            player_2_grand_total += player_2_totals
            i += 1
    elif num_of_packs == 'e':
        logging.info('Selected to exit game.')
        sys.exit(0)
    else:
        logging.info('Invalid choice selected, existing!')
        sys.exit(0)

    _declare_winner(player_1_grand_total, player_2_grand_total)


if __name__ == '__main__':
    main()
