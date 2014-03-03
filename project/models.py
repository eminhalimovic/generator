from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=64)
    home_dir = models.CharField(max_length=1024)
    allowed_hosts = models.CharField(max_length=1024, blank=True)
    debug = models.BooleanField(default=True)
    language_code = models.CharField(max_length=16)
    logging = models.CharField(max_length=1024)
    managers = models.CharField(max_length=1024, default='ADMINS')
    media_root = models.CharField(max_length=1024, blank=True)
    media_url = models.CharField(max_length=1024, blank=True)
    root_urlconf = models.CharField(max_length=1024, default='.urls')
    secret_key = models.CharField(max_length=1024)
    site_id = models.IntegerField(default=1)
    staticfiles_dirs = models.CharField(max_length=1024, blank=True)
    static_root = models.CharField(max_length=1024, blank=True)
    static_url = models.CharField(max_length=1024, default='/static/')
    template_debug = models.CharField(max_length=1024, default = 'DEBUG')
    template_dirs = models.CharField(max_length=1024, blank=True)
    time_zone = models.CharField(max_length=64)
    use_i18n = models.BooleanField(default=True)
    use_l10n = models.BooleanField(default=True)
    use_tz = models.BooleanField(default=True)
    wsgi_application = models.CharField(max_length=1024, default='.wsgi.application')
    
    def __unicode__(self):
        return self.project_name
        
class DjangoApp(models.Model):
    name = models.CharField(max_length=256, unique=True)
    class Meta:
        db_table = 'settings_django_apps'
        
    def __unicode__(self):
        return self.name
        
        
class InstalledApp(models.Model):
    project = models.ForeignKey(Project)
    installed_app = models.ForeignKey(DjangoApp)
    enabled = models.BooleanField(default=True)
    class Meta:
        db_table = 'settings_installed_apps'
    
    def __unicode__(self):
        return self.installed_app.name

class ProjectAdmin(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    
    class Meta:
        db_table = 'settings_project_admins'
    
    def __unicode__(self):
        return self.name
        
class DatabaseEngine(models.Model):
        name = models.CharField(max_length=256)
        
        class Meta:
            db_table = 'settings_db_engine'
            
        def __unicode__(self):
            return self.name

class DatabaseConnection(models.Model):
    connection_name = models.CharField(max_length=256)
    engine = models.ForeignKey(DatabaseEngine)
    name = models.CharField(max_length=256)
    user = models.CharField(max_length=256, blank=True)
    password = models.CharField(max_length=256, blank=True)
    host = models.CharField(max_length=25, blank=True)
    port = models.IntegerField(null=True, blank=True)    
    
    class Meta:
        db_table = 'settings_db_connection'
    
    def __unicode__(self):
        return self.connection_name
                
class ProjectDatabase(models.Model):
    project = models.ForeignKey(Project)
    connection = models.ForeignKey(DatabaseConnection)
    
    class Meta:
        db_table = 'settings_database_project'
        
class MiddlewareClass(models.Model):
    name = models.CharField(max_length=256, unique=True)
    class Meta:
        verbose_name_plural = 'Middleware classes'
        db_table = 'settings_middleware_classes'
        
    def __unicode__(self):
        return self.name
        
        
class InstalledMiddlewareClass(models.Model):
    project = models.ForeignKey(Project)
    installed_middleware_class = models.ForeignKey(MiddlewareClass)
    enabled = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Installed Middleware Classes'
        db_table = 'settings_installed_middleware_classes'
    
    def __unicode__(self):
        return self.installed_middleware_class.name

class StaticfilesFinder(models.Model):
    name=models.CharField(max_length=256, unique=True)
    class Meta:
        db_table = 'settings_staticfiles_finders'

    def __unicode__(self):
        return self.name
        
class InstalledStaticfilesFinder(models.Model):
    project = models.ForeignKey(Project)
    installed_staticfiles_finder = models.ForeignKey(StaticfilesFinder)
    enabled = models.BooleanField(default=True)
    class Meta:
        db_table = 'settings_installed_staticfiles_finders'
        
class TemplateLoader(models.Model):
    name=models.CharField(max_length=256, unique=True)
    class Meta:
        db_table = 'settings_template_loaders'
        
    def __unicode__(self):
        return self.name
        
class InstalledTemplateLoader(models.Model):
    project = models.ForeignKey(Project)
    installed_template_loader = models.ForeignKey(TemplateLoader)
    enabled = models.BooleanField(default=True)
    class Meta:
        db_table = 'settings_installed_template_loaders'