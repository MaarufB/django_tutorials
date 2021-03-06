# Generated by Django 4.1a1 on 2022-06-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_query_app', '0003_reporter_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['headline']},
        ),
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.AddField(
            model_name='article',
            name='publication',
            field=models.ManyToManyField(to='db_query_app.publication'),
        ),
        migrations.AlterModelTable(
            name='publication',
            table=None,
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
