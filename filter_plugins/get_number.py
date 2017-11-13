from jinja2.utils import soft_unicode

def get_number(value, pattern, position):
    pos = int(position)
    return int(value.split(soft_unicode(pattern))[pos])

class FilterModule(object):

    def filters(self):
        return {
            'get_number': get_number,
        }