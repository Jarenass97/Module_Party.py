# -*- coding: utf-8 -*-
import datetime
import logging
import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError


_logger=logging.getLogger(__name__)

class director(models.Model):
    _name = 'party.director'
    _description = 'party.director'

    photo=fields.Image(max_width=200,max_height=200)
    name = fields.Char(required='1')
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='directors_films',
                           column1='director_id',column2='film_id')
    _sql_constraints=[('name_uniq','unique(name)','Name can\'t be repeated')]


class producer(models.Model):
    _name = 'party.producer'
    _description = 'party.producer'

    photo = fields.Image(max_width=200, max_height=200)
    name = fields.Char(required='1')
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='producers_films',
                           column1='producer_id',column2='film_id')
    musical_themes = fields.Many2many(string="Musical Themes", comodel_name="party.musical_theme",
                                      relation='producers_musical_themes',
                                      column1='producers_id', column2='musical_theme_id')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class screenwriter(models.Model):
    _name = 'party.screenwriter'
    _description = 'party.screenwriter'

    photo = fields.Image(max_width=200, max_height=200)
    name = fields.Char(required='1')
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='screenwriters_films',
                           column1='screenwriter_id',column2='film_id')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class gender(models.Model):
    _name = 'party.gender'
    _description = 'party.gender'

    name = fields.Char(required='1')
    films=fields.Many2many(string="Films",comodel_name="party.film",relation='genders_films',
                           column1='gender_id',column2='film_id')
    musical_themes=fields.Many2many(string="Musical Themes",comodel_name="party.musical_theme",relation='genders_musical_themes',
                           column1='gender_id',column2='musical_theme_id')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Gender can\'t be repeated')]

class film(models.Model):
    _name = 'party.film'
    _description = 'party.film'

    cover=fields.Image(max_width=200,max_height=200)
    title = fields.Char(required='1')
    director = fields.Many2many(string="Directors",comodel_name="party.director",relation='directors_films',
                                column1='film_id',column2='director_id')
    producers = fields.Many2many(comodel_name="party.producer", relation='producers_films',
                                column1='film_id', column2='producer_id')
    screenwriters=fields.Many2many(comodel_name="party.screenwriter", relation='screenwriter_films',
                                column1='film_id', column2='screenwriter_id')
    country = fields.Char()
    release_Date= fields.Date(string="Release Date")
    genders=fields.Many2many(comodel_name="party.gender", relation='genders_films',
                                column1='film_id', column2='gender_id')
    duration=fields.Float()
    language=fields.Char()
    _sql_constraints = [('title_uniq', 'unique(title)', 'Title can\'t be repeated')]

class author(models.Model):
    _name = 'party.author'
    _description = 'party.author'

    photo = fields.Image(max_width=200, max_height=200)
    name = fields.Char(required='1')
    musical_themes=fields.Many2many(string="Musical Themes",comodel_name="party.musical_theme",relation='authors_musical_themes',
                           column1='author_id',column2='musical_theme_id')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]


class album(models.Model):
    _name = 'party.album'
    _description = 'party.album'

    cover = fields.Image(max_width=200, max_height=200)
    name = fields.Char(required='1')
    musical_themes = fields.One2many('party.musical_theme','album')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class format(models.Model):
    _name = 'party.format'
    _description = 'party.format'

    name = fields.Char(string='Format Type',required='1')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Format can\'t be repeated')]

class record_company(models.Model):
    _name = 'party.record_company'
    _description = 'party.record_company'

    logo = fields.Image(max_width=200, max_height=200)
    name = fields.Char(required='1')
    musical_themes=fields.One2many("party.musical_theme","record_company")
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class group(models.Model):
    _name = 'party.group'
    _description = 'party.group'

    photo = fields.Image(max_width=200, max_height=200)
    name = fields.Char(required='1')
    musical_themes=fields.One2many("party.musical_theme","group")
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class musical_theme(models.Model):
    _name = 'party.musical_theme'
    _description = 'party.musical_theme'

    cover = fields.Image(max_width=200, max_height=200)
    title = fields.Char(required='1')
    album=fields.Many2one('party.album')
    release_Date=fields.Integer(string="Release date")
    format=fields.Many2many(comodel_name="party.format", relation='formats_musical_themes',
                                column1='musical_theme_id', column2='format_id')
    genders = fields.Many2many(comodel_name="party.gender", relation='genders_musical_themes',
                               column1='musical_theme_id', column2='gender_id')
    duration=fields.Float()
    record_company=fields.Many2one("party.record_company")
    authors=fields.Many2many(comodel_name="party.author", relation='authors_musical_themes',
                                column1='musical_theme_id', column2='author_id')
    producers = fields.Many2many(comodel_name="party.producer", relation='producers_musical_themes',
                                 column1='musical_theme_id', column2='producers_id')
    is_group=fields.Boolean()
    group=fields.Many2one("party.group")
    _sql_constraints = [('title_uniq', 'unique(title)', 'Title can\'t be repeated')]

class place(models.Model):
    _name='party.place'
    _description='party.place'

    photo = fields.Image(max_width=200, max_height=200)
    name=fields.Char(required='1')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class assistant(models.Model):
    _name='party.assistant'
    _description='party.assistant'

    photo=fields.Image(max_width=200,max_height=200)
    dni=fields.Char(string="DNI",required='1')
    name=fields.Char(required='1')
    email=fields.Char(required='1')
    Birthday=fields.Date(default=datetime.date.today(),required='1')
    Age=fields.Integer(compute='_edad',store=True)

    @api.constrains('email')
    def _check_email(self):
        regex=re.compile('\w+@\w+\.[a-z]*\Z',re.I)
        for assistant in self:
            if not regex.match(assistant.email):
                raise ValidationError('El formato de email no es correcto')
    @api.constrains('dni')
    def _check_dni(self):
        regex=re.compile('[0-9]{8}[a-z]\Z',re.I)
        for assistant in self:
            if not regex.match(assistant.dni):
                raise ValidationError('El formato de DNI no es correcto')

    _sql_constraints=[('dni_uniq','unique(dni)','DNI can\'t be repeated')]

    @api.depends('Birthday')
    def _edad(self):
        for assistant in self:
            hoy = datetime.datetime.now()
            fnac=assistant.Birthday
            assistant.Age = hoy.year - fnac.year - ((hoy.month, hoy.day) < (fnac.month, fnac.day))

class organizer(models.Model):
    _name='party.organizer'
    _description='party.organizer'

    photo = fields.Image(max_width=200, max_height=200)
    name=fields.Char(required='1')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]

class party(models.Model):
    _name = 'party.party'
    _description = 'party.party'

    photo=fields.Image(max_width=200,max_height=200)
    name = fields.Char(required='1')
    date = fields.Date(default=datetime.date.today()+datetime.timedelta(days=1),required='1')
    place = fields.Many2one("party.place")
    organizer=fields.Many2one("party.organizer")
    assistants=fields.Many2many("party.assistant")
    films=fields.Many2many("party.film")
    musical_themes=fields.Many2many("party.musical_theme",string="Musical themes")
    _sql_constraints = [('name_uniq', 'unique(name)', 'Name can\'t be repeated')]



