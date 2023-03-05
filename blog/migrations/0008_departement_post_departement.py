# Generated by Django 4.1.7 on 2023-03-02 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_nationalite_post_pays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departementname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='DEPARTEMENT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.departement'),
        ),
    ]
