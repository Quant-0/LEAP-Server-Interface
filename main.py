import customtkinter
from tkinter import *
import configparser
import os
from PIL import Image
import collections

customtkinter.set_appearance_mode("System")

class ConfigParserMultiValues(collections.OrderedDict):

    def __setitem__(self, key, value):
        if key in self and isinstance(value, list):
            self[key].extend(value)
        else:
            super().__setitem__(key, value)

    @staticmethod
    def getlist(value):
        return value.split(os.linesep)

#config = ConfigParser.RawConfigParser(dict_type=MultiOrderedDict)



#par = configparser.ConfigParser()
par = configparser.ConfigParser(strict=False, empty_lines_in_values=False, allow_no_value=True, dict_type=ConfigParserMultiValues, converters={"list": ConfigParserMultiValues.getlist})
par.read('game.ini')
session_name = par.get('/Script/ProjectX.ProjectXGameSession', 'servername')
session_region = par.get('/Script/ProjectX.ProjectXGameSession', 'serverregion')
session_password = par.get('/Script/ProjectX.ProjectXGameSession', 'serverpassword')
mode_maxplayer = par.get('/Script/ProjectX.ProjectXGameMode', 'maxplayersoverride')
mode_maxteamimbal = par.get('/Script/ProjectX.ProjectXGameMode', 'maxteamimbalance')
mode_matchlength = par.get('/Script/ProjectX.ProjectXGameMode', 'matchlengthoverride')
mode_maxdeplayable = par.get('/Script/ProjectX.ProjectXGameMode', 'maxplayerdeployablesoverride')
state_respawndelay = par.get('/Script/ProjectX.ProjectXGameState', 'RespawnDelayOverride')
state_RedeployRespawn = par.get('/Script/ProjectX.ProjectXGameState', 'redeployrespawndelayoverride')
state_UltimateDamage = par.get('/Script/ProjectX.ProjectXGameState', 'UltimateDamageMultiplier')
state_ExplosiveDamage = par.get('/Script/ProjectX.ProjectXGameState', 'ExplosiveDamageMultiplier')
state_HeadshotDamage = par.get('/Script/ProjectX.ProjectXGameState', 'HeadshotDamageMultiplier')
state_WeaponDamage = par.get('/Script/ProjectX.ProjectXGameState', 'WeaponDamageMultiplier')
state_AbilityCooldown = par.get('/Script/ProjectX.ProjectXGameState', 'AbilityCooldownMultiplier')
state_HookshotDistance = par.get('/Script/ProjectX.ProjectXGameState', 'HookshotDistanceMultiplier')
state_HookshotSpeed = par.get('/Script/ProjectX.ProjectXGameState', 'HookshotSpeedMultipler')
state_UltimateChargeRate = par.get('/Script/ProjectX.ProjectXGameState', 'UltimateChargeRateMultiplier')
state_GrenadeCount = par.get('/Script/ProjectX.ProjectXGameState', 'GrenadeCountModifier')
state_DashCharge = par.get('/Script/ProjectX.ProjectXGameState', 'DashChargeModifier')
state_Gravity = par.get('/Script/ProjectX.ProjectXGameState', 'GravityMultiplier')
state_GroundSpeed = par.get('/Script/ProjectX.ProjectXGameState', 'GroundSpeedMultiplier')
state_bIsAL = par.get('/Script/ProjectX.ProjectXGameState', 'bIsAmmoLimited')
controller_Idle = par.get('/Script/ProjectX.ProjectXPlayerController', 'IdleTimeoutTime')
instance_mods = par.get('/Script/ProjectX.ProjectXGameInstance', 'CF_ModIds')
instance_maps = par.get('/Script/ProjectX.ProjectXGameInstance', 'MapListConfig')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("LEAP Server")
        self.geometry("1200x600")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Logo.webp")), size=(120, 22))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")), dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")), dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_f = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_f.grid(row=0, column=0, sticky="nsew")
        self.navigation_f.grid_rowconfigure(6, weight=1)

        self.navigation_f_label = customtkinter.CTkLabel(self.navigation_f, text="  ", image=self.logo_image, compound="left", font=customtkinter.CTkFont(weight="bold", size=15))
        self.navigation_f_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_f, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.install_button = customtkinter.CTkButton(self.navigation_f, corner_radius=0, height=40, border_spacing=10, text="Install", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.chat_image, anchor="w", command=self.install_button_event)
        self.install_button.grid(row=2, column=0, sticky="ew")

        self.sts_button = customtkinter.CTkButton(self.navigation_f, corner_radius=0, height=40, border_spacing=10, text="Settings", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.sts_button_event)
        self.sts_button.grid(row=3, column=0, sticky="ew")

        self.modsmaps_button = customtkinter.CTkButton(self.navigation_f, corner_radius=0, height=40, border_spacing=10, text="Mods & Maps", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.modsmaps_button_event)
        self.modsmaps_button.grid(row=4, column=0, sticky="ew")

        self.mltpl_button = customtkinter.CTkButton(self.navigation_f, corner_radius=0, height=40, border_spacing=10, text="Multipliers", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.mltpl_button_event)
        self.mltpl_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_f, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        self.appearance_mode_menu.set("System")

        # create home frame
        self.home_f = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_f.grid_columnconfigure(0, weight=1)

        self.home_f_large_image_label = customtkinter.CTkLabel(self.home_f, text="", image=self.large_test_image)
        self.home_f_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_f_button_1 = customtkinter.CTkButton(self.home_f, text="", image=self.image_icon_image)
        self.home_f_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_f_button_2 = customtkinter.CTkButton(self.home_f, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_f_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_f_button_3 = customtkinter.CTkButton(self.home_f, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_f_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_f_button_4 = customtkinter.CTkButton(self.home_f, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_f_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create install frame
        self.install_f = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")




        # create settings frame
        self.sts_f = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sts_f.grid_columnconfigure((0, 1, 2), weight=3)

        # [/Script/ProjectX.ProjectXGameSession] settings LABELS
        self.sts_f_servername = customtkinter.CTkLabel(self.sts_f, text="Server Name", font=("TkDefaultFont", 20))
        self.sts_f_servername.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_servername_info = customtkinter.CTkLabel(self.sts_f, text="Change your server name here. This will show up in the browser", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_servername_info.grid(row=2, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.sts_f_password = customtkinter.CTkLabel(self.sts_f, text="Password", font=("TkDefaultFont", 20))
        self.sts_f_password.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_password_info = customtkinter.CTkLabel(self.sts_f, text="Use this to prevent unwanted visitors.", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_password_info.grid(row=2, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.sts_f_region = customtkinter.CTkLabel(self.sts_f, text="Region", font=("TkDefaultFont", 20))
        self.sts_f_region.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_region_info = customtkinter.CTkLabel(self.sts_f, text="Telegraph what region your server is from", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_region_info.grid(row=2, column=2, padx=(20, 0), pady=(0, 0), sticky="nsew")

        # Server name Field
        self.sts_f.entry_name = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_name.grid(row=3, column=0, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_name.insert(0, session_name)

        # Password Field
        self.sts_f.entry_password = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_password.grid(row=3, column=1, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_password.insert(0, session_password)

        # Region Dropdown
        self.sts_f.combobox_region = customtkinter.CTkComboBox(self.sts_f, values=["uswest", "asia", "russia", "europe", "australia", "brazil"])
        self.sts_f.combobox_region.grid(row=3, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")

        # [/Script/ProjectX.ProjectXGameMode] settings LABLES
        self.sts_f_mxplay = customtkinter.CTkLabel(self.sts_f, text="Max Players Overrid", font=("TkDefaultFont", 20))
        self.sts_f_mxplay.grid(row=4, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_mxplay_info = customtkinter.CTkLabel(self.sts_f, text="Number of players allowed in the server, if unused will use the gamemode default", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_mxplay_info.grid(row=5, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.sts_f_maxtb = customtkinter.CTkLabel(self.sts_f, text="Max Team Imbalance", font=("TkDefaultFont", 20))
        self.sts_f_maxtb.grid(row=4, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_maxtb_info = customtkinter.CTkLabel(self.sts_f, text="How many more players can be on one team vs the other, default 2", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_maxtb_info.grid(row=5, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.sts_f_matchlo = customtkinter.CTkLabel(self.sts_f, text="Match Length Override", font=("TkDefaultFont", 20))
        self.sts_f_matchlo.grid(row=4, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.sts_f_matchlo_info = customtkinter.CTkLabel(self.sts_f, text="Overrides the length of the match with the specified value. If not specified, will use the game mode’s default", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_matchlo_info.grid(row=5, column=2, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.sts_f_maxplaydo = customtkinter.CTkLabel(self.sts_f, text="Max Player Deployables Override", font=("TkDefaultFont", 20), wraplength=220)
        self.sts_f_maxplaydo.grid(row=7, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_maxplaydo_info = customtkinter.CTkLabel(self.sts_f, text="Overrides the number of deployables a player is allowed to have at once. Default is 1", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_maxplaydo_info.grid(row=8, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        # MaxPlayersOverride Field
        self.sts_f.entry_MaxPO = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_MaxPO.grid(row=6, column=0, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_MaxPO.insert(10, mode_maxplayer)

        # MaxTeamImbalance Field
        self.sts_f.entry_maxtb = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_maxtb.grid(row=6, column=1, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_maxtb.insert(10, mode_maxteamimbal)

        # MatchLengthOverride Field
        self.sts_f.entry_MatchLO = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_MatchLO.grid(row=6, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_MatchLO.insert(10, mode_matchlength)

        # MaxPlayerDeployablesOverride Field
        self.sts_f.entry_maxplaydo = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_maxplaydo.grid(row=9, column=0, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_maxplaydo.insert(10, mode_maxdeplayable)

        # [/Script/ProjectX.ProjectXPlayerController] LABELS
        self.sts_f_IdleTimeoutTime = customtkinter.CTkLabel(self.sts_f, text="Idle Timeout Time", font=("TkDefaultFont", 20))
        self.sts_f_IdleTimeoutTime.grid(row=7, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.sts_f_IdleTimeoutTime_info = customtkinter.CTkLabel(self.sts_f, text="How long before an idle player is kicked?", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.sts_f_IdleTimeoutTime_info.grid(row=8, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        # IdleTimeoutTime Field
        self.sts_f.entry_Idle = customtkinter.CTkEntry(self.sts_f)
        self.sts_f.entry_Idle.grid(row=9, column=1, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.sts_f.entry_Idle.insert(10, controller_Idle)



        # INI save button def
        def save_sts():
            par.read("game.ini")
            par.set('/Script/ProjectX.ProjectXGameSession', 'servername', self.sts_f.entry_name.get())
            par.set('/Script/ProjectX.ProjectXGameSession', 'serverregion', self.sts_f.combobox_region.get())
            par.set('/Script/ProjectX.ProjectXGameSession', 'serverpassword', self.sts_f.entry_password.get())
            par.set('/Script/ProjectX.ProjectXGameMode', 'maxplayersoverride', self.sts_f.entry_MaxPO.get())
            par.set('/Script/ProjectX.ProjectXGameMode', 'maxteamimbalance', self.sts_f.entry_maxtb.get())
            par.set('/Script/ProjectX.ProjectXGameMode', 'matchlengthoverride', self.sts_f.entry_MatchLO.get())
            par.set('/Script/ProjectX.ProjectXGameMode', 'maxplayerdeployablesoverride', self.sts_f.entry_maxplaydo.get())
            par.set('/Script/ProjectX.ProjectXPlayerController', 'idletimeouttime', self.sts_f.entry_Idle.get())
            with open('game.ini', 'w') as configfile:
                par.write(configfile)

        self.sts_f.main_button_1 = customtkinter.CTkButton(master=self.sts_f, text="Save", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=save_sts)
        self.sts_f.main_button_1.grid(row=15, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")




        # create mods & maps frame
        self.modsmaps_f = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.modsmaps_f.grid_columnconfigure((0, 1, 2), weight=3)

        #Mods Lable
        self.modsmaps_f.lable_mods = customtkinter.CTkLabel(self.modsmaps_f, text="Paste all your mods in the text field", font=("TkDefaultFont", 20),)
        self.modsmaps_f.lable_mods.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")

        #Mods textbox
        self.modsmaps_f.textbox_mods = customtkinter.CTkTextbox(self.modsmaps_f, width=250)
        self.modsmaps_f.textbox_mods.grid(row=1, column=0, padx=(20, 20), pady=(30, 0), sticky="nsew", columnspan=3)
        self.modsmaps_f.textbox_mods.insert(INSERT, instance_mods)

        #Maps Lable
        self.modsmaps_f.lable_maps = customtkinter.CTkLabel(self.modsmaps_f, text="Paste all your maps in the text field", font=("TkDefaultFont", 20),)
        self.modsmaps_f.lable_maps.grid(row=2, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")

        # Maps textbox
        self.modsmaps_f.textbox_maps = customtkinter.CTkTextbox(self.modsmaps_f, width=250)
        self.modsmaps_f.textbox_maps.grid(row=3, column=0, padx=(20, 20), pady=(30, 0), sticky="nsew", columnspan=3)
        self.modsmaps_f.textbox_maps.insert(INSERT, instance_maps)

        # INI save button def
        def save_mods():
            par.read("game.ini")
            par.set('/Script/ProjectX.ProjectXGameInstance','CF_ModIds', self.modsmaps_f.textbox_mods)
            #par.set('/Script/ProjectX.ProjectXGameInstance', 'MapListConfig', self.modsmaps_f.textbox_maps.get())
            with open('game.ini', 'w') as configfile:
                par.write(configfile)

        self.modsmaps_f.main_button_1 = customtkinter.CTkButton(master=self.modsmaps_f, text="Save", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=save_mods)
        self.modsmaps_f.main_button_1.grid(row=50, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")


        # create multipliers frame
        self.mltpl_f = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")
        self.mltpl_f.grid_columnconfigure((0, 1, 2), weight=3)

        # [/Script/ProjectX.ProjectXGameState] LABELS
        self.mltpl_f_RespwanDO = customtkinter.CTkLabel(self.mltpl_f, text="Respawn Delay Override", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_RespwanDO.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_RespwanDO_info = customtkinter.CTkLabel(self.mltpl_f, text="Override respawn times", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_RespwanDO_info.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_RedeployRespwanDO = customtkinter.CTkLabel(self.mltpl_f, text="Redeploy Respawn Delay Override", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_RedeployRespwanDO.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_RedeployRespwanDO_info = customtkinter.CTkLabel(self.mltpl_f, text="Override redeploy times", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_RedeployRespwanDO_info.grid(row=1, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_UltimateDM = customtkinter.CTkLabel(self.mltpl_f, text="Ultimate Damage Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_UltimateDM.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.mltpl_f_UltimateDM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the damage of ultimates", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_UltimateDM_info.grid(row=1, column=2, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.mltpl_f_ExplosiveDM = customtkinter.CTkLabel(self.mltpl_f, text="Explosive Damage Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_ExplosiveDM.grid(row=4, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_ExplosiveDM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the damage of explosives", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_ExplosiveDM_info.grid(row=5, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_HeadshotDM = customtkinter.CTkLabel(self.mltpl_f, text="Headshot Damage Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_HeadshotDM.grid(row=4, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_HeadshotDM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the damage of headshots", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_HeadshotDM_info.grid(row=5, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_WeaponDM = customtkinter.CTkLabel(self.mltpl_f, text="Weapon Damage Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_WeaponDM.grid(row=4, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.mltpl_f_WeaponDM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the damage of weapons", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_WeaponDM_info.grid(row=5, column=2, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.mltpl_f_AbilityCM = customtkinter.CTkLabel(self.mltpl_f, text="Ability Cooldown Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_AbilityCM.grid(row=7, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_AbilityCM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the cooldown of abilities", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_AbilityCM_info.grid(row=8, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_HookshotDM = customtkinter.CTkLabel(self.mltpl_f, text="Hookshot Distance Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_HookshotDM.grid(row=7, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_HookshotDM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the distance of the hookshot", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_HookshotDM_info.grid(row=8, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_HookshotSM = customtkinter.CTkLabel(self.mltpl_f, text="Hookshot Speed Multipler", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_HookshotSM.grid(row=7, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.mltpl_f_HookshotSM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the speed of the hookshot", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_HookshotSM_info.grid(row=8, column=2, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.mltpl_f_UltimateCRM = customtkinter.CTkLabel(self.mltpl_f, text="Ultimate ChargeRate Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_UltimateCRM.grid(row=10, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_UltimateCRM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplies the speed of ultimate charge", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_UltimateCRM_info.grid(row=11, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_GrenadeCM = customtkinter.CTkLabel(self.mltpl_f, text="Grenade Count Modifier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_GrenadeCM.grid(row=10, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_GrenadeCM_info = customtkinter.CTkLabel(self.mltpl_f, text="Modifies the number of grenades a player can carry", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_GrenadeCM_info.grid(row=11, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_DashCM = customtkinter.CTkLabel(self.mltpl_f, text="Dash Charge Modifier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_DashCM.grid(row=10, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.mltpl_f_DashCM_info = customtkinter.CTkLabel(self.mltpl_f, text="Modifies the number of dash charges", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_DashCM_info.grid(row=11, column=2, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.mltpl_f_GravityM = customtkinter.CTkLabel(self.mltpl_f, text="Gravity Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_GravityM.grid(row=13, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_GravityM_info = customtkinter.CTkLabel(self.mltpl_f, text="Multiplier for the amount of gravity affecting players", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_GravityM_info.grid(row=14, column=0, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_GroundSM = customtkinter.CTkLabel(self.mltpl_f, text="Ground Speed Multiplier", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_GroundSM.grid(row=13, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.mltpl_f_GroundSM_info = customtkinter.CTkLabel(self.mltpl_f, text="Modifies the number of grenades a player can carry", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_GroundSM_info.grid(row=14, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")

        self.mltpl_f_bIsAL = customtkinter.CTkLabel(self.mltpl_f, text="Ammo Limited", font=("TkDefaultFont", 20), wraplength=220)
        self.mltpl_f_bIsAL.grid(row=13, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.mltpl_f_bIsAL_info = customtkinter.CTkLabel(self.mltpl_f, text="Overrides the unlimited ammo flag on weapons, rendering their ammo limited", font=("TkDefaultFont", 12), wraplength=220, text_color="#848484")
        self.mltpl_f_bIsAL_info.grid(row=14, column=2, padx=(20, 20), pady=(0, 0), sticky="nsew")

        # RespawnDelayOverride Field
        self.mltpl_f.entry_RespwanDO = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_RespwanDO.grid(row=3, column=0, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_RespwanDO.insert(10, state_respawndelay)

        # RedeployRespawnDelayOverride Field
        self.mltpl_f.entry_RedeployRespwanDO = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_RedeployRespwanDO.grid(row=3, column=1, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_RedeployRespwanDO.insert(10, state_RedeployRespawn)

        # UltimateDamageMultiplier Field
        self.mltpl_f.entry_UltimateDM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_UltimateDM.grid(row=3, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_UltimateDM.insert(10, state_UltimateDamage)

        # ExplosiveDamageMultiplier Field
        self.mltpl_f.entry_ExplosiveDM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_ExplosiveDM.grid(row=6, column=0, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_ExplosiveDM.insert(10, state_ExplosiveDamage)

        # HeadshotDamageMultiplier Field
        self.mltpl_f.entry_HeadshotDM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_HeadshotDM.grid(row=6, column=1, padx=(20, 0), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_HeadshotDM.insert(10, state_HeadshotDamage)

        # WeaponDamageMultiplier Field
        self.mltpl_f.entry_WeaponDM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_WeaponDM.grid(row=6, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_WeaponDM.insert(10, state_WeaponDamage)

        # AbilityCooldownMultiplier Field
        self.mltpl_f.entry_AbilityCM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_AbilityCM.grid(row=9, column=0, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_AbilityCM.insert(10, state_AbilityCooldown)

        # HookshotDistanceMultiplier Field
        self.mltpl_f.entry_HookshotDM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_HookshotDM.grid(row=9, column=1, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_HookshotDM.insert(10, state_HookshotDistance)

        # HookshotSpeedMultipler Field
        self.mltpl_f.entry_HookshotSM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_HookshotSM.grid(row=9, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_HookshotSM.insert(10, state_HookshotSpeed)

        #UltimateChargeRateMultiplier Field
        self.mltpl_f.entry_UltimateCRM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_UltimateCRM.grid(row=12, column=0, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_UltimateCRM.insert(10, state_UltimateChargeRate)

        #GrenadeCountModifier Field
        self.mltpl_f.entry_GrenadeCM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_GrenadeCM.grid(row=12, column=1, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_GrenadeCM.insert(10, state_GrenadeCount)

        #DashChargeModifier Field
        self.mltpl_f.entry_DashCM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_DashCM.grid(row=12, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_DashCM.insert(10, state_DashCharge)

        #GravityMultiplier Field
        self.mltpl_f.entry_GravityM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_GravityM.grid(row=15, column=0, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_GravityM.insert(10, state_Gravity)

        #GroundSpeedMultiplier Field
        self.mltpl_f.entry_GroundSM = customtkinter.CTkEntry(self.mltpl_f)
        self.mltpl_f.entry_GroundSM.grid(row=15, column=1, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.mltpl_f.entry_GroundSM.insert(10, state_GroundSpeed)

        #bIsAmmoLimited Field
        self.mltpl_f.combobox_bIsAL = customtkinter.CTkComboBox(self.mltpl_f, values=["false", "true"])
        self.mltpl_f.combobox_bIsAL.grid(row=15, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")

        # INI save button def
        def save_mltpl():
            par.read("game.ini")
            par.set('/Script/ProjectX.ProjectXGameState', 'RespawnDelayOverride', self.mltpl_f.entry_RespwanDO.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'RedeployRespawnDelayOverride', self.mltpl_f.entry_RedeployRespwanDO.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'UltimateDamageMultiplier', self.mltpl_f.entry_UltimateDM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'ExplosiveDamageMultiplier', self.mltpl_f.entry_ExplosiveDM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'HeadshotDamageMultiplier', self.mltpl_f.entry_HeadshotDM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'WeaponDamageMultiplier', self.mltpl_f.entry_WeaponDM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'AbilityCooldownMultiplier', self.mltpl_f.entry_AbilityCM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'HookshotDistanceMultiplier', self.mltpl_f.entry_HookshotDM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'HookshotSpeedMultipler', self.mltpl_f.entry_HookshotSM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'UltimateChargeRateMultiplier', self.mltpl_f.entry_UltimateCRM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'GrenadeCountModifier', self.mltpl_f.entry_GrenadeCM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'DashChargeModifier', self.mltpl_f.entry_DashCM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'GravityMultiplier', self.mltpl_f.entry_GravityM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'GroundSpeedMultiplier', self.mltpl_f.entry_GroundSM.get())
            par.set('/Script/ProjectX.ProjectXGameState', 'bIsAmmoLimited', self.mltpl_f.combobox_bIsAL.get())
            with open('game.ini', 'w') as configfile:
                par.write(configfile)

        self.mltpl_f.main_button_1 = customtkinter.CTkButton(master=self.mltpl_f, text="Save", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=save_mltpl)
        self.mltpl_f.main_button_1.grid(row=50, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.install_button.configure(fg_color=("gray75", "gray25") if name == "install" else "transparent")
        self.sts_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")
        self.modsmaps_button.configure(fg_color=("gray75", "gray25") if name == "modsmaps" else "transparent")
        self.mltpl_button.configure(fg_color=("gray75", "gray25") if name == "multipliers" else "transparent")

        # show selected frame
        if name == "home":
            self.home_f.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_f.grid_forget()
        if name == "install":
            self.install_f.grid(row=0, column=1, sticky="nsew")
        else:
            self.install_f.grid_forget()
        if name == "settings":
            self.sts_f.grid(row=0, column=1, sticky="nsew")
        else:
            self.sts_f.grid_forget()
        if name == "modsmaps":
            self.modsmaps_f.grid(row=0, column=1, sticky="nsew")
        else:
            self.modsmaps_f.grid_forget()
        if name == "multipliers":
            self.mltpl_f.grid(row=0, column=1, sticky="nsew")
        else:
            self.mltpl_f.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def install_button_event(self):
        self.select_frame_by_name("install")

    def sts_button_event(self):
        self.select_frame_by_name("settings")

    def modsmaps_button_event(self):
        self.select_frame_by_name("modsmaps")

    def mltpl_button_event(self):
        self.select_frame_by_name("multipliers")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
