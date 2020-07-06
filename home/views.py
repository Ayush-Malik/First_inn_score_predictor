from django.shortcuts import render
from home.models import input_form_class

from django.utils import timezone
from django.http import HttpResponseRedirect



# Unzipping and loading the model
import _pickle as cPickle
import gzip

def load_zipped_pickle(filename):
    with gzip.open(filename, 'rb') as f:
        loaded_object = cPickle.load(f)
        return loaded_object


# Create your views here.

venues = ['Eden Gardens', 'M Chinnaswamy Stadium', 'Wankhede Stadium',
       'Feroz Shah Kotla', 'MA Chidambaram Stadium, Chepauk',
       'Punjab Cricket Association Stadium, Mohali', 'Sawai Mansingh Stadium',
       'Rajiv Gandhi International Stadium, Uppal',
       'Sardar Patel Stadium, Motera', 'Kingsmead', 'Brabourne Stadium',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'SuperSport Park', 'Dubai International Cricket Stadium',
       'Himachal Pradesh Cricket Association Stadium', 'Sheikh Zayed Stadium',
       "St George's Park", 'Sharjah Cricket Stadium',
       'JSCA International Stadium Complex', 'New Wanderers Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'Dr DY Patil Sports Academy', 'Maharashtra Cricket Association Stadium',
       'Newlands', 'Barabati Stadium', 'Buffalo Park', 'OUTsurance Oval',
       'Holkar Cricket Stadium', 'Subrata Roy Sahara Stadium',
       'De Beers Diamond Oval']

bat_teams = ['Mumbai Indians', 'Kings XI Punjab', 'Chennai Super Kings',
       'Royal Challengers Bangalore', 'Kolkata Knight Riders',
       'Rajasthan Royals', 'Delhi Daredevils', 'Sunrisers Hyderabad']

bowl_teams = ['Royal Challengers Bangalore' ,'Mumbai Indians', 'Kings XI Punjab',
                'Chennai Super Kings','Kolkata Knight Riders','Rajasthan Royals', 
                'Delhi Daredevils', 'Sunrisers Hyderabad']




venues_for_calculations = ['Brabourne Stadium', 'Buffalo Park', 'De Beers Diamond Oval', 'Dr DY Patil Sports Academy', 
'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Dubai International Cricket Stadium', 'Eden Gardens',
 'Feroz Shah Kotla', 'Himachal Pradesh Cricket Association Stadium', 'Holkar Cricket Stadium', 
 'JSCA International Stadium Complex', 'Kingsmead', 'M Chinnaswamy Stadium', 'MA Chidambaram Stadium, Chepauk',
  'Maharashtra Cricket Association Stadium', 'New Wanderers Stadium', 'Newlands', 'OUTsurance Oval',
   'Punjab Cricket Association IS Bindra Stadium, Mohali', 'Punjab Cricket Association Stadium, Mohali',
    'Rajiv Gandhi International Stadium, Uppal', 'Sardar Patel Stadium, Motera', 'Sawai Mansingh Stadium',
     'Shaheed Veer Narayan Singh International Stadium', 'Sharjah Cricket Stadium', 'Sheikh Zayed Stadium',
      "St George's Park", 'Subrata Roy Sahara Stadium', 'SuperSport Park', 'Wankhede Stadium']

bat_teams_for_calculations = ['Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 
                            'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 
                            'Sunrisers Hyderabad']

bowl_teams_for_calculations = ['Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 
                            'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 
                            'Sunrisers Hyderabad']






context = { 'venues' : venues , 'bat_teams' : bat_teams , 'bowl_teams' : bowl_teams }
def home_page(request):
 
    return render(request , 'home_page.html' , context)

def submit_and_process_data(request):

    name = request.POST['name']

    venue = request.POST['venue']
    Batting_Team = request.POST['Batting_Team']
    Bowling_Team = request.POST['Bowling_Team']
    overs = request.POST['overs']
    runs = request.POST['runs']
    wickets = request.POST['wickets']
    runs_last_5 = request.POST['runs_last_5']
    wickets_last_5 = request.POST['wickets_last_5']

    input_form_class.objects.create( name = name , venue = venue , Batting_Team = Batting_Team , Bowling_Team = Bowling_Team , overs = overs , 
                                   runs = runs  , wickets = wickets , runs_last_5 = runs_last_5 , wickets_last_5 = wickets_last_5 , added_date = timezone.now()   )

    

    # Preparing the data for model as it requires encoded data
    A = []
    for stadium in venues_for_calculations :
        if stadium == venue:
            A.append(1)
        else:
            A.append(0)

    
    B = []
    for team in bat_teams_for_calculations :
        if team == Batting_Team:
            B.append(1)
        else:
            B.append(0)

    C = []
    for team in bowl_teams_for_calculations :
        if  team == Bowling_Team :
            C.append(1)
        else:
            C.append(0)

 
    final = [ A + B + C + [ runs , wickets , overs , runs_last_5 , wickets_last_5 ] ]

    
    forest_reg = load_zipped_pickle('model')
    pred_value = int(forest_reg.predict(final))
    print("Predictions :" ,  pred_value )
    
    context = {"Predicted_score" : pred_value}

    return render(request , 'output.html' , context)
    
    # return HttpResponseRedirect('/' , context)
        
