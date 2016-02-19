#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(
        blank=True,
        null= True,
        max_length=30
    )

    class Meta:
        verbose_name = 'Categroia'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.categoria
