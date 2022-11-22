"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFielPanel
from wagtail.models import Page
from wagtail.fields import StreamField

class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex_page.html"
    
    content = StreamField()

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages" 