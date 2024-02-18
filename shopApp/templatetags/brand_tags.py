from django import template
from shopApp.models import Brand

register = template.Library()

@register.filter
def category_filter(qs, cid):
    return qs.filter(category_id=cid)

@register.filter
def get_chiled_cats(obj):
    return Brand.objects.filter(parent = obj)

@register.filter
@register.inclusion_tag('shop/tags/draw_brands.html')
def draw_brands(sub_category_id):
    brands = Brand.objects.filter(category_id=sub_category_id)
    context = {
        'brands': brands
    }
    return context