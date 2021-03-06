# -*- coding: utf-8 -*-
#
#	Copyright (C) 2014 by Igor E. Novikov
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import wal

from sk1 import _, rc


class KeepRatioLabel(wal.ClickableImage):

	value = True

	def __init__(self, master):
		wal.ClickableImage.__init__(self, master, rc.IMG_KEEP_RATIO,
						tooltip=_('Keep aspect ratio'), cmd=self.process_click)

	def process_click(self, *args):
		self.value = not self.value
		if self.value:
			self.set_image(rc.IMG_KEEP_RATIO)
			self.set_tooltip(_('Don\'t keep aspect ratio'))
		else:
			self.set_image(rc.IMG_DONT_KEEP_RATIO)
			self.set_tooltip(_('Keep aspect ratio'))
