# -*- coding: utf-8 -*-

from odoo import models, fields, api

class director(models.Model):
    _name = 'party.director'
    _description = 'party.director'

    name = fields.Char()
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='directors_films',
                           column1='director_id',column2='film_id')

class producer(models.Model):
    _name = 'party.producer'
    _description = 'party.producer'

    name = fields.Char()
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='producers_films',
                           column1='producer_id',column2='film_id')

class screenwriter(models.Model):
    _name = 'party.screenwriter'
    _description = 'party.screenwriter'

    name = fields.Char()
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='screenwriters_films',
                           column1='screenwriter_id',column2='film_id')

class film(models.Model):
    _name = 'party.film'
    _description = 'party.film'

    Title = fields.Char()
    director = fields.Many2many(string="Directors",comodel_name="party.director",relation='directors_films',
                                column1='film_id',column2='director_id')
    Producers = fields.Many2many(comodel_name="party.producer", relation='producers_films',
                                column1='film_id', column2='producer_id')
    Screenwriters=fields.Many2many(comodel_name="party.screenwriter", relation='screenwriter_films',
                                column1='film_id', column2='screenwriter_id')
    Country = fields.Selection([('Spain','Spain'),('EE.UU','EE.UU')])
    releaseDate= fields.Date(string="Release Date")
    Duration=fields.Integer()
    Language=fields.Selection([('Spanish','Spanish'),('English','English')])

