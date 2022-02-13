# Generated by Django 4.0.2 on 2022-02-12 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_remove_libro_autor_id_libro_autor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libro.autor'),
            preserve_default=False,
        ),
    ]