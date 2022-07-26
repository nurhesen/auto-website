# This function gets the data and filters it out according to the query

class CustomFilter:
    def __init__(self, model, request, fields ):
        self.model=model
        self.request=request
        self.fields=fields
        raw_query=request.META['QUERY_STRING']
        self.all_query=[{
            'name':x.split("=")[0],
            'value':x.split("=")[1]
                } if x.split("=")[0].startswith('min') or x.split("=")[0].startswith('max') else {
                   'name':x.split("=")[0],
                   'value':x.split("=")[1].split(',')
                      } for x in raw_query.split("&") 
                          if x.split("=")[0] in fields]



    def filter(self):
        filtered=self.model
        if len(self.all_query)==0:
            return self.model.all()

        for each in self.all_query:

            if each['name'].startswith('max'):
                for_filter={each['name'].split('max_')[1]+"__lte":each['value']}
            elif each['name'].startswith('min'):
                for_filter={each['name'].split('min_')[1]+"__gte":each['value']}
            else:
                for_filter={each['name']+"__in":each['value']}
            if filtered:
                filtered=getattr(filtered, 'filter')(**for_filter)
        return filtered