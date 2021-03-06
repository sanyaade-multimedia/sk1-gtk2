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

import gtk

LEFT_BUTTON = 1
MIDDLE_BUTTON = 2
RIGHT_BUTTON = 3

SCROLL_UP = gtk.gdk.SCROLL_UP
SCROLL_DOWN = gtk.gdk.SCROLL_DOWN
SCROLL_LEFT = gtk.gdk.SCROLL_LEFT
SCROLL_RIGHT = gtk.gdk.SCROLL_RIGHT

KEY_KP_ENTER = 65421
KEY_RETURN = 65293

RENDERING_DELAY = 50
DEFAULT_CURSOR = -1

TXT_SMALL = 'small'
TXT_SMALLER = 'smaller'
TXT_MEDIUM = 'medium'
TXT_LARGE = 'large'
TXT_LARGER = 'larger'

PROP_RELIEF = 'relief'
PROP_CAN_FOCUS = 'can-focus'
PROP_EDITABLE = 'editable'
PROP_HAS_TOOLTIP = 'has-tooltip'
PROP_SCROLLABLE = 'scrollable'

EVENT_DELETE = 'delete-event'
EVENT_ACTIVATE = 'activate'
EVENT_EXPOSE = 'expose_event'
EVENT_BUTTON_PRESS = 'button-press-event'
EVENT_BUTTON_RELEASE = 'button-release-event'
EVENT_MOUSE_MOTION = 'motion_notify_event'
EVENT_MOUSE_SCROLL = 'scroll-event'
EVENT_CLICKED = 'clicked'
EVENT_TOGGLED = 'toggled'
EVENT_CHANGED = 'changed'
EVENT_VALUE_CHANGED = 'value-changed'
EVENT_COLOR_SET = 'color-set'
EVENT_KEY_PRESS = 'key_press_event'
EVENT_FOCUS_OUT = 'focus-out-event'
EVENT_ENTER_NOTIFY = 'enter-notify-event'
EVENT_LEAVE_NOTIFY = 'leave-notify-event'
EVENT_QUERY_TOOLTIP = 'query-tooltip'
EVENT_SWITCH_PAGE = 'switch-page'
