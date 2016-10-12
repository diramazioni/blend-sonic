null = None
args_types_conversion = {
  ":array": "String List", # notes (ring) :A3, :B4, :C4 
  ":boolean": "Boolean", 
  ":list": "String List", # notes [ :A, :B4, :C4 ]
  ":list_or_number": "String List", # notes AND int_List [ :A, :B4, :C4 ], [ 1,2,3 ]
  ":midi_number": "Integer", # note (only used in pitch_to_ratio)
  ":note": "Integer", # note (ring) # :A3 or 60
  ":number": "Float",
  ":number_symbol_or_map": "Integer", # note (only used in :rest?)
  ":pos_int": "Integer", # note (ring)
  ":sample_name_or_duration": "String", # string_or_number (only used in :use_sample_bpm :with_sample_bpm)
  ":source_and_filter_types": "String", # same as symbol_or_string sample (only used in :sample_paths)
  ":string": "String",
  ":symbol": "String", # note/reference with :
  ":symbol_or_number": "String", # note/reference: :A or 60
  ":synth_node": "String", # reference to var = 
  ":true_or_false": "String" # true or false (lowercase)
}

simple_sampler_args = [':amp', ':amp_slide', ':amp_slide_shape', ':amp_slide_curve', ':pan', ':pan_slide', ':pan_slide_shape', ':pan_slide_curve', ':cutoff', ':cutoff_slide', ':cutoff_slide_shape', ':cutoff_slide_curve', ':lpf', ':lpf_slide', ':lpf_slide_shape', ':lpf_slide_curve', ':hpf', ':hpf_slide', ':hpf_slide_shape', ':hpf_slide_curve', ':rate', ':slide', ':beat_stretch', ':rpitch', ':attack', ':decay', ':sustain', ':release', ':attack_level', ':decay_level', ':sustain_level', ':env_curve']


notes = {
  "A2": 45,
  "A3": 57,
  "A4": 69,
  "A5": 81,
  "Ab2": 44,
  "Ab3": 56,
  "Ab4": 68,
  "Ab5": 80,
  "As2": 46,
  "As3": 58,
  "As4": 70,
  "As5": 82,
  "B3": 59,
  "B4": 71,
  "B5": 83,
  "Bb2": 46,
  "Bb3": 58,
  "Bb4": 70,
  "Bb5": 82,
  "C2": 36,
  "C3": 48,
  "C4": 60,
  "C5": 72,
  "C6": 84,
  "Cs2": 37,
  "Cs3": 49,
  "Cs4": 61,
  "Cs5": 73,
  "D2": 38,
  "D3": 50,
  "D4": 62,
  "D5": 74,
  "Db2": 37,
  "Db3": 49,
  "Db4": 61,
  "Db5": 73,
  "Ds2": 39,
  "Ds3": 51,
  "Ds4": 63,
  "Ds5": 75,
  "E2": 40,
  "E3": 52,
  "E4": 64,
  "E5": 76,
  "Eb2": 39,
  "Eb3": 51,
  "Eb4": 63,
  "Eb5": 75,
  "F2": 41,
  "F3": 53,
  "F4": 65,
  "F5": 77,
  "Fs2": 42,
  "Fs3": 54,
  "Fs4": 66,
  "Fs5": 78,
  "G2": 43,
  "G3": 55,
  "G4": 67,
  "G5": 79,
  "Gb2": 42,
  "Gb3": 54,
  "Gb4": 66,
  "Gb5": 78,
  "Gs2": 44,
  "Gs3": 56,
  "Gs4": 68,
  "Gs5": 80,
  ":rest": ":rest"
}

synthezier = {
  "BEEP": "beep",
  "BLADE": "blade",
  "BNOISE": "bnoise",
  "CNOISE": "cnoise",
  "DARK_AMBIENCE": "dark_ambience",
  "DARK_SEA_HORN": "dark_sea_horn",
  "DPULSE": "dpulse",
  "DSAW": "dsaw",
  "DTRI": "dtri",
  "DULL_BELL": "dull_bell",
  "FM": "fm",
  "GNOISE": "gnoise",
  "GROWL": "growl",
  "HOLLOW": "hollow",
  "HOOVER": "hoover",
  "MOD_DSAW": "mod_dsaw",
  "MOD_FM": "mod_fm",
  "MOD_PULSE": "mod_pulse",
  "MOD_SAW": "mod_saw",
  "MOD_SINE": "mod_sine",
  "MOD_TRI": "mod_tri",
  "NOISE": "noise",
  "PIANO": "piano",
  "PLUCK": "pluck",
  "PRETTY_BELL": "pretty_bell",
  "PROPHET": "prophet",
  "PULSE": "pulse",
  "SAW": "saw",
  "SQUARE": "square",
  "SUBPULSE": "subpulse",
  "SUPERSAW": "supersaw",
  "SYNTH_VIOLIN": "synth_violin",
  "TB303": "tb303",
  "TRI": "tri",
  "ZAWA": "zawa"
}

