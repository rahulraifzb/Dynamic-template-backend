# Generated by Django 4.1.7 on 2023-02-21 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_alter_template_footer_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to=settings.AUTH_USER_MODEL),
        ),
    ]
