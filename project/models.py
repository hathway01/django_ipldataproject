# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Matches(models.Model):
    season = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    team1 = models.CharField(max_length=50, null=True)
    team2 = models.CharField(max_length=50, null=True)
    toss_winner = models.CharField(max_length=50, null=True)
    toss_decision = models.CharField(max_length=50, null=True)
    result = models.CharField(max_length=50, null=True)
    dl_applied = models.IntegerField(default=0)
    winner = models.CharField(max_length=50, null=True)
    win_by_runs = models.IntegerField(default=0)
    win_by_wickets = models.IntegerField(default=0)
    player_of_match = models.CharField(max_length=50, null=True)
    venue = models.CharField(max_length=150, null=True)
    umpire1 = models.CharField(max_length=50, null=True)
    umpire2 = models.CharField(max_length=50, null=True)
    umpire3 = models.CharField(max_length=50, null=True)


class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches,on_delete=models.SET_NULL,null=True)
    inning = models.IntegerField(null=True)
    batting_team = models.CharField(max_length=50, null=True)
    bowling_team = models.CharField(max_length=50, null=True)
    over = models.IntegerField(null=True)
    ball = models.IntegerField(null=True)
    batsman = models.CharField(max_length=50, null=True)
    non_striker = models.CharField(max_length=50, null=True)
    bowler = models.CharField(max_length=50, null=True)
    is_super_over = models.IntegerField(null=True)
    wide_runs = models.IntegerField(null=True)
    bye_runs = models.IntegerField(null=True)
    legbye_runs = models.IntegerField(null=True)
    noball_runs = models.IntegerField(null=True)
    penalty_runs = models.IntegerField(null=True)
    batsman_runs = models.IntegerField(null=True)
    extra_runs = models.IntegerField(null=True)
    total_runs = models.IntegerField(null=True)
    player_dismissed = models.CharField(max_length=50, null=True)
    dismissal_kind = models.CharField(max_length=50, null=True)
    fielder = models.CharField(max_length=50, null=True)