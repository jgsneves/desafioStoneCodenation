# Generated by Django 3.0.8 on 2020-07-15 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=25)),
                ('details', models.TextField(max_length=100)),
                ('type_of', models.CharField(choices=[('DEBUG', 'DEBUG'), ('WARNING', 'WARNING'), ('ERROR', 'ERROR')], max_length=25)),
                ('count_of_events', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False)),
                ('coleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
