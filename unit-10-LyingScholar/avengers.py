class avenger:
    __slots__ = ["made_up_name","real_name","powers","weapons"]
    
    def __init__ (self, made_up_name,real_name,powers,weapons):
        
        self.made_up_name = made_up_name
        self.real_name = real_name
        self.powers=powers
        self.weapons=weapons

class Avengers:
    __slots__ = ['team_heroes', 'team_leader']

    def __init__(self):
        self.team_heroes = []
        self.team_leader = None


    def add_hero(self, avenger):
        self.team_heroes.append(avenger)
    
    def make_leader(self, avenger):
        self.team_leader = avenger


    def print_details(self, avenger):
        print("Hero Name:", avenger.made_up_name)
        print("Real Identity:", avenger.real_name)
        print("Super Powers:")
        for i in avenger.powers:
            try:
                print('\t'+i)
            except:
                break
        print("Weapons:")
        for i in avenger.weapons:
            try:
                print('\t'+i)
            except:
                break
        pass

    def print_roster(self):
        for member in self.team_heroes:
            if member == self.team_leader:
                print(member.made_up_name + " (Team Leader)")
            else:
                print(member.made_up_name)
        pass

    def find_member(self, name):
        for member in self.team_heroes:
            if member.made_up_name.lower().strip() == name.lower().strip():
                return member
        print("Avenger not found.")
        return None

    def get_team_leader(self):
        if self.team_leader is not None:
            return self.team_leader
        else:
            print("No team leader assigned.")
            return None

