# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011-2012 by Igor E. Novikov
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

"""
The package provides Qt-like signal-slot functionality
for internal events processing.

Signal arguments:
CONFIG_MODIFIED   attr, value - modified config field
APP_STATUS		  msg    - statusbar message
CMS_CHANGED		  no args 
NO_DOCS		      no args
DOC_MODIFIED	  doc - presenter instance
DOC_CHANGED	      doc - actual presenter instance
DOC_SAVED		  doc - saved presenter instance
DOC_CLOSED		  doc - closed presenter instance
MODE_CHANGED	  mode - canvas MODE value
SELECTION_CHANGED doc - presenter instance
CLIPBOARD		  no args 
PAGE_CHANGED      doc - presenter instance
"""

#Signal channels

CONFIG_MODIFIED = ['CONFIG_MODIFIED']

APP_STATUS = ['APP_STATUS']
CMS_CHANGED = ['CMS_CHANGED']

NO_DOCS = ['NO_DOCS']
DOC_MODIFIED = ['DOC_MODIFIED']
DOC_CHANGED = ['DOC_CHANGED']
DOC_SAVED = ['DOC_SAVED']
DOC_CLOSED = ['DOC_CLOSED']

MODE_CHANGED = ['MODE_CHANGED']
SELECTION_CHANGED = ['SELECTION_CHANGED']
CLIPBOARD = ['CLIPBOARD']
PAGE_CHANGED = ['PAGE_CHANGED']



def connect(channel, receiver):
	"""
	Connects signal receive method
	to provided channel. 
	"""
	if callable(receiver):
		try:
			channel.append(receiver)
		except:
			msg = "Cannot connect to channel:"
			print msg, channel, "receiver:", receiver

def disconnect(channel, receiver):
	"""
	Disconnects signal receive method
	from provided channel. 
	"""
	if callable(receiver):
		try:
			channel.remove(receiver)
		except:
			msg = "Cannot disconnect from channel:"
			print msg, channel, "receiver:", receiver

def emit(channel, *args):
	"""
	Sends signal to all receivers in channel.
	"""
#	print 'signal', channel[0]
	try:
		for receiver in channel[1:]:
			try:
				if callable(receiver):
					receiver(*args)
			except:
				pass
	except:
		print "Cannot send signal to channel:", channel





