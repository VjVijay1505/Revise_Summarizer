# Generated by Django 4.0.5 on 2022-06-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0003_prompt_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='engine',
            field=models.CharField(blank=True, choices=[('New-davinci', 'Instruct New davinci'), ('Old-davinci', 'Instruct Old davinci'), ('Curie', 'Instruct curie')], max_length=25, null=True),
        ),
    ]
