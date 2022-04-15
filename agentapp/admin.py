from django.contrib import admin
from .models import agent,contact_info,location,address
# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ['agentid','firstname','lastname','experience','company']
    list_filter = ['agentid','company']
    class Meta:
        model = agent
admin.site.register(agent,AgentAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contactid','agentid','mobileno','email']
    list_filter = ['contactid','agentid']
    class Meta:
        model = contact_info
admin.site.register(contact_info,ContactAdmin)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['locationid','agentloc','locname','loccity','locstate','pincode']
    list_filter = ['locationid','agentloc','locstate']
    class Meta:
        model = location
admin.site.register(location,LocationAdmin)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['addressid','agentid','addressline1','addressline2','city','state','pincode','landmark']
    list_filter = ['agentid','city','state','pincode']
    class Meta:
        model = address
admin.site.register(address,AddressAdmin)
