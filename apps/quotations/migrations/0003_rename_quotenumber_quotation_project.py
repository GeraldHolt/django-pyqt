# Generated by Django 4.1.2 on 2022-10-20 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quotations", "0002_alter_supportquotation_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quotation",
            old_name="quoteNumber",
            new_name="project",
        ),
    ]
