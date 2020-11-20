# Generated by Django 3.1.3 on 2020-11-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news_board", "0002_auto_20201119_1356"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="news_board.post",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="amount_of_upvotes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]