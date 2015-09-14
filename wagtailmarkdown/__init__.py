# vim:sw=4 ts=4 et:
# Copyright (c) 2015 Torchbox Ltd.
# felicity@torchbox.com 2015-09-14
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

from django.db.models import TextField
from wagtail.wagtailcore.blocks import TextBlock
import wagtailmarkdown.utils

class MarkdownBlock(TextBlock):
    def render_basic(self, value):
        return wagtailmarkdown.utils.render(value)