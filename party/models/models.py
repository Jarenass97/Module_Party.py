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
    musical_themes = fields.Many2many(string="Musical Themes", comodel_name="party.musical_theme",
                                      relation='producers_musical_themes',
                                      column1='producers_id', column2='musical_theme_id')

class screenwriter(models.Model):
    _name = 'party.screenwriter'
    _description = 'party.screenwriter'

    name = fields.Char()
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='screenwriters_films',
                           column1='screenwriter_id',column2='film_id')

class gender(models.Model):
    _name = 'party.gender'
    _description = 'party.gender'

    name = fields.Char()
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='genders_films',
                           column1='gender_id',column2='film_id')
    musical_themes=fields.Many2many(string="Musical Themes",comodel_name="party.musical_theme",relation='genders_musical_themes',
                           column1='gender_id',column2='musical_theme_id')

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
    Genders=fields.Many2many(comodel_name="party.gender", relation='genders_films',
                                column1='film_id', column2='gender_id')
    Duration=fields.Float()
    Language=fields.Selection([('Spanish','Spanish'),('English','English')])

class author(models.Model):
    _name = 'party.author'
    _description = 'party.author'

    name = fields.Char()
    musical_themes=fields.Many2many(string="Musical Themes",comodel_name="party.musical_theme",relation='authors_musical_themes',
                           column1='author_id',column2='musical_theme_id')


class album(models.Model):
    _name = 'party.album'
    _description = 'party.album'

    name = fields.Char()
    musical_themes = fields.Many2many(string="Musical Themes", comodel_name="party.musical_theme",
                                      relation='albums_musical_themes',
                                      column1='album_id', column2='musical_theme_id')

class format(models.Model):
    _name = 'party.format'
    _description = 'party.format'

    name = fields.Char(string='Format Type')

class record_company(models.Model):
    _name = 'party.record_company'
    _description = 'party.record_company'

    name = fields.Char()
    musical_themes=fields.One2many("party.musical_theme","record_company")

class group(models.Model):
    _name = 'party.group'
    _description = 'party.group'

    name = fields.Char()
    musical_themes=fields.One2many("party.musical_theme","Group")

class musical_theme(models.Model):
    _name = 'party.musical_theme'
    _description = 'party.musical_theme'

    Title = fields.Char()
    Albums=fields.Many2many(comodel_name="party.album", relation='albums_musical_themes',
                                column1='musical_theme_id', column2='album_id')
    releaseDate=fields.Integer(string="Release date")
    Format=fields.Many2many(comodel_name="party.format", relation='formats_musical_themes',
                                column1='musical_theme_id', column2='format_id')
    Genders = fields.Many2many(comodel_name="party.gender", relation='genders_musical_themes',
                               column1='musical_theme_id', column2='gender_id')
    Duration=fields.Float()
    record_company=fields.Many2one("party.record_company")
    Authors=fields.Many2many(comodel_name="party.author", relation='authors_musical_themes',
                                column1='musical_theme_id', column2='author_id')
    Producers = fields.Many2many(comodel_name="party.producer", relation='producers_musical_themes',
                                 column1='musical_theme_id', column2='producers_id')
    Group=fields.Many2one("party.group")

class place(models.Model):
    _name='party.place'
    _description='party.place'

    name=fields.Char()

class assistant(models.Model):
    _name='party.assistant'
    _description='party.assistant'

    name=fields.Char()

class organizer(models.Model):
    _name='party.organizer'
    _description='party.organizer'

    name=fields.Char()

class party(models.Model):
    _name = 'party.party'
    _description = 'party.party'

    Name = fields.Char()
    Date = fields.Date()
    Place = fields.Many2one("party.place")
    Organizer=fields.Many2one("party.organizer")
    Assistants=fields.Many2many("party.assistant")
    Films=fields.Many2many("party.film")
    musical_themes=fields.Many2many("party.musical_theme",string="Musical themes")



