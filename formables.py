import pprint

# python dictionary of formable/mission requirements
# { "Country name" : { "Must" : { keys: province ID/area name/region name } } }
#keys
# 'dc' - direct_core - own + core
# 'ic' - indirect_core - own or non-tributary subject own + core
# 'do' - direct_own - own
# 'io' - indirect_own - own or non-tributary subject own


# adds an entry to req_dict; asserts if name is already an entry
def add_country(name, reqs):
    assert(name not in req_dict)
    req_dict[name] = reqs

# synthesizes a reqs map (ready to be added using add_country) with must/nice req maps
def syn_reqs(must, nice):
    ref_keys = sorted(['dc', 'ic', 'do', 'io', 'comments'])
    must_keys = sorted(must.keys())
    nice_keys = sorted(nice.keys())
    assert(ref_keys == must_keys)
    assert(ref_keys == nice_keys)
    return {"Must" : must, "Nice" : nice}

def add_dc(req, dc):
    req['dc'] += dc
def add_ic(req, ic):
    req['ic'] += ic
def add_do(req, do):
    req['do'] += do
def add_io(req, io):
    req['io'] += io
# coerce string into a singleton list
def add_comment(req, comment):
    if type(comment) is list: # eeek
        req['comments'] += comment
    else:
        req['comments'].append(comment)

def populate_reqs():
    # Golden Horde
    glh_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    glh_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    # formation
    add_dc(glh_m, [284, 302, 464, 465, 466, 476, 1075, 1082, 1778, 2411])
    add_io(glh_m, [294, 295, 301, 307, 308, 1956])
    # must missions
    add_dc(glh_m, [303, 466, 464, 1082, 465, 2190])
    add_do(glh_m, ['mongolia_region'])
    add_io(glh_m, ['nogai_area', 'kazakhstan_area', 'syr_darya_area', 'kyzylkum_area', 'central_asia_region', 'north_china_region'])
    # nice missions
    # 6 CoTs in Persia/Central Asia/Khorasan region (technically only need to own and not core, but realistically speaking I'd need to upgrade the CoTs and dev push)
    # add_dc(glh_n, ...)
    add_comment(glh_n, "Need to own 6 CoTs in Persia/Central Asia/Khorasan region")
    add_io(glh_n, [301, 'ryazan_area', 'moscow_area', 'suzdal_area', 'tver_area', 'yaroslavl_area',
      'vladimir_area', 'azov_area', 'crimea_area', 'zaporizhia_area', 'yedisan_area',
      'sloboda_ukraine_area', 'west_dniepr_area', 'east_dniepr_area',
      'podolia_volhynia_area', 'caucasia_region', 'tabriz_area', 'azerbaijan_area',
      'shahrizor_area', 'luristan_area', 'tabarestan_area', 'mashhad_area', 'herat_area',
      'birjand_area', 'isfahan_area', 'iraq_e_ajam_area'])
    add_country("Golden Horde", syn_reqs(glh_m, glh_n))

    # Timurids
    tim_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    tim_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    # formation
    add_dc(tim_m, [446, 454, 451, 445, 428])
    # must missions (CCR)
    add_do(tim_m, ['mashhad_area', 'birjand_area', 'sistan_area', 'herat_area',
                   'ghor_area', 'kabulistan_area', 'balkh_area'])
    # nice missions
    add_do(tim_n, [431, 4327, 2217, 4342, 'farsistan_area', 'persian_gulf_coast', 'kerman_area',
                   413, 414, 2210, 'isfahan_area', 'iraq_e_ajam_area', 'azerbaijan_area',
                   458, 1967, 457, 2356, 'transoxiana_area', 'termez_area',
                   437, 438, 2349, 2214, 441, 2362, 1973, 'merv_area',
                   'lahore_area', 'sind_sagar_area',
                   'sirhind_area', 'upper_doab_area'])
    add_country("Timurids", syn_reqs(tim_m, tim_n))

    # Bavaria
    # skip -- their missions are very complicated to put nicely on a map, and I already have it mapped out in my head
    # tl;dr own 8 provinces in venezia/carniola and revoke HRE. Buildings on Munich _could_ be nice

    # Siam
    sia_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    sia_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    # formation
    add_dc(sia_m, [600, 601, 589])
    add_dc(sia_m, ['indo_china_region'])
    add_comment(sia_m, "Only need to have 20 cores in indochina, so maybe different color here?")
    # must missions
    # and so on... TBH Siamese missions don't conflict with other missions, so I don't mind handling these mentally
    add_country("Siam", syn_reqs(sia_m, sia_n))

    # Yuan
    yua_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    yua_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    add_dc(yua_m, [723, 1816, 2190, 2136])
    add_comment(yua_m, "Subject owns all Mongol/Korchin/Khalka/Oirat culture provinces")
    add_country("Yuan", syn_reqs(yua_m, yua_n))

    # Mongol Empire
    mge_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    mge_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    add_do(mge_m, [1816, 1821, 667, 'mongolia_region', 'central_asia_region', 'pontic_steppe_region'])
    add_io(mge_m, ['khorasan_region', 'persia_region', 295, 280])
    add_country("Mongol Empire", syn_reqs(mge_m, mge_n))

    # Non hordes

    # Delhi
    dlh_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    dlh_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    # formation
    add_dc(dlh_m, [522, 510, 507]) # technically Jaunpur stuff work too, but keep it simple since I know I'll be conquering Sirhind stuff first
    # TODO Delhi missions
    add_country("Delhi", syn_reqs(dlh_m, dlh_n))

    # Poland
    pol_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    pol_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    # formation
    add_dc(pol_m, [262, 257, 254, 255, 258, 259, 1939])
    # TODO nice to haves
    add_country("Poland", syn_reqs(pol_m, pol_n))

    # Persia (mostly for formation and events)
    per_m = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    per_n = {"dc":[], "ic":[], "do":[], "io":[], "comments":[]}
    # formation, picking cores that I know I'll have and omitting other options
    add_dc(per_m, [414, 429, 433, 2213, 2215, 426, 2221])
    # TODO nice to haves
    #add_io(per_n, ['tabriz_area', 'azerbaijan_area', 
    add_country("Persia", syn_reqs(per_m, per_n))


if __name__ == "__main__":
    hordes = ["Golden Horde", "Timurids", "Siam", "Bavaria", "Manchu", "Yuan", "Mongol Empire"]
    req_dict = {}
    populate_reqs()
    pprint.pprint(req_dict)
