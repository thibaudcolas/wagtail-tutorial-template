from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
