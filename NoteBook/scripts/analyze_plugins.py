import re
import inspect


def analyze(plugin):
    module_description = inspect.getdoc(plugin)
    # print(module_description)

    data = dict()

    found = False
    valuelines = False
    key = None
    value = None

    for line in module_description.split('\n'):
        if not found:
            if line == 'Plugin:':
                found = True
            continue

        if valuelines:
            m = __valueline.fullmatch(line)
            if not m:
                valuelines = False
                data[key] = '\n'.join(value)
            else:
                value.append(m.group('value') or '')
                continue

        m = __only_key.fullmatch(line)
        if m:
            key = m.group('key')
            value = []
            valuelines = True
            continue

        m = __key_value.fullmatch(line)
        if m:
            data[m.group('key')] = m.group('value')
            continue

        break

    return data


__key_value = re.compile(r'[ ]{4}(?P<key>\w+): (?P<value>.+)')
__only_key = re.compile(r'[ ]{4}(?P<key>\w+):\s*')
__valueline = re.compile(r'[ ]{8}(?P<value>.*)|')  # (or empty line)
