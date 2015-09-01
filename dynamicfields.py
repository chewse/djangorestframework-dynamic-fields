# -*- coding: utf-8 -*-

from collections import defaultdict


class DynamicFieldsMixin(object):
    """
    Serializer mixin to allow restricting the fields processed and returned.

    This serializer mixin allows you to supply a "fields" query parameter in an
    API call to limit the fields that are processed, serialized, and returned.
    This can be a big help in keeping request times reasonable.

    Fields should be specified as a comma-separated list of the names of the
    fields you want returned. If you want to restrict nested serializer fields,
    you should include both the serializer field name and the nested field
    names desired, using the double-underscore syntax.

    Example: fields=id,name,vendor,vendor__name
    """

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsMixin, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            requested_fields = request.query_params.get('fields')
            if requested_fields:
                requested_fields = set(requested_fields.split(','))
                self._restrict_dynamic_fields(self.fields, requested_fields)

    def _restrict_dynamic_fields(self, fields, requested_fields):
        # Remove the fields that were not requested for this serializer
        standard_fields = set(fields.keys())
        for field in standard_fields - requested_fields:
            fields.pop(field)

        # Find restricted fields for nested serializers
        nested_fields = defaultdict(set)
        for field in requested_fields - standard_fields:
            if '__' in field:
                serializer_field, nested_field = field.split('__', 1)
                if serializer_field in standard_fields & requested_fields:
                    nested_fields[serializer_field].add(nested_field)

        # Recursively restrict fields on nested serializers
        for serializer_field, nested_fields in nested_fields.iteritems():
            nested_serializer = fields[serializer_field]
            self._restrict_dynamic_fields(
                nested_serializer.fields, nested_fields)
