from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from . import models

class LdapGroupAdminForm(forms.ModelForm):
    usernames = forms.ModelMultipleChoiceField(
        queryset=models.LdapUser.objects.all(),
        widget=FilteredSelectMultiple('Users', is_stacked=False),
        required=False,
    )

    class Meta:
        exclude = []
        model = models.LdapGroup

    def clean_usernames(self):
        data = self.cleaned_data['usernames']
        if not data:
            return []
        return list(data.values_list('username', flat=True))

@admin.register(models.LdapGroup)
class LdapGroupAdmin(admin.ModelAdmin):
    exclude = ('dn', 'objectClass')
    list_display = ('gid', 'name')
    ordering = ('name',)
    form = LdapGroupAdminForm

@admin.register(models.LdapUser)
class LdapUserAdmin(admin.ModelAdmin):
    exclude = ('dn', 'photo')
    list_display = ('username', 'uid', 'gecos')
    search_fields = ('username', 'gecos')
    readonly_fields = ('username', 'uid', 'home_directory')