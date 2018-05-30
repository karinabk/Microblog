#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:56:32 2018

@author: karina
"""

from app import app
from flask import render_template,flash, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
#fake user
    user= {'nickname':'Marat'}
    posts=[
    {'author':{'nickname':'Bubenchik'},
    'body':'Privet privet'
    },
    {'author':{'nickname':'Blah'},
    'body':'Kak delaa'

    }
    ]
    return render_template('index.html',title='Fuck offf', user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {},remember me= {}'.format(
        form.username.data , form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title ='log in', form = form )
