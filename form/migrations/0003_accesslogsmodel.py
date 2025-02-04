# Generated by Django 5.0.6 on 2024-06-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_feedback_options_alter_feedback_customer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLogsModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('session_key', models.CharField(blank=True, max_length=1024)),
                ('path', models.CharField(blank=True, max_length=1024)),
                ('method', models.CharField(blank=True, max_length=8)),
                ('data', models.TextField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=45)),
                ('referrer', models.CharField(blank=True, max_length=512, null=True)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'access_logs',
            },
        ),
    ]
