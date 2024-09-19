from dataclasses import dataclass


@dataclass
class Player:
    player_name : str
    position:str
    points:int
    games:int
    twopercent:float = None
    threepercent:float = None
    atr:float = None
    ppgratio:float = None
    id:int = None