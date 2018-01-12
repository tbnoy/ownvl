def fieldsDecider(fields):
    exists = [
        'metadata',
        'links',
        'cons',
        'another',
        'urls',
        'modifiers',
        'captions',
        'rays',
        'auth',
        'waivers',
        'thumbnail',
        'audio',
        'ads'
    ]
    
    fieldRules = {
        'all': exists,
        'default': ['metadata', 'urls', 'modifiers', 'captions'],
    }   

    fieldsToRet = []

    try:
        fields = fields.split(",")
        for field in fields:
            if field in fieldRules:
                fieldsToRet = fieldsToRet + fieldRules[field]
            elif field in exists:
                fieldsToRet.append(field)
    except:
        return fieldRules['default']

    

    return list(set(fieldsToRet))