samples = {
  "AMBI_CHOIR": "ambi_choir",
  "AMBI_DARK_WOOSH": "ambi_dark_woosh",
  "AMBI_DRONE": "ambi_drone",
  "AMBI_GLASS_HUM": "ambi_glass_hum",
  "AMBI_GLASS_RUB": "ambi_glass_rub",
  "AMBI_HAUNTED_HUM": "ambi_haunted_hum",
  "AMBI_LUNAR_LAND": "ambi_lunar_land",
  "AMBI_PIANO": "ambi_piano",
  "AMBI_SOFT_BUZZ": "ambi_soft_buzz",
  "AMBI_SWOOSH": "ambi_swoosh",
  "BASS_DNB_F": "bass_dnb_f",
  "BASS_DROP_C": "bass_drop_c",
  "BASS_HARD_C": "bass_hard_c",
  "BASS_HIT_C": "bass_hit_c",
  "BASS_THICK_C": "bass_thick_c",
  "BASS_VOXY_C": "bass_voxy_c",
  "BASS_VOXY_HIT_C": "bass_voxy_hit_c",
  "BASS_WOODSY_C": "bass_woodsy_c",
  "BD_808": "bd_808",
  "BD_ADA": "bd_ada",
  "BD_BOOM": "bd_boom",
  "BD_FAT": "bd_fat",
  "BD_GAS": "bd_gas",
  "BD_HAUS": "bd_haus",
  "BD_KLUB": "bd_klub",
  "BD_PURE": "bd_pure",
  "BD_SONE": "bd_sone",
  "BD_TEK": "bd_tek",
  "BD_ZOME": "bd_zome",
  "BD_ZUM": "bd_zum",
  "DRUM_BASS_HARD": "drum_bass_hard",
  "DRUM_BASS_SOFT": "drum_bass_soft",
  "DRUM_CYMBAL_CLOSED": "drum_cymbal_closed",
  "DRUM_CYMBAL_HARD": "drum_cymbal_hard",
  "DRUM_CYMBAL_OPEN": "drum_cymbal_open",
  "DRUM_CYMBAL_PEDAL": "drum_cymbal_pedal",
  "DRUM_CYMBAL_SOFT": "drum_cymbal_soft",
  "DRUM_HEAVY_KICK": "drum_heavy_kick",
  "DRUM_SNARE_HARD": "drum_snare_hard",
  "DRUM_SNARE_SOFT": "drum_snare_soft",
  "DRUM_SPLASH_HARD": "drum_splash_hard",
  "DRUM_SPLASH_SOFT": "drum_splash_soft",
  "DRUM_TOM_HI_HARD": "drum_tom_hi_hard",
  "DRUM_TOM_HI_SOFT": "drum_tom_hi_soft",
  "DRUM_TOM_LO_HARD": "drum_tom_lo_hard",
  "DRUM_TOM_LO_SOFT": "drum_tom_lo_soft",
  "DRUM_TOM_MID_HARD": "drum_tom_mid_hard",
  "DRUM_TOM_MID_SOFT": "drum_tom_mid_soft",
  "ELEC_BEEP": "elec_beep",
  "ELEC_BELL": "elec_bell",
  "ELEC_BLIP": "elec_blip",
  "ELEC_BLIP2": "elec_blip2",
  "ELEC_BLUP": "elec_blup",
  "ELEC_BONG": "elec_bong",
  "ELEC_CHIME": "elec_chime",
  "ELEC_CYMBAL": "elec_cymbal",
  "ELEC_FILT_SNARE": "elec_filt_snare",
  "ELEC_FLIP": "elec_flip",
  "ELEC_FUZZ_TOM": "elec_fuzz_tom",
  "ELEC_HI_SNARE": "elec_hi_snare",
  "ELEC_HOLLOW_KICK": "elec_hollow_kick",
  "ELEC_LO_SNARE": "elec_lo_snare",
  "ELEC_MID_SNARE": "elec_mid_snare",
  "ELEC_PING": "elec_ping",
  "ELEC_PLIP": "elec_plip",
  "ELEC_POP": "elec_pop",
  "ELEC_SNARE": "elec_snare",
  "ELEC_SOFT_KICK": "elec_soft_kick",
  "ELEC_TICK": "elec_tick",
  "ELEC_TRIANGLE": "elec_triangle",
  "ELEC_TWANG": "elec_twang",
  "ELEC_TWIP": "elec_twip",
  "ELEC_WOOD": "elec_wood",
  "GUIT_E_FIFTHS": "guit_e_fifths",
  "GUIT_E_SLIDE": "guit_e_slide",
  "GUIT_HARMONICS": "guit_harmonics",
  "LOOP_AMEN": "loop_amen",
  "LOOP_AMEN_FULL": "loop_amen_full",
  "LOOP_COMPUS": "loop_compus",
  "LOOP_INDUSTRIAL": "loop_industrial",
  "MISC_BURP": "misc_burp",
  "PERC_BELL": "perc_bell"
}

