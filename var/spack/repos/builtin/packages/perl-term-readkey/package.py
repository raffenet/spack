##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PerlTermReadkey(PerlPackage):
    """Term::ReadKey is a compiled perl module dedicated to providing simple
    control over terminal driver modes (cbreak, raw, cooked, etc.,) support
    for non-blocking reads, if the architecture allows, and some generalized
    handy functions for working with terminals. One of the main goals is to
    have the functions as portable as possible, so you can just plug in
    "use Term::ReadKey" on any architecture and have a good likelihood of it
    working."""

    homepage = "http://search.cpan.org/perldoc/Term::ReadKey"
    url = "http://www.cpan.org/authors/id/J/JS/JSTOWE/TermReadKey-2.37.tar.gz"

    version('2.37', 'e8ea15c16333ac4f8d146d702e83cc0c')
