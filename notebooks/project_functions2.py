import pandas as pd
import numpy as np

def processplayers(file): #This would be the function for loading and processing the players dataset

    
    df1 = (
    pd.read_csv(file)
    .drop(columns = ['DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 
                     'PLAYER_SLUG','TEAM_ABBREVIATION','PLAYERCODE','TEAM_CODE','NBA_FLAG',
                     'GAMES_PLAYED_FLAG','JERSEY', "GAMES_PLAYED_CURRENT_SEASON_FLAG", "DLEAGUE_FLAG", "DISPLAY_FIRST_LAST"])
    .rename(columns = {"ALL_STAR_APPEARANCES":"ALLSTAR", "SEASON_EXP":"SEASON"})
    .sort_values("ALLSTAR", ascending=False)
    .reset_index(drop=True)
    ) 

    df2 = (
    df1.assign(OD = lambda a: (a.PTS*a.AST*a.REB*a.SEASON)/((a.PTS + a.AST + a.REB)*100))
    .assign(Attratio = lambda b: (b.PTS+b.AST)/(b.PTS+b.AST+b.REB))
    .assign(Defratio = lambda c: (c.REB)/(c.PTS+c.AST+c.REB))   
     )
    
    df2['IS_ACTIVE'] = df2['IS_ACTIVE'].replace([0,1],['No','Yes'])
    return df2


def processgame(file):
    #This method will be used to process the game dataset
    df1 = (
    pd.read_csv(file, low_memory = False)
    .drop(columns = ['TEAM_ABBREVIATION_HOME', 'GAME_DATE', 'MATCHUP_HOME', 
                               'MIN_HOME','VIDEO_AVAILABLE_HOME', 'TEAM_ABBREVIATION_AWAY' , 'MIN_AWAY', 'VIDEO_AVAILABLE_AWAY', 
                               'GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_STATUS_ID', 'GAME_STATUS_TEXT', 'GAMECODE', 'LIVE_PERIOD', 'LIVE_PC_TIME', 
                               'NATL_TV_BROADCASTER_ABBREVIATION', 'LIVE_PERIOD_TIME_BCAST', 'WH_STATUS', 'TEAM_CITY_HOME', 'PTS_PAINT_HOME', 
                               'PTS_2ND_CHANCE_HOME', 'PTS_FB_HOME', 'LARGEST_LEAD_HOME', 'LEAD_CHANGES_HOME', 'TIMES_TIED_HOME', 
                               'TEAM_TURNOVERS_HOME', 'TOTAL_TURNOVERS_HOME', 'PTS_OFF_TO_HOME', 'TEAM_CITY_AWAY', 'PTS_PAINT_AWAY', 
                               'PTS_2ND_CHANCE_AWAY', 'PTS_FB_AWAY', 'LARGEST_LEAD_AWAY', 'LEAD_CHANGES_AWAY', 'TIMES_TIED_AWAY', 
                               'TEAM_TURNOVERS_AWAY', 'TOTAL_TURNOVERS_AWAY', 'PTS_OFF_TO_AWAY', 'LEAGUE_ID', 'GAME_TIME', 'TEAM_CITY_NAME_HOME', 
                               'TEAM_NICKNAME_HOME', 'PTS_OT1_HOME', 'PTS_OT2_HOME', 'PTS_OT3_HOME', 'PTS_OT4_HOME', 'PTS_OT5_HOME', 'PTS_OT6_HOME', 
                               'PTS_OT7_HOME', 'PTS_OT8_HOME', 'PTS_OT9_HOME', 'PTS_OT10_HOME', 'TEAM_CITY_NAME_AWAY', 'TEAM_NICKNAME_AWAY', 
                               'PTS_OT1_AWAY', 'PTS_OT2_AWAY', 'PTS_OT3_AWAY', 'PTS_OT4_AWAY', 'PTS_OT5_AWAY', 'PTS_OT6_AWAY', 'PTS_OT7_AWAY', 
                               'PTS_OT8_AWAY', 'PTS_OT9_AWAY', 'PTS_OT10_AWAY', 'LAST_GAME_ID', 'LAST_GAME_DATE_EST', 'LAST_GAME_HOME_TEAM_ID', 
                               'LAST_GAME_HOME_TEAM_CITY', 'LAST_GAME_HOME_TEAM_NAME', 'LAST_GAME_HOME_TEAM_ABBREVIATION', 
                               'LAST_GAME_HOME_TEAM_POINTS', 'LAST_GAME_VISITOR_TEAM_ID', 'LAST_GAME_VISITOR_TEAM_CITY', 
                               'LAST_GAME_VISITOR_TEAM_NAME', 'LAST_GAME_VISITOR_TEAM_CITY1', 'LAST_GAME_VISITOR_TEAM_POINTS', 
                               'VIDEO_AVAILABLE_FLAG', 'PT_AVAILABLE', 'PT_XYZ_AVAILABLE', 'HUSTLE_STATUS', 
                               'HISTORICAL_STATUS', 'FG3M_HOME', 'FG3A_HOME', 'FG3_PCT_HOME', 'FTM_HOME', 
                               'FTA_HOME', 'FT_PCT_HOME', 'FG3M_AWAY', 'FG3A_AWAY', 'FG3_PCT_AWAY', 'FTM_AWAY', 'FTA_AWAY', 'FT_PCT_AWAY', 'FGM_HOME', 
                               'FGA_HOME','OREB_HOME', 'DREB_HOME','MATCHUP_AWAY','WL_AWAY', 'FGM_AWAY', 'FGA_AWAY','OREB_AWAY', 'DREB_AWAY',
                               'HOME_TEAM_ID', 'VISITOR_TEAM_ID','PTS_HOME_y','HOME_TEAM_WINS', 'HOME_TEAM_LOSSES', 'SERIES_LEADER'])
    .dropna()
    .reset_index(drop=True)
    .rename(columns = {"TEAM_ID_HOME":"ID_HOME", "TEAM_ID_AWAY":"ID_AWAY", "TEAM_NAME_HOME":"HOME_TEAM", "TEAM_NAME_AWAY":"AWAY_TEAM"})
)
    return df1