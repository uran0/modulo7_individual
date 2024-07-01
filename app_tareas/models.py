from django.db import models
from django.utils.timezone import now
from account.models import User


class Tag(models.Model):
    tag_choices= [
        ('HOG', 'Hogar'),
        ('TRA', 'Trabajo'),
        ('EST', 'Estudios'),
    ]
    name= models.CharField(max_length=3,choices=tag_choices,default='HOG')
    def __str__(self):
        return dict(self.tag_choices).get(self.name, '')
    class Meta:
        ordering=['name']

class Priority(models.Model):
    priority = models.BooleanField(default=False)

    def __str__(self):
        return "Alta" if self.priority else "Baja"
    
    class Meta:
        ordering = ['-priority']

class Task(models.Model):
    status_choices= [
        ('pendiente', 'Pendiente'),
        ('progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('expirada', 'Expirada'),
    ]
    name = models.CharField(max_length=150)
    expire_date = models.DateField(blank=False, null=False, default=now)
    description = models.TextField()
    status = models.CharField(max_length=10,choices=status_choices, null=True, default='pendiente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default='HOG', related_name='tasks')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['expire_date', 'priority']
        indexes = [
            models.Index(fields=['name']),
        ]

