# Generated by Django 4.2.1 on 2023-05-25 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Milk', 'Milk'), ('Yogurt', 'Yogurt'), ('Apple', 'Apple'), ('Banana', 'Banana'), ('Orange', 'Orange'), ('Grapes', 'Grapes'), ('Strawberry', 'Strawberry'), ('Pineapple', 'Pineapple'), ('Watermelon', 'Watermelon'), ('Mango', 'Mango'), ('Chicken', 'Chicken'), ('Beef', 'Beef'), ('vegetables', 'vegetables'), ('fruits', 'fruits'), ('meat', 'meat'), ('fish', 'fish'), ('eggs', 'eggs'), ('bread', 'bread'), ('cereal', 'cereal'), ('rice', 'rice'), ('pasta', 'pasta'), ('nuts', 'nuts'), ('beans', 'beans'), ('oil', 'oil'), ('butter', 'butter'), ('margarine', 'margarine'), ('salad dressing', 'salad dressing'), ('sugar', 'sugar'), ('honey', 'honey'), ('jam', 'jam'), ('jelly', 'jelly'), ('syrup', 'syrup'), ('cookies', 'cookies')], max_length=50)),
                ('product_image', models.ImageField(upload_to='productimg')),
                ('total_calroes', models.IntegerField(default=0)),
                ('total_fat', models.IntegerField(default=0)),
                ('total_protein', models.IntegerField(default=0)),
                ('total_carbohydrates', models.IntegerField(default=0)),
                ('total_sodium', models.IntegerField(default=0)),
                ('total_sugar', models.IntegerField(default=0)),
                ('total_cholesterol', models.IntegerField(default=0)),
                ('total_potassium', models.IntegerField(default=0)),
                ('total_vitamin_a', models.IntegerField(default=0)),
                ('total_vitamin_c', models.IntegerField(default=0)),
                ('total_calcium', models.IntegerField(default=0)),
                ('total_iron', models.IntegerField(default=0)),
                ('total_vitamin_d', models.IntegerField(default=0)),
                ('total_magnesium', models.IntegerField(default=0)),
                ('total_fiber', models.IntegerField(default=0)),
                ('total_water', models.IntegerField(default=0)),
                ('total_zinc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Kot Begum', 'Kot Begum'), ('Thokar Naiz baig', 'Thokar Naiz baig'), ('Shah Alam Market', 'Shah Alam Market'), ('Model Town', 'Model Town'), ('wapda Town', 'wapda Town'), ('Gulshan Ravi', 'Gulshan Ravi'), ('Gulberg', 'Gulberg'), ('Garden Town', 'Garden Town'), ('Faisal Town', 'Faisal Town'), ('DHA', 'DHA'), ('Cantt', 'Cantt'), ('Johar Town', 'Johar Town'), ('Bahria Town', 'Bahria Town'), ('Askari', 'Askari'), ('Valencia', 'Valencia'), ('Punjab Society', 'Punjab Society'), ('Punjab Coop Housing Society', 'Punjab Coop Housing Society'), ('Punjab Govt Servants Housing Foundation', 'Punjab Govt Servants Housing Foundation'), ('Punjab Small Industries Colony', 'Punjab Small Industries Colony'), ('Punjab University Employees Society', 'Punjab University Employees Society'), ('Punjab University Society', 'Punjab University Society'), ('Punjab Govt Employees Society', 'Punjab Govt Employees Society')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_calroes', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutranta_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
