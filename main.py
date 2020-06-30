import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
import xml.etree.ElementTree as ET
from kivy.effects.scroll import ScrollEffect

current_god = ''
skills_num = 0
#skills_with_states = []
#double_diamonds = False
#special_int_input = False
god_class = ""

def elements_number(lista):
    number = 0
    for i in lista:
        number = number + 1
    return number
    
def approximate_number_to_int(number):
        if number - int(number) >= 0.5:
            number = int(number) + 1
            return number
        elif number - int(number) < 0.5:
            number = int(number)
            return number
            
def editar_numero_de_imagen(palabra_a_editar, nuevo_indice):
        nueva_palabra = ""
        numero_de_caracteres = 0
        numero_de_caracter = 1
        for j in palabra_a_editar:
            if numero_de_caracter != 13:
                nueva_palabra = nueva_palabra + j
            if numero_de_caracter == 13:
                nueva_palabra = nueva_palabra + nuevo_indice
                nueva_palabra = nueva_palabra + ".png"
                return nueva_palabra
            numero_de_caracter = numero_de_caracter + 1
            
def string_with_commas_to_list(string, float_or_int):
        string_to_use = string + ","
        the_list = []
        current_number_list = []
        current_number = 0
        number = 0
        j = ""
        if float_or_int == False:
            for char in string_to_use:
                if char == " ":
                    pass
                elif char != ',':
                    number = int(char)
                    current_number_list.append(number)
                elif char == ',':
                    for n in current_number_list:
                        i = str(n)
                        j = j + i
                    current_number = int(j)
                    j = ""
                    the_list.append(current_number)
                    current_number_list = []
            return the_list
        elif float_or_int == True:
            for char in string_to_use:
                if char == " ":
                    pass
                elif char != ',':
                    if char != '.':
                        number = int(char)
                        current_number_list.append(number)
                    elif char == '.':
                        current_number_list.append(char)
                elif char == ',':
                    for n in current_number_list:
                        i = str(n)
                        j = j + i
                    current_number = float(j)
                    j = ""
                    the_list.append(current_number)
                    current_number_list = []
            return the_list


#class Info_Screen(Screen):
#    pass

cidh_mode = 0
class Main_Screen(Screen):
    pass

#class god_info_Screen(Screen):
#    helptext = StringProperty('')
#    toScreen = StringProperty('')
#    def update_text(self):
#        global current_god
#        current_info_screen = "%s info" % (current_god)
#        filename = current_god + ".txt"
#        f = open(filename, "r")
#        self.helptext = f.read()
#
#        if current_god == "fafnir" or current_god == "terra":
#            self.toScreen = current_god
#        else:
#            self.toScreen = "normal god screen"

class Class_Selection_Screen(Screen):
    guardian_btn = ObjectProperty
    hunter_btn = ObjectProperty
    warrior_btn = ObjectProperty
    mage_btn = ObjectProperty
    assassin_btn = ObjectProperty

    def initialize_next_screen_and_go(self, class_selected):
        global god_class
        god_class = class_selected
        options = { "assassin": 0 , "guardian": 1, "warrior": 2,
                    "mage": 3, "hunter": 4 }
        self.manager.get_screen("god selection screen").initialize(options[class_selected])
        self.manager.current = "god selection screen"
    def reset_pages_and_go_back(self):
        global classes_pages_numbers
        classes_pages_numbers = [1, 1, 1, 1, 1]
        self.manager.current = "main screen"
class ClickableImage(ButtonBehavior, Image):
    pass
        
