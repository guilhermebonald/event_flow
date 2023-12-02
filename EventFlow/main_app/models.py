from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class User(models.Model):
    name = models.CharField(max_length=20)
