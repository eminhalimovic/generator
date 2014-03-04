import subprocess, os, sys
from django.contrib import admin
from project.models import Project, InstalledApp, DjangoApp, ProjectAdmin, DatabaseConnection, ProjectDatabase, MiddlewareClass, InstalledMiddlewareClass, StaticfilesFinder, InstalledStaticfilesFinder, TemplateLoader, InstalledTemplateLoader
from django.forms import ModelForm
import django.conf
from django.utils.functional import curry

project_template_path = '/usr/share/pyshared/django/conf/project_template'
sys.path.append(project_template_path)
import settings          
        

class InstalledAppAdmin(admin.TabularInline):
    model = InstalledApp
    extra = 6   
    
    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == "GET":
            for app in DjangoApp.objects.all():
                initial.append({
                    'installed_app': app,
                })
        formset = super(InstalledAppAdmin, self).get_formset(request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, initial=initial)
        return formset

class ProjectAdminAdmin(admin.TabularInline):
    model = ProjectAdmin
    extra = 1     

class ProjectDatabaseAdmin(admin.TabularInline):
    model = ProjectDatabase
    extra = 1

class InstalledMiddlewareClassAdmin(admin.TabularInline):
    model = InstalledMiddlewareClass
    extra = 6
    
    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == "GET":
            for mclass in MiddlewareClass.objects.all():
                initial.append({
                    'installed_middleware_class': mclass,
                })
        formset = super(InstalledMiddlewareClassAdmin, self).get_formset(request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, initial=initial)
        return formset        
        
class InstalledStaticfilesFinderAdmin(admin.TabularInline):
    model = InstalledStaticfilesFinder
    extra = 3
        
    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == "GET":
            for finder in StaticfilesFinder.objects.all():
                initial.append({
                    'installed_staticfiles_finder': finder,
                })
        formset = super(InstalledStaticfilesFinderAdmin, self).get_formset(request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, initial=initial)
        return formset
        
class InstalledTemplateLoaderAdmin(admin.TabularInline):
    model = InstalledTemplateLoader
    extra = 3        

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == "GET":
            for loader in TemplateLoader.objects.all():
                initial.append({
                    'installed_template_loader': loader,
                })
        formset = super(InstalledTemplateLoaderAdmin, self).get_formset(request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, initial=initial)
        return formset        
     
    
class DjangoAppAdmin(admin.ModelAdmin):
    class Meta:
        model = DjangoApp

admin.site.register(DjangoApp, DjangoAppAdmin)

class MiddlewareClassAdmin(admin.ModelAdmin):
    class Meta:
        model = MiddlewareClass
        
admin.site.register(MiddlewareClass, MiddlewareClassAdmin)

class StaticfilesFinderAdmin(admin.ModelAdmin):
    class Meta:
        model = StaticfilesFinder
        
admin.site.register(StaticfilesFinder, StaticfilesFinderAdmin)

class TemplateLoaderAdmin(admin.ModelAdmin):
    class Meta:
        model = TemplateLoader
        
admin.site.register(TemplateLoader, TemplateLoaderAdmin)

class DatabaseConnectionForm(ModelForm):
    class Meta:
        model = DatabaseConnection
        
    def __init__(self, *args, **kwargs):
        super(DatabaseConnectionForm, self).__init__(*args, **kwargs)
        default_settings = settings.DATABASES['default']
        self.fields['connection_name'].initial = 'default'
        self.fields['engine'].initial = default_settings['ENGINE']
        self.fields['name'].initial = default_settings['NAME']
        self.fields['user'].initial = default_settings['USER']
        self.fields['password'].initial = default_settings['PASSWORD']
        self.fields['host'].initial = default_settings['HOST']
        self.fields['port'].initial = default_settings['PORT']
        
class DatabaseConnectionAdmin(admin.ModelAdmin):
    form = DatabaseConnectionForm
    # class Meta:
        # model = DatabaseConnection
        
admin.site.register(DatabaseConnection, DatabaseConnectionAdmin)   

class ProjectForm(ModelForm):
    class Meta:
        model = Project
    
    def __init__(self, *args, **kwargs):
        ### override ModelForm __init__() metode
        # dohvati project template settings kao modul
        # project_template_path = os.path.join(os.path.dirname(django.conf.__file__), 'project_template')
        
        # inicijaliziramo polja forme 
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['time_zone'].initial = settings.TIME_ZONE
        self.fields['allowed_hosts'].initial = ', '.join(repr(x) for x in settings.ALLOWED_HOSTS)
        self.fields['debug'].initial = repr(settings.DEBUG)
        self.fields['language_code'].initial = settings.LANGUAGE_CODE
        self.fields['logging'].initial = repr(settings.LOGGING)
        #self.fields['managers'].initial = repr(settings.DEBUG)
        self.fields['media_root'].initial = settings.MEDIA_ROOT
        self.fields['media_url'].initial = settings.MEDIA_URL
        self.fields['root_urlconf'].initial = settings.ROOT_URLCONF
        self.fields['secret_key'].initial = settings.SECRET_KEY
        self.fields['site_id'].initial = str(settings.SITE_ID)
        self.fields['staticfiles_dirs'].initial = settings.STATICFILES_DIRS
        self.fields['static_root'].initial = settings.STATIC_ROOT
        self.fields['static_url'].initial = settings.STATIC_URL
        #self.fields['template_debug'].initial = settings.TEMPLATE_DEBUG
        self.fields['template_dirs'].initial = settings.TEMPLATE_DIRS
        self.fields['time_zone'].initial = settings.TIME_ZONE
        self.fields['use_i18n'].initial = repr(settings.USE_I18N)
        self.fields['use_l10n'].initial = repr(settings.USE_L10N)
        #self.fields['use_tz'].initial = settings.USE_TZ
        #self.fields['wsgi_application'].initial = settings.WSGI_APPLICATION
        
                
    def clean_home_dir(self):
        # clean_FIELD_NAME - validacija polja
        # uvijek treba vratiti cleaned_data od toga polja    
        home_dir = self.cleaned_data['home_dir']
        project_name = self.cleaned_data['project_name']
        if os.path.exists(home_dir):
            # r = subprocess.call(["/usr/bin/django-admin", "startproject", project_name, "--settings=django.conf.global_settings"], cwd=home_dir, stderr=subprocess.STDOUT, shell=True)
            r = subprocess.call(["/usr/bin/django-admin", "startproject", project_name, "--settings=django.conf.global_settings"], cwd=home_dir)            
            if r == 0:
                settings_file_path = os.path.join(home_dir, project_name, project_name, 'settings.py')
                r = subprocess.call("rm " + settings_file_path, stderr=subprocess.STDOUT, shell=True)
        return home_dir
        
class ProjectProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    inlines = [InstalledAppAdmin, ProjectAdminAdmin, ProjectDatabaseAdmin, InstalledMiddlewareClassAdmin, InstalledStaticfilesFinderAdmin, InstalledTemplateLoaderAdmin]

admin.site.register(Project, ProjectProjectAdmin) 