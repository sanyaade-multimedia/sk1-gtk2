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

class DocumentInspector:

	def __init__(self, app):
		self.app = app

	def is_doc(self):
		if self.app.docs:
			return True
		else:
			return False

	def is_not_doc(self):
		if self.app.docs:
			return False
		else:
			return True