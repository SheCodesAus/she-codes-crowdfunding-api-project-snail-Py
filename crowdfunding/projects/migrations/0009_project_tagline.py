# Generated by Django 4.0.2 on 2022-05-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_faq_milestone_alter_project_category_delete_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tagline',
            field=models.TextField(default='tagline'),
            preserve_default=False,
        ),
    ]
