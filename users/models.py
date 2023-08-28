from django.db import models

# Create your models here.

class Product(models.Model):
    name: models.CharField(max_length=300)

class ProductDetail(models.Model):
    name: models.CharField(max_length=300)

class Provider(models.Model):
    name: models.CharField(max_length=300)

class Client(models.Model):
    name: models.CharField(max_length=300)

class Driver(models.Model):
    name: models.CharField(max_length=300)

class DeliverProduct(models.Model):
    name: models.CharField(max_length=300)

class RegisterProducts(models.Model):
    name: models.CharField(max_length=300)

class Resource(models.Model):
    name: models.CharField(max_length=300)

class ResourceDetail(models.Model):
    name: models.CharField(max_length=300)
