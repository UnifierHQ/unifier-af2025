"""
Unifier AF2025 - a filter for April Fools
Copyright (C) 2025  UnifierHQ

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from random import randint
from datetime import datetime
from utils.base_filter import FilterResult, BaseFilter

class Filter(BaseFilter):
    def __init__(self):
        super().__init__(
            'bobolx',
            'bobolx chat',
            'the 10000% best unifier filter in the world (source: trust me bro)'
        )

    def check(self, message, data) -> FilterResult:
        # Each word has a 5% chance of being tagged

        words = []
        for word in message['content'].split(' '):
            num = randint(1,20)
            if num == 1 and any(c.isalpha() for c in word):
                words.append('\\'+('#'*len(word))) # add backslash here to escape formatting
            else:
                words.append(word)

        message = ' '.join(words)

        # The entire message has a 2% chance of being censored
        ban_message = (
            '## Banned for 3 days\n' +
            '-# (not really)\n'+
            'Our content monitors have determined that your behaviour at Unifier has been in violation of our terms of service.\n'+
            'Received: ' + datetime.now().strftime("%m/%d/%Y %I:%M:%S %p") + '\n' +
            'Moderator note: merry april fools'
        )
        
        return FilterResult(
            False, None, message=ban_message, should_log=True, safe_content=message if randint(1,50) > 1 else None
        )