class_option_number = 0
classes_pages_numbers = [1, 1, 1, 1, 1]
class God_Selection_Screen(Screen):
    next_button = ObjectProperty()
    previous_button = ObjectProperty()

    guardians = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                   "cerberus", "fafnir", "ganesha", "geb", "jormungandr"
                   "khepri", "kumbhakarna", "kuzenbo", "sobek", "sylvanus",
                   "terra", "xing-tian", "ymir" ]
    hunters = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                 "chernobog", "chiron", "cupid", "hachiman",
                 "hou-yi", "izanami", "jing-wei", "medusa", "neith",
                 "rama", "skadi", "ullr", "xbalanque" ]
    warriors = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                  "erlang-shen", "guan-yu", "hercules", "king-arthur", "nike",
                  "odin", "osiris", "sun-wukong", "tyr", "vamana" ]
    mages = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
               "baron-samedi", "change", "chronos", "discordia",
               "freya", "hades", "he-bo", "hel", "hera", "isis",
               "janus", "kukulkan", "merlin", "nox", "nu-wa",
               "poseidon", "ra", "raijin", "scylla", "sol",
               "the-morrigan", "thoth", "vulcan", "zeus",
               "zhong-kui" ]
    assassins = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                   "da-ji", "fenrir", "hun-batz", "kali",
                   "loki", "mercury", "ne-zha", "nemesis", "pele",
                   "ratatoskr", "ravana", "serqet", "susano",
                   "thanatos", "thor" ]
    deleter_assassins = [ "loki", "nothing", "nothing",
                          "nothing", "nothing", "nothing",
                          "nothing", "nothing", "nothing" ]

    button_positions = [ [0.123, 0.7], [0.391, 0.7], [0.659, 0.7],
                         [0.123, 0.508], [0.391, 0.508], [0.659, 0.508],
                         [0.123, 0.316], [0.391, 0.316], [0.659, 0.316] ]
    
    list_of_lists = [assassins, guardians, warriors, mages, hunters,
                     deleter_assassins]

    btn1 = ClickableImage(pos_hint = { "x": button_positions[0][0] , "y": button_positions[0][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn2 = ClickableImage(pos_hint = { "x": button_positions[1][0] , "y": button_positions[1][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn3 = ClickableImage(pos_hint = { "x": button_positions[2][0] , "y": button_positions[2][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn4 = ClickableImage(pos_hint = { "x": button_positions[3][0] , "y": button_positions[3][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn5 = ClickableImage(pos_hint = { "x": button_positions[4][0] , "y": button_positions[4][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn6 = ClickableImage(pos_hint = { "x": button_positions[5][0] , "y": button_positions[5][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn7 = ClickableImage(pos_hint = { "x": button_positions[6][0] , "y": button_positions[6][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn8 = ClickableImage(pos_hint = { "x": button_positions[7][0] , "y": button_positions[7][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn9 = ClickableImage(pos_hint = { "x": button_positions[8][0] , "y": button_positions[8][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

    initialized = False

    def initialize(self, option):
        global classes_pages_numbers
        
        global cidh_mode
        if option == 0:
            option = 5
        
        selected_list = self.list_of_lists[option]
        if option == 5:
            page_number = 1
        else:
            page_number = classes_pages_numbers[option]
        elements_number = 0
        
        global class_option_number
        class_option_number = option
        
        for x in selected_list:
            elements_number = elements_number + 1

        number_of_pages = elements_number/9 + 1
        if elements_number == 9 or elements_number == 18 or elements_number == 27 or elements_number == 36 or elements_number == 45:
            number_of_pages = number_of_pages - 1
            
        if self.initialized == False:
            layout = FloatLayout()
            i = 0
            page_number = 1
            for button in self.buttons:
                if i == 9:
                    break
                button.source = selected_list[i] + ".png"
                button.name = selected_list[i]
                button.bind(on_press=self.go_to_combo)
                layout.add_widget(button)
                i = i + 1
            self.add_widget(layout)
            self.initialized = True
        elif self.initialized == True:
            if page_number == 1:
                i = 8
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_combo)
                    if i == 0:
                        break
                    i = i - 1
            if page_number == 2:
                i = 17
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_combo)
                    if i == 9:
                        break
                    i = i - 1
            if page_number == 3:
                i = 26
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_combo)
                    if i == 18:
                        break
                    i = i - 1
            if page_number == 4:
                i = 35
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_combo)
                    if i == 27:
                        break
                    i = i - 1

        if page_number == 1:
            self.previous_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.previous_button.pos_hint = { "x": 0.0 , "y": 0.0 }
        if page_number == number_of_pages:
            self.next_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.next_button.pos_hint = { "x": 0.8 , "y": 0.0 }
    def go_to_combo(self, btn):
        if btn.name != "nothing":
            global current_god
            current_god = btn.name
            self.manager.get_screen("combo screen").initialize()
            self.manager.current = "combo screen"
    def next_page(self):
        global classes_pages_numbers
        global class_option_number
        classes_pages_numbers[class_option_number] = classes_pages_numbers[class_option_number] + 1
        self.initialize(class_option_number)
    def previous_page(self):
        global classes_pages_numbers
        global class_option_number
        classes_pages_numbers[class_option_number] = classes_pages_numbers[class_option_number] - 1
        self.initialize(class_option_number)

selected_combo = 0
class Combo_Screen(Screen):
    combos_number = { "loki": 3 }
    initialized = 0
    def initialize(self):
        if self.initialized == 0:
            global current_god
            self.rows_number = self.combos_number[current_god]
    
            layout = FloatLayout()
            scroll = ScrollView(size_hint=(0.9, 0.75), pos_hint={"x": 0.05, "y": 0.1},
                                    effect_cls = ScrollEffect)
            grid = GridLayout( size_hint = (1,None), col_default_width = 50, row_default_height = 100,
                                   cols = 1, rows = self.rows_number )

            self.combos_images = []
            for i in range(0, self.rows_number):
                current_picture = current_god + "_combo_" + str(i + 1) + ".png"
                self.combos_images.append(Image( size_hint=(1,1), pos_hint={"x":0.0, "y":0.0},
                                                    source=current_picture, id=str(i+1), keep_ratio=False,
                                                    allow_stretch=True))
                grid.add_widget(self.combos_images[i])

            grid.bind(minimum_height=grid.setter('height'))

            scroll.add_widget(grid)
            layout.add_widget(scroll)
            self.add_widget(layout)

class Item():
    name_id = ""
    power = 0
    cost = 0

    power2 = 0
    mana = 0
    power_states = []
    mana_states = []
    ba_flat_buff = 0
    ba_flat_buff_states = []
    mana_to_power_percent = []
    can_change = []
    mana_to_power_percent = 0
    mages_blessing_buff = 0
    hydras_multiplier_buff = 0
    hydras_affected_bas = 0
    hydras_affected_bas_states = []
    heartseeker_buff = 0
    heartseeker_states = []
    crusher_flat_buff = 0
    crusher_buff_based_on_power = 0
    poly_buff_based_on_power = 0
    polys_affected_bas = 0
    polys_affected_bas_states = []
    p_prot = 0
    p_prot_states = []
    power_per_charge = 0
    mana_per_charge = 0
    penetration = 0
    penetration_states = []
    percent_penetration = 0
    percent_penetration_protections_scaling = []
    max_percent_penetration = 0
    executioner_reduction = 0
    qins_bonus = 0
    qins_health_scaling = []
    qins_max_bonus = 0
    crit_chance = 0
    crit_chance_states = []
    malice_bonus = 0
    scs_bonus = 0
    aura_penetration = 0
    percent_pen_per_prot = 0
    percent_hp_per_hp = 0
    total_damage_buff_percent_against_gods = 0
    total_damage_buff = 0
    current_health_true_damage = 0
    health = 0
    
    state = 1
    max_state = 1
    
    def __init__(self, name_id_p, power_p, cost_p):
        self.name_id = name_id_p
        self.power = power_p
        self.cost = cost_p
    def update_power(self):
        self.power = self.power_states[self.state - 1]
    def update_mana(self):
        self.mana = self.mana_states[self.state - 1]
    def update_mana_to_power_percent(self):
        self.mana_to_power_percent = self.mana_to_power_percent_states[self.state - 1]
    def update_ba_flat_buff(self):
        self.ba_flat_buff = self.ba_flat_buff_states[self.state - 1]
    def update_hydras_affected_bas(self):
        self.hydras_affected_bas = self.hydras_affected_bas_states[self.state - 1]
    def update_heartseeker_buff(self):
        self.heartseeker_buff = self.heartseeker_buff_states[self.state - 1]
    def update_polys_affected_bas(self):
        self.polys_affected_bas = self.polys_affected_bas_states[self.state - 1]
    def update_p_prot(self):
        self.p_prot = self.p_prot_states[self.state - 1]
    def update_penetration(self):
        self.penetration = self.penetration_states[self.state - 1]
    def update_crit_chance(self):
        self.crit_chance = self.crit_chance_states[self.state - 1]


attackers_blessing = Item("x_sta1_1", 20, 700)
attackers_blessing.power2 = 25
attackers_blessing.max_state = 2
attackers_blessing.penetration_states = [0, 10]
attackers_blessing.can_change = ["penetration"]
mages_blessing = Item("x_sta2", 10, 700)
mages_blessing.power2 = 20
mages_blessing.mages_blessing_buff = 10
hunters_blessing = Item("x_sta3_1", 0, 700)
hunters_blessing.ba_flat_buff = 15
hunters_blessing.max_state = 2
hunters_blessing.ba_flat_buff_states = [15, 30]
hunters_blessing.can_change = ["ba_flat_buff"]
assassins_blessing = Item("x_sta4_1", 0, 0)
assassins_blessing.max_state = 2
assassins_blessing.penetration_states = [0, 5]

mask = Item("x_mas1", 0, 500)
mask.mana = 50
mask.health = 50
messengers_mask = Item("x_mas3", 10, 1200)
bumbas_mask = Item("x_mas5", 30, 2500)
bumbas_mask.total_damage_debuff = 0.1
lonos_mask = Item("x_mas6", 0, 2300)
lonos_mask.total_damage_debuff = 0.25

potion_of_physical_might = Item("p_pot1", 30, 500)
potion_of_physical_might.ability_damage_buff_based_on_power = 0.15
elixir_of_power = Item("x_eli1", 0, 3000)
elixir_of_power.power_buff_percent = 0.25
damage_camp_buff = Item("x_buf1", 5, 0) #hay que considerar el campamento de dano de justa
damage_camp_buff.power2 = 10
damage_camp_buff.total_damage_buff_percent = 0.1
damage_camp_buff.total_damage_buff_percent_against_gods = 0.15

frenzy = Item("x_rel1", 0, 0)
frenzy.total_damage_buff = 1.1
frenzy_upgraded = Item("x_rel2", 0, 0)
frenzy_upgraded.total_damage_buff = 1.1
frenzy_upgraded.penetration = 10
sunder = Item("x_rel3", 0, 0)
sunder.current_health_true_damage = 0.15
sunder_upgraded = Item("x_rel4", 0, 0)
sunder_upgraded.current_health_true_damage = 0.15
sunder_upgraded.total_damage_buff = 1.2

breastplate = Item("d_bre1", 0, 600)
breastplate.p_prot = 20
silver_breastplate = Item("d_bre2", 0, 1050)
silver_breastplate.mana = 200
silver_breastplate.p_prot = 35
hide_of_the_nemean_lion = Item("d_bre3", 0, 2200)
hide_of_the_nemean_lion.mana = 200
hide_of_the_nemean_lion.p_prot = 70
breastplate_of_valor = Item("d_bre4", 0, 2300)
breastplate_of_valor.mana = 300
breastplate_of_valor.p_prot = 65
spectral_armor = Item("d_bre5", 0, 2100)
spectral_armor.mana = 300
spectral_armor.p_prot = 70

cloak = Item("d_clo1", 0, 650)
cloak.p_prot = 10
cloak_of_concentration = Item("d_clo2", 0, 1500)
cloak_of_concentration.p_prot = 30
spirit_robe = Item("d_clo3", 0, 2500)
spirit_robe.p_prot = 40
mantle_of_discord = Item("d_clo4", 0, 2900)
mantle_of_discord.p_prot = 60
clerics_cloak = Item("d_clo5", 0, 1150)
clerics_cloak.p_prot = 10
clerics_cloak.health = 200
magis_cloak = Item("d_clo6", 0, 2150)
magis_cloak.p_prot = 15
magis_cloak.health = 300
armored_cloak = Item("d_clo7", 0, 1550)
armored_cloak.mana = 125
armored_cloak.health = 125
armored_cloak.p_prot = 25
hide_of_the_urchin = Item("d_clo8", 0, 2450)
hide_of_the_urchin.mana = 250
hide_of_the_urchin.health = 250
hide_of_the_urchin.p_prot = 30
hide_of_the_urchin.can_change = ["p_prot"]
hide_of_the_urchin.p_prot_states = [30, 51]
hide_of_the_urchin.max_state = 2

gauntlet_of_thebes = Item("d_glo1", 0, 2400)
gauntlet_of_thebes.health = 200
gauntlet_of_thebes.can_change = ["p_prot"]
gauntlet_of_thebes.p_prot_states = [0, 60]
gauntlet_of_thebes.max_state = 2

iron_mail = Item("d_mai1", 0, 650)
iron_mail.p_prot = 10
iron_mail.health = 75
steel_mail = Item("d_mai2", 0, 1400)
steel_mail.p_prot = 20
steel_mail.health = 200
sovereignty = Item("d_mai3", 0, 2100)
sovereignty.p_prot = 60
sovereignty.health = 250
mystical_mail = Item("d_mai4", 0, 2700)
mystical_mail.p_prot = 40
mystical_mail.health = 300
midgardian_mail = Item("d_mai5", 0, 2300)
midgardian_mail.p_prot = 40
midgardian_mail.health = 300
emperors_armor = Item("d_mai6", 0, 2000)
emperors_armor.p_prot = 40
emperors_armor.health = 250

combat_boots = Item("p_boo1", 10, 900)
warrior_tabi = Item("p_boo2", 40, 1600)
ninja_tabi = Item("p_boo3", 20, 1550)
ninja_tabi.mana = 100
reinforced_greaves = Item("p_boo4", 10, 1550)
reinforced_greaves.health = 100
talaria_boots = Item("p_boo5", 20, 1600)

morningstar = Item("p_mor1", 10, 550)
charged_morningstar = Item("p_mor2", 20, 1200)
charged_morningstar.mana = 150
transcendence = Item("p_mor3", 35, 2600)
transcendence.mana = 300
transcendence.mana_per_charge = 15
transcendence.mana_to_power_percent = 0.03
transcendence.max_state = 4
transcendence.mana_states = [300, (300 + transcendence.mana_per_charge * 20), (300 + transcendence.mana_per_charge * 40), (300 + transcendence.mana_per_charge * 50)]
transcendence.can_change = ["mana"]
hydras_star = Item("p_mor4", 20, 1200)
hydras_star.hydras_multiplier_buff = 1.1
hydras_lament = Item("p_mor5", 40, 2150)
hydras_lament.hydras_multiplier_buff = 1.5
heartseeker = Item("p_kat4", 30, 2300)
heartseeker.mana = 200
heartseeker.max_state = 2
heartseeker.heartseeker_buff = 0.0
heartseeker.heartseeker_buff_states = [0.0, 0.8]
heartseeker.penetration = 10
    
mace = Item("p_mac1", 15, 700)
heavy_mace = Item("p_mac2", 25, 1550)
heavy_mace.penetration = 10
brawlers_beat_stick = Item("p_mac3", 40, 2350)
brawlers_beat_stick.penetration = 15
jotunns_wrath = Item("p_mac4", 40, 2350)
jotunns_wrath.mana = 150
jotunns_wrath.penetration = 10
the_crusher = Item("p_mac5", 30, 2400)
the_crusher.crusher_flat_buff = 20
the_crusher.crusher_buff_based_on_power = 0.15
the_crusher.penetration = 15
warriors_bane = Item("p_mac6", 20, 1500)
warriors_bane.percent_penetration = 0.15
titans_bane = Item("p_mac7", 30, 2300)
titans_bane.percent_penetration = 0.15
titans_bane.max_percent_penetration = 0.4
titans_bane.percent_penetration_protections_scaling = [65, 200]
titans_bane.percent_pen_per_prot = (titans_bane.max_percent_penetration - titans_bane.percent_penetration)/(titans_bane.percent_penetration_protections_scaling[1] - titans_bane.percent_penetration_protections_scaling[0])

balanced_blade = Item("p_lig1", 15, 1250)
the_executioner = Item("p_lig2", 30, 2350)
the_executioner.executioner_reduction = 0.12
qins_sais = Item("p_lig3", 40, 2700)
qins_sais.qins_bonus = 0.03
qins_sais.qins_max_bonus = 0.05
qins_sais.qins_health_scaling = [2000, 2750]
qins_sais.percent_hp_per_hp = (qins_sais.qins_max_bonus - qins_sais.qins_bonus)/(qins_sais.qins_health_scaling[1] - qins_sais.qins_health_scaling[0])
asi = Item("p_lig4", 0, 0)
asi.penetration = 10

hidden_dagger = Item("p_hid1", 10, 700)
hidden_dagger.crit_chance = 0.05
short_sword = Item("p_hid2", 20, 1500)
short_sword.crit_chance = 0.1
deathbringer = Item("p_hid3", 40, 3000)
deathbringer.crit_chance = 0.25
deathbringer.db_crit_bonus = 0.3
rage = Item("p_hid4", 20, 2400)
rage.crit_chance = 0.3
rage.can_change = ["crit_chance"]
rage.crit_chance_states = [0.3, 0.32, 0.34, 0.36, 0.38, 0.4]
malice = Item("p_hid5", 40, 3000)
malice.crit_chance = 0.25
malice.malice_bonus = 0.35

shuriken = Item("p_shu1", 10, 650)
eight_pointed_shuriken = Item("p_shu2", 15, 1500)
eight_pointed_shuriken.crit_chance = 0.1
poisoned_star = Item("p_shu3", 20, 2400)
poisoned_star.crit_chance = 0.2
wind_demon = Item("p_shu4", 30, 2700)
wind_demon.crit_chance = 0.2

spiked_gauntlet = Item("p_spi1", 5, 600)
cursed_gauntlet = Item("p_spi2", 20, 1400)
devourers_gauntlet = Item("p_spi3", 30, 2300)
devourers_gauntlet.power_per_charge = 0.5
devourers_gauntlet.max_state = 4
devourers_gauntlet.power_states = [30, (30 + devourers_gauntlet.power_per_charge * 25),
                                       (30 + devourers_gauntlet.power_per_charge * 50), (30 + devourers_gauntlet.power_per_charge * 70)]
devourers_gauntlet.can_change = ["power"]
bloodforge = Item("p_spi4", 75, 2800)
bound_gauntlet = Item("p_spi5", 15, 1050)
bound_gauntlet.mana = 75
soul_eater = Item("p_spi6", 40, 2300)
soul_eater.mana = 200
soul_eater.max_state = 2
soul_eater.power_states = [40, 60]
soul_eater.can_change = ["power"]

katana = Item("p_kat1", 10, 700)
thousand_fold_blade = Item("p_kat2", 20, 1300)
hastened_katana = Item("p_kat3", 25, 2200)
stone_cutting_sword = Item("p_kat5", 50, 2500)
stone_cutting_sword.scs_bonus = 10
masamune = Item("p_kat6", 50, 2500)
masamune.health = 100
golden_blade = Item("p_kat7", 30, 2200)

round_shield = Item("p_rou1", 10, 650)
round_shield.p_prot = 5
spiked_shield = Item("p_rou2", 20, 1600)
spiked_shield.p_prot = 30
spiked_shield.aura_penetration = 8
void_shield = Item("p_rou3", 20, 2600)
void_shield.p_prot = 50
void_shield.aura_penetration = 20
tower_shield = Item("p_rou4", 20, 1150)
tower_shield.p_prot = 15
shifters_shield = Item("p_rou5", 70, 2400)
shifters_shield.p_prot = 15
shifters_shield.can_change = ["power", "p_prot"]
shifters_shield.max_state = 2
shifters_shield.power_states = [70, 35] 
shifters_shield.p_prot_states = [15, 50]
gladiators_shield = Item("p_rou6", 20, 1700)
gladiators_shield.p_prot = 30
berserkers_shield = Item("p_rou7", 25, 1050)
berserkers_shield.p_prot = 15

enchanted_buckler = Item("p_enc1", 10, 650)
warded_shield = Item("p_enc2", 15, 1400)
runic_shield = Item("p_enc3", 35, 2150)
ancile = Item("p_enc4", 40, 2000)

hunters_bow = Item("p_bow1", 10, 1200)
atalantas_bow = Item("p_bow2", 30, 2200)
silverbranch_bow = Item("p_bow3", 30, 2200)
silverbranch_bow.penetration = 10
ichaival = Item("p_bow4", 0, 0)
ichaival.penetration = 10

cudgel = Item("p_cud1", 10, 650)
heavy_hammer = Item("p_cud2", 20, 1350)
frostbound_hammer = Item("p_cud3", 25, 2300)
runeforged_hammer = Item("p_cud4", 40, 2300)
runeforged_hammer.runeforged_bonus = 0.15
shillelagh = Item("p_cud5", 15, 1500)
shillelagh.mana = 100
blackthorn_hammer = Item("p_cud6", 35, 2200)
blackthorn_hammer.mana = 200

toxic_blade = Item("x_bla1", 0, 0)
toxic_blade.penetration = 15


magic_shoes = Item("m_sho1", 20, 900)
shoes_of_the_magi = Item("m_sho2", 55, 1600)
shoes_of_focus = Item("m_sho3", 55, 1550)
shoes_of_focus.mana = 250
reinforced_shoes = Item("m_sho4", 20, 1550)
travelers_shoes = Item("m_sho5", 25, 1600)

spellbook = Item("m_spe1", 20, 650)
book_of_souls = Item("m_spe2", 65, 1350)
book_of_souls.mana = 125
book_of_thoth = Item("m_spe3", 80, 2800)
book_of_thoth.mana = 250
book_of_thoth.mana_per_charge = 10
book_of_thoth.mana_to_power_percent = 0.03
book_of_thoth.max_state = 4
book_of_thoth.mana_states = [250, (250 + book_of_thoth.mana_per_charge * 25),
                                 (250 + book_of_thoth.mana_per_charge * 50), (250 + book_of_thoth.mana_per_charge * 75)]
book_of_thoth.mana_to_power_percent_states = [0.03, 0.03, 0.03, 0.05]
book_of_thoth.can_change = ["mana", "mana_to_power_percent"]
polynomicon = Item("m_spe4", 75, 2300)
polynomicon.mana = 300
polynomicon.poly_buff_based_on_power = 0.75
polynomicon.polys_affected_bas = 0
polynomicon.max_state = 4
polynomicon.polys_affected_bas_states = [0, 1, 2, 3]
polynomicon.can_change = ["polys_affected_bas"]
    #polynomicon.lifesteal = 0.12
soul_reaver = Item("m_spe5", 130, 2750)
soul_reaver.mana = 300
book_of_the_dead = Item("m_spe6", 100, 2600)
book_of_the_dead.mana = 200

magic_focus = Item("m_foc1", 25, 650)
enchanted_spear = Item("m_foc2", 30, 1400)
divine_ruin = Item("m_foc3", 80, 2300)
spear_of_the_magus = Item("m_foc4", 65, 2300)
spear_of_desolation = Item("m_foc5", 100, 2600)
spell_focus = Item("m_foc6", 45, 1500)
obsidian_shard = Item("m_foc7", 60, 2150)
    
uncommon_staff = Item("m_unc1", 15, 650)
fortified_scepter = Item("m_unc2", 50, 1350)
gem_of_isolation = Item("m_unc3", 90, 2700)
ethereal_staff = Item("m_unc4", 90, 2700)
rod_of_healing = Item("m_unc5", 45, 1500)
rod_of_asclepius = Item("m_unc6", 90, 2600)
sorcerers_staff = Item("m_unc7", 30, 1350)
sorcerers_staff.mana = 100
warlocks_staff = Item("m_unc8", 65, 2650)
warlocks_staff.mana = 200
warlocks_staff.power_per_charge = 0.5
warlocks_staff.max_state = 4
warlocks_staff.power_states = [65, (65 + warlocks_staff.power_per_charge * 40),
                                   (65 + warlocks_staff.power_per_charge * 80), (65 + warlocks_staff.power_per_charge * 100)]
warlocks_staff.can_change = ["power"]

tiny_trinket = Item("m_tin1", 20, 550)
    #tiny_trinket.lifesteal = 0.06
talon_trinket = Item("m_tin2", 60, 1400)
talon_trinket.mana = 100
    #talon_trinket.lifesteal = 0.08
bancrofts_talon = Item("m_tin3", 100, 2500)
bancrofts_talon.mana = 150
    #bancrofts_talon.lifesteal = 0.15
bancrofts_talon.max_state = 4
bancrofts_talon.power_states = [ 100, 125, 150, 200 ]
bancrofts_talon.can_change = ["power"]
typhons_fang = Item("m_tin4", 80, 2800)
typhons_fang.mana = 200
    #typhons_fang.lifesteal = 0.1
enchanted_trinket = Item("m_tin5", 30, 1100)
    #enchanted_trinket.lifesteal = 0.12
soul_gem = Item("m_tin6", 65, 2300)
    #soul_gem.lifesteal = 0.12
    #soul_gem.max_state = 2
    #soul_gem.extra_power_based_damage_percent = 0.3
pythagorems_piece = Item("m_tin7", 70, 2300)
    #pythagorems_piece.lifesteal = 0.24

lost_artifact = Item("m_los1", 20, 550)
restored_artifact = Item("m_los2", 50, 1600)
rod_of_tahuti = Item("m_los3", 150, 300)
chronos_pendant = Item("m_los4", 90, 2800)
doom_orb = Item("m_los5", 70, 1700)
doom_orb.mana = 200
    

emerald_ring = Item("m_eme1", 20, 600)
enchanted_ring = Item("m_eme2", 45, 1200)
demonic_grip = Item("m_eme3", 65, 2150)
hastened_ring = Item("m_eme4", 50, 2300)
shamans_ring = Item("m_eme5", 100, 2400)
    #shamans_ring.max_state = 2
telkhines_ring = Item("m_eme6", 90, 2700)
    #telkhines_ring.basic_attacks_buff = 10
    #telkhines_ring.basic_attacks_buff_based_on_power = 0.1

imperial_helmet = Item("m_imp1", 10, 600)
jade_mountain_helm = Item("m_imp2", 20, 1200)
celestial_legion_helm = Item("m_imp3", 60, 2050)
jade_emperors_crown = Item("m_imp4", 20, 2150)
lotus_crown = Item("m_imp5", 30, 2050)
dinasty_plate_helm = Item("m_imp6", 45, 1700)

druid_stone = Item("m_dru1", 10, 600)
ward_stone = Item("m_dru2", 20, 1350)
void_stone = Item("m_dru3", 20, 2150)
sages_stone = Item("m_dru4", 40, 1400)
stone_of_fal = Item("m_dru5", 70, 2300)
stone_of_binding = Item("m_dru6", 20, 1700)

nothing = Item("nothing", 0, 0) # Items definitions

item_objects = { "nothing.png": nothing,
                     "item_x_sta1_1.png": attackers_blessing, "item_x_sta2.png": mages_blessing,
                     "item_x_sta3_1.png": hunters_blessing, "item_x_sta4_1.png": assassins_blessing,
                     #"item_x_mas1.png": fighters_mask, "item_x_mas2.png": messengers_mask,
                     #"item_x_mas3.png": rangdas_mask, "item_x_mas4.png": lonos_mask,
                     #"item_x_mas5.png": bumbas_mask,

                     #"item_p_pot1.png": potion_of_physical_might, "item_m_pot1.png": potion_of_magical_might,
                     #"item_x_eli1.png": elixir_of_power, "item_x_buf1.png": damage_camp_buff,
                     #"item_x_buf2.png": attack_speed_camp_buff, "item_x_buf3.png": shadow_of_apophis,
                     #"item_x_buf4.png": fire_giants_might,

                     "item_d_bre1.png": breastplate, "item_d_bre2.png": silver_breastplate,
                     "item_d_bre3.png": hide_of_the_nemean_lion, "item_d_bre4.png": breastplate_of_valor,
                     "item_d_bre5.png": spectral_armor,
                     "item_d_clo1.png": cloak, "item_d_clo2.png": cloak_of_concentration,
                     "item_d_clo3.png": spirit_robe, "item_d_clo4.png": mantle_of_discord,
                     "item_d_clo5.png": clerics_cloak, "item_d_clo6.png": magis_cloak,
                     "item_d_clo7.png": armored_cloak, "item_d_clo8_1.png": hide_of_the_urchin,
                     "item_d_glo1_1.png": gauntlet_of_thebes,
                     "item_d_mai1.png": iron_mail, "item_d_mai2.png": steel_mail,
                     "item_d_mai3.png": sovereignty, "item_d_mai4.png": mystical_mail,
                     "item_d_mai5.png": midgardian_mail, "item_d_mai6.png": emperors_armor,

                     "item_p_boo1.png": combat_boots, "item_p_boo2.png": warrior_tabi,
                     "item_p_boo3.png": ninja_tabi, "item_p_boo4.png": reinforced_greaves,
                     "item_p_boo5.png": talaria_boots,
                     "item_p_mor1.png": morningstar, "item_p_mor2.png": charged_morningstar,
                     "item_p_mor3_1.png": transcendence, "item_p_mor4_1.png": hydras_star,
                     "item_p_mor5_1.png": hydras_lament,
                     "item_p_mac1.png": mace, "item_p_mac2.png": heavy_mace,
                     "item_p_mac3.png": brawlers_beat_stick, "item_p_mac4.png": jotunns_wrath,
                     "item_p_mac5.png": the_crusher, "item_p_mac6.png": warriors_bane,
                     "item_p_mac7.png": titans_bane,
                     "item_p_lig1.png": balanced_blade, "item_p_lig2.png": the_executioner,
                     "item_p_lig3.png": qins_sais, "item_p_lig4.png": asi,
                     "item_p_hid1.png": hidden_dagger, "item_p_hid2.png": short_sword,
                     "item_p_hid3.png": deathbringer, "item_p_hid4.png": rage,
                     "item_p_hid5.png": malice,
                     "item_p_shu1.png": shuriken, "item_p_shu2.png": eight_pointed_shuriken,
                     "item_p_shu3.png": poisoned_star, "item_p_shu4.png": wind_demon,
                     "item_p_spi1.png": spiked_gauntlet, "item_p_spi2.png": cursed_gauntlet,
                     "item_p_spi3_1.png": devourers_gauntlet, "item_p_spi4.png": bloodforge,
                     "item_p_spi5.png": bound_gauntlet,  "item_p_spi6_1.png": soul_eater,
                     "item_p_kat1.png": katana, "item_p_kat2.png": thousand_fold_blade,
                     "item_p_kat3.png": hastened_katana, "item_p_kat4_1.png": heartseeker,
                     "item_p_kat5.png": stone_cutting_sword, "item_p_kat6.png": masamune,
                     "item_p_kat7.png": golden_blade,
                     "item_p_rou1.png": round_shield, "item_p_rou2.png": spiked_shield,
                     "item_p_rou3.png": void_shield, "item_p_rou4.png": tower_shield,
                     "item_p_rou5_1.png": shifters_shield, "item_p_rou6.png": gladiators_shield,
                     "item_p_rou7.png": berserkers_shield,
                     "item_p_enc1.png": enchanted_buckler, "item_p_enc2.png": warded_shield,
                     "item_p_enc3.png": runic_shield, "item_p_enc4.png": ancile,
                     "item_p_bow1.png": hunters_bow, "item_p_bow2.png": atalantas_bow,
                     "item_p_bow3.png": silverbranch_bow,
                     "item_p_cud1.png": cudgel, "item_p_cud2.png": heavy_hammer,
                     "item_p_cud3.png": frostbound_hammer, "item_p_cud4.png": runeforged_hammer,
                     "item_p_cud5.png": shillelagh, "item_p_cud6.png": blackthorn_hammer,
                     
                     "item_m_sho1.png": magic_shoes, "item_m_sho2.png": shoes_of_the_magi,
                     "item_m_sho3.png": shoes_of_focus, "item_m_sho4.png": reinforced_shoes,
                     "item_m_sho5.png": travelers_shoes,
                     "item_m_spe1.png": spellbook, "item_m_spe2.png": book_of_souls,
                     "item_m_spe3_1.png": book_of_thoth, "item_m_spe4_1.png": polynomicon,
                     "item_m_spe5.png": soul_reaver, "item_m_spe6.png": book_of_the_dead,
                     "item_m_foc1.png": magic_focus, "item_m_foc2.png": enchanted_spear,
                     "item_m_foc3.png": divine_ruin, "item_m_foc4.png": spear_of_the_magus,
                     "item_m_foc5.png": spear_of_desolation, "item_m_foc6.png": spell_focus,
                     "item_m_foc7.png": obsidian_shard,
                     "item_m_unc1.png": uncommon_staff, "item_m_unc2.png": fortified_scepter,
                     "item_m_unc3.png": gem_of_isolation, "item_m_unc4.png": ethereal_staff,
                     "item_m_unc5.png": rod_of_healing, "item_m_unc6.png": rod_of_asclepius,
                     "item_m_unc7.png": sorcerers_staff, "item_m_unc8_1.png": warlocks_staff,
                     "item_m_tin1.png": tiny_trinket, "item_m_tin2.png": talon_trinket,
                     "item_m_tin3_1.png": bancrofts_talon, "item_m_tin4.png": typhons_fang,
                     "item_m_tin5.png": enchanted_trinket, "item_m_tin6_1.png": soul_gem,
                     "item_m_tin7.png": pythagorems_piece,
                     "item_m_los1.png": lost_artifact, "item_m_los2.png": restored_artifact,
                     "item_m_los3.png": rod_of_tahuti, "item_m_los4.png": chronos_pendant,
                     "item_m_los5.png": doom_orb,
                     "item_m_eme1.png": emerald_ring, "item_m_eme2.png": enchanted_ring,
                     "item_m_eme3.png": demonic_grip, "item_m_eme4.png": hastened_ring,
                     "item_m_eme5_1.png": shamans_ring, "item_m_eme6.png": telkhines_ring,
                     "item_m_imp1.png": imperial_helmet, "item_m_imp2.png": jade_mountain_helm,
                     "item_m_imp3.png": celestial_legion_helm, "item_m_imp4.png": jade_emperors_crown,
                     "item_m_imp5.png": lotus_crown, "item_m_imp6.png": dinasty_plate_helm,
                     "item_m_dru1.png": druid_stone, "item_m_dru2.png": ward_stone,
                     "item_m_dru3.png": void_stone, "item_m_dru4.png": sages_stone,
                     "item_m_dru5.png": stone_of_fal, "item_m_dru6.png": stone_of_binding }
items_trees = { "d_bre2": ["item_d_bre1.png", "item_d_bre2.png"],
                "d_bre3": ["item_d_bre1.png", "item_d_bre2.png", "item_d_bre3.png"],
                "d_bre4": ["item_d_bre1.png", "item_d_bre2.png", "item_d_bre4.png"],
                "d_bre5": ["item_d_bre1.png", "item_d_bre2.png", "item_d_bre5.png"],
                "d_clo2": ["item_d_clo1.png", "item_d_clo2.png"],
                "d_clo3": ["item_d_clo1.png", "item_d_clo2.png", "item_d_clo3.png"],
                "d_clo4": ["item_d_clo1.png", "item_d_clo2.png", "item_d_clo4.png"],
                "d_clo5": ["item_d_clo1.png", "item_d_clo5.png"],
                "d_clo6": ["item_d_clo1.png", "item_d_clo5.png", "item_d_clo6.png"],
                "d_clo7": ["item_d_clo1.png", "item_d_clo7.png"],
                "d_clo8": ["item_d_clo1.png", "item_d_clo7.png", "item_d_clo8_1.png"],
                "d_mai2": ["item_d_mai1.png", "item_d_mai2.png"],
                "d_mai3": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai3.png"],
                "d_mai4": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai4.png"],
                "d_mai5": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai5.png"],
                "d_mai6": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai6.png"],
                "p_aco2": ["item_p_aco1.png", "item_p_aco2.png"],
                "p_boo2": ["item_p_boo1.png", "item_p_boo2.png"],
                "p_boo3": ["item_p_boo1.png", "item_p_boo3.png"],
                "p_boo4": ["item_p_boo1.png", "item_p_boo4.png"],
                "p_boo5": ["item_p_boo1.png", "item_p_boo5.png"],
                "p_mor2": ["item_p_mor1.png", "item_p_mor2.png"],
                "p_mor3": ["item_p_mor1.png", "item_p_mor2.png", "item_p_mor3_1.png"],
                "p_mor4": ["item_p_mor1.png", "item_p_mor4_1.png"],
                "p_mor5": ["item_p_mor1.png", "item_p_mor4_1.png", "item_p_mor5_1.png"],
                "p_mac2": ["item_p_mac1.png", "item_p_mac2.png"],
                "p_mac3": ["item_p_mac1.png", "item_p_mac2.png", "item_p_mac3.png"],
                "p_mac4": ["item_p_mac1.png", "item_p_mac2.png", "item_p_mac4.png"],
                "p_mac5": ["item_p_mac1.png", "item_p_mac2.png", "item_p_mac5.png"],
                "p_mac6": ["item_p_mac1.png", "item_p_mac6.png"],
                "p_mac7": ["item_p_mac1.png", "item_p_mac6.png", "item_p_mac7.png"],
                "p_lig2": ["item_p_lig1.png", "item_p_lig2.png"],
                "p_lig3": ["item_p_lig1.png", "item_p_lig3.png"],
                "p_hid2": ["item_p_hid1.png", "item_p_hid2.png"],
                "p_hid3": ["item_p_hid1.png", "item_p_hid2.png", "item_p_hid3.png"],
                "p_hid4": ["item_p_hid1.png", "item_p_hid2.png", "item_p_hid4.png"],
                "p_hid5": ["item_p_hid1.png", "item_p_hid2.png", "item_p_hid5.png"],
                "p_shu2": ["item_p_shu1.png", "item_p_shu2.png"],
                "p_shu3": ["item_p_shu1.png", "item_p_shu2.png", "item_p_shu3.png"],
                "p_shu4": ["item_p_shu1.png", "item_p_shu2.png", "item_p_shu4.png"],
                "p_spi2": ["item_p_spi1.png", "item_p_spi2.png"],
                "p_spi3": ["item_p_spi1.png", "item_p_spi2.png", "item_p_spi3_1.png"],
                "p_spi4": ["item_p_spi1.png", "item_p_spi2.png", "item_p_spi4.png"],
                "p_spi5": ["item_p_spi1.png", "item_p_spi5.png"],
                "p_spi6": ["item_p_spi1.png", "item_p_spi5.png", "item_p_spi6_1.png"],
                "p_kat2": ["item_p_kat1.png", "item_p_kat2.png"],
                "p_kat3": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat3.png"],
                "p_kat4": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat4_1.png"],
                "p_kat5": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat5.png"],
                "p_kat6": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat6.png"],
                "p_kat7": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat7.png"],
                "p_rou2": ["item_p_rou1.png", "item_p_rou2.png"],
                "p_rou3": ["item_p_rou1.png", "item_p_rou2.png", "item_p_rou3.png"],
                "p_rou4": ["item_p_rou1.png", "item_p_rou4.png"],
                "p_rou5": ["item_p_rou1.png", "item_p_rou4.png", "item_p_rou5_1.png"],
                "p_rou6": ["item_p_rou1.png", "item_p_rou6.png"],
                "p_rou7": ["item_p_rou1.png", "item_p_rou7.png"],
                "p_enc2": ["item_p_enc1.png", "item_p_enc2.png"],
                "p_enc3": ["item_p_enc1.png", "item_p_enc2.png", "item_p_enc3.png"],
                "p_enc4": ["item_p_enc1.png", "item_p_enc4.png"],
                "p_bow2": ["item_p_bow1.png", "item_p_bow2.png"],
                "p_bow3": ["item_p_bow1.png", "item_p_bow3.png"],
                "p_cud2": ["item_p_cud1.png", "item_p_cud2.png"],
                "p_cud3": ["item_p_cud1.png", "item_p_cud2.png", "item_p_cud3.png"],
                "p_cud4": ["item_p_cud1.png", "item_p_cud2.png", "item_p_cud4.png"],
                "p_cud5": ["item_p_cud1.png", "item_p_cud5.png"],
                "p_cud6": ["item_p_cud1.png", "item_p_cud5.png", "item_p_cud6.png"],
                "m_sho2": ["item_m_sho1.png", "item_m_sho2.png"],
                "m_sho3": ["item_m_sho1.png", "item_m_sho3.png"],
                "m_sho4": ["item_m_sho1.png", "item_m_sho4.png"],
                "m_sho5": ["item_m_sho1.png", "item_m_sho5.png"],
                "m_spe2": ["item_m_spe1.png", "item_m_spe2.png"],
                "m_spe3": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe3.png"],
                "m_spe4": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe4.png"],
                "m_spe5": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe5.png"],
                "m_spe6": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe6.png"],
                "m_foc2": ["item_m_foc1.png", "item_m_foc2.png"],
                "m_foc3": ["item_m_foc1.png", "item_m_foc2.png", "item_m_foc3.png"],
                "m_foc4": ["item_m_foc1.png", "item_m_foc2.png", "item_m_foc4.png"],
                "m_foc5": ["item_m_foc1.png", "item_m_foc2.png", "item_m_foc5.png"],
                "m_foc6": ["item_m_foc1.png", "item_m_foc6.png"],
                "m_foc7": ["item_m_foc1.png", "item_m_foc6.png", "item_m_foc7.png"],
                "m_unc2": ["item_m_unc1.png", "item_m_unc2.png"],
                "m_unc3": ["item_m_unc1.png", "item_m_unc2.png", "item_m_unc3.png"],
                "m_unc4": ["item_m_unc1.png", "item_m_unc2.png", "item_m_unc4.png"],
                "m_unc5": ["item_m_unc1.png", "item_m_unc5.png"],
                "m_unc6": ["item_m_unc1.png", "item_m_unc5.png", "item_m_unc6.png"],
                "m_unc7": ["item_m_unc1.png", "item_m_unc7.png"],
                "m_unc8": ["item_m_unc1.png", "item_m_unc7.png", "item_m_unc8_1.png"],
                "m_tin2": ["item_m_tin1.png", "item_m_tin2.png"],
                "m_tin3": ["item_m_tin1.png", "item_m_tin2.png", "item_m_tin3_1.png"],
                "m_tin4": ["item_m_tin1.png", "item_m_tin2.png", "item_m_tin4.png"],
                "m_tin5": ["item_m_tin1.png", "item_m_tin5.png"],
                "m_tin6": ["item_m_tin1.png", "item_m_tin6_1.png"],
                "m_tin7": ["item_m_tin1.png", "item_m_tin7.png"],
                "m_los2": ["item_m_los1.png", "item_m_los2.png"],
                "m_los3": ["item_m_los1.png", "item_m_los2.png", "item_m_los3.png"],
                "m_los4": ["item_m_los1.png", "item_m_los2.png", "item_m_los4.png"],
                "m_los5": ["item_m_los1.png", "item_m_los5.png"],
                "m_eme2": ["item_m_eme1.png", "item_m_eme2.png"],
                "m_eme3": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme3.png"],
                "m_eme4": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme4.png"],
                "m_eme5": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme5_1.png"],
                "m_eme6": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme6.png"],
                "m_imp2": ["item_m_imp1.png", "item_m_imp2.png"],
                "m_imp3": ["item_m_imp1.png", "item_m_imp2.png", "item_m_imp3.png"],
                "m_imp4": ["item_m_imp1.png", "item_m_imp2.png", "item_m_imp4.png"],
                "m_imp5": ["item_m_imp1.png", "item_m_imp2.png", "item_m_imp5.png"],
                "m_imp6": ["item_m_imp1.png", "item_m_imp6.png"],
                "m_dru2": ["item_m_dru1.png", "item_m_dru2.png"],
                "m_dru3": ["item_m_dru1.png", "item_m_dru2.png", "item_m_dru3.png"],
                "m_dru4": ["item_m_dru1.png", "item_m_dru4.png"],
                "m_dru5": ["item_m_dru1.png", "item_m_dru4.png", "item_m_dru5.png"],
                "m_dru6": ["item_m_dru1.png", "item_m_dru6.png"],
                "x_mas3": ["item_x_mas1.png", "item_x_mas3.png"],
                "x_mas5": ["item_x_mas1.png", "item_x_mas3.png", "item_x_mas5.png"],
                "x_mas6": ["item_x_mas1.png", "item_x_mas6.png"]}
                
selected_objects = [Item("", 0, 0), Item("", 0, 0), Item("", 0, 0),
                    Item("", 0, 0), Item("", 0, 0), Item("", 0, 0)]


class Build_Screen(Screen):
    slot1 = ObjectProperty()
    slot2 = ObjectProperty()
    slot3 = ObjectProperty()
    slot4 = ObjectProperty()
    slot5 = ObjectProperty()
    slot6 = ObjectProperty()

    list_of_slots = [slot1, slot2, slot3,
                     slot4, slot5, slot6]

    total_damage_label = ObjectProperty()
    total_power_label = ObjectProperty()
    total_gold_label = ObjectProperty()
    total_mana_label = ObjectProperty()

    remove_item = ObjectProperty()

    background1 = ObjectProperty()
    background2 = ObjectProperty()

    def select_item_slot_and_do_something(self, slot_number):
        global current_item_slot
        current_item_slot = slot_number
        list_of_slots = [self.slot1, self.slot2, self.slot3,
                         self.slot4, self.slot5, self.slot6]

        if self.remove_mode_state == 1:
            if list_of_slots[current_item_slot - 1].source != "nothing.png":
                self.quitar_item()
            elif list_of_slots[current_item_slot - 1].source == "nothing.png":
                self.toggle_remove_mode()
        else:
            self.manager.get_screen("items screen 2").initialize()
            self.manager.current = "items screen 2"

    def toggle_remove_mode(self):
        remove_states = ["interface_remove_item.png", "interface_remove_item_2.png"]
        if self.remove_mode_state == 0:
            self.remove_mode_state = 1
            self.remove_item.source = remove_states[self.remove_mode_state]
            self.background1.source = "color_golden.png"
            if self.slot1.source == "1st.png":
                self.slot1.source = "1st_gold.png"
            if self.slot2.source == "2nd.png":
                self.slot2.source = "2nd_gold.png"
            if self.slot3.source == "3rd.png":
                self.slot3.source = "3rd_gold.png"
            if self.slot4.source == "4th.png":
                self.slot4.source = "4th_gold.png"
            if self.slot5.source == "5th.png":
                self.slot5.source = "5th_gold.png"
            if self.slot6.source == "6th.png":
                self.slot6.source = "6th_gold.png"
        elif self.remove_mode_state == 1:
            self.remove_mode_state = 0
            self.remove_item.source = remove_states[self.remove_mode_state]
            self.background1.source = "color_gray.png"
            if self.slot1.source == "1st_gold.png":
                self.slot1.source = "1st.png"
            if self.slot2.source == "2nd_gold.png":
                self.slot2.source = "2nd.png"
            if self.slot3.source == "3rd_gold.png":
                self.slot3.source = "3rd.png"
            if self.slot4.source == "4th_gold.png":
                self.slot4.source = "4th.png"
            if self.slot5.source == "5th_gold.png":
                self.slot5.source = "5th.png"
            if self.slot6.source == "6th_gold.png":
                self.slot6.source = "6th.png"

    def quitar_item(self):
        global current_item_slot
        global selected_objects
        if current_item_slot == 1:
            self.slot1.source = "1st_gold.png"
            selected_objects[0] = Item("", 0, 0)
        if current_item_slot == 2:
            self.slot2.source = "2nd_gold.png"
            selected_objects[1] = Item("", 0, 0)
        if current_item_slot == 3:
            self.slot3.source = "3rd_gold.png"
            selected_objects[2] = Item("", 0, 0)
        if current_item_slot == 4:
            self.slot4.source = "4th_gold.png"
            selected_objects[3] = Item("", 0, 0)
        if current_item_slot == 5:
            self.slot5.source = "5th_gold.png"
            selected_objects[4] = Item("", 0, 0)
        if current_item_slot == 6:
            self.slot6.source = "6th_gold.png"
            selected_objects[5] = Item("", 0, 0)
        global selected_items 
        selected_items = [self.slot1.source, self.slot2.source, self.slot3.source,
                          self.slot4.source, self.slot5.source, self.slot6.source]

    def reset_items_to_zero(self):
        self.slot1.source = "1st.png"
        self.slot2.source = "2nd.png"
        self.slot3.source = "3rd.png"
        self.slot4.source = "4th.png"
        self.slot5.source = "5th.png"
        self.slot6.source = "6th.png"
        global selected_items
        selected_items = ["a", "a", "a",
                          "a", "a", "a"]
        global selected_objects
        selected_objects = [Item("", 0, 0), Item("", 0, 0), Item("", 0, 0),
                            Item("", 0, 0), Item("", 0, 0), Item("", 0, 0)]

    def update_items(self):
        global current_item_slot
        global selected_item_picture
        global selected_objects
        global item_objects
        
        slots = [self.slot1, self.slot2, self.slot3,
                 self.slot4, self.slot5, self.slot6]
        
        for i in range(1, 7):
            if current_item_slot == i:
                slots[i-1].source = selected_item_picture
                selected_objects[i-1] = item_objects[selected_item_picture]

        global selected_items
        selected_items = [self.slot1.source, self.slot2.source, self.slot3.source,
                          self.slot4.source, self.slot5.source, self.slot6.source]

    total_power = 0
    mana_to_power_percent = 0
    initialized = 0

    remove_mode_state = 0
    edit_mode_state = 0

class Items_Screen_2(Screen):
    god_class = ""

    guardian_gods = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                      "cerberus", "fafnir", "ganesha", "geb", "khepri",
                      "kumbhakarna", "kuzenbo", "sobek", "sylvanus", "terra",
                      "xing-tian", "ymir"]
    hunter_gods = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                      "chernobog", "chiron", "cupid", "hachiman", "hou-yi",
                      "izanami", "jing-wei", "medusa", "neith", "rama",
                      "skadi", "ullr", "xbalanque"]
    warrior_gods = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                      "erlang-shen", "guan-yu", "hercules", "nike", "odin",
                      "osiris", "sun-wukong", "tyr", "vamana"]
    mage_gods = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
                 "baron-samedi", "change", "chronos", "discordia", "freya",
                 "hades", "he-bo", "hel", "isis", "janus",
                 "kukulkan", "nox", "nu-wa", "poseidon", "ra",
                 "raijin", "scylla", "sol", "the-morrigan", "thoth",
                 "vulcan", "zeus", "zhong-kui"]
    assassin_gods = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                     "da-ji", "fenrir", "hun-batz", "kali", "loki",
                     "mercury", "ne-zha", "nemesis", "pele", "ratatoskr",
                     "ravana", "serqet", "susano", "thanatos", "thor"]
    warrior_items = [ "item_p_boo1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_kat1", "item_p_kat2", "nothing", "nothing",
                           "item_p_kat3", "item_p_kat4_1", "item_p_kat5", "item_p_kat6",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                           "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]
    assassin_items = [ "item_p_boo1", "item_x_sta1_1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           #"item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_lig1", "item_p_lig3", "nothing", "nothing",
                           #"item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           #"item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           #"item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_kat1", "item_p_kat2", "nothing", "nothing",
                           #"item_p_kat3", "item_p_kat4_1", "item_p_kat5", "item_p_kat6",
                           "item_p_kat3", "item_p_kat4_1", "item_p_kat6", "nothing",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           #"item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           #"nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_p_cud1", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_x_mas1", "item_x_mas3", "item_x_mas5", "item_x_mas6",
                           "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                           "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]
    hunter_items = [ "item_p_boo1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                           "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]
    guardian_items = [ "item_m_sho1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                          "item_m_sho2", "item_m_sho3", "item_m_sho4", "item_m_sho5",
                          "item_m_spe1", "item_m_spe2", "nothing", "nothing",
                          "item_m_spe3_1", "item_m_spe4_1", "item_m_spe5", "item_m_spe6",
                          "item_m_foc1", "item_m_foc2", "item_m_foc6", "nothing",
                          "item_m_foc3", "item_m_foc4", "item_m_foc5", "item_m_foc7",
                          "item_m_unc1", "item_m_unc2", "item_m_unc3", "item_m_unc4",
                          "item_m_unc5", "item_m_unc6", "item_m_unc7", "item_m_unc8_1",
                          "item_m_tin1", "item_m_tin2", "item_m_tin3_1", "item_m_tin4",
                          "nothing", "item_m_tin5", "item_m_tin6_1", "item_m_tin7",
                          "item_m_los1", "item_m_los2", "item_m_los3", "item_m_los4",
                          "nothing", "item_m_los5", "nothing", "nothing",
                          "item_m_eme1", "item_m_eme2", "nothing", "nothing",
                          "item_m_eme3", "item_m_eme4", "item_m_eme5_1", "item_m_eme6",
                          "item_m_imp1", "item_m_imp2", "nothing", "nothing",
                          "nothing", "item_m_imp3", "item_m_imp4", "item_m_imp5",
                          "nothing", "item_m_imp6", "nothing", "nothing",
                          "item_m_dru1", "item_m_dru2", "item_m_dru3", "nothing",
                          "nothing", "item_m_dru4", "item_m_dru5", "nothing",
                          "nothing", "item_m_dru6", "nothing", "nothing",
                          "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                          "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]
    mage_items = [ "item_m_sho1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                          "item_m_sho2", "item_m_sho3", "item_m_sho4", "item_m_sho5",
                          "item_m_spe1", "item_m_spe2", "nothing", "nothing",
                          "item_m_spe3_1", "item_m_spe4_1", "item_m_spe5", "item_m_spe6",
                          "item_m_foc1", "item_m_foc2", "item_m_foc6", "nothing",
                          "item_m_foc3", "item_m_foc4", "item_m_foc5", "item_m_foc7",
                          "item_m_unc1", "item_m_unc2", "item_m_unc3", "item_m_unc4",
                          "item_m_unc5", "item_m_unc6", "item_m_unc7", "item_m_unc8_1",
                          "item_m_tin1", "item_m_tin2", "item_m_tin3_1", "item_m_tin4",
                          "nothing", "item_m_tin5", "item_m_tin6_1", "item_m_tin7",
                          "item_m_los1", "item_m_los2", "item_m_los3", "item_m_los4",
                          "nothing", "item_m_los5", "nothing", "nothing",
                          "item_m_eme1", "item_m_eme2", "nothing", "nothing",
                          "item_m_eme3", "item_m_eme4", "item_m_eme5_1", "item_m_eme6",
                          "item_m_imp1", "item_m_imp2", "nothing", "nothing",
                          "nothing", "item_m_imp3", "item_m_imp4", "item_m_imp5",
                          "nothing", "item_m_imp6", "nothing", "nothing",
                          "item_m_dru1", "item_m_dru2", "item_m_dru3", "nothing",
                          "nothing", "item_m_dru4", "item_m_dru5", "nothing",
                          "nothing", "item_m_dru6", "nothing", "nothing",
                          "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                          "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]
    vamana_items = [ "item_p_boo1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_kat1", "item_p_kat2", "nothing", "nothing",
                           "item_p_kat3", "item_p_kat4_1", "item_p_kat5", "item_p_kat6",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_d_bre1", "item_d_bre2", "nothing", "nothing",
                           "item_d_bre3", "item_d_bre4", "item_d_bre5", "nothing",
                           "item_d_clo1", "item_d_clo2", "item_d_clo3", "item_d_clo4",
                           "item_d_clo5", "item_d_clo6", "item_d_clo7", "item_d_clo8_1",
                           "item_d_glo1_1", "nothing", "nothing", "nothing",
                           "item_d_mai1", "item_d_mai2", "nothing", "nothing",
                           "item_d_mai3", "item_d_mai4", "item_d_mai5", "item_d_mai6"]
    ares_items = [ "item_m_sho1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                          "item_m_sho2", "item_m_sho3", "item_m_sho4", "item_m_sho5",
                          "item_m_spe1", "item_m_spe2", "nothing", "nothing",
                          "item_m_spe3_1", "item_m_spe4_1", "item_m_spe5", "item_m_spe6",
                          "item_m_foc1", "item_m_foc2", "item_m_foc6", "nothing",
                          "item_m_foc3", "item_m_foc4", "item_m_foc5", "item_m_foc7",
                          "item_m_unc1", "item_m_unc2", "item_m_unc3", "item_m_unc4",
                          "item_m_unc5", "item_m_unc6", "item_m_unc7", "item_m_unc8_1",
                          "item_m_tin1", "item_m_tin2", "item_m_tin3_1", "item_m_tin4",
                          "nothing", "item_m_tin5", "item_m_tin6_1", "item_m_tin7",
                          "item_m_los1", "item_m_los2", "item_m_los3", "item_m_los4",
                          "nothing", "item_m_los5", "nothing", "nothing",
                          "item_m_eme1", "item_m_eme2", "nothing", "nothing",
                          "item_m_eme3", "item_m_eme4", "item_m_eme5_1", "item_m_eme6",
                          "item_m_imp1", "item_m_imp2", "nothing", "nothing",
                          "nothing", "item_m_imp3", "item_m_imp4", "item_m_imp5",
                          "nothing", "item_m_imp6", "nothing", "nothing",
                          "item_m_dru1", "item_m_dru2", "item_m_dru3", "nothing",
                          "nothing", "item_m_dru4", "item_m_dru5", "nothing",
                          "nothing", "item_m_dru6", "nothing", "nothing",
                          "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                          "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    def initialize(self):
        selected_list = []
        
        global current_god                   
        
        for god in self.guardian_gods:
            if current_god == god:
                self.god_class = "guardian"
        for god in self.hunter_gods:
            if current_god == god:
                self.god_class = "hunter"
        for god in self.warrior_gods:
            if current_god == god:
                self.god_class = "warrior"
        for god in self.mage_gods:
            if current_god == god:
                self.god_class = "mage"
        for god in self.assassin_gods:
            if current_god == god:
                self.god_class = "assassin"

        if current_god == "vamana":
            selected_list = self.vamana_items
        elif god_class == "warrior":
            selected_list = self.warrior_items
        elif god_class == "assassin":
            selected_list = self.assassin_items
        elif god_class == "hunter":
            selected_list = self.hunter_items
        elif god_class == "guardian":
            selected_list = self.guardian_items
        elif god_class == "mage":
            selected_list = self.mage_items
            
        elements_number = 0
        for image in selected_list:
            elements_number = elements_number + 1
            
        rows_number = elements_number / 4

        flt = FloatLayout()
        self.add_widget(flt)
        
        scroll = ScrollView( size_hint = (0.9, 0.8), pos_hint = { "x": 0.05, "y": 0.07 }, effect_cls = ScrollEffect)
        self.children[0].add_widget(scroll)
        
        grid = GridLayout( size_hint = (1,None), col_default_width = 50, row_default_height = 100, cols = 4, rows = rows_number )
        self.buttons = []
        picture = ""
        i = 0
        k = 0
        global selected_items                   
        for item in selected_list:              
            picture = item + ".png"                                              
            for h in selected_items:            
                if picture == h:                
                    picture = "nothing.png"     
                    break                       
            self.buttons.append(ClickableImage(source = picture))
            if item != "nothing":
                k = 1
            if item == "nothing" or picture == "nothing.png":
                k = 0
            if k == 1:
                self.buttons[i].bind(on_press=self.select_item_and_go_back)
            if k == 0:
                self.buttons[i].bind(on_press=self.do_nothing)
            grid.add_widget(self.buttons[i])
            i = i + 1
        grid.bind(minimum_height=grid.setter('height'))
        self.children[0].children[0].add_widget(grid)
    def do_nothing(self, j):
        pass
    def select_item_and_go_back(self, button_object):
        global selected_item_picture
        selected_item_picture = button_object.source
        self.manager.get_screen("build screen").update_items()
        self.clean_screen()
        self.manager.current = "build screen"
    def clean_screen(self):
        for button in self.buttons:
            button.source = "nothing.png"
            button.bind(on_press=self.do_nothing)
    def clean_and_go_back(self):
        self.clean_screen()
        self.manager.current = "build screen"

target_god_class = ""

class Targets_List_Screen(Screen):
    target_1_btn = ObjectProperty
    target_2_btn = ObjectProperty
    target_3_btn = ObjectProperty
    target_4_btn = ObjectProperty
    target_5_btn = ObjectProperty
    next_btn = ObjectProperty
    remove_item_btn = ObjectProperty

    target_selected = 0
    remove_mode = False

    selected_targets = ["", "", "", "", "", ""]

    def go_to_select_a_target(self, target_number):
        self.target_selected = target_number
        if self.remove_mode == False:
            self.manager.get_screen("target class screen")
            self.manager.current = "target class screen"
        else:
            self.update_targets()
    def update_targets(self):

        global target_god
        if self.target_selected == 0:
            if self.remove_mode == False:
                self.target_1_btn.source = target_god + ".png"
                self.selected_targets[0] = target_god
                self.next_btn.disabled = False
                if self.target_2_btn.source == "signo-menos.png":
                    self.target_2_btn.source = "signo-mas.png"
                    self.target_2_btn.disabled = False
            else:
                if self.target_1_btn.source == "signo-mas.png":
                    pass
                else:
                    if self.target_2_btn.source == "signo-mas.png":
                        self.target_2_btn.source = "signo-menos.png"
                        self.target_2_btn.disabled = True
                        self.target_1_btn.source = "signo-mas.png"
                        self.selected_targets[0] = ""
                        self.next_btn.disabled = True
                    elif self.target_3_btn.source == "signo-mas.png":
                        self.target_3_btn.source = "signo-menos.png"
                        self.target_3_btn.disabled = True
                        self.target_1_btn.source = self.target_2_btn.source
                        self.selected_targets[0] = self.selected_targets[1]
                        self.target_2_btn.source = "signo-mas.png"
                        self.selected_targets[1] = ""
                    elif self.target_4_btn.source == "signo-mas.png":
                        self.target_4_btn.source = "signo-menos.png"
                        self.target_4_btn.disabled = True
                        self.target_1_btn.source = self.target_2_btn.source
                        self.selected_targets[0] = self.selected_targets[1]
                        self.target_2_btn.source = self.target_3_btn.source
                        self.selected_targets[1] = self.selected_targets[2]
                        self.target_3_btn.source = "signo-mas.png"
                        self.selected_targets[2] = ""
                    elif self.target_5_btn.source == "signo-mas.png":
                        self.target_5_btn.source = "signo-menos.png"
                        self.target_5_btn.disabled = True
                        self.target_1_btn.source = self.target_2_btn.source
                        self.selected_targets[0] = self.selected_targets[1]
                        self.target_2_btn.source = self.target_3_btn.source
                        self.selected_targets[1] = self.selected_targets[2]
                        self.target_3_btn.source = self.target_4_btn.source
                        self.selected_targets[2] = self.selected_targets[3]
                        self.target_4_btn.source = "signo-mas.png"
                        self.selected_targets[3] = ""
                    else:
                        self.target_1_btn.source = self.target_2_btn.source
                        self.selected_targets[0] = self.selected_targets[1]
                        self.target_2_btn.source = self.target_3_btn.source
                        self.selected_targets[1] = self.selected_targets[2]
                        self.target_3_btn.source = self.target_4_btn.source
                        self.selected_targets[2] = self.selected_targets[3]
                        self.target_4_btn.source = self.target_5_btn.source
                        self.selected_targets[3] = self.selected_targets[4]
                        self.target_5_btn.source = "signo-mas.png"
                        self.selected_targets[4] = ""

        if self.target_selected == 1:
            if self.remove_mode == False:
                self.target_2_btn.source = target_god + ".png"
                self.selected_targets[1] = target_god
                if self.target_3_btn.source == "signo-menos.png":
                    self.target_3_btn.source = "signo-mas.png"
                    self.target_3_btn.disabled = False
            else:
                if self.target_2_btn.source == "signo-mas.png":
                    pass
                else:
                    if self.target_3_btn.source == "signo-mas.png":
                        self.target_3_btn.source = "signo-menos.png"
                        self.target_3_btn.disabled = True
                        self.target_2_btn.source = "signo-mas.png"
                        self.selected_targets[1] = ""
                    elif self.target_4_btn.source == "signo-mas.png":
                        self.target_4_btn.source = "signo-menos.png"
                        self.target_4_btn.disabled = True
                        self.target_2_btn.source = self.target_3_btn.source
                        self.selected_targets[1] = self.selected_targets[2]
                        self.target_3_btn.source = "signo-mas.png"
                        self.selected_targets[2] = ""
                    elif self.target_5_btn.source == "signo-mas.png":
                        self.target_5_btn.source = "signo-menos.png"
                        self.target_5_btn.disabled = True
                        self.target_2_btn.source = self.target_3_btn.source
                        self.selected_targets[1] = self.selected_targets[2]
                        self.target_3_btn.source = self.target_4_btn.source
                        self.selected_targets[2] = self.selected_targets[3]
                        self.target_4_btn.source = "signo-mas.png"
                        self.selected_targets[3] = ""
                    else:
                        self.target_2_btn.source = self.target_3_btn.source
                        self.selected_targets[1] = self.selected_targets[2]
                        self.target_3_btn.source = self.target_4_btn.source
                        self.selected_targets[2] = self.selected_targets[3]
                        self.target_4_btn.source = self.target_5_btn.source
                        self.selected_targets[3] = self.selected_targets[4]
                        self.target_5_btn.source = "signo-mas.png"
                        self.selected_targets[4] = ""

        if self.target_selected == 2:
            if self.remove_mode == False:
                self.target_3_btn.source = target_god + ".png"
                self.selected_targets[2] = target_god
                if self.target_4_btn.source == "signo-menos.png":
                    self.target_4_btn.source = "signo-mas.png"
                    self.target_4_btn.disabled = False
            else:
                if self.target_3_btn.source == "signo-mas.png":
                    pass
                else:
                    if self.target_4_btn.source == "signo-mas.png":
                        self.target_4_btn.source = "signo-menos.png"
                        self.target_4_btn.disabled = True
                        self.target_3_btn.source = "signo-mas.png"
                        self.selected_targets[2] = ""
                    elif self.target_5_btn.source == "signo-mas.png":
                        self.target_5_btn.source = "signo-menos.png"
                        self.target_5_btn.disabled = True
                        self.target_3_btn.source = self.target_4_btn.source
                        self.selected_targets[2] = self.selected_targets[3]
                        self.target_4_btn.source = "signo-mas.png"
                        self.selected_targets[3] = ""
                    else:
                        self.target_3_btn.source = self.target_4_btn.source
                        self.selected_targets[2] = self.selected_targets[3]
                        self.target_4_btn.source = self.target_5_btn.source
                        self.selected_targets[3] = self.selected_targets[4]
                        self.target_5_btn.source = "signo-mas.png"
                        self.selected_targets[4] = ""

        if self.target_selected == 3:
            if self.remove_mode == False:
                self.target_4_btn.source = target_god + ".png"
                self.selected_targets[3] = target_god
                if self.target_5_btn.source == "signo-menos.png":
                    self.target_5_btn.source = "signo-mas.png"
                    self.target_5_btn.disabled = False
            else:
                if self.target_4_btn.source == "signo-mas.png":
                    pass
                else:
                    if self.target_5_btn.source == "signo-mas.png":
                        self.target_5_btn.source = "signo-menos.png"
                        self.target_5_btn.disabled = True
                        self.target_4_btn.source = "signo-mas.png"
                        self.selected_targets[3] = ""
                    else:
                        self.target_4_btn.source = self.target_5_btn.source
                        self.selected_targets[3] = self.selected_targets[4]
                        self.target_5_btn.source = "signo-mas.png"
                        self.selected_targets[4] = ""
        if self.target_selected == 4:
            if self.remove_mode == False:
                self.target_5_btn.source = target_god + ".png"
                self.selected_targets[4] = target_god
            else:
                if self.target_5_btn.source == "signo-mas.png":
                    pass
                else:
                    self.target_5_btn.source = "signo-mas.png"
                    self.selected_targets[4] = ""
    def toggle_remove_mode(self):
        if self.remove_item_btn.source == "interface_remove_item.png":
            self.remove_item_btn.source = "interface_remove_item_2.png"
            self.background1.source = "color_golden.png"
            self.background2.source = "color_golden.png"
            self.remove_mode = True
        else:
            self.remove_item_btn.source = "interface_remove_item.png"
            self.background1.source = "color_gray.png"
            self.background2.source = "color_gray.png"
            self.remove_mode = False
    def start_cidt(self):
        selected_targets = self.selected_targets
        self.manager.get_screen("cidt final screen 2").initialize(selected_targets)
        self.manager.current = "cidt final screen 2"

class Target_Class_Screen(Screen):
    guardian_btn = ObjectProperty
    hunter_btn = ObjectProperty
    warrior_btn = ObjectProperty
    mage_btn = ObjectProperty
    assassin_btn = ObjectProperty

    def initialize_next_screen_and_go(self, class_selected):
        global target_god_class
        target_god_class = class_selected
        options = { "guardian": 0 , "hunter": 1, "warrior": 2,
                    "mage": 3, "assassin": 4 }
        self.manager.get_screen("target god selection screen").initialize(options[class_selected])
        self.manager.current = "target god selection screen"
    def reset_pages_and_go_back(self):
        global target_classes_pages_numbers
        target_classes_pages_numbers = [1, 1, 1, 1, 1]
        self.manager.current = "targets list screen"


target_class_option_number = 0
target_classes_pages_numbers = [1, 1, 1, 1, 1]
target_god = ""

class Target_God_Selection_Screen(Screen):

    next_button = ObjectProperty()
    previous_button = ObjectProperty()

    guardians = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                   "cerberus", "fafnir", "ganesha", "geb", "jormungandr",
                   "khepri", "kumbhakarna", "kuzenbo", "sobek", "sylvanus",
                   "terra", "xing-tian", "ymir" ]
    hunters = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                 "chernobog", "chiron", "cupid", "hachiman",
                 "hou-yi", "izanami", "jing-wei", "medusa", "neith",
                 "rama", "skadi", "ullr", "xbalanque" ]
    warriors = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                  "erlang-shen", "guan-yu", "hercules", "king-arthur", "nike",
                  "odin", "osiris", "sun-wukong", "tyr", "vamana" ]
    mages = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
               "baron-samedi", "change", "chronos", "discordia",
               "freya", "hades", "he-bo", "hel", "hera", "isis",
               "janus", "merlin", "kukulkan", "nox", "nu-wa",
               "poseidon", "ra", "raijin", "scylla", "sol",
               "the-morrigan", "thoth", "vulcan", "zeus",
               "zhong-kui" ]
    assassins = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                   "da-ji", "fenrir", "hun-batz", "kali",
                   "loki", "mercury", "ne-zha", "nemesis", "pele",
                   "ratatoskr", "ravana", "serqet", "susano",
                   "thanatos", "thor" ]

    button_positions = [ [0.123, 0.7], [0.391, 0.7], [0.659, 0.7],
                         [0.123, 0.508], [0.391, 0.508], [0.659, 0.508],
                         [0.123, 0.316], [0.391, 0.316], [0.659, 0.316] ]
    
    list_of_lists = [guardians, hunters, warriors, mages, assassins]

    btn1 = ClickableImage(pos_hint = { "x": button_positions[0][0] , "y": button_positions[0][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn2 = ClickableImage(pos_hint = { "x": button_positions[1][0] , "y": button_positions[1][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn3 = ClickableImage(pos_hint = { "x": button_positions[2][0] , "y": button_positions[2][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn4 = ClickableImage(pos_hint = { "x": button_positions[3][0] , "y": button_positions[3][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn5 = ClickableImage(pos_hint = { "x": button_positions[4][0] , "y": button_positions[4][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn6 = ClickableImage(pos_hint = { "x": button_positions[5][0] , "y": button_positions[5][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn7 = ClickableImage(pos_hint = { "x": button_positions[6][0] , "y": button_positions[6][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn8 = ClickableImage(pos_hint = { "x": button_positions[7][0] , "y": button_positions[7][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn9 = ClickableImage(pos_hint = { "x": button_positions[8][0] , "y": button_positions[8][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

    initialized = False

    def initialize(self, option):
        global target_classes_pages_numbers
        selected_list = self.list_of_lists[option]
        page_number = target_classes_pages_numbers[option]
        elements_number = 0
        
        global target_class_option_number
        target_class_option_number = option
        
        for x in selected_list:
            elements_number = elements_number + 1

        number_of_pages = elements_number/9 + 1
        if elements_number == 18 or elements_number == 27 or elements_number == 36 or elements_number == 45:
            number_of_pages = number_of_pages - 1
            
        if self.initialized == False:
            layout = FloatLayout()
            i = 0
            page_number = 1
            for button in self.buttons:
                if i == 9:
                    break
                button.source = selected_list[i] + ".png"
                button.name = selected_list[i]
                button.bind(on_press=self.go_to_god)
                layout.add_widget(button)
                i = i + 1
            self.add_widget(layout)
            self.initialized = True
        elif self.initialized == True:
            if page_number == 1:
                i = 8
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 0:
                        break
                    i = i - 1
            if page_number == 2:
                i = 17
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 9:
                        break
                    i = i - 1
            if page_number == 3:
                i = 26
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 18:
                        break
                    i = i - 1
            if page_number == 4:
                i = 35
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 27:
                        break
                    i = i - 1

        if page_number == 1:
            self.previous_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.previous_button.pos_hint = { "x": 0.0 , "y": 0.0 }
        if page_number == number_of_pages:
            self.next_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.next_button.pos_hint = { "x": 0.8 , "y": 0.0 }
    def go_to_god(self, btn):
        if btn.name != "nothing":
            global target_god
            target_god = btn.name
            self.manager.get_screen("targets list screen").update_targets()
            self.manager.current = "targets list screen"
    def next_page(self):
        global target_classes_pages_numbers
        global target_class_option_number
        target_classes_pages_numbers[target_class_option_number] = target_classes_pages_numbers[target_class_option_number] + 1
        self.initialize(target_class_option_number)
    def previous_page(self):
        global target_classes_pages_numbers
        global target_class_option_number
        target_classes_pages_numbers[target_class_option_number] = target_classes_pages_numbers[target_class_option_number] - 1
        self.initialize(target_class_option_number)

class CIDH_Final_Screen_2(Screen):

    #objects
    #build objects
    background1 = ObjectProperty
    item1_img = ObjectProperty
    item2_img = ObjectProperty
    item3_img = ObjectProperty
    item4_img = ObjectProperty
    item5_img = ObjectProperty
    item6_img = ObjectProperty

    #skills HUD objects
    skill_1_lvl_up_btn = ObjectProperty
    skill_1_icon = ObjectProperty
    skill_1_lvl_img = ObjectProperty
    skill_1_lvl_down_btn = ObjectProperty

    skill_2_lvl_up_btn = ObjectProperty
    skill_2_icon = ObjectProperty
    skill_2_lvl_img = ObjectProperty
    skill_2_lvl_down_btn = ObjectProperty

    skill_3_lvl_up_btn = ObjectProperty
    skill_3_icon = ObjectProperty
    skill_3_lvl_img = ObjectProperty
    skill_3_lvl_down_btn = ObjectProperty

    skill_4_lvl_up_btn = ObjectProperty
    skill_4_icon = ObjectProperty
    skill_4_lvl_img = ObjectProperty
    skill_4_lvl_down_btn = ObjectProperty

    #targets HUD objects
    target_1_btn = ObjectProperty
    target_1_lvl_down_btn = ObjectProperty
    target_1_lvl_btn = ObjectProperty
    target_1_lvl_up_btn = ObjectProperty
    target_1_cidh_state = ObjectProperty
    shield_icon_1 = ObjectProperty

    target_2_btn = ObjectProperty
    target_2_lvl_down_btn = ObjectProperty
    target_2_lvl_btn = ObjectProperty
    target_2_lvl_up_btn = ObjectProperty
    target_2_cidh_state = ObjectProperty
    shield_icon_2 = ObjectProperty

    target_3_btn = ObjectProperty
    target_3_lvl_down_btn = ObjectProperty
    target_3_lvl_btn = ObjectProperty
    target_3_lvl_up_btn = ObjectProperty
    target_3_cidh_state = ObjectProperty
    shield_icon_3 = ObjectProperty

    target_4_btn = ObjectProperty
    target_4_lvl_down_btn = ObjectProperty
    target_4_lvl_btn = ObjectProperty
    target_4_lvl_up_btn = ObjectProperty
    target_4_cidh_state = ObjectProperty
    shield_icon_4 = ObjectProperty

    target_5_btn = ObjectProperty
    target_5_lvl_down_btn = ObjectProperty
    target_5_lvl_btn = ObjectProperty
    target_5_lvl_up_btn = ObjectProperty
    target_5_cidh_state = ObjectProperty
    shield_icon_5 = ObjectProperty

    #player level HUD objects
    player_lvl_down_btn = ObjectProperty
    player_lvl_indicator = ObjectProperty
    player_lvl_up_btn = ObjectProperty

    #killeable targets indicator HUD objects
    combos_indicator_btn = ObjectProperty
    combo_a_ind = ObjectProperty
    combo_b_ind = ObjectProperty
    combo_c_ind = ObjectProperty
    combo_d_ind = ObjectProperty
    combo_indicator_btn = ObjectProperty

    edit_item_btn = ObjectProperty

    targets = ["", "", "", "", ""]
    user_god = ""

    #user god stats
    sk1_bs = 0
    sk1_ps = 0
    sk1_bs2 = 0
    sk1_ps2 = 0
    sk2_bs = 0
    sk2_ps = 0
    sk2_bs2 = 0
    sk2_ps2 = 0
    sk3_bs = 0
    sk3_ps = 0
    sk3_bs2 = 0
    sk3_ps2 = 0
    sk4_bs = 0
    sk4_ps = 0
    sk4_bs2 = 0
    sk4_ps2 = 0

    player_lvl = 1

    base_ba_d_simple = 0
    base_ba_d_per_level = 0.0
    base_ba_d_power_multiplier = 0
    ba_progression = []

    base_mana = 0
    mana_per_level = 0

    #targets stats
    target_1_base_health = 0
    target_1_health_per_level = 0
    target_1_base_p_prot = 0.0
    target_1_p_prot_per_level = 0.0
    target_1_base_m_prot = 0.0
    target_1_m_prot_per_level = 0.0

    target_2_base_health = 0
    target_2_health_per_level = 0
    target_2_base_p_prot = 0.0
    target_2_p_prot_per_level = 0.0
    target_2_base_m_prot = 0.0
    target_2_m_prot_per_level = 0.0

    target_3_base_health = 0
    target_3_health_per_level = 0
    target_3_base_p_prot = 0.0
    target_3_p_prot_per_level = 0.0
    target_3_base_m_prot = 0.0
    target_3_m_prot_per_level = 0.0

    target_4_base_health = 0
    target_4_health_per_level = 0
    target_4_base_p_prot = 0.0
    target_4_p_prot_per_level = 0.0
    target_4_base_m_prot = 0.0
    target_4_m_prot_per_level = 0.0

    target_5_base_health = 0
    target_5_health_per_level = 0
    target_5_base_p_prot = 0.0
    target_5_p_prot_per_level = 0.0
    target_5_base_m_prot = 0.0
    target_5_m_prot_per_level = 0.0

    skills_levels = [0, 0, 0, 0]

    target_1_lvl = 1
    target_2_lvl = 1
    target_3_lvl = 1
    target_4_lvl = 1
    target_5_lvl = 1

    final_build = []  # [obj1, obj2, obj3, obj4, obj5, obj6]
    current_build = [nothing, nothing, nothing, nothing, nothing, nothing]
    building_order = []  # [[], [], [], [], [], []]
    current_slot = 1
    current_tree_item = 1
    finished_build = False

    combos_number = 0

    killeable_targets = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    selected_combo = 1

    targets_number = 1

    def initialize(self, selected_targets):

        self.reset_screen()

        global current_god
        self.user_god = current_god

        self.skill_1_icon.source = self.user_god + "_sk_1.png"
        self.skill_2_icon.source = self.user_god + "_sk_2.png"
        self.skill_3_icon.source = self.user_god + "_sk_3.png"
        self.skill_4_icon.source = self.user_god + "_sk_4.png"

        self.skill_1_lvl_up_btn.source = "up_arrow.png"
        self.skill_1_lvl_up_btn.disabled = False
        self.skill_1_icon.disabled = False
        self.skill_1_lvl_img.source = "sk_l_0.jpg"
        self.skill_1_lvl_down_btn.source = "nothing.png"
        self.skill_1_lvl_down_btn.disabled = True
        self.skill_2_lvl_up_btn.source = "up_arrow.png"
        self.skill_2_lvl_up_btn.disabled = False
        self.skill_2_icon.disabled = False
        self.skill_2_lvl_img.source = "sk_l_0.jpg"
        self.skill_2_lvl_down_btn.source = "nothing.png"
        self.skill_2_lvl_down_btn.disabled = True
        self.skill_3_lvl_up_btn.source = "up_arrow.png"
        self.skill_3_lvl_up_btn.disabled = False
        self.skill_3_icon.disabled = False
        self.skill_3_lvl_img.source = "sk_l_0.jpg"
        self.skill_3_lvl_down_btn.source = "nothing.png"
        self.skill_3_lvl_down_btn.disabled = True
        self.skill_4_lvl_up_btn.source = "up_arrow.png"
        self.skill_4_lvl_up_btn.disabled = False
        self.skill_4_icon.disabled = False
        self.skill_4_lvl_img.source = "sk_l_0.jpg"
        self.skill_4_lvl_down_btn.source = "nothing.png"
        self.skill_4_lvl_down_btn.disabled = True

        global selected_objects     #
        global item_trees
        i = -1
        for item in selected_objects:
            if item.name_id != "" and item.name_id != "nothing":
                self.final_build.append(item)
                self.building_order.append([])
                i = i + 1
                j = 0
                finished_tree = False
                while finished_tree == False:
                    try:
                        self.building_order[i].append(items_trees[item.name_id][j])
                    except:
                        self.building_order[i].append(("item_" + item.name_id + ".png"))
                        break

                    if elements_number(items_trees[item.name_id]) == (j + 1):
                        finished_tree = True
                    else:
                        j = j + 1

        self.item1_img.source = "nothing.png"
        self.item2_img.source = "nothing.png"
        self.item3_img.source = "nothing.png"
        self.item4_img.source = "nothing.png"
        self.item5_img.source = "nothing.png"
        self.item6_img.source = "nothing.png"

        # Load user god stats
        tree = ET.parse("gods.xml")
        raet = tree.getroot()
        for god in raet.findall("god"):
            if god.get("name") == self.user_god:
                if current_god == "anhur":
                    self.sk1_bs = string_with_commas_to_list(god.find("sk1bs").text, True)
                else:
                    self.sk1_bs = string_with_commas_to_list(god.find("sk1bs").text, False)
                if current_god == "hachiman":
                    self.sk1_ps = string_with_commas_to_list(god.find("sk1ps").text, False)
                else:
                    self.sk1_ps = float(god.find("sk1ps").text)
                self.sk1_bs2 = string_with_commas_to_list(god.find("sk1bs2").text, False)
                self.sk1_ps2 = float(god.find("sk1ps2").text)

                if current_god == "hou-yi" or current_god == "skadi":
                    self.sk2_bs = string_with_commas_to_list(god.find("sk2bs").text, True)
                else:
                    self.sk2_bs = string_with_commas_to_list(god.find("sk2bs").text, False)
                self.sk2_ps = float(god.find("sk2ps").text)
                if current_god == "skadi":
                    self.sk2_bs2 = string_with_commas_to_list(god.find("sk2bs2").text, True)
                else:
                    self.sk2_bs2 = string_with_commas_to_list(god.find("sk2bs2").text, False)
                self.sk2_ps2 = float(god.find("sk2ps2").text)

                self.sk3_bs = string_with_commas_to_list(god.find("sk3bs").text, False)
                self.sk3_ps = float(god.find("sk3ps").text)
                if current_god == "isis":
                    self.sk3_bs2 = string_with_commas_to_list(god.find("sk3bs2").text, True)
                else:
                    self.sk3_bs2 = string_with_commas_to_list(god.find("sk3bs2").text, False)
                self.sk3_ps2 = float(god.find("sk3ps2").text)

                if current_god == "nemesis":
                    self.sk4_bs = string_with_commas_to_list(god.find("sk4bs").text, True)
                else:
                    self.sk4_bs = string_with_commas_to_list(god.find("sk4bs").text, False)
                self.sk4_ps = float(god.find("sk4ps").text)
                self.sk4_bs2 = string_with_commas_to_list(god.find("sk4bs2").text, False)
                self.sk4_ps2 = float(god.find("sk4ps2").text)

                self.base_ba_d_simple = int(god.find("base_ba_d_simple").text)
                self.base_ba_d_per_level = float(god.find("base_ba_d_per_level").text)
                self.base_ba_d_power_multiplier = float(god.find("base_ba_d_power_multiplier").text)
                self.ba_progression = string_with_commas_to_list(god.find("ba_progression").text, True)

                self.base_mana = int(god.find("base_mana").text)
                self.mana_per_level = int(god.find("mana_per_level").text)

                break

        self.killeable_targets = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # Load targets stats

        self.targets = selected_targets

        self.targets_number = 1
        for i in self.targets:
            total_targets = 0
            if i != "":
                total_targets = total_targets + 1
            else:
                break

        if self.targets[0] == "":
            self.target_1_btn.source = "nothing.png"
            self.target_1_lvl_down_btn.source = "nothing.png"#
            self.target_1_lvl_down_btn.disabled = True#
            self.target_1_lvl_btn.source = "nothing.png"
            self.target_1_lvl_up_btn.source = "nothing.png"
            self.target_1_lvl_up_btn.disabled = True
            self.target_1_cidh_state.source = "nothing.png"
            #self.shield_icon_1.source = "nothing.png"
            #self.shield_icon_1.disabled = True
        else:
            self.target_1_btn.source = selected_targets[0] + ".png"
            self.target_1_lvl_down_btn.source = "nothing.png"#
            self.target_1_lvl_down_btn.disabled = True#
            self.target_1_lvl_btn.source = "1.png"#
            self.target_1_lvl_up_btn.source = "right_arrow.png"#
            self.target_1_lvl_up_btn.disabled = False#
            #self.shield_icon_1.source = "shield_icon.png"#
            #self.shield_icon_1.disabled = False#
            for god in raet.findall("god"):
                if god.get("name") == self.targets[0]:
                    self.target_1_base_health = int(god.find("base_health").text)
                    self.target_1_health_per_level = int(god.find("health_per_level").text)
                    self.target_1_base_p_prot = int(god.find("base_p_prot").text)
                    self.target_1_p_prot_per_level = float(god.find("p_prot_per_level").text)
                    self.target_1_base_m_prot = int(god.find("base_m_prot").text)
                    self.target_1_m_prot_per_level = float(god.find("m_prot_per_level").text)
                    break
            self.target_1_lvl = 1
            h = self.target_1_base_health + self.target_1_health_per_level
            p = self.target_1_base_p_prot + self.target_1_p_prot_per_level
            if current_god == "loki":
                if self.loki_combo_A(h, p):
                    self.killeable_targets[0][0] = 1
                    self.target_1_cidh_state.source = "cidh_answer_yes.png"#
                else:#
                    self.target_1_cidh_state.source = "cidh_answer_no.png"#
                if self.loki_combo_B(h, p):
                    self.killeable_targets[1][0] = 1
                if self.loki_combo_C(h, p):
                    self.killeable_targets[2][0] = 1

        if self.targets[1] == "":
            self.target_2_btn.source = "nothing.png"
            self.target_2_lvl_down_btn.source = "nothing.png"
            self.target_2_lvl_down_btn.disabled = True
            self.target_2_lvl_btn.source = "nothing.png"
            self.target_2_lvl_up_btn.source = "nothing.png"
            self.target_2_lvl_up_btn.disabled = True
            self.target_2_cidh_state.source = "nothing.png"
            #self.shield_icon_2.source = "nothing.png"
            #self.shield_icon_2.disabled = True
        else:
            self.target_2_btn.source = selected_targets[1] + ".png"
            self.target_2_lvl_down_btn.source = "nothing.png"
            self.target_2_lvl_down_btn.disabled = True
            self.target_2_lvl_btn.source = "1.png"
            self.target_2_lvl_up_btn.source = "right_arrow.png"
            self.target_2_lvl_up_btn.disabled = False
            #self.shield_icon_2.source = "shield_icon.png"
            #self.shield_icon_2.disabled = False
            for god in raet.findall("god"):
                if god.get("name") == self.targets[1]:
                    self.target_2_base_health = int(god.find("base_health").text)
                    self.target_2_health_per_level = int(god.find("health_per_level").text)
                    self.target_2_base_p_prot = int(god.find("base_p_prot").text)
                    self.target_2_p_prot_per_level = float(god.find("p_prot_per_level").text)
                    self.target_2_base_m_prot = int(god.find("base_m_prot").text)
                    self.target_2_m_prot_per_level = float(god.find("m_prot_per_level").text)
                    break
            self.target_2_lvl = 1
            h = self.target_2_base_health + self.target_2_health_per_level
            p = self.target_2_base_p_prot + self.target_2_p_prot_per_level
            if current_god == "loki":
                if self.loki_combo_A(h, p):
                    self.killeable_targets[0][1] = 1
                    self.target_2_cidh_state.source = "cidh_answer_yes.png"
                else:
                    self.target_2_cidh_state.source = "cidh_answer_no.png"
                if self.loki_combo_B(h, p):
                    self.killeable_targets[1][1] = 1
                if self.loki_combo_C(h, p):
                    self.killeable_targets[2][1] = 1

        if self.targets[2] == "":
            self.target_3_btn.source = "nothing.png"
            self.target_3_lvl_down_btn.source = "nothing.png"
            self.target_3_lvl_down_btn.disabled = True
            self.target_3_lvl_btn.source = "nothing.png"
            self.target_3_lvl_up_btn.source = "nothing.png"
            self.target_3_lvl_up_btn.disabled = True
            self.target_3_cidh_state.source = "nothing.png"
            #self.shield_icon_3.source = "nothing.png"
            #self.shield_icon_3.disabled = True
        else:
            self.target_3_btn.source = selected_targets[2] + ".png"
            self.target_3_lvl_down_btn.source = "nothing.png"
            self.target_3_lvl_down_btn.disabled = True
            self.target_3_lvl_btn.source = "1.png"
            self.target_3_lvl_up_btn.source = "right_arrow.png"
            self.target_3_lvl_up_btn.disabled = False
            #self.shield_icon_3.source = "shield_icon.png"
            #self.shield_icon_3.disabled = False
            for god in raet.findall("god"):
                if god.get("name") == self.targets[2]:
                    self.target_3_base_health = int(god.find("base_health").text)
                    self.target_3_health_per_level = int(god.find("health_per_level").text)
                    self.target_3_base_p_prot = int(god.find("base_p_prot").text)
                    self.target_3_p_prot_per_level = float(god.find("p_prot_per_level").text)
                    self.target_3_base_m_prot = int(god.find("base_m_prot").text)
                    self.target_3_m_prot_per_level = float(god.find("m_prot_per_level").text)
                    break
            self.target_3_lvl = 1
            h = self.target_3_base_health + self.target_3_health_per_level
            p = self.target_3_base_p_prot + self.target_3_p_prot_per_level
            if current_god == "loki":
                if self.loki_combo_A(h, p):
                    self.killeable_targets[0][2] = 1
                    self.target_3_cidh_state.source = "cidh_answer_yes.png"
                else:
                    self.target_3_cidh_state.source = "cidh_answer_no.png"
                if self.loki_combo_B(h, p):
                    self.killeable_targets[1][2] = 1
                if self.loki_combo_C(h, p):
                    self.killeable_targets[2][2] = 1

        if self.targets[3] == "":
            self.target_4_btn.source = "nothing.png"
            self.target_4_lvl_down_btn.source = "nothing.png"
            self.target_4_lvl_down_btn.disabled = True
            self.target_4_lvl_btn.source = "nothing.png"
            self.target_4_lvl_up_btn.source = "nothing.png"
            self.target_4_lvl_up_btn.disabled = True
            self.target_4_cidh_state.source = "nothing.png"
            #self.shield_icon_4.source = "nothing.png"
            #self.shield_icon_4.disabled = True
        else:
            self.target_4_btn.source = selected_targets[3] + ".png"
            self.target_4_lvl_down_btn.source = "nothing.png"
            self.target_4_lvl_down_btn.disabled = True
            self.target_4_lvl_btn.source = "1.png"
            self.target_4_lvl_up_btn.source = "right_arrow.png"
            self.target_4_lvl_up_btn.disabled = False
            #self.shield_icon_4.source = "shield_icon.png"
            #self.shield_icon_4.disabled = False
            for god in raet.findall("god"):
                if god.get("name") == self.targets[3]:
                    self.target_4_base_health = int(god.find("base_health").text)
                    self.target_4_health_per_level = int(god.find("health_per_level").text)
                    self.target_4_base_p_prot = int(god.find("base_p_prot").text)
                    self.target_4_p_prot_per_level = float(god.find("p_prot_per_level").text)
                    self.target_4_base_m_prot = int(god.find("base_m_prot").text)
                    self.target_4_m_prot_per_level = float(god.find("m_prot_per_level").text)
                    break
            self.target_4_lvl = 1
            h = self.target_4_base_health + self.target_4_health_per_level
            p = self.target_4_base_p_prot + self.target_4_p_prot_per_level
            if current_god == "loki":
                if self.loki_combo_A(h, p):
                    self.killeable_targets[0][3] = 1
                    self.target_4_cidh_state.source = "cidh_answer_yes.png"
                else:
                    self.target_4_cidh_state.source = "cidh_answer_no.png"
                if self.loki_combo_B(h, p):
                    self.killeable_targets[1][3] = 1
                if self.loki_combo_C(h, p):
                    self.killeable_targets[2][3] = 1

        if self.targets[4] == "":
            self.target_5_btn.source = "nothing.png"
            self.target_5_lvl_down_btn.source = "nothing.png"
            self.target_5_lvl_down_btn.disabled = True
            self.target_5_lvl_btn.source = "nothing.png"
            self.target_5_lvl_up_btn.source = "nothing.png"
            self.target_5_lvl_up_btn.disabled = True
            self.target_5_cidh_state.source = "nothing.png"
            #self.shield_icon_5.source = "nothing.png"
            #self.shield_icon_5.disabled = True
        else:
            self.target_5_btn.source = selected_targets[4] + ".png"
            self.target_5_lvl_down_btn.source = "nothing.png"
            self.target_5_lvl_down_btn.disabled = True
            self.target_5_lvl_btn.source = "1.png"
            self.target_5_lvl_up_btn.source = "right_arrow.png"
            self.target_5_lvl_up_btn.disabled = False
            #self.shield_icon_5.source = "shield_icon.png"
            #self.shield_icon_5.disabled = False
            for god in raet.findall("god"):
                if god.get("name") == self.targets[4]:
                    self.target_5_base_health = int(god.find("base_health").text)
                    self.target_5_health_per_level = int(god.find("health_per_level").text)
                    self.target_5_base_p_prot = int(god.find("base_p_prot").text)
                    self.target_5_p_prot_per_level = float(god.find("p_prot_per_level").text)
                    self.target_5_base_m_prot = int(god.find("base_m_prot").text)
                    self.target_5_m_prot_per_level = float(god.find("m_prot_per_level").text)
                    break
            self.target_5_lvl = 1
            h = self.target_5_base_health + self.target_5_health_per_level
            p = self.target_5_base_p_prot + self.target_5_p_prot_per_level
            if current_god == "loki":
                if self.loki_combo_A(h, p):
                    self.killeable_targets[0][4] = 1
                    self.target_5_cidh_state.source = "cidh_answer_yes.png"
                else:
                    self.target_5_cidh_state.source = "cidh_answer_no.png"
                if self.loki_combo_B(h, p):
                    self.killeable_targets[1][4] = 1
                if self.loki_combo_C(h, p):
                    self.killeable_targets[2][4] = 1

        self.player_lvl_down_btn.source = "nothing.png"
        self.player_lvl_down_btn.disabled = True
        self.player_lvl_indicator.source = "1.png"
        self.player_lvl_up_btn.source = "right_arrow.png"
        self.player_lvl_up_btn.disabled = False

        self.combos_number = self.manager.get_screen("combo screen").combos_number[current_god]
        self.selected_combo = 1
        self.show_killeable_targets()

    def reset_screen(self):
        self.targets = ["", "", "", "", ""]
        self.user_god = ""

        #user god stats
        self.sk1_bs = 0
        self.sk1_ps = 0
        self.sk1_bs2 = 0
        self.sk1_ps2 = 0
        self.sk2_bs = 0
        self.sk2_ps = 0
        self.sk2_bs2 = 0
        self.sk2_ps2 = 0
        self.sk3_bs = 0
        self.sk3_ps = 0
        self.sk3_bs2 = 0
        self.sk3_ps2 = 0
        self.sk4_bs = 0
        self.sk4_ps = 0
        self.sk4_bs2 = 0
        self.sk4_ps2 = 0

        self.player_lvl = 1

        self.base_ba_d_simple = 0
        self.base_ba_d_per_level = 0.0
        self.base_ba_d_power_multiplier = 0
        self.ba_progression = []

        self.base_mana = 0
        self.mana_per_level = 0

        #targets stats
        self.target_1_base_health = 0
        self.target_1_health_per_level = 0
        self.target_1_base_p_prot = 0.0
        self.target_1_p_prot_per_level = 0.0
        self.target_1_base_m_prot = 0.0
        self.target_1_m_prot_per_level = 0.0

        self.target_2_base_health = 0
        self.target_2_health_per_level = 0
        self.target_2_base_p_prot = 0.0
        self.target_2_p_prot_per_level = 0.0
        self.target_2_base_m_prot = 0.0
        self.target_2_m_prot_per_level = 0.0

        self.target_3_base_health = 0
        self.target_3_health_per_level = 0
        self.target_3_base_p_prot = 0.0
        self.target_3_p_prot_per_level = 0.0
        self.target_3_base_m_prot = 0.0
        self.target_3_m_prot_per_level = 0.0

        self.target_4_base_health = 0
        self.target_4_health_per_level = 0
        self.target_4_base_p_prot = 0.0
        self.target_4_p_prot_per_level = 0.0
        self.target_4_base_m_prot = 0.0
        self.target_4_m_prot_per_level = 0.0

        self.target_5_base_health = 0
        self.target_5_health_per_level = 0
        self.target_5_base_p_prot = 0.0
        self.target_5_p_prot_per_level = 0.0
        self.target_5_base_m_prot = 0.0
        self.target_5_m_prot_per_level = 0.0

        self.skills_levels = [0, 0, 0, 0]

        self.target_1_lvl = 1
        self.target_2_lvl = 1
        self.target_3_lvl = 1
        self.target_4_lvl = 1
        self.target_5_lvl = 1

        self.final_build = []  # [obj1, obj2, obj3, obj4, obj5, obj6]
        self.current_build = [nothing, nothing, nothing, nothing, nothing, nothing]
        self.building_order = []  # [[], [], [], [], [], []]
        self.current_slot = 1
        self.current_tree_item = 1
        self.finished_build = False

        self.combos_number = 0

        self.killeable_targets = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        self.selected_combo = 1

        self.targets_number = 1

        self.edit_mode = False

        self.p_void_shield_reduction = 0
        self.mask_multiplier = 1.0
        self.total_power = 0.0

        self.warrior_bane = False
        self.titan_bane = False

        self.flat_penetration = 0
        self.mages_blessing_buff = 0
        self.heartseeker_buff = 0
        self.crusher_flat_buff = 0
        self.crusher_power_buff = 0
        self.hunters_blessing_buff = 0
        self.hydras_buff = 1.0

        self.qins = False #

        self.power_buff = False
        self.power_potion = False
        self.power_elixir = False
        self.frenzy = False
        self.frenzy_upgraded = False
        self.sunder = False
        self.sunder_upgraded = False

        self.camp_buff = 1.0
        self.elixir_buff = 1.0
        self.camp_buff_against_gods = 1.0
        self.power_potion_buff = 0.0
        self.frenzy_buff = 1.0
        self.sunder_upgraded_buff = 1.0

    def next_combo(self):
        self.selected_combo = self.selected_combo + 1
        if self.selected_combo > self.combos_number:
            self.selected_combo = 1
        self.show_killeable_targets()

    def show_killeable_targets(self):
        if self.selected_combo == 1:
            if self.killeable_targets[0][0] == 1:
                self.target_1_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_1_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[0][1] == 1:
                self.target_2_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_2_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[0][2] == 1:
                self.target_3_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_3_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[0][3] == 1:
                self.target_4_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_4_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[0][4] == 1:
                self.target_5_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_5_cidh_state.source = "cidh_answer_no.png"
        elif self.selected_combo == 2:
            if self.killeable_targets[1][0] == 1:
                self.target_1_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_1_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[1][1] == 1:
                self.target_2_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_2_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[1][2] == 1:
                self.target_3_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_3_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[1][3] == 1:
                self.target_4_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_4_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[1][4] == 1:
                self.target_5_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_5_cidh_state.source = "cidh_answer_no.png"
        elif self.selected_combo == 3:
            if self.killeable_targets[2][0] == 1:
                self.target_1_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_1_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[2][1] == 1:
                self.target_2_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_2_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[2][2] == 1:
                self.target_3_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_3_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[2][3] == 1:
                self.target_4_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_4_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[2][4] == 1:
                self.target_5_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_5_cidh_state.source = "cidh_answer_no.png"
        elif self.selected_combo == 4:
            if self.killeable_targets[3][0] == 1:
                self.target_1_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_1_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[3][1] == 1:
                self.target_2_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_2_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[3][2] == 1:
                self.target_3_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_3_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[3][3] == 1:
                self.target_4_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_4_cidh_state.source = "cidh_answer_no.png"

            if self.killeable_targets[3][4] == 1:
                self.target_5_cidh_state.source = "cidh_answer_yes.png"
            else:
                self.target_5_cidh_state.source = "cidh_answer_no.png"
        k = 0
        for i in self.targets:
            k = k + 1
            if i == "":
                if k == 1:
                    self.target_1_cidh_state.source = "nothing.png"
                elif k == 2:
                    self.target_2_cidh_state.source = "nothing.png"
                elif k == 3:
                    self.target_3_cidh_state.source = "nothing.png"
                elif k == 4:
                    self.target_4_cidh_state.source = "nothing.png"
                elif k == 5:
                    self.target_5_cidh_state.source = "nothing.png"

        if self.killeable_targets[0][0] == 0 and self.killeable_targets[0][1] == 0 and self.killeable_targets[0][2] == 0 and self.killeable_targets[0][3] == 0 and self.killeable_targets[0][4] == 0:
            if self.selected_combo == 1:
                self.combos_indicator_btn.source = "combos_indicator_a.png"
                self.combo_indicator_btn.source = "combo_indicator_a.png"
                self.combo_a_ind.source = "selected_combo_red.png"
            else:
                self.combo_a_ind.source = "unselected_combo_red.png"
        else:
            if self.selected_combo == 1:
                self.combos_indicator_btn.source = "combos_indicator_a.png"
                self.combo_indicator_btn.source = "combo_indicator_a.png"
                self.combo_a_ind.source = "selected_combo_green.png"
            else:
                self.combo_a_ind.source = "unselected_combo_green.png"

        if self.killeable_targets[1][0] == 0 and self.killeable_targets[1][1] == 0 and self.killeable_targets[1][2] == 0 and self.killeable_targets[1][3] == 0 and self.killeable_targets[1][4] == 0:
            if self.selected_combo == 2:
                self.combos_indicator_btn.source = "combos_indicator_b.png"
                self.combo_indicator_btn.source = "combo_indicator_b.png"
                self.combo_b_ind.source = "selected_combo_red.png"
            else:
                self.combo_b_ind.source = "unselected_combo_red.png"
        else:
            if self.selected_combo == 2:
                self.combos_indicator_btn.source = "combos_indicator_b.png"
                self.combo_indicator_btn.source = "combo_indicator_b.png"
                self.combo_b_ind.source = "selected_combo_green.png"
            else:
                self.combo_b_ind.source = "unselected_combo_green.png"

        if self.killeable_targets[2][0] == 0 and self.killeable_targets[2][1] == 0 and self.killeable_targets[2][2] == 0 and self.killeable_targets[2][3] == 0 and self.killeable_targets[2][4] == 0:
            if self.selected_combo == 3:
                self.combos_indicator_btn.source = "combos_indicator_c.png"
                self.combo_indicator_btn.source = "combo_indicator_c.png"
                self.combo_c_ind.source = "selected_combo_red.png"
            else:
                self.combo_c_ind.source = "unselected_combo_red.png"
        else:
            if self.selected_combo == 3:
                self.combos_indicator_btn.source = "combos_indicator_c.png"
                self.combo_indicator_btn.source = "combo_indicator_c.png"
                self.combo_c_ind.source = "selected_combo_green.png"
            else:
                self.combo_c_ind.source = "unselected_combo_green.png"

        if self.killeable_targets[3][0] == 0 and self.killeable_targets[3][1] == 0 and self.killeable_targets[3][2] == 0 and self.killeable_targets[3][3] == 0 and self.killeable_targets[3][4] == 0:
            if self.selected_combo == 4:
                self.combos_indicator_btn.source = "combos_indicator_d.png"
                self.combo_indicator_btn.source = "combo_indicator_d.png"
                self.combo_d_ind.source = "selected_combo_red.png"
            else:
                self.combo_d_ind.source = "unselected_combo_red.png"
        else:
            if self.selected_combo == 4:
                self.combos_indicator_btn.source = "combos_indicator_d.png"
                self.combo_indicator_btn.source = "combo_indicator_d.png"
                self.combo_d_ind.source = "selected_combo_green.png"
            else:
                self.combo_d_ind.source = "unselected_combo_green.png"

        if self.combos_number == 1:
            self.combo_b_ind.source = "nothing.png"
            self.combo_c_ind.source = "nothing.png"
            self.combo_d_ind.source = "nothing.png"
        elif self.combos_number == 2:
            self.combo_c_ind.source = "nothing.png"
            self.combo_d_ind.source = "nothing.png"
        elif self.combos_number == 3:
            self.combo_d_ind.source = "nothing.png"

    def level_up_skill(self, skill_n):
        self.skills_levels[skill_n] = self.skills_levels[skill_n] + 1

        self.skill_1_lvl_img.source = "sk_l_" + str(self.skills_levels[0]) + ".jpg"
        self.skill_2_lvl_img.source = "sk_l_" + str(self.skills_levels[1]) + ".jpg"
        self.skill_3_lvl_img.source = "sk_l_" + str(self.skills_levels[2]) + ".jpg"
        self.skill_4_lvl_img.source = "sk_l_" + str(self.skills_levels[3]) + ".jpg"

        if skill_n == 0:
            self.skill_1_lvl_down_btn.source = "down_arrow.png"
            self.skill_1_lvl_down_btn.disabled = False
        if skill_n == 1:
            self.skill_2_lvl_down_btn.source = "down_arrow.png"
            self.skill_2_lvl_down_btn.disabled = False
        if skill_n == 2:
            self.skill_3_lvl_down_btn.source = "down_arrow.png"
            self.skill_3_lvl_down_btn.disabled = False
        if skill_n == 3:
            self.skill_4_lvl_down_btn.source = "down_arrow.png"
            self.skill_4_lvl_down_btn.disabled = False

        if self.skills_levels[0] == 5:
            self.skill_1_lvl_up_btn.source = "nothing.png"
            self.skill_1_lvl_up_btn.disabled = True
            self.skill_1_icon.disabled = True
        if self.skills_levels[1] == 5:
            self.skill_2_lvl_up_btn.source = "nothing.png"
            self.skill_2_lvl_up_btn.disabled = True
            self.skill_2_icon.disabled = True
        if self.skills_levels[2] == 5:
            self.skill_3_lvl_up_btn.source = "nothing.png"
            self.skill_3_lvl_up_btn.disabled = True
            self.skill_3_icon.disabled = True
        if self.skills_levels[3] == 5:
            self.skill_4_lvl_up_btn.source = "nothing.png"
            self.skill_4_lvl_up_btn.disabled = True
            self.skill_4_icon.disabled = True

        self.check_if_icdh(0)
        self.show_killeable_targets()

    def level_down_skill(self, skill_n):
        self.skills_levels[skill_n] = self.skills_levels[skill_n] - 1

        self.skill_1_lvl_img.source = "sk_l_" + str(self.skills_levels[0]) + ".jpg"
        self.skill_2_lvl_img.source = "sk_l_" + str(self.skills_levels[1]) + ".jpg"
        self.skill_3_lvl_img.source = "sk_l_" + str(self.skills_levels[2]) + ".jpg"
        self.skill_4_lvl_img.source = "sk_l_" + str(self.skills_levels[3]) + ".jpg"

        if skill_n == 0:
            self.skill_1_lvl_up_btn.source = "up_arrow.png"
            self.skill_1_lvl_up_btn.disabled = False
            self.skill_1_icon.disabled = False
        if skill_n == 1:
            self.skill_2_lvl_up_btn.source = "up_arrow.png"
            self.skill_2_lvl_up_btn.disabled = False
            self.skill_2_icon.disabled = False
        if skill_n == 2:
            self.skill_3_lvl_up_btn.source = "up_arrow.png"
            self.skill_3_lvl_up_btn.disabled = False
            self.skill_3_icon.disabled = False
        if skill_n == 3:
            self.skill_4_lvl_up_btn.source = "up_arrow.png"
            self.skill_4_lvl_up_btn.disabled = False
            self.skill_4_icon.disabled = False

        if self.skills_levels[0] == 0:
            self.skill_1_lvl_down_btn.source = "nothing.png"
            self.skill_1_lvl_down_btn.disabled = True
        if self.skills_levels[1] == 0:
            self.skill_2_lvl_down_btn.source = "nothing.png"
            self.skill_2_lvl_down_btn.disabled = True
        if self.skills_levels[2] == 0:
            self.skill_3_lvl_down_btn.source = "nothing.png"
            self.skill_3_lvl_down_btn.disabled = True
        if self.skills_levels[3] == 0:
            self.skill_4_lvl_down_btn.source = "nothing.png"
            self.skill_4_lvl_down_btn.disabled = True

        self.check_if_icdh(0)
        self.show_killeable_targets()

    def build_up(self):

        if self.edit_mode == True:
            return

        if self.finished_build == True or self.building_order == []:
            return

        slot = self.current_slot
        item = self.current_tree_item

        buttons_list = [self.item1_img, self.item2_img, self.item3_img,
                        self.item4_img, self.item5_img, self.item6_img]
        current_build = self.current_build

        buttons_list[slot - 1].source = self.building_order[slot - 1][item - 1]
        global item_objects
        current_build[slot - 1] = item_objects[self.building_order[slot - 1][item - 1]]

        item = item + 1
        if elements_number(self.building_order[slot - 1]) < item:
            slot = slot + 1
            item = 1

        if elements_number(self.building_order) < slot:
            self.finished_build = True

        self.current_slot = slot
        self.current_tree_item = item

        self.check_items()
        self.check_if_icdh(0)
        self.show_killeable_targets()

    def level_up_target(self, target_n):
        if target_n == 0:
            self.target_1_lvl = self.target_1_lvl + 1
            self.target_1_lvl_btn.source = str(self.target_1_lvl) + ".png"
            self.target_1_lvl_down_btn.source = "left_arrow.png"
            self.target_1_lvl_down_btn.disabled = False
            if self.target_1_lvl == 20:
                self.target_1_lvl_up_btn.source = "nothing.png"
                self.target_1_lvl_up_btn.disabled = True
        elif target_n == 1:
            self.target_2_lvl = self.target_2_lvl + 1
            self.target_2_lvl_btn.source = str(self.target_2_lvl) + ".png"
            self.target_2_lvl_down_btn.source = "left_arrow.png"
            self.target_2_lvl_down_btn.disabled = False
            if self.target_2_lvl == 20:
                self.target_2_lvl_up_btn.source = "nothing.png"
                self.target_2_lvl_up_btn.disabled = True
        elif target_n == 2:
            self.target_3_lvl = self.target_3_lvl + 1
            self.target_3_lvl_btn.source = str(self.target_3_lvl) + ".png"
            self.target_3_lvl_down_btn.source = "left_arrow.png"
            self.target_3_lvl_down_btn.disabled = False
            if self.target_3_lvl == 20:
                self.target_3_lvl_up_btn.source = "nothing.png"
                self.target_3_lvl_up_btn.disabled = True
        elif target_n == 3:
            self.target_4_lvl = self.target_4_lvl + 1
            self.target_4_lvl_btn.source = str(self.target_4_lvl) + ".png"
            self.target_4_lvl_down_btn.source = "left_arrow.png"
            self.target_4_lvl_down_btn.disabled = False
            if self.target_4_lvl == 20:
                self.target_4_lvl_up_btn.source = "nothing.png"
                self.target_4_lvl_up_btn.disabled = True
        elif target_n == 4:
            self.target_5_lvl = self.target_5_lvl + 1
            self.target_5_lvl_btn.source = str(self.target_5_lvl) + ".png"
            self.target_5_lvl_down_btn.source = "left_arrow.png"
            self.target_5_lvl_down_btn.disabled = False
            if self.target_5_lvl == 20:
                self.target_5_lvl_up_btn.source = "nothing.png"
                self.target_5_lvl_up_btn.disabled = True
        self.check_if_icdh(target_n + 1)
        self.show_killeable_targets()

    def level_down_target(self, target_n):
        if target_n == 0:
            self.target_1_lvl = self.target_1_lvl - 1
            self.target_1_lvl_btn.source = str(self.target_1_lvl) + ".png"
            self.target_1_lvl_up_btn.source = "right_arrow.png"
            self.target_1_lvl_up_btn.disabled = False
            if self.target_1_lvl == 1:
                self.target_1_lvl_down_btn.source = "nothing.png"
                self.target_1_lvl_down_btn.disabled = True
        if target_n == 1:
            self.target_2_lvl = self.target_2_lvl - 1
            self.target_2_lvl_btn.source = str(self.target_2_lvl) + ".png"
            self.target_2_lvl_up_btn.source = "right_arrow.png"
            self.target_2_lvl_up_btn.disabled = False
            if self.target_2_lvl == 1:
                self.target_2_lvl_down_btn.source = "nothing.png"
                self.target_2_lvl_down_btn.disabled = True
        if target_n == 2:
            self.target_3_lvl = self.target_3_lvl - 1
            self.target_3_lvl_btn.source = str(self.target_3_lvl) + ".png"
            self.target_3_lvl_up_btn.source = "right_arrow.png"
            self.target_3_lvl_up_btn.disabled = False
            if self.target_3_lvl == 1:
                self.target_3_lvl_down_btn.source = "nothing.png"
                self.target_3_lvl_down_btn.disabled = True
        if target_n == 3:
            self.target_4_lvl = self.target_4_lvl - 1
            self.target_4_lvl_btn.source = str(self.target_4_lvl) + ".png"
            self.target_4_lvl_up_btn.source = "right_arrow.png"
            self.target_4_lvl_up_btn.disabled = False
            if self.target_4_lvl == 1:
                self.target_4_lvl_down_btn.source = "nothing.png"
                self.target_4_lvl_down_btn.disabled = True
        if target_n == 4:
            self.target_5_lvl = self.target_5_lvl - 1
            self.target_5_lvl_btn.source = str(self.target_5_lvl) + ".png"
            self.target_5_lvl_up_btn.source = "right_arrow.png"
            self.target_5_lvl_up_btn.disabled = False
            if self.target_5_lvl == 1:
                self.target_5_lvl_down_btn.source = "nothing.png"
                self.target_5_lvl_down_btn.disabled = True
        self.check_if_icdh(target_n + 1)
        self.show_killeable_targets()

    def level_up_player(self):
        self.player_lvl = self.player_lvl + 1
        self.player_lvl_indicator.source = str(self.player_lvl) + ".png"
        self.player_lvl_down_btn.source = "left_arrow.png"
        self.player_lvl_down_btn.disabled = False
        if self.player_lvl == 20:
            self.player_lvl_up_btn.source = "nothing.png"
            self.player_lvl_up_btn.disabled = True
        self.check_items()
        self.check_if_icdh(0)
        self.show_killeable_targets()

    def level_down_player(self):
        self.player_lvl = self.player_lvl - 1
        self.player_lvl_indicator.source = str(self.player_lvl) + ".png"
        self.player_lvl_up_btn.source = "right_arrow.png"
        self.player_lvl_up_btn.disabled = False
        if self.player_lvl == 1:
            self.player_lvl_down_btn.source = "nothing.png"
            self.player_lvl_down_btn.disabled = True
        self.check_items()
        self.check_if_icdh(0)
        self.show_killeable_targets()

    def check_items(self):

        total_mana = self.base_mana + self.mana_per_level * self.player_lvl
        total_mana_to_power_percent = 0.0

        self.total_power = 0
        self.flat_penetration = 0
        self.heartseeker_buff = 0.0

        self.p_void_shield_reduction = 0
        self.mask_multiplier = 1.0

        self.warrior_bane = False
        self.titan_bane = False

        self.mages_blessing_buff = 0
        self.crusher_flat_buff = 0
        self.crusher_power_buff = 0
        self.hunters_blessing_buff = 0
        self.hydras_buff = 1.0

        self.qins = False

        self.camp_buff = 1.0
        self.elixir_buff = 1.0
        self.camp_buff_against_gods = 1.0
        self.power_potion_buff = 0.0

        self.frenzy_buff = 1.0
        self.sunder_upgraded_buff = 1.0

        items = self.current_build
        for i in range(0, 6):
            if items[i].name_id == "x_sta2":
                self.mages_blessing_buff = mages_blessing.mages_blessing_buff
            if items[i].name_id == "x_sta3":
                self.hunters_blessing_buff = hunters_blessing.ba_flat_buff
            if items[i].name_id == "p_mor4":
                self.hydras_buff = hydras_star.hydras_multiplier_buff
            if items[i].name_id == "p_mor5":
                self.hydras_buff = hydras_lament.hydras_multiplier_buff
            if items[i].name_id == "p_kat4" and items[i].state != 1:
                self.heartseeker_buff = heartseeker.heartseeker_buff_states[heartseeker.state - 1]
            if items[i].name_id == "p_mac5":
                self.crusher_flat_buff = the_crusher.crusher_flat_buff
                self.crusher_power_buff = the_crusher.crusher_buff_based_on_power
            if items[i].name_id == "p_mac6":
                self.warrior_bane = True
            if items[i].name_id == "p_mac7":
                self.titan_bane = True
            if items[i].name_id == "p_lig3":
                self.qins = True
            if items[i].name_id == "p_rou3":
                self.p_void_shield_reduction = void_shield.aura_penetration

            self.total_power = self.total_power + items[i].power

            total_mana = total_mana + items[i].mana
            total_mana_to_power_percent = total_mana_to_power_percent + items[i].mana_to_power_percent
            
            if items[i].name_id == "x_sta1":
                self.flat_penetration = self.flat_penetration + items[i].penetration_states[items[i].state - 1]
            else:
                self.flat_penetration = self.flat_penetration + items[i].penetration

        self.total_power = self.total_power + total_mana * total_mana_to_power_percent

        if self.power_buff:
            self.total_power = self.total_power + damage_camp_buff.power
            self.camp_buff = 1.0 + damage_camp_buff.total_damage_buff_percent
            self.camp_buff_against_gods = 1.0 + damage_camp_buff.total_damage_buff_percent_against_gods

        if self.power_potion:
            self.total_power = self.total_power + potion_of_physical_might.power
            self.power_potion_buff = potion_of_physical_might.ability_damage_buff_based_on_power
            
        if self.power_elixir:
            self.elixir_buff = 1.0 + elixir_of_power.power_buff_percent

        if self.frenzy:
            self.frenzy_buff = frenzy.total_damage_buff

        if self.frenzy_upgraded:
            self.frenzy_buff = frenzy.total_damage_buff
            self.flat_penetration = self.flat_penetration + frenzy_upgraded.penetration

        if self.sunder_upgraded:
            self.sunder_upgraded_buff = sunder_upgraded.total_damage_buff

        if self.total_power > 400:
            self.total_power = 400

        if self.flat_penetration > 50:
            self.flat_penetration = 50
            
    def check_if_icdh(self, option):

        h = 0
        p = 0

        if option == 0:
            if self.user_god == "loki":
                i = 0
                for target in self.targets:
                    if target != "":
                        if i == 0:
                            h = self.target_1_base_health + self.target_1_health_per_level * self.target_1_lvl
                            p = self.target_1_base_p_prot + self.target_1_p_prot_per_level * self.target_1_lvl
                        elif i == 1:
                            h = self.target_2_base_health + self.target_2_health_per_level * self.target_2_lvl
                            p = self.target_2_base_p_prot + self.target_2_p_prot_per_level * self.target_2_lvl
                        elif i == 2:
                            h = self.target_3_base_health + self.target_3_health_per_level * self.target_3_lvl
                            p = self.target_3_base_p_prot + self.target_3_p_prot_per_level * self.target_3_lvl
                        elif i == 3:
                            h = self.target_4_base_health + self.target_4_health_per_level * self.target_4_lvl
                            p = self.target_4_base_p_prot + self.target_4_p_prot_per_level * self.target_4_lvl
                        elif i == 4:
                            h = self.target_5_base_health + self.target_5_health_per_level * self.target_5_lvl
                            p = self.target_5_base_p_prot + self.target_5_p_prot_per_level * self.target_5_lvl

                        if self.loki_combo_A(h, p):
                            self.killeable_targets[0][i] = 1
                        else:
                            self.killeable_targets[0][i] = 0
                        if self.loki_combo_B(h, p):
                            self.killeable_targets[1][i] = 1
                        else:
                            self.killeable_targets[1][i] = 0
                        if self.loki_combo_C(h, p):
                            self.killeable_targets[2][i] = 1
                        else:
                            self.killeable_targets[2][i] = 0
                        i = i + 1
                    else:
                        break

        elif option == 1:
            h = self.target_1_base_health + self.target_1_health_per_level * self.target_1_lvl
            p = self.target_1_base_p_prot + self.target_1_p_prot_per_level * self.target_1_lvl

        elif option == 2:
            h = self.target_2_base_health + self.target_2_health_per_level * self.target_2_lvl
            p = self.target_2_base_p_prot + self.target_2_p_prot_per_level * self.target_2_lvl

        elif option == 3:
            h = self.target_3_base_health + self.target_3_health_per_level * self.target_3_lvl
            p = self.target_3_base_p_prot + self.target_3_p_prot_per_level * self.target_3_lvl

        elif option == 4:
            h = self.target_4_base_health + self.target_4_health_per_level * self.target_4_lvl
            p = self.target_4_base_p_prot + self.target_4_p_prot_per_level * self.target_4_lvl

        elif option == 5:
            h = self.target_5_base_health + self.target_5_health_per_level * self.target_5_lvl
            p = self.target_5_base_p_prot + self.target_5_p_prot_per_level * self.target_5_lvl

        if option != 0:
            if self.user_god == "loki":
                if self.loki_combo_A(h, p):
                    self.killeable_targets[0][option - 1] = 1
                else:
                    self.killeable_targets[0][option - 1] = 0
                if self.loki_combo_B(h, p):
                    self.killeable_targets[1][option - 1] = 1
                else:
                    self.killeable_targets[1][option - 1] = 0
                if self.loki_combo_C(h, p):
                    self.killeable_targets[2][option - 1] = 1
                else:
                    self.killeable_targets[2][option - 1] = 0

    edit_mode = False
    def toggle_edit_mode(self):
        if self.edit_mode == False:
            self.edit_mode = True
            self.edit_item_btn.source = "interface_edit_item_2.png"
        else:
            self.edit_mode = False
            self.edit_item_btn.source = "interface_edit_item.png"

    def upgrade_item_or_do_nothing(self, item_number):
        i = item_number - 1
        if self.edit_mode == True:
            if self.current_build[i].max_state != 1 and (self.current_build[i].state < self.current_build[i].max_state):
                self.current_build[i].state = self.current_build[i].state + 1
                if self.current_build[i].name_id == "x_sta1_1":
                    self.current_build[i].update_penetration()
                if self.current_build[i].name_id == "x_sta3_1":
                    self.current_build[i].update_ba_flat_buff()
                if self.current_build[i].name_id == "p_mor3":
                    self.current_build[i].update_mana()
                if self.current_build[i].name_id == "p_spi3":
                    self.current_build[i].update_power()
                if self.current_build[i].name_id == "p_spi6":
                    self.current_build[i].update_power()
                if self.current_build[i].name_id == "p_kat4":
                    self.current_build[i].update_heartseeker_buff()
                if i == 0:
                    self.item1_img.source = editar_numero_de_imagen(self.item1_img.source, str(self.current_build[i].state))
                elif i == 1:
                    self.item2_img.source = editar_numero_de_imagen(self.item2_img.source, str(self.current_build[i].state))
                elif i == 2:
                    self.item3_img.source = editar_numero_de_imagen(self.item3_img.source, str(self.current_build[i].state))
                elif i == 3:
                    self.item4_img.source = editar_numero_de_imagen(self.item4_img.source, str(self.current_build[i].state))
                elif i == 4:
                    self.item5_img.source = editar_numero_de_imagen(self.item5_img.source, str(self.current_build[i].state))
                elif i == 5:
                    self.item6_img.source = editar_numero_de_imagen(self.item6_img.source, str(self.current_build[i].state))
                self.check_items()
                self.check_if_icdh(0)
                self.show_killeable_targets()
            elif self.current_build[i].name_id == "p_kat4" and (self.current_build[i].state == self.current_build[i].max_state):
                self.current_build[i].state = self.current_build[i].state - 1
                self.current_build[i].update_heartseeker_buff()
                if i == 0:
                    self.item1_img.source = editar_numero_de_imagen(self.item1_img.source, str(self.current_build[i].state))
                elif i == 1:
                    self.item2_img.source = editar_numero_de_imagen(self.item2_img.source, str(self.current_build[i].state))
                elif i == 2:
                    self.item3_img.source = editar_numero_de_imagen(self.item3_img.source, str(self.current_build[i].state))
                elif i == 3:
                    self.item4_img.source = editar_numero_de_imagen(self.item4_img.source, str(self.current_build[i].state))
                elif i == 4:
                    self.item5_img.source = editar_numero_de_imagen(self.item5_img.source, str(self.current_build[i].state))
                elif i == 5:
                    self.item6_img.source = editar_numero_de_imagen(self.item6_img.source, str(self.current_build[i].state))
                self.check_items()
                self.check_if_icdh(0)
                self.show_killeable_targets()
        else:
            self.build_up()

    p_void_shield_reduction = 0
    mask_multiplier = 1.0
    total_power = 0.0

    warrior_bane = False
    titan_bane = False

    flat_penetration = 0
    mages_blessing_buff = 0
    heartseeker_buff = 0
    crusher_flat_buff = 0
    crusher_power_buff = 0
    hunters_blessing_buff = 0
    hydras_buff = 1.0

    qins = False #
    
    power_buff = False
    power_potion = False
    power_elixir = False
    frenzy = False
    frenzy_upgraded = False
    sunder = False
    sunder_upgraded = False
    
    camp_buff = 1.0
    elixir_buff = 1.0
    camp_buff_against_gods = 1.0
    power_potion_buff = 0.0
    frenzy_buff = 1.0
    sunder_upgraded_buff = 1.0

    def loki_combo_A(self, health, prot):

        if self.skills_levels[0] == 0 or self.skills_levels[2] == 0 or self.skills_levels[3] == 0:
            return False

        if self.sunder:
            health = health - health * sunder.current_health_true_damage
        elif self.sunder_upgraded:
            health = health - health * sunder_upgraded.current_health_true_damage

        prot = prot - self.p_void_shield_reduction
        if self.warrior_bane == True:
            prot = prot - prot * warriors_bane.percent_penetration
        elif self.titan_bane == True:
            if prot <= titans_bane.percent_penetration_protections_scaling[0]:
                prot = prot - prot * titans_bane.percent_penetration
            elif titans_bane.percent_penetration_protections_scaling[0] < prot < titans_bane.percent_penetration_protections_scaling[1]:
                total_percent_pen = titans_bane.percent_penetration + titans_bane.percent_pen_per_prot * (prot - titans_bane.percent_penetration_protections_scaling[0])
                prot = prot - prot * total_percent_pen
            elif prot >= titans_bane.percent_penetration_protections_scaling[1]:
                prot = prot - prot * titans_bane.max_percent_penetration
        prot = prot - self.flat_penetration

        sk4d = (self.sk4_bs[self.skills_levels[3] - 1] + self.sk4_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk4d = sk4d - sk4d * prot / (prot + 100)
        sk4d = approximate_number_to_int(sk4d)

        mag_bless_1_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff
        mag_bless_1_dmg = mag_bless_1_dmg - mag_bless_1_dmg * prot / (prot + 100)
        mag_bless_1_dmg = approximate_number_to_int(mag_bless_1_dmg)

        heartseeker_dmg = self.heartseeker_buff * self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        heartseeker_dmg = heartseeker_dmg - heartseeker_dmg * prot / (prot + 100)
        heartseeker_dmg = approximate_number_to_int(heartseeker_dmg)

        crusher_tick_1_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_1_dmg = crusher_tick_1_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_1_dmg = crusher_tick_1_dmg - crusher_tick_1_dmg * prot / (prot + 100)
        crusher_tick_1_dmg = approximate_number_to_int(crusher_tick_1_dmg)

        crusher_tick_2_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_2_dmg = crusher_tick_2_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_2_dmg = crusher_tick_2_dmg - crusher_tick_2_dmg * prot / (prot + 100)
        crusher_tick_2_dmg = approximate_number_to_int(crusher_tick_2_dmg)

        power_potion_1_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_1_dmg = power_potion_1_dmg - power_potion_1_dmg * prot / (prot + 100)
        power_potion_1_dmg = approximate_number_to_int(power_potion_1_dmg)

        ba_1_dmg = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + self.total_power * self.elixir_buff + self.hunters_blessing_buff) * self.ba_progression[0] * 1.2 * self.hydras_buff * self.mask_multiplier * self.camp_buff_against_gods * self.frenzy_buff * self.sunder_upgraded_buff
        ba_1_dmg = ba_1_dmg - ba_1_dmg * prot / (prot + 100)
        ba_1_dmg = approximate_number_to_int(ba_1_dmg)

        if self.qins == True:
            if health <= qins_sais.qins_health_scaling[0]:
                qins_tick_1_dmg = health * qins_sais.qins_bonus
            elif qins_sais.qins_health_scaling[0] < health < qins_sais.qins_health_scaling[1]:
                total_percent_health_bonus = qins_sais.qins_bonus + qins_sais.percent_hp_per_hp * (health - qins_sais.qins_health_scaling[0])
                qins_tick_1_dmg = health * total_percent_health_bonus
            elif health >= qins_sais.qins_health_scaling[1]:
                qins_tick_1_dmg = health * qins_sais.qins_max_bonus
        else:
            qins_tick_1_dmg = 0
        qins_tick_1_dmg = qins_tick_1_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        qins_tick_1_dmg = qins_tick_1_dmg - qins_tick_1_dmg * prot / (prot + 100)
        qins_tick_1_dmg = approximate_number_to_int(qins_tick_1_dmg)

        sk3d = (self.sk3_bs[self.skills_levels[2] - 1] + self.sk3_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk3d = sk3d - sk3d * prot / (prot + 100)
        sk3d = approximate_number_to_int(sk3d)

        mag_bless_2_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        mag_bless_2_dmg = mag_bless_2_dmg - mag_bless_2_dmg * prot / (prot + 100)
        mag_bless_2_dmg = approximate_number_to_int(mag_bless_2_dmg)

        crusher_tick_3_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_3_dmg = crusher_tick_3_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_3_dmg = crusher_tick_3_dmg - crusher_tick_3_dmg * prot / (prot + 100)
        crusher_tick_3_dmg = approximate_number_to_int(crusher_tick_3_dmg)

        crusher_tick_4_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_4_dmg = crusher_tick_4_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_4_dmg = crusher_tick_4_dmg - crusher_tick_4_dmg * prot / (prot + 100)
        crusher_tick_4_dmg = approximate_number_to_int(crusher_tick_4_dmg)

        power_potion_2_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_2_dmg = power_potion_2_dmg - power_potion_2_dmg * prot / (prot + 100)
        power_potion_2_dmg = approximate_number_to_int(power_potion_2_dmg)

        sk1d_tick_1 = (self.sk1_bs[self.skills_levels[0] - 1] + self.sk1_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk1d_tick_1 = sk1d_tick_1 - sk1d_tick_1 * prot / (prot + 100)
        sk1d_tick_1 = approximate_number_to_int(sk1d_tick_1)

        sk1d_tick_2 = (self.sk1_bs[self.skills_levels[0] - 1] + self.sk1_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk1d_tick_2 = sk1d_tick_2 - sk1d_tick_2 * prot / (prot + 100)
        sk1d_tick_2 = approximate_number_to_int(sk1d_tick_2)

        sk1d_tick_3 = (self.sk1_bs[self.skills_levels[0] - 1] + self.sk1_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk1d_tick_3 = sk1d_tick_3 - sk1d_tick_3 * prot / (prot + 100)
        sk1d_tick_3 = approximate_number_to_int(sk1d_tick_3)

        sk1d_tick_4 = (self.sk1_bs[self.skills_levels[0] - 1] + self.sk1_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk1d_tick_4 = sk1d_tick_4 - sk1d_tick_4 * prot / (prot + 100)
        sk1d_tick_4 = approximate_number_to_int(sk1d_tick_4)

        mag_bless_3_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        mag_bless_3_dmg = mag_bless_3_dmg - mag_bless_3_dmg * prot / (prot + 100)
        mag_bless_3_dmg = approximate_number_to_int(mag_bless_3_dmg)

        crusher_tick_5_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_5_dmg = crusher_tick_5_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_5_dmg = crusher_tick_5_dmg - crusher_tick_5_dmg * prot / (prot + 100)
        crusher_tick_5_dmg = approximate_number_to_int(crusher_tick_5_dmg)

        crusher_tick_6_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_6_dmg = crusher_tick_6_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_6_dmg = crusher_tick_6_dmg - crusher_tick_6_dmg * prot / (prot + 100)
        crusher_tick_6_dmg = approximate_number_to_int(crusher_tick_6_dmg)

        power_potion_3_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_3_dmg = power_potion_3_dmg - power_potion_3_dmg * prot / (prot + 100)
        power_potion_3_dmg = approximate_number_to_int(power_potion_3_dmg)

        total_damage = sk4d + mag_bless_1_dmg + heartseeker_dmg + crusher_tick_1_dmg + crusher_tick_2_dmg + ba_1_dmg + qins_tick_1_dmg
        total_damage = total_damage + sk3d + mag_bless_2_dmg + crusher_tick_3_dmg + crusher_tick_4_dmg + sk1d_tick_1 + sk1d_tick_2
        total_damage = total_damage + sk1d_tick_3 + sk1d_tick_4 + mag_bless_3_dmg + crusher_tick_5_dmg + crusher_tick_6_dmg
        total_damage = total_damage + power_potion_1_dmg + power_potion_2_dmg + power_potion_3_dmg

        remaining_health = health - total_damage
        if remaining_health < 0:
            return True
        else:
            return False

    def loki_combo_B(self, health, prot):

        if self.skills_levels[2] == 0 or self.skills_levels[3] == 0:
            return False

        if self.sunder:
            health = health - health * sunder.current_health_true_damage
        elif self.sunder_upgraded:
            health = health - health * sunder_upgraded.current_health_true_damage

        prot = prot - self.p_void_shield_reduction
        if self.warrior_bane == True:
            prot = prot - prot * warriors_bane.percent_penetration
        elif self.titan_bane == True:
            if prot <= titans_bane.percent_penetration_protections_scaling[0]:
                prot = prot - prot * titans_bane.percent_penetration
            elif titans_bane.percent_penetration_protections_scaling[0] < prot < titans_bane.percent_penetration_protections_scaling[1]:
                total_percent_pen = titans_bane.percent_penetration + titans_bane.percent_pen_per_prot * (prot - titans_bane.percent_penetration_protections_scaling[0])
                prot = prot - prot * total_percent_pen
            elif prot >= titans_bane.percent_penetration_protections_scaling[1]:
                prot = prot - prot * titans_bane.max_percent_penetration
        prot = prot - self.flat_penetration

        sk4d = (self.sk4_bs[self.skills_levels[3] - 1] + self.sk4_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk4d = sk4d - sk4d * prot / (prot + 100)
        sk4d = approximate_number_to_int(sk4d)
        print "---------------------------------"
        print self.total_power
        print sk4d

        mag_bless_1_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        mag_bless_1_dmg = mag_bless_1_dmg - mag_bless_1_dmg * prot / (prot + 100)
        mag_bless_1_dmg = approximate_number_to_int(mag_bless_1_dmg)
        print mag_bless_1_dmg

        heartseeker_dmg = self.heartseeker_buff * self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        heartseeker_dmg = heartseeker_dmg - heartseeker_dmg * prot / (prot + 100)
        heartseeker_dmg = approximate_number_to_int(heartseeker_dmg)
        print heartseeker_dmg

        crusher_tick_1_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_1_dmg = crusher_tick_1_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_1_dmg = crusher_tick_1_dmg - crusher_tick_1_dmg * prot / (prot + 100)
        crusher_tick_1_dmg = approximate_number_to_int(crusher_tick_1_dmg)
        print crusher_tick_1_dmg

        crusher_tick_2_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_2_dmg = crusher_tick_2_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_2_dmg = crusher_tick_2_dmg - crusher_tick_2_dmg * prot / (prot + 100)
        crusher_tick_2_dmg = approximate_number_to_int(crusher_tick_2_dmg)
        print crusher_tick_2_dmg

        power_potion_1_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_1_dmg = power_potion_1_dmg - power_potion_1_dmg * prot / (prot + 100)
        power_potion_1_dmg = approximate_number_to_int(power_potion_1_dmg)

        ba_1_dmg = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + self.total_power * self.elixir_buff + self.hunters_blessing_buff) * self.ba_progression[0] * 1.2 * self.hydras_buff * self.mask_multiplier * self.camp_buff_against_gods * self.frenzy_buff * self.sunder_upgraded_buff
        ba_1_dmg = ba_1_dmg - ba_1_dmg * prot / (prot + 100)
        ba_1_dmg = approximate_number_to_int(ba_1_dmg)
        print ba_1_dmg

        if self.qins == True:
            if health <= qins_sais.qins_health_scaling[0]:
                qins_tick_1_dmg = health * qins_sais.qins_bonus
            elif qins_sais.qins_health_scaling[0] < health < qins_sais.qins_health_scaling[1]:
                total_percent_health_bonus = qins_sais.qins_bonus + qins_sais.percent_hp_per_hp * (health - qins_sais.qins_health_scaling[0])
                qins_tick_1_dmg = health * total_percent_health_bonus
            elif health >= qins_sais.qins_health_scaling[1]:
                qins_tick_1_dmg = health * qins_sais.qins_max_bonus
        else:
            qins_tick_1_dmg = 0
        qins_tick_1_dmg = qins_tick_1_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        qins_tick_1_dmg = qins_tick_1_dmg - qins_tick_1_dmg * prot / (prot + 100)
        qins_tick_1_dmg = approximate_number_to_int(qins_tick_1_dmg)
        print qins_tick_1_dmg

        ba_2_dmg = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + self.total_power * self.elixir_buff + self.hunters_blessing_buff) * self.ba_progression[0] * 1.2 * self.hydras_buff * self.mask_multiplier * self.camp_buff_against_gods * self.frenzy_buff * self.sunder_upgraded_buff
        ba_2_dmg = ba_2_dmg - ba_2_dmg * prot / (prot + 100)
        ba_2_dmg = approximate_number_to_int(ba_2_dmg)
        print ba_2_dmg


        if self.qins == True:
            if health <= qins_sais.qins_health_scaling[0]:
                qins_tick_2_dmg = health * qins_sais.qins_bonus
            elif qins_sais.qins_health_scaling[0] < health < qins_sais.qins_health_scaling[1]:
                total_percent_health_bonus = qins_sais.qins_bonus + qins_sais.percent_hp_per_hp * (health - qins_sais.qins_health_scaling[0])
                qins_tick_2_dmg = health * total_percent_health_bonus
            elif health >= qins_sais.qins_health_scaling[1]:
                qins_tick_2_dmg = health * qins_sais.qins_max_bonus
        else:
            qins_tick_2_dmg = 0
        qins_tick_2_dmg = qins_tick_2_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        qins_tick_2_dmg = qins_tick_2_dmg - qins_tick_2_dmg * prot / (prot + 100)
        qins_tick_2_dmg = approximate_number_to_int(qins_tick_2_dmg)
        print qins_tick_2_dmg

        sk3d = (self.sk3_bs[self.skills_levels[2] - 1] + self.sk3_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk3d = sk3d - sk3d * prot / (prot + 100)
        sk3d = approximate_number_to_int(sk3d)
        print sk3d

        mag_bless_2_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        mag_bless_2_dmg = mag_bless_2_dmg - mag_bless_2_dmg * prot / (prot + 100)
        mag_bless_2_dmg = approximate_number_to_int(mag_bless_2_dmg)
        print mag_bless_2_dmg

        crusher_tick_3_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_3_dmg = crusher_tick_3_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_3_dmg = crusher_tick_3_dmg - crusher_tick_3_dmg * prot / (prot + 100)
        crusher_tick_3_dmg = approximate_number_to_int(crusher_tick_3_dmg)
        print crusher_tick_3_dmg

        crusher_tick_4_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_4_dmg = crusher_tick_4_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_4_dmg = crusher_tick_4_dmg - crusher_tick_4_dmg * prot / (prot + 100)
        crusher_tick_4_dmg = approximate_number_to_int(crusher_tick_4_dmg)
        print crusher_tick_4_dmg

        power_potion_2_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_2_dmg = power_potion_2_dmg - power_potion_2_dmg * prot / (prot + 100)
        power_potion_2_dmg = approximate_number_to_int(power_potion_2_dmg)

        total_damage = sk4d + mag_bless_1_dmg + heartseeker_dmg + crusher_tick_1_dmg + crusher_tick_2_dmg + ba_1_dmg + qins_tick_1_dmg
        total_damage = total_damage + ba_2_dmg + qins_tick_2_dmg + sk3d + mag_bless_2_dmg + crusher_tick_3_dmg + crusher_tick_4_dmg
        total_damage = total_damage + power_potion_1_dmg + power_potion_2_dmg

        print total_damage
        print "---------------------------------"

        remaining_health = health - total_damage
        if remaining_health < 0:
            return True
        else:
            return False

    def loki_combo_C(self, health, prot):

        if self.skills_levels[2] == 0 or self.skills_levels[3] == 0:
            return False

        if self.sunder:
            health = health - health * sunder.current_health_true_damage
        elif self.sunder_upgraded:
            health = health - health * sunder_upgraded.current_health_true_damage

        prot = prot - self.p_void_shield_reduction
        if self.warrior_bane == True:
            prot = prot - prot * warriors_bane.percent_penetration
        elif self.titan_bane == True:
            if prot <= titans_bane.percent_penetration_protections_scaling[0]:
                prot = prot - prot * titans_bane.percent_penetration
            elif titans_bane.percent_penetration_protections_scaling[0] < prot < titans_bane.percent_penetration_protections_scaling[1]:
                total_percent_pen = titans_bane.percent_penetration + titans_bane.percent_pen_per_prot * (prot - titans_bane.percent_penetration_protections_scaling[0])
                prot = prot - prot * total_percent_pen
            elif prot >= titans_bane.percent_penetration_protections_scaling[1]:
                prot = prot - prot * titans_bane.max_percent_penetration
        prot = prot - self.flat_penetration

        sk4d = (self.sk4_bs[self.skills_levels[3] - 1] + self.sk4_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk4d = sk4d - sk4d * prot / (prot + 100)
        sk4d = approximate_number_to_int(sk4d)

        mag_bless_1_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        mag_bless_1_dmg = mag_bless_1_dmg - mag_bless_1_dmg * prot / (prot + 100)
        mag_bless_1_dmg = approximate_number_to_int(mag_bless_1_dmg)

        heartseeker_dmg = self.heartseeker_buff * self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        heartseeker_dmg = heartseeker_dmg - heartseeker_dmg * prot / (prot + 100)
        heartseeker_dmg = approximate_number_to_int(heartseeker_dmg)

        crusher_tick_1_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_1_dmg = crusher_tick_1_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_1_dmg = crusher_tick_1_dmg - crusher_tick_1_dmg * prot / (prot + 100)
        crusher_tick_1_dmg = approximate_number_to_int(crusher_tick_1_dmg)

        crusher_tick_2_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_2_dmg = crusher_tick_2_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_2_dmg = crusher_tick_2_dmg - crusher_tick_2_dmg * prot / (prot + 100)
        crusher_tick_2_dmg = approximate_number_to_int(crusher_tick_2_dmg)

        power_potion_1_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_1_dmg = power_potion_1_dmg - power_potion_1_dmg * prot / (prot + 100)
        power_potion_1_dmg = approximate_number_to_int(power_potion_1_dmg)

        ba_1_dmg = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + self.total_power * self.elixir_buff + self.hunters_blessing_buff) * self.ba_progression[0] * 1.2 * self.hydras_buff * self.mask_multiplier * self.camp_buff_against_gods * self.frenzy_buff * self.sunder_upgraded_buff
        ba_1_dmg = ba_1_dmg - ba_1_dmg * prot / (prot + 100)
        ba_1_dmg = approximate_number_to_int(ba_1_dmg)

        if self.qins == True:
            if health <= qins_sais.qins_health_scaling[0]:
                qins_tick_1_dmg = health * qins_sais.qins_bonus
            elif qins_sais.qins_health_scaling[0] < health < qins_sais.qins_health_scaling[1]:
                total_percent_health_bonus = qins_sais.qins_bonus + qins_sais.percent_hp_per_hp * (health - qins_sais.qins_health_scaling[0])
                qins_tick_1_dmg = health * total_percent_health_bonus
            elif health >= qins_sais.qins_health_scaling[1]:
                qins_tick_1_dmg = health * qins_sais.qins_max_bonus
        else:
            qins_tick_1_dmg = 0
        qins_tick_1_dmg = qins_tick_1_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        qins_tick_1_dmg = qins_tick_1_dmg - qins_tick_1_dmg * prot / (prot + 100)
        qins_tick_1_dmg = approximate_number_to_int(qins_tick_1_dmg)

        sk3d = (self.sk3_bs[self.skills_levels[2] - 1] + self.sk3_ps * self.total_power * self.camp_buff_against_gods * self.elixir_buff) * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        sk3d = sk3d - sk3d * prot / (prot + 100)
        sk3d = approximate_number_to_int(sk3d)

        mag_bless_2_dmg = self.mages_blessing_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        mag_bless_2_dmg = mag_bless_2_dmg - mag_bless_2_dmg * prot / (prot + 100)
        mag_bless_2_dmg = approximate_number_to_int(mag_bless_2_dmg)

        crusher_tick_3_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_3_dmg = crusher_tick_3_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_3_dmg = crusher_tick_3_dmg - crusher_tick_3_dmg * prot / (prot + 100)
        crusher_tick_3_dmg = approximate_number_to_int(crusher_tick_3_dmg)

        crusher_tick_4_dmg = self.crusher_flat_buff * 0.5 + self.total_power * self.camp_buff_against_gods * self.elixir_buff * self.crusher_power_buff * 0.5
        crusher_tick_4_dmg = crusher_tick_4_dmg * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        crusher_tick_4_dmg = crusher_tick_4_dmg - crusher_tick_4_dmg * prot / (prot + 100)
        crusher_tick_4_dmg = approximate_number_to_int(crusher_tick_4_dmg)

        power_potion_2_dmg = self.total_power * self.camp_buff * self.power_potion_buff * self.mask_multiplier * self.frenzy_buff * self.sunder_upgraded_buff
        power_potion_2_dmg = power_potion_2_dmg - power_potion_2_dmg * prot / (prot + 100)
        power_potion_2_dmg = approximate_number_to_int(power_potion_2_dmg)

        total_damage = sk4d + mag_bless_1_dmg + heartseeker_dmg + crusher_tick_1_dmg + crusher_tick_2_dmg + ba_1_dmg + qins_tick_1_dmg
        total_damage = total_damage + sk3d + mag_bless_2_dmg + crusher_tick_3_dmg + crusher_tick_4_dmg + power_potion_1_dmg + power_potion_2_dmg

        remaining_health = health - total_damage
        if remaining_health < 0:
            return True
        else:
            return False

class Buffs_Screen(Screen):
    power_buff_btn = ObjectProperty
    power_potion_btn = ObjectProperty
    power_elixir_btn = ObjectProperty
    frenzy_btn = ObjectProperty
    frenzy_upgraded_btn = ObjectProperty
    sunder_btn = ObjectProperty
    sunder_upgraded_btn = ObjectProperty

    def toggle_buff_state(self, buff_number):
        if buff_number == 0:
            if self.manager.get_screen("cidh final screen 2").power_buff:
                self.manager.get_screen("cidh final screen 2").power_buff = False
                self.power_buff_btn.source = "item_x_buf1.png"
                self.power_buff_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").power_buff = True
                self.power_buff_btn.source = "item_x_buf1_selected.png"
                self.power_buff_btn.opacity = 1.0
        elif buff_number == 1:
            if self.manager.get_screen("cidh final screen 2").power_potion:
                self.power_potion = False
                self.power_potion_btn.source = "item_p_pot1.png"
                self.power_potion_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").power_potion = True
                self.power_potion_btn.source = "item_p_pot1_selected.png"
                self.power_potion_btn.opacity = 1.0
        elif buff_number == 2:
            if self.manager.get_screen("cidh final screen 2").power_elixir:
                self.manager.get_screen("cidh final screen 2").power_elixir = False
                self.power_elixir_btn.source = "item_x_eli1.png"
                self.power_elixir_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").power_elixir = True
                self.power_elixir_btn.source = "item_x_eli1_selected.png"
                self.power_elixir_btn.opacity = 1.0
        elif buff_number == 3:
            self.manager.get_screen("cidh final screen 2").frenzy_upgraded = False
            self.frenzy_upgraded_btn.source = "item_r_frenzy_upgraded.png"
            self.frenzy_upgraded_btn.opacity = 0.3
            if self.manager.get_screen("cidh final screen 2").frenzy:
                self.manager.get_screen("cidh final screen 2").frenzy = False
                self.frenzy_btn.source = "item_r_frenzy.png"
                self.frenzy_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").frenzy = True
                self.frenzy_btn.source = "item_r_frenzy_selected.png"
                self.frenzy_btn.opacity = 1.0
        elif buff_number == 4:
            self.manager.get_screen("cidh final screen 2").frenzy = False
            self.frenzy_btn.source = "item_r_frenzy.png"
            self.frenzy_btn.opacity = 0.3
            if self.manager.get_screen("cidh final screen 2").frenzy_upgraded:
                self.manager.get_screen("cidh final screen 2").frenzy_upgraded = False
                self.frenzy_upgraded_btn.source = "item_r_frenzy_upgraded.png"
                self.frenzy_upgraded_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").frenzy_upgraded = True
                self.frenzy_upgraded_btn.source = "item_r_frenzy_upgraded_selected.png"
                self.frenzy_upgraded_btn.opacity = 1.0
        elif buff_number == 5:
            self.manager.get_screen("cidh final screen 2").sunder_upgraded = False
            self.sunder_upgraded_btn.source = "item_r_sunder_upgraded.png"
            self.sunder_upgraded_btn.opacity = 0.3
            if self.manager.get_screen("cidh final screen 2").sunder:
                self.manager.get_screen("cidh final screen 2").sunder = False
                self.sunder_btn.source = "item_r_sunder.png"
                self.sunder_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").sunder = True
                self.sunder_btn.source = "item_r_sunder_selected.png"
                self.sunder_btn.opacity = 1.0
        elif buff_number == 6:
            self.manager.get_screen("cidh final screen 2").sunder = False
            self.sunder_btn.source = "item_r_sunder.png"
            self.sunder_btn.opacity = 0.3
            if self.manager.get_screen("cidh final screen 2").sunder_upgraded:
                self.manager.get_screen("cidh final screen 2").sunder_upgraded = False
                self.sunder_upgraded_btn.source = "item_r_sunder_upgraded.png"
                self.sunder_upgraded_btn.opacity = 0.3
            else:
                self.manager.get_screen("cidh final screen 2").sunder_upgraded = True
                self.sunder_upgraded_btn.source = "item_r_sunder_upgraded_selected.png"
                self.sunder_upgraded_btn.opacity = 1.0
        self.manager.get_screen("cidh final screen 2").check_items()
        self.manager.get_screen("cidh final screen 2").check_if_icdh(0)
        self.manager.get_screen("cidh final screen 2").show_killeable_targets()

current_item_slot = 0
selected_items = ["a", "a", "a", "a", "a", "a", "a", "a", "a"]

selected_item_picture = "a"

god_level = 0
base_mana = 0
mana_per_level = 0
base_p_prot = 0
p_prot_per_level = 0

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class BackButton(Button):
    pass

class sm(ScreenManager):
    pass
        
class DylanApp(App):
    def build(self):
        return sm()

if __name__ == "__main__":
    DylanApp().run()
