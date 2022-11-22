# Generated by Django 4.1.3 on 2022-11-22 13:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("flex", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="flexpage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "title_and_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add your title", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.TextBlock(
                                        help_text="Add additional text", required=True
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=None,
            ),
        ),
    ]
