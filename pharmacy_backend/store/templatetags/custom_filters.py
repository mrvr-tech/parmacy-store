from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_days(date, num_days):
    """Add days to a date"""
    return date + timedelta(days=num_days)