def main():
    avenger4 = avenger("Super coder","CA",["clickity-clackity"],["Python","Pytest","Github"])
    
    avenger3 = avenger("Black Widow", "Natasha Romanoff", ['Enhanced Physicality','Master Martial Artist','Espionage','Expert Marksman','Acrobatics','Multilingualism','Tactical Planning','Infiltration','Stealth','Hacking Skills','Interrogation','Manipulation','Seduction','Deception','Multi Vehicular Driver','Combat Strategy','Resilience','Stamina','Master Spy','Covert Operations','Assassination Skills','Escape Artist','Impersonation','Close-Quarters Combat Expert','Weapon Proficiency','High Pain Threshold','Enhanced Reflexes','Intelligence Gathering','Surveillance Expert','Encryption','Knowledge of Explosives','Expert Lock-picking','Hand-to-Hand Combat Specialist','Tactical Firearms Training','Infiltration Expert'], ['Glock 26','Widow\'s Bite','Glock 17','Widow\'s Line','Tactical Baton','Dual Glock 18C','Combat Knives','Glock 19','Widow\'s Bite Wrist Gauntlets','MK 2 Grenades','Widow\'s Kiss','Dual Beretta 92F','Desert Eagle','AK-47','MP-446 Viking','FN SCAR-L','SIG Sauer P226','Heckler & Koch USP','Mossberg 500 shotgun','Steyr AUG A3','Remington 700 Sniper Rifle','Taser X26','M4A1 Carbine','Glock 22','Taser Disks','Dual MP-443 Grach','Widow\'s Stingers','MP5 Submachine Gun','Widow\'s Kiss Mark II','Widow\'s Bite Mark II','FN F2000','Beretta 92FS','Walther PPK','H&K MP7','M1911 pistol','Benelli M4 shotgun','Dragunov sniper rifle','FN Five-seven','Steyr SPP','Compound Bow','FN P90','Ruger MK III','SPAS-12 shotgun','H&K G36C','Steyr AUG HBAR','Colt Python revolver','Smith & Wesson M&P','Mossberg 590 shotgun','Barrett M82 sniper rifle','Crossbow'])
    
    avenger1 = avenger(None,None,None,None)
    avenger1.made_up_name = "Iron Man"
    avenger1.real_name = "Tony Stark"
    avenger1.powers = [
        "Genius",
        "Billionaire",
        "Playboy",
        "Philanthrophist",
        'Super Powers',
        'Agility',
        'Changing Armor',
        'Cold Resistance',
        'Durability',
        'Energy Beams',
        'Energy Blasts',
        'Enhanced Condition',
        'Fire Resistance',
        'Flight',
        'Gadget Usage',
        'Hacking',
        'Heat Resistance',
        'Indomitable Will',
        'Information Analysis',
        'Intelligence',
        'Jump',
        'Levitation',
        'Marksmanship',
        'Master Martial Artist',
        'Master Tactician',
        'Power Suit',
        'Preparation',
        'Reflexes',
        'Robotic Engineering',
        'Scanning',
        'Stamina',
        'Stealth',
        'Super Speed',
        'Super Strength',
        'Vision - Heat',
        'Vision - Infrared',
        'Vision - Microscopic',
        'Vision - Night',
        'Vision - Telescopic',
        'Vision - Thermal',
        'Weapon-Based Powers',
        'Weapons Master',
        'Acrobatics',
        'Adaptation',
        'Attack Reflection',
        'Damage Boost',
        'Danger Sense',
        'Dexterity',
        'Electricity Absorption',
        'Electricity Resistance',
        'EMP Generation',
        'Endurance',
        'Energy Absorption',
        'Energy Manipulation',
        'Energy Resistance',
        'Enhanced Hearing',
        'Enhanced Sight',
        'Explosion Manipulation',
        'Extrasensory Perception',
        'Force Fields',
        'Heat Generation',
        'Homing Attack',
        'Intuitive Aptitude',
        'Invisibility',
        'Invulnerability',
        'Laser Manipulation',
        'Light Control',
        'Magnetism',
        'Mechanical Aptitude',
        'Multilingualism',
        'Nanotechnology',
        'Radar Sense',
        'Radiation Immunity',
        'Space Survivability',
        'Spaceflight',
        'Spatial Awareness',
        'Summoning',
        'Technological Possession',
        'Technopath/Cyberpath',
        'Telepathy Resistance',
        'Underwater Breathing',
        'Vehicular Mastery',
        'Weapon Summoning',
        'Toxin And Disease Resistance']
    avenger1.weapons = [
        'Heckler & Koch USP',
        'Heckler & Koch UMP',
        'Colt MA',
        'Heckler & Koch GKV',
        'Heckler & Koch GC',
        'Heckler & Koch GK with AG',
        'SIG SG ',
        'IMI Galil MAR',
        'M Grenade Launcher',
        'ME SAW',
        'FN MB',
        'Browning MHB',
        'FN GAU- Aircraft Machine Gun',
        'MA Vulcan',
        'FGM- Javelin (Prop)',
        'BGM- TOW',
        'Mark I',
        'Flamethrower',
        'Mark II',
        'M Minigun',
        'Mark III',
        'Forearm Rocket Launcher',
        'Multiple Projectile Launcher',
        'Iron Monger',
        'Gatling Gun',
        'Rotary Rocket Launcher',
        'Golden Avenger',
        'Space Armor',
        'Hydro Armor',
        'Stealth Armor',
        'Silver Centurion Armor',
        'War Machine Armor',
        'Neuromimetic Telepresence Unit-150',
        'Modular Armor',
        'Arctic Armor',
        'Prometheum Armor',
        'Renaissance Armor',
        'Experimental Safe Armor',
        'Outer Atmospheric Armor',
        'S.K.I.N. Armor',
        'Thorbuster Armor',
        'Ablative Armor',
        'Anti-Radiation Armor',
        'High Gravity Suit',
        'Extremis Armor',
        'Battle Argonaut',
        'Hulkbuster Argonaut',
        'Subterranean Argonaut',
        'Submarine Argonaut',
        'Stealth Argonaut',
        'Hulkbuster Armor',
        'Bleeding Edge Armor',
        'Phoenix-Killer Armor',
        'Heavy Duty Armor',
        'Deep Space Armor',
        'Endo-Sym Armor',
        'Model-Prime Armor',
        'Fin Fang Foombuster Armor',
        'Nano Iron Man Armor',
        'Godkiller Armor Mk. II',
        'Godbuster Armor',
        'Ultronbuster Armor',
        'Ice Armor',
        'Virtual Armor',
        'Hulk Buster Armor'
    ]

    avenger2 = avenger(None,None,None,None)
    avenger2.made_up_name = "Captain America"
    avenger2.real_name = "Steve Rogers"
    avenger2.powers = [
        'Accelerated Development',
        'Accelerated Healing',
        'Acid Resistants',
        'Acrobatics',
        'Adaptation',
        'Agility',
        'Apathy',
        'Attack Reflection',
        'Cold Resistance',
        'Dexterity',
        'Durability',
        'Endurance',
        'Energy Resistance',
        'Enhanced Hearing',
        'Enhanced Memory',
        'Enhanced Sight',
        'Enhanced Smell',
        'Enhanced Touch',
        'Fire Resistance',
        'Gadget Usage',
        'Hacking',
        'Heat Resistance',
        'Indomitable Will',
        'Information Analysis',
        'Intelligence',
        'Intuitive Aptitude',
        'Jump',
        'Longevity',
        'Marksmanship',
        'Master Martial Artist',
        'Master Tactician',
        'Mind Control Resistance',
        'Pain Suppression',
        'Peak Human Condition',
        'Photographic Reflexes',
        'Precognition',
        'Pressure Points',
        'Radiation Immunity',
        'Reflexes',
        'Regeneration',
        'Self-Sustenance',
        'Stamina',
        'Stealth',
        'Super Speed',
        'Super Strength',
        'Telepathy Resistance',
        'Toxin And Disease Resistance',
        'Vehicular Mastery',
        'Weapon-Based Powers',
        'Weapons Master'
    ]
    avenger2.weapons = [
        'Classic Vibranium Shield',
        'World War Shield',
        'Wakandian Extendable Shield',
        'Glock 19',
        'Cosmic Cube',
        'Jarnbjorn',
        'Mjolnir'
    ]
    
    avengers_team = Avengers()
    avengers_team.add_hero(avenger1)
    avengers_team.add_hero(avenger2)
    avengers_team.add_hero(avenger3)
    avengers_team.add_hero(avenger4)
    avengers_team.make_leader(avenger1)
    
    print("Printing Bio for Iron Man:")
    avengers_team.print_details(avenger1)
    print()

    print("Avengers Roster:")
    avengers_team.print_roster()
    print()


    print("Finding Black Widow:")
    member = avengers_team.find_member("Black Widow")
    if member:
        avengers_team.print_details(member)
    print()

    print("Getting Team Leader:")
    leader = avengers_team.get_team_leader()
    if leader:
        avengers_team.print_details(leader)

main()