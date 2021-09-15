from django.shortcuts import render, redirect
from django.db.models import Count
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		#"baseball_leagues": League.objects.filter(sport="Baseball"),
		"baseball_leagues": League.objects.filter(sport__contains="baseball"),
		"women_leagues": League.objects.filter(name__contains="women"),
		"all_hockey_leagues": League.objects.filter(sport__contains="hockey"),
		"not_football_leagues": League.objects.exclude(sport__contains="football"),
		"conferences_leagues": League.objects.filter(name__contains="conference"),
		"all_league_atlantic": League.objects.filter(name__contains="atlantic"),
		"teams_house_dallas": Team.objects.filter(location__contains="dallas"),
		"teams_with_raptors": Team.objects.filter(team_name__contains="raptors"),
		"teams_with_city": Team.objects.filter(location__contains="city"),
		"teams_startswith_t": Team.objects.filter(team_name__startswith="T"),
		"teams_orderby_location": Team.objects.all().order_by("location"),
		"teams_orderby_name": Team.objects.all().order_by("-team_name"),
		"player_lastname_cooper": Player.objects.filter(last_name__contains="cooper"),
		"player_name_joshua": Player.objects.filter(first_name__contains="joshua"),
		"player_cooper_less_joshua": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
		"player_name_alexander_or_wyatt": Player.objects.filter(first_name__in=["Alexander","Wyatt"]),
	}
	return render(request, "leagues/index.html", context)

def index2(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		#1
		"teams_atlantic_soccer_conference": Team.objects.filter(league__name__contains="atlantic soccer conference"),
		#2
		"current_players_of_Boston_Penguins" : Player.objects.filter(curr_team__team_name = "Penguins"),
		#3
		"current_players_of_ICBC" : Player.objects.filter(curr_team__league__name__contains = "International Collegiate"),
		#4
		"current_players_of_CAFA_Lopez" : Player.objects.filter(last_name = "Lopez", curr_team__league__name__contains = "Amateur Football"),
		#5
		"all_futbol_player" : Player.objects.filter( curr_team__league__sport__contains = "Football"),
		#6
		"all_team_with_sophia" : Team.objects.filter(curr_players__first_name__contains = "Sophia"),
		#7
		"all_league_with_sophia" : League.objects.filter(teams__curr_players__first_name = "Sophia"),
		#8
		"all_flores_no_wr" : Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders"),
		#9
		"all_team_samuel_evans" : Player.objects.get(first_name = "Samuel", last_name = "Evans").all_teams.all(),
		#10
		"all_players_TCM" : Player.objects.filter(all_teams__team_name__contains = "Tiger-Cats"),
		#11
		"all_oldplayers_WV" :  Player.objects.filter(all_teams__team_name__contains = "Vikings").exclude(curr_team__team_name__contains = "Vikings"),
		#12
		"old_teams_JG" : Player.objects.get(first_name = "Jacob", last_name = "Gray").all_teams.all().exclude(team_name = "Colts"),
		#13
		"all_Joshua_in_FAJBA" : Player.objects.filter(first_name = "Joshua", all_teams__league__name__contains = "Amateur Baseball Player"),
		#14
		"all_team_with_12" : Team.objects.annotate(Count('all_players')).filter(all_players__count__gt = 12),
		#15
		"all_player_with_teams" : Player.objects.annotate(teams = Count("all_teams")).order_by('-teams'),

	}
	return render(request, "leagues/index2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")