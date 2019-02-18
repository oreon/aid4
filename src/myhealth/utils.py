
import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin

class CreatorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super(CreatorAdmin, self).save_model(request, obj, form, change)

'''
    Function to export data to csv from admin
'''
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;'\
        'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
 
    fields = [field for field in opts.get_fields() if not field.many_to_many\
        and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'