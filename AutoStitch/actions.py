#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def install():
    shelltools.system("chmod 0755 -Rv "+get.workDIR()+"/*")
    pisitools.insinto("/opt/AutoStitch/","*")
    pisitools.dodoc("*.TXT")