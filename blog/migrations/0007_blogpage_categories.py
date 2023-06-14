from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blogcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="blog.blogcategory"
            ),
        ),
    ]
