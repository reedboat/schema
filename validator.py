
import re
from functools import wraps

def ValidIdentifier(msg = None):
    ''' Value Must be a valid identifier 
      started with underline or letter
      only numbers, underline or letter included'''
    @wraps(ValidIdentifier)
    def f(v):
        pattern = re.compile('^[a-z_]\w*$')
        if not pattern.match(v):
            raise ValueError(msg or 'invalid identifier')
        return True
    return f

def List(validator, seperator, msg = None):
    @wraps(ValidIdentifier)
    def f(v):
        items = v.split(seperator)
        for item in items:
            if not validator(item):
                raise ValueError(msg or 'invalid list')
        return items
    return f

def ValidDict(msg = None):
    '''Value Must be JSON Dict'''
    @wraps(ValidDict)
    def f(v):
        if v[0] != '{' or v[-1] != '}':
            raise ValueError(msg or 'invalid Json Dict')
        return True
    return f

def Boolean(v):
    if isinstance(v, basestring):
        v = v.lower()
        if v in ('1', 'true', 'yes', 'on', 'enable'):
            return True
        if v in ('0', 'false', 'no', 'off', 'disable'):
            return False
        raise ValueError
    return bool(v)


def Match(pattern, msg=None):
    """Value must match the regular expression."""
    if isinstance(pattern, basestring):
        pattern = re.compile(pattern)

    def f(v):
        if not pattern.match(v):
            raise ValueError(msg or 'does not match regular expression')
        return v
    return f

def Range(min=None, max=None, msg=None):
    """Limit a value to a range."""
    @wraps(Range)
    def f(v):
        if min is not None and v < min:
            raise ValueError(msg or 'value must be at least %s' % min)
        if max is not None and v > max:
            raise ValueError(msg or 'value must be at most %s' % max)
        return v
    return f

def Length(min=None, max=None, msg=None):
    """The length of a value must be in a certain range."""
    @wraps(Length)
    def f(v):
        if min is not None and len(v) < min:
            raise ValueError(msg or 'length of value must be at least %s' % min)
        if max is not None and len(v) > max:
            raise ValueError(msg or 'length of value must be at most %s' % max)
        return v
    return f

def Url(v):
    if v[0:7] != 'http://':
        raise ValueError('invalid url %s' % v)
    return True

def Int(v):
    if str(int(v)) != str(v):
        raise ValueError('invalid integer %s' % v)
    return True

def Str(v):
    if type(v) == str or type(v) == unicode:
        return True
    raise ValueError('invalid string %s' % v)


























