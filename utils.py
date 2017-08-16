#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import logging

from telegram.ext.dispatcher import run_async

from internationalization import _, __

logger = logging.getLogger(__name__)

TIMEOUT = 2.5


def list_subtract(list1, list2):
    """ Helper function to subtract two lists and return the sorted result """
    list1 = list1.copy()

    for x in list2:
        list1.remove(x)

    return list(sorted(list1))


def display_name(user):
    """ Get the current players name including their username, if possible """
    user_name = user.first_name
    if user.username:
        user_name += ' (@' + user.username + ')'
    return user_name


def display_color(color):
    """ Convert a color code to actual color name """
    if color == "r":
        return _("{emoji} Red").format(emoji='❤️')
    if color == "b":
        return _("{emoji} Blue").format(emoji='💙')
    if color == "g":
        return _("{emoji} Green").format(emoji='💚')
    if color == "y":
        return _("{emoji} Yellow").format(emoji='💛')


def display_color_group(color, game):
    """ Convert a color code to actual color name """
    if color == "r":
        return __("{emoji} Red", game.translate).format(
            emoji='❤️')
    if color == "b":
        return __("{emoji} Blue", game.translate).format(
            emoji='💙')
    if color == "g":
        return __("{emoji} Green", game.translate).format(
            emoji='💚')
    if color == "y":
        return __("{emoji} Yellow", game.translate).format(
            emoji='💛')


def error(bot, update, error):
    """Simple error handler"""
    logger.exception(error)


@run_async
def send_async(bot, *args, **kwargs):
    """Send a message asynchronously"""
    if 'timeout' not in kwargs:
        kwargs['timeout'] = TIMEOUT

    try:
        bot.sendMessage(*args, **kwargs)
    except Exception as e:
        error(None, None, e)


@run_async
def answer_async(bot, *args, **kwargs):
    """Answer an inline query asynchronously"""
    if 'timeout' not in kwargs:
        kwargs['timeout'] = TIMEOUT

    try:
        bot.answerInlineQuery(*args, **kwargs)
    except Exception as e:
        error(None, None, e)
