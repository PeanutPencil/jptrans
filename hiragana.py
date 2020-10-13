""" Module to translate from Romanji to Hiragana
This module is responsible solely for translating words from Romanji
to Hiragana.  Its called only by the deck module and only within its 
add and edit functions.  It is modeled after the katakana module.
Important work that needs to be done:
Catch errors from bad romanji (eg. Computer, Love, etc)
"""
import logging

_vowel = ('A', 'I', 'U', 'E', 'O')
_hiraganaDict = {   'A':  'あ', 'I':  'い', 'U':  'う', 'E':  'え', 'O':  'お',
                    'KA': 'か', 'KI': 'き', 'KU': 'く', 'KE': 'け', 'KO': 'こ',
                    'GA': 'が', 'GI': 'ぎ', 'GU': 'ぐ', 'GE': 'げ', 'GO': 'ご',
                    'SA': 'さ', 'SHI':'し', 'SU': 'す', 'SE': 'せ', 'SO': 'そ',
                    'ZA': 'ざ', 'JI': 'じ', 'ZU': 'ず', 'ZE': 'ぜ', 'ZO': 'ぞ',
                    'TA': 'た', 'CHI':'ち', 'TSU':'つ', 'TE': 'て', 'TO': 'と',
                    'DA': 'だ', 'DI': 'ぢ', 'DU': 'づ', 'DE': 'で', 'DO': 'ど',
                    'NA': 'な', 'NI': 'に', 'NU': 'ぬ', 'NE': 'ね', 'NO': 'の',
                    'HA': 'は', 'HI': 'ひ', 'FU': 'ふ', 'HE': 'へ', 'HO': 'ほ',
                    'BA': 'ば', 'BI': 'び', 'BU': 'ぶ', 'BE': 'べ', 'BO': 'ぼ',
                    'PA': 'ぱ', 'PI': 'ぴ', 'PU': 'ぷ', 'PE': 'ぺ', 'PO': 'ぽ',
                    'MA': 'ま', 'MI': 'み', 'MU': 'む', 'ME': 'め', 'MO': 'も',
                    'YA': 'や',			    'YU': 'ゆ', 		   'YO': 'よ',
                    'RA': 'ら', 'RI': 'り', 'RU': 'る', 'RE': 'れ', 'RO': 'ろ',
                    'WA': 'わ', 					  			   'WO': 'を',
                    'stsu': 'っ',                                  'N':  'ん',
                    'KYA': 'きゃ', 'KYU': 'きゅ', 'KYO': 'きょ', 
                    'SHA': 'しゃ', 'SHU': 'しゅ', 'SHO': 'しょ', 
                    'CHA': 'ちゃ', 'CHU': 'ちゅ', 'CHO': 'ちょ', 
                    'NYA': 'にゃ', 'NYU': 'にゅ', 'NYO': 'にょ', 
                    'HYA': 'ひゃ', 'HYU': 'ひゅ', 'HYO': 'ひょ', 
                    'MYA': 'みゃ', 'MYU': 'みゅ', 'MYO': 'みょ', 
                    'RYA': 'りゃ', 'RYU': 'りゅ', 'RYO': 'りょ', 
                    'GYA': 'ぎゃ', 'GYU': 'ぎゅ', 'GYO': 'ぎょ', 
                    'JA':  'じゃ', 'JU':  'じゅ', 'JO':  'じょ', 
                    'BYA': 'びゃ', 'BYU': 'びゅ', 'BYO': 'びょ', 
                    'PYA': 'ぴゃ', 'PYU': 'ぴゅ', 'PYO': 'ぴょ', 
                    '.':   '。',   '!':   '!',   '?':   '?', 
				}