chord = {
  "AUG": "aug",
  "DIM": "dim",
  "DIM7": "dim7",
  "DOM7": "dom7",
  "MAJOR7": "major7",
  "MINOR7": "minor7"
}

scale_mode = {
  "AEOLIAN": "aeolian",
  "AHIRBHAIRAV": "ahirbhairav",
  "AUGMENTED": "augmented",
  "AUGMENTED2": "augmented2",
  "BARTOK": "bartok",
  "BHAIRAV": "bhairav",
  "CHINESE": "chinese",
  "CHROMATIC": "chromatic",
  "DIATONIC": "diatonic",
  "DIMISHED": "diminished",
  "DIMISHED2": "diminished2",
  "DORIAN": "dorian",
  "EGYPTIAN": "egyptian",
  "ENIGMATIC": "enigmatic",
  "GONG": "gong",
  "HARMONIC_MAJOR": "harmonic_major",
  "HARMONIC_MINOR": "harmonic_minor",
  "HEX_AEOLIAN": "hex_aeolian",
  "HEX_DORIAN": "hex_dorian",
  "HEX_MAJOR6": "hex_major6",
  "HEX_MAJOR7": "hex_major7",
  "HEX_PHRYGIAN": "hex_phrygian",
  "HEX_SUS": "hex_sus",
  "HINDU": "hindu",
  "HIRAJOSHI": "hirajoshi",
  "HUNGARIAN_MINOR": "hungarian_minor",
  "I": "i",
  "II": "ii",
  "III": "iii",
  "INDIAN": "indian",
  "IONIAN": "ionian",
  "IV": "iv",
  "IWATO": "iwato",
  "JIAO": "jiao",
  "KUMOI": "kumoi",
  "LEADING_WHOLE": "leading_whole",
  "LOCRIAN": "locrian",
  "LOCRIAN_MAJOR": "locrian_major",
  "LYDIAN": "lydian",
  "LYDIAN_MINOR": "lydian_minor",
  "MAJOR": "major",
  "MAJOR_PENTATONIC": "major_pentatonic",
  "MARVA": "marva",
  "MELODIC_MAJOR": "melodic_major",
  "MELODIC_MINOR": "melodic_minor",
  "MELODIC_MINOR_ASC": "melodic_minor_asc",
  "MELODIC_MINOR_DESC": "melodic_minor_desc",
  "MESSIAEN1": "messiaen1",
  "MESSIAEN2": "messiaen2",
  "MESSIAEN3": "messiaen3",
  "MESSIAEN4": "messiaen4",
  "MESSIAEN5": "messiaen5",
  "MESSIAEN6": "messiaen6",
  "MESSIAEN7": "messiaen7",
  "MINOR": "minor",
  "MINOR_PENTATONIC": "minor_pentatonic",
  "MIXOLYDIAN": "mixolydian",
  "NEAPLOLITAN_MAJOR": "neapolitan_major",
  "NEAPLOLITAN_MINOR": "neapolitan_minor",
  "OCTATONIC": "octatonic",
  "PELOG": "pelog",
  "PHRYGIAN": "phrygian",
  "PROMETHEUS": "prometheus",
  "PRUVI": "purvi",
  "RITUSEN": "ritusen",
  "ROMANIAN_MINOR": "romanian_minor",
  "SCRIABIN": "scriabin",
  "SHANG": "shang",
  "SPANISH": "spanish",
  "SUPER_LOCRIAN": "super_locrian",
  "TODI": "todi",
  "V": "v",
  "VI": "vi",
  "VII": "vii",
  "VIII": "viii",
  "WHOLE": "whole",
  "WHOLE_TONE": "whole_tone",
  "YU": "yu",
  "ZHI": "zhi"
